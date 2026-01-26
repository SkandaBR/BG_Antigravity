import streamlit as st
import json
import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer
import os
from gtts import gTTS
import tempfile
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# --- Configuration ---
st.set_page_config(page_title="Bhagavad Gita Knowledge Repository", layout="wide")

# --- Constants ---
JSON_FILE_PATH = "bhagavadgita_Chapter_2.json"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
COLLECTION_NAME = "gita_chapter_2_v3" # Changed to force re-indexing
RELEVANCE_THRESHOLD = 0.3 

# --- Helper Functions ---

@st.cache_resource
def load_data():
    """Loads the Bhagavad Gita JSON data."""
    try:
        with open(JSON_FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        st.error(f"File not found: {JSON_FILE_PATH}")
        return None

@st.cache_resource
def initialize_vector_store():
    """Initializes ChromaDB and loads data if not present."""
    data = load_data()
    if not data:
        return None, None

    # Use PersistentClient to save data to disk
    db_path = os.path.join(os.getcwd(), "chroma_db")
    client = chromadb.PersistentClient(path=db_path)
    
    # Use SentenceTransformer for embeddings
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL_NAME)
    
    try:
        collection = client.get_or_create_collection(name=COLLECTION_NAME, embedding_function=sentence_transformer_ef)
        
        # Check if we need to populate
        if collection.count() == 0:
            documents = []
            metadatas = []
            ids = []
            
            chapter = data['chapters'][0]
            for verse in chapter['verses']:
                # Chunking Strategy:
                # Since each verse is a distinct, self-contained semantic unit, we treat each verse as a single chunk.
                # We combine English, Kannada, and Sanskrit text to ensure the embedding captures the full context 
                # and allows for multilingual retrieval (though the model is English-focused).
                doc_text = f"{verse['english_translation']} {verse['translation']} {verse['text']}"
                
                documents.append(doc_text)
                metadatas.append({
                    "verse": verse['verse'],
                    "text": verse['text'], # Sanskrit in Kannada script
                    "translation": verse['translation'],
                    "english_translation": verse['english_translation']
                })
                ids.append(f"verse_{verse['verse']}")
            
            # Add to collection (Chroma handles tokenization and embedding internally via the EF)
            collection.add(documents=documents, metadatas=metadatas, ids=ids)
            print(f"Added {len(documents)} documents to ChromaDB at {db_path}")
            
    except Exception as e:
        st.error(f"Error initializing ChromaDB: {e}")
        return None, None
        
    return client, collection

@st.cache_resource
def get_embedding_model():
    return SentenceTransformer(EMBEDDING_MODEL_NAME)

def get_audio_file(verse_number, lang='en'):
    """
    Get pre-generated audio file for a verse.
    If not found, generate it on-demand as fallback.
    """
    audio_dir = os.path.join(os.getcwd(), "audio_files", lang)
    audio_file = os.path.join(audio_dir, f"verse_{verse_number}.mp3")
    
    if os.path.exists(audio_file):
        return audio_file
    else:
        # Fallback: generate on-demand if pre-generated file doesn't exist
        st.warning(f"Pre-generated audio not found for verse {verse_number}. Generating now...")
        return None

def text_to_speech_gtts(text, lang='en'):
    """Fallback: Generates audio from text using gTTS (online, slower)."""
    try:
        tts = gTTS(text=text, lang=lang)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            return fp.name
    except Exception as e:
        st.error(f"Error generating audio with gTTS: {e}")
        return None

# --- Callbacks ---
def generate_audio_callback(idx, verse_number, lang):
    """Callback to load pre-generated audio and store in session state."""
    import time
    
    if 'debug_logs' not in st.session_state:
        st.session_state['debug_logs'] = []
    
    start_time = time.time()
    st.session_state['debug_logs'].append(f"Callback triggered for verse {verse_number}, index {idx}")
    
    print(f"DEBUG: Callback triggered for verse {verse_number}, index {idx}")
    try:
        # Try to get pre-generated audio
        load_start = time.time()
        audio_file = get_audio_file(verse_number, lang)
        load_end = time.time()
        
        st.session_state['debug_logs'].append(f"Audio file lookup took: {load_end - load_start:.4f}s")
        
        if audio_file:
            read_start = time.time()
            with open(audio_file, "rb") as f:
                audio_bytes = f.read()
            read_end = time.time()
            
            st.session_state['debug_logs'].append(f"File read took: {read_end - read_start:.4f}s")
            
            # Store in session state with a unique key using verse number
            key = f"audio_verse_{verse_number}_{lang}" 
            st.session_state[key] = audio_bytes
            
            total_time = time.time() - start_time
            st.session_state['debug_logs'].append(f"Success! Audio loaded for {key}. Size: {len(audio_bytes)} bytes")
            st.session_state['debug_logs'].append(f"Total callback time: {total_time:.4f}s")
            print(f"DEBUG: Audio stored in session state: {key}")
        else:
            st.session_state['debug_logs'].append("Pre-generated audio not found")
            print("DEBUG: Pre-generated audio not found")
    except Exception as e:
        st.session_state['debug_logs'].append(f"Exception: {str(e)}")
        print(f"DEBUG: Exception in callback: {e}")

# --- Main App ---

def main():
    st.title("Bhagavad Gita Knowledge Repository")
    
    # Sidebar for Debug
    with st.sidebar:
        st.header("Settings")
        debug_mode = st.checkbox("Show Debug Info")
        
        st.divider()
        st.subheader("Debug Logs")
        if 'debug_logs' in st.session_state:
            for log in st.session_state['debug_logs']:
                st.text(log)
        
        if st.button("Clear Logs"):
            st.session_state['debug_logs'] = []
            
        st.divider()
        st.subheader("Audio System Test")
        if st.button("Test Audio Playback"):
            print("DEBUG: Test Audio Button Clicked")
            try:
                test_text = "Testing audio system. One, two, three."
                test_file = text_to_speech(test_text)
                if test_file:
                    with open(test_file, "rb") as f:
                        test_bytes = f.read()
                    st.audio(test_bytes, format='audio/mp3')
                    st.success("Test audio generated.")
                else:
                    st.error("Test audio generation failed.")
            except Exception as e:
                st.error(f"Test failed: {e}")
                print(f"DEBUG: Test Exception: {e}")
    
    # Global Language Selection
    lang_choice = st.radio("Select Language / ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ:", ('English', 'Kannada'), horizontal=True)
    
    # Auto-clear query when language changes
    if 'previous_lang' not in st.session_state:
        st.session_state['previous_lang'] = lang_choice
    
    if st.session_state['previous_lang'] != lang_choice:
        st.session_state['current_query'] = ''
        st.session_state['previous_lang'] = lang_choice
    
    # Initialize resources
    client, collection = initialize_vector_store()
    model = get_embedding_model()
    
    if not collection:
        st.stop()
        
    if debug_mode:
        st.write(f"Collection Count: {collection.count()}")

    # Sample Questions
    st.subheader("Ask a question / ಪ್ರಶ್ನೆ ಕೇಳಿ")
    
    sample_questions = {
        'English': [
            "What is the nature of the soul?",
            "What is the duty of a Kshatriya?",
            "How to control senses?",
            "How to find peace?"
        ],
        'Kannada': [
            "ಆತ್ಮದ ಸ್ವರೂಪವೇನು?",
            "ಕ್ಷತ್ರಿಯನ ಧರ್ಮವೇನು?",
            "ಇಂದ್ರಿಯಗಳನ್ನು ನಿಗ್ರಹಿಸುವುದು ಹೇಗೆ?",
            "ಶಾಂತಿಯನ್ನು ಪಡೆಯುವುದು ಹೇಗೆ?"
        ]
    }
    
    current_questions = sample_questions[lang_choice]
    
    col1, col2, col3, col4 = st.columns(4)
    
    if col1.button(current_questions[0]):
        st.session_state['current_query'] = current_questions[0]
    if col2.button(current_questions[1]):
        st.session_state['current_query'] = current_questions[1]
    if col3.button(current_questions[2]):
        st.session_state['current_query'] = current_questions[2]
    if col4.button(current_questions[3]):
        st.session_state['current_query'] = current_questions[3]

    # Input Area
    input_label = "Or type your question here:" if lang_choice == 'English' else "ಅಥವಾ ನಿಮ್ಮ ಪ್ರಶ್ನೆಯನ್ನು ಇಲ್ಲಿ ಟೈಪ್ ಮಾಡಿ:"
    
    # Get query from session state or text input
    default_query = st.session_state.get('current_query', '')
    
    col_input, col_clear = st.columns([4, 1])
    with col_input:
        user_query = st.text_input(input_label, value=default_query, label_visibility="visible")
    with col_clear:
        st.write("")  # Spacing
        if st.button("Clear / ತೆರವುಗೊಳಿಸಿ", key="clear_query_btn"):
            st.session_state['current_query'] = ''
            # Clear all audio state
            keys_to_remove = [k for k in st.session_state.keys() if k.startswith('audio_')]
            for k in keys_to_remove:
                del st.session_state[k]
            st.rerun()
    
    # Update session state if user types
    if user_query:
        st.session_state['current_query'] = user_query

    if user_query:
        # Search
        results_with_embeddings = collection.query(
            query_texts=[user_query],
            n_results=3,
            include=['documents', 'metadatas', 'embeddings', 'distances']
        )
        
        query_embedding = model.encode([user_query])
        
        # Display Results
        st.markdown("### Relevant Verses / ಸಂಬಂಧಿತ ಶ್ಲೋಕಗಳು")
        
        ids = results_with_embeddings['ids'][0]
        metadatas = results_with_embeddings['metadatas'][0]
        embeddings = results_with_embeddings['embeddings'][0]
        
        if not ids:
             st.error("No results found.")
             return
        # normalized dot product
        top_sim = cosine_similarity(query_embedding, [embeddings[0]])[0][0]
        
        if top_sim < RELEVANCE_THRESHOLD:
             msg = "This data store does not have the required answer." if lang_choice == 'English' else "ಈ ಡೇಟಾ ಸ್ಟೋರ್‌ನಲ್ಲಿ ಅಗತ್ಯವಿರುವ ಉತ್ತರವಿಲ್ಲ."
             st.warning(f"{msg} (Low relevance score: {top_sim:.2f})")
        else:
            for i in range(len(ids)):
                meta = metadatas[i]
                doc_embedding = embeddings[i]
                
                if debug_mode:
                    st.json(meta)
                
                # Metrics Calculation
                #Answer relevance 
                sim_score = cosine_similarity(query_embedding, [doc_embedding])[0][0]
                relevant_count = sum(1 for emb in embeddings if cosine_similarity(query_embedding, [emb])[0][0] > RELEVANCE_THRESHOLD)
                #context precision
                context_precision = relevant_count / len(ids)
                
                with st.container():
                    st.markdown(f"**Verse {meta['verse']}**")
                    
                    # Display Content
                    st.markdown(f"**Original Shloka (Kannada Script):**")
                    st.code(meta['text'], language=None)
                    
                    # Play button for original Sanskrit verse
                    sanskrit_audio_key = f"audio_verse_{meta['verse']}_sa"
                    if sanskrit_audio_key in st.session_state:
                        st.audio(st.session_state[sanskrit_audio_key], format='audio/mp3')
                    else:
                        st.button(
                            f"🔊 Play Original Verse ({i+1})", 
                            key=f"play_sanskrit_{i}",
                            on_click=generate_audio_callback,
                            args=(i, meta['verse'], 'sa')
                        )
                    
                    st.markdown(f"**Kannada Translation:** {meta['translation']}")
                    st.markdown(f"**English Translation:** {meta['english_translation']}")
                    
                    # TTS for translation
                    text_to_speak = meta['english_translation'] if lang_choice == 'English' else meta['translation']
                    tts_lang = 'en' if lang_choice == 'English' else 'kn'
                    
                    # Unique key for this result's audio state - MUST match callback key
                    audio_state_key = f"audio_verse_{meta['verse']}_{tts_lang}"
                    
                    if debug_mode:
                        st.write(f"Looking for key: {audio_state_key}")
                        st.write(f"Keys in session_state: {[k for k in st.session_state.keys() if k.startswith('audio_')]}")
                    
                    # Check if audio exists in session state for this item
                    if audio_state_key in st.session_state:
                        audio_data = st.session_state[audio_state_key]
                        st.audio(audio_data, format='audio/mp3')
                        
                        # Add download button as fallback
                        st.download_button(
                            label="Download Audio",
                            data=audio_data,
                            file_name=f"verse_{meta['verse']}.mp3",
                            mime="audio/mp3",
                            key=f"dl_{i}"
                        )
                    else:
                        # Show "Play Audio" button if not yet generated
                        st.button(
                            f"Play Audio / ಆಡಿಯೋ ಪ್ಲೇ ಮಾಡಿ ({i+1})", 
                            key=f"play_audio_{i}",
                            on_click=generate_audio_callback,
                            args=(i, meta['verse'], tts_lang)
                        )

                    # Metrics Display
                    c1, c2 = st.columns(2)
                    c1.metric("Answer Relevance", f"{sim_score:.4f}")
                    c2.metric("Context Precision", f"{context_precision:.2f}")
                    
                    st.divider()

if __name__ == "__main__":
    main()
