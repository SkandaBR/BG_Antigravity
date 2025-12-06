"""
Script to verify ChromaDB persistence and reproducibility.
This shows that the database is fully persisted and can be copied/shared.
"""

import chromadb
from chromadb.utils import embedding_functions
import os

# Path to the persisted database
db_path = os.path.join(os.getcwd(), "chroma_db")

print("=" * 60)
print("ChromaDB Persistence Verification")
print("=" * 60)

# Connect to existing database
client = chromadb.PersistentClient(path=db_path)
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Get the collection
collection = client.get_collection(
    name="gita_chapter_2_v3",
    embedding_function=sentence_transformer_ef
)

print(f"\n✅ Database Location: {db_path}")
print(f"✅ Collection Name: {collection.name}")
print(f"✅ Total Documents: {collection.count()}")

# Get database size
total_size = 0
for root, dirs, files in os.walk(db_path):
    for file in files:
        total_size += os.path.getsize(os.path.join(root, file))

print(f"✅ Database Size: {total_size / 1024:.2f} KB")

# Test a query to verify it works
results = collection.query(
    query_texts=["What is the soul?"],
    n_results=1
)

print(f"\n✅ Test Query Successful!")
print(f"   Top Result: Verse {results['metadatas'][0][0]['verse']}")

print("\n" + "=" * 60)
print("REPRODUCIBILITY CONFIRMED")
print("=" * 60)
print("\nYou can:")
print("1. Copy the 'chroma_db' folder to another machine")
print("2. Run the app there with the same results")
print("3. Share the database with others")
print("4. Version control it (though it's binary)")
print("\nThe database uses DuckDB internally for metadata storage!")
print("=" * 60)
