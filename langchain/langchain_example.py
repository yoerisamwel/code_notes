"""
# Introduction

## LangChain and PGVector:
1. **LangChain**:
   - `LangChain` is a framework for building applications powered by language models. It allows for document storage, embedding generation, and advanced querying.
   - It supports various vector stores, enabling efficient searches on large datasets by storing vectorized document embeddings.

2. **PGVector**:
   - `PGVector` is a PostgreSQL extension for vector similarity search. It allows users to store and query embeddings directly within a PostgreSQL database.
   - This is especially useful for building search engines where documents or data points are represented as vectors.

## Code Explanation:
- The script demonstrates how to create embeddings using Cohere's language model, store these embeddings in a PostgreSQL database (using PGVector), and perform similarity searches based on vectorized documents.
"""

from langchain_cohere import CohereEmbeddings
from langchain.core.documents import Document
from langchain_postgres import PGVector

# Initialize the embedding model
embeddings = CohereEmbeddings()

# Initialize the vector store with PostgreSQL connection
vectorstore = PGVector(
    embeddings=embeddings,
    collection_name="my_docs",
    connection="postgresql+psycopg://langchain:langchain@localhost:6024/langchain",
    use_jsonb=True,
)

# Add documents to the vector store
vectorstore.add_documents([
    Document(
        page_content="there are cats in the pond",
        metadata={"id": 1, "location": "pond", "topic": "animals"},
    ),
    Document(
        page_content="ducks are also found in the pond",
        metadata={"id": 2, "location": "pond", "topic": "animals"},
    ),
    Document(
        page_content="fresh apples are available at the market",
        metadata={"id": 3, "location": "market", "topic": "food"},
    ),
    Document(
        page_content="the new art exhibit is fascinating",
        metadata={"id": 5, "location": "museum", "topic": "art"},
    ),
])

# Perform a similarity search
results = vectorstore.similarity_search(
    "ducks",  # Search query
    k=2,      # Return top 2 results
    filter={"location": {"$in": ["pond", "market"]}},  # Filter by location
)

# Example Output:
# Document("ducks are also found in the pond")
# Document("there are cats in the pond")

# Additional Example: Searching for "apples"
apple_results = vectorstore.similarity_search(
    "apples",
    k=1,
    filter={"location": "market"},
)

# Explanation of Key Concepts:
# 1. **CohereEmbeddings**: This generates embeddings (numerical vectors) for the text data, which are used to represent semantic similarity.
# 2. **PGVector**: Allows for storing and querying these embeddings in a PostgreSQL database.
# 3. **Similarity Search**: The search uses vector comparison to find documents that are semantically similar to the query.