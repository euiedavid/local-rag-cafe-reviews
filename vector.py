# vector store database
# this will be considered a stockroom for relevant data
# to also give the llm a more contextually relevant replies

# embedding modules
# these essentially take the texts then convert it to a vector
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

# load csv
df = pd.read_csv("reviews.csv")

# initialize embedding model
embeddings = OllamaEmbeddings(model='mxbai-embed-large')

# location to store vector database
# create folder to store database
db_location = "./reviews_chroma_db"
add_documents = not os.path.exists(db_location)

# create individual documents
# add them to vector store
if add_documents:
    documents = []
    
    ids = []
    
    for i, row in df.iterrows():
        document = Document(
            page_content = (
                f"Restaurant: {row['Name']}\n"
                f"City: {row['City']}\n"
                f"Rating: {row['Overall_Rating']}\n"
                f"Cuisine: {row['Cuisine']}\n"
                f"Rate for two: {row['Rate for two']}\n"
                f"Review: {row['Review']}"
            ),
            metadata={
                "restaurant": row['Name'],
                "city": row['City'],
                "rating": row['Overall_Rating'],
                "cuisine": row['Cuisine'],
                "rate_for_two": row['Rate for two']
            },
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)
        
# initialize vector store
vector_store = Chroma(
    collection_name='restaurant_reviews',
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)


# initialize retriever
# retrieves the 5 most semantically relevant doc for a user query
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)

# test retrieval
# test_results = retriever.invoke("What do customers say about the chocolate room?")
# test_results = retriever.invoke("what do customers say about the food quality?")

# for result in test_results:
#     print("\n---")
#     print(result.page_content)
#     print(result.metadata)