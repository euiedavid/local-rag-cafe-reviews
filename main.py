# import libraries

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# initialize model
model = OllamaLLM(model="llama3.2")

# define what the model will do
# template = """
# You are an expert in answering questions about a pizza restaurant

# Here are the relevant reviews: {reviews}

# Here is the question to answer: {question}
# """

template = """
You are a helpful AI assistant that answers questions about restaurants
using customer reviews and restaurant information provided in the context.

Use the provided context to answer the user's question.

Context:
{reviews}

Question:
{question}

Answer the question based only on the provided context.
If the context does not contain enough information to answer the question,
say that the available reviews do not provide enough information.
"""

prompt = ChatPromptTemplate.from_template(template)

# invoke entire chain to combine everything and run the llm
chain = prompt | model

# create loop for continuous chat
while True:
    print("\n" + "=" * 50)
    print("\t 🍽️   RESTAURANT REVIEW ASSISTANT")
    print("=" * 50)
    print()
    
    question = input("Type a question... (press 'q' to quit): ")
    
    if question.strip().lower() == "q":
        print("Talk to you later!")
        break
    
    context = retriever.invoke(question)
    result = chain.invoke({'reviews': context, 'question': question})
    print("\nAssistant: ")
    print(result)