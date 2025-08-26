import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("movies.csv")

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Precompute embeddings
embeddings = model.encode(df["plot"].tolist(), convert_to_tensor=True)

def search_movies(query, top_n=5):
    """
    Search for movies most relevant to the query using semantic similarity.
    Returns top_n rows from the dataset as a DataFrame.
    """
    query_embedding = model.encode([query], convert_to_tensor=True)
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    top_indices = similarities.argsort()[-top_n:][::-1]
    return df.iloc[top_indices]
