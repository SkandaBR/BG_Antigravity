# Role
You are an expert AI Engineer and Python Developer specializing in Streamlit, RAG (Retrieval Augmented Generation), and NLP.

# Task
Build a Streamlit application that serves as a Q&A bot for "Chapter 2 of the Bhagavad Gita" using the provided `bhagavadgita_Chapter_2.json` file.

# Specifications

1.  **Data Ingestion & Vector Store:**
    * Load the `bhagavadgita_Chapter_2.json` file.
    * Parse the JSON to extract verses. Each document in the store should contain the `translation` (Kannada) and `english_translation` combined or indexed suitably.
    * Use `ChromaDB` as the vector store.
    * Use a standard open-source embedding model (like `all-MiniLM-L6-v2` from `sentence-transformers`) to embed the text.

2.  **User Interface (Streamlit):**
    * **Title:** "Bhagavad Gita Ch. 2 - AI Assistant".
    * **TTS Settings:** Add Radio Buttons to select the TTS (Text-to-Speech) output language: 'English' or 'Kannada'.
    * **Input Area:** A text input box for the user to ask questions.
    * **Sample Questions:** Display 3-4 clickable "Auto Preview" questions (English and Kannada - the selection should be top level selectgion )  extracted from the content (e.g., "What is the nature of the soul?", "ಆತ್ಮದ ಸ್ವರೂಪವೇನು?"). Clicking these should populate the search.

3.  **Search & Retrieval:**
    * When a question is asked, convert the query to an embedding and retrieve the **Top K** (e.g., k=3) relevant verses from the Chroma vector store.
    * **Strict Anti-Hallucination:** The answer must be derived *only* from the retrieved JSON content. If the distance/similarity score indicates low relevance (set a reasonable threshold), explicitly state: "This data store does not have the required answer."

4.  **Response Generation & TTS:**
    * Display the relevant verses found (Sanskrit text, Kannada translation, and English translation).
    * Implement Text-to-Speech using a library like `gTTS` (Google Text-to-Speech).
    * Play the audio of the summary/answer in the selected language (English or Kannada) automatically or via a play button.

5.  **RAG Metrics Display:**
    * For every result, calculate and display these two metrics in the UI:
        * **Context Precision:** (Calculate the ratio of relevant retrieved documents to the total k retrieved).
        * **Answer Relevance:** (Compute the cosine similarity between the User Query embedding and the Retrieved Result embedding).


Generate the complete app.py file and a requirements.txt file needed to run this application.


# Code Structure
* Ensure the code is modular.
* Cache the model loading and database creation using `@st.cache_resource` to improve performance.
* Handle errors gracefully (e.g., if the JSON file is missing).

# JSON Structure Reference
The file `bhagavadgita_Chapter_2.json` has the following structure:
```json
{
  "chapters": [
    {
      "chapter_number": 2,
      "verses": [
        {
          "verse": 1,
          "text": "Sanskrit text...",
          "translation": "Kannada translation...",
          "english_translation": "English translation..."
        }
      ]
    }
  ]
}

1. Create a virtual environment (Windows):
```bash
python -m venv .venv
```

2. Activate the virtual environment:
```bash
.venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt

streamlit run app.py
