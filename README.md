# 🍽️ Local AI Restaurant Review Assistant

A local **Retrieval-Augmented Generation (RAG)** application that uses cafe customer reviews to answer questions about restaurants and customer experiences.

The application combines **LangChain**, **ChromaDB**, **Ollama embeddings**, and **Llama 3.2** to retrieve relevant customer reviews and generate responses based on the retrieved context.

---

## Project Overview

This project explores the fundamentals of building a **local Retrieval-Augmented Generation (RAG)** system using a real-world cafe review dataset.

The application uses **775 customer reviews** from cafes across multiple cities in India. Users can ask questions about restaurants or customer experiences, and the system retrieves semantically relevant reviews before passing them to a locally hosted LLM for response generation.

This repository serves as the **baseline implementation** for a local RAG application. More advanced retrieval, grounding, filtering, and response-generation techniques will be explored in a separate project.

---

## RAG Pipeline

```text
Cafe Review Dataset
        ↓
   Pandas DataFrame
        ↓
  Document Creation
        ↓
  Ollama Embeddings
 (mxbai-embed-large)
        ↓
     ChromaDB
        ↓
 Semantic Retriever
      (k = 5)
        ↓
 Retrieved Context
        ↓
      Prompt
        ↓
     Llama 3.2
        ↓
  Generated Answer
```

---

## Technologies Used

- Python
- Pandas
- LangChain
- ChromaDB
- Ollama
- Llama 3.2
- mxbai-embed-large
- Jupyter Notebook
- Git / GitHub

---

## Dataset

This project uses the **CafeCritic: A Flavorful Dataset of Cafe Reviews** dataset from Kaggle.

**Source:** [CafeCritic: A Flavorful Dataset of Cafe Reviews](https://www.kaggle.com/datasets/juhibhojani/zomato-cafe-reviews)

### About the Dataset

According to the dataset author:

> "Uncover the essence of cafe experiences with CafeCritic, a comprehensive dataset that captures the aroma and ambiance of cafes through genuine customer reviews."

The dataset contains cafe information and customer reviews, including:

- Cafe name
- Overall rating
- Cuisine
- Average cost for two people
- City
- Customer-written review

### Dataset Columns

| Column | Description |
|---|---|
| `Index` | Unique identifier for each review entry |
| `Name` | Name of the cafe being reviewed |
| `Overall_Rating` | Overall rating of the cafe |
| `Cuisine` | Types of cuisine offered by the cafe |
| `Rate for two` | Average cost for two people |
| `City` | City where the cafe is located |
| `Review` | Customer-written review describing their experience |

### Dataset Used in This Project

The dataset used in this project contains:

- **775 reviews**
- **299 unique cafes**
- **10 cities**

The `Index` column was excluded from the document content and metadata because it does not provide useful semantic information for the retrieval task.

---

## Document Representation

Each review is converted into a LangChain `Document` containing both review content and structured metadata.

### Document Content

The following information is included in the document content:

```text
Restaurant
City
Rating
Cuisine
Rate for Two
Review
```

### Metadata

The following structured fields are stored as metadata:

```text
restaurant
city
rating
cuisine
rate_for_two
```

This approach preserves both the **natural-language review** and relevant **restaurant attributes**, allowing the retrieved documents to provide richer context to the language model.

---

## Vector Database and Retrieval

The application uses **ChromaDB** as its local vector database.

The `mxbai-embed-large` embedding model converts each review document into a vector representation. These vectors are stored locally in ChromaDB.

For each user question, the retriever returns the **5 most semantically relevant documents**.

The retrieved documents are then passed to **Llama 3.2** as context for response generation.

The vector database is generated locally and is **not included in the repository**.

---

## Retrieval Testing

The retrieval pipeline was tested independently before connecting it to the language model.

### Restaurant-Specific Query

```text
What do customers say about The Chocolate Room?
```

The retriever successfully returned relevant reviews for **The Chocolate Room** across multiple cities.

### Concept-Based Query

```text
What do customers say about the food quality?
```

The retriever returned reviews from multiple cafes discussing food quality, taste, preparation, and related customer experiences.

These tests were used to verify that the semantic retrieval layer was returning relevant context before evaluating the generated LLM responses.

---

## Example

### User

```text
What do customers say about The Chocolate Room?
```

### Assistant

```text
Based on the provided context, here's what customers say about The Chocolate Room:

- Some customers liked the ambiance and certain dishes.
- Some reviewers reported issues with shakes, cheesecake, and other food items.
- One reviewer reported problems with food packaging.
- Other customers described their experience positively.

Overall, the available reviews suggest mixed customer experiences.
```

---

## Project Structure

```text
local-rag-cafe-reviews/
│
├── .gitignore
├── main.py
├── vector.py
├── reviews.ipynb
└── README.md
```

### `main.py`

Handles:

- Local LLM initialization
- Prompt construction
- User interaction
- Review retrieval
- LLM response generation

### `vector.py`

Handles:

- Dataset loading
- Document creation
- Embedding initialization
- ChromaDB initialization
- Document vectorization
- Retriever initialization

### `reviews.ipynb`

Used for dataset inspection and exploratory analysis before integrating the dataset into the RAG pipeline.

---

## Current Limitations

This repository represents the **baseline version** of the local RAG application.

Current limitations include:

- Retrieval is currently limited to the top 5 documents.
- Cafe branches across different cities are not explicitly separated during retrieval.
- The LLM may occasionally make minor interpretation or counting errors when synthesizing reviews.
- The application does not currently provide source citations for individual claims.
- There is no conversational memory between questions.

---

## Future Development

Further improvements to:

- Retrieval quality
- Restaurant and location filtering
- Context grounding
- Response accuracy
- Source attribution
- Conversational capabilities

will be explored in a **separate project**.

This repository will remain as the **baseline implementation and reference point for future experimentation**.

---

## Dataset Setup

The dataset used for this project is included in the repository as:

```text
reviews.csv
```

The expected structure is:

```text
local-rag-cafe-reviews/
│
├── main.py
├── vector.py
├── reviews.ipynb
├── reviews.csv
├── .gitignore
└── README.md
```

---

## How to Run

### 1. Clone the Repository

```bash
git clone <repository-url>
cd local-rag-cafe-reviews
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

Windows:

```powershell
.venv\Scripts\activate
```

### 4. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 5. Install and Run Ollama

The application uses the following local models:

- `llama3.2`
- `mxbai-embed-large`

Make sure both models are available through Ollama before running the application.

### 6. Generate the Vector Database

Run:

```powershell
python .\vector.py
```

This creates the local ChromaDB vector database from `reviews.csv`.

### 7. Run the Assistant

Run:

```powershell
python .\main.py
```

The terminal will display:

```text
==================================================
        🍽️ RESTAURANT REVIEW ASSISTANT
==================================================

Type a question... (press 'q' to quit):
```

Type `q` to exit the application.

---

## Note

This project is a learning and portfolio project focused on understanding the fundamentals of **local Retrieval-Augmented Generation (RAG)**, including:

- Document processing
- Text embeddings
- Vector databases
- Semantic retrieval
- Prompt construction
- Context-based generation
- Local LLM inference

The project demonstrates an end-to-end RAG workflow while keeping the system lightweight and fully local.