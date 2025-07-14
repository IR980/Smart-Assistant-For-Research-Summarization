
# 🧠 Smart Assistant for Research Summarization

A GenAI-powered assistant that reads uploaded documents and helps users:
- Answer complex, logic-based questions
- Summarize research material
- Evaluate user comprehension
- Justify all answers with references from source
- A powerful, interactive assistant that helps you summarize, query, and test
- your understanding of research documents (PDF/TXT)
- using advanced language models and semantic search.
-  Built with Streamlit for an intuitive dashboard experience.

---

## 🌐 Live Link

https://smartassistantirshad.streamlit.app/

---

## 🎥 Demo Photo/Video

---
<img width="1902" height="1022" alt="smart-1" src="https://github.com/user-attachments/assets/f57dc272-36b3-4935-9ca4-0525050d8c40" />


---

<img width="1912" height="1030" alt="smart-2" src="https://github.com/user-attachments/assets/ecf6fd9c-4e9c-43af-bdc5-687309cce1b3" />

---
<img width="1907" height="1022" alt="smart-3" src="https://github.com/user-attachments/assets/e2c5ef92-d086-4246-809b-f6bf14cb97a7" />

---

📹 Loom: https://www.loom.com/share/31957017e6bb4e25acc374133c3927db

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/IR980/smart-assistant-research-summarization.git
cd smart-assistant-research-summarization

```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
venv/Scripts/activate
      
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run src/app.py

```
### 4. Set up API Key
# Create a .env file:
```
OPENAI_API_KEY=your_openai_key_here

```
---

## 📂 Project Structure

```
src/
│
├── app.py                        # Main Streamlit app
├── challenge/
│   └── question_generator.py     # Challenge mode logic
├── embedding/
│   ├── embedder.py               # Embedding functions
│   └── vector_store.py           # Vector search
├── utils/
│   └── helpers.py                # Utilities (chunking, highlighting, etc.)
├── document_processing/
│   ├── pdf_parser.py             # PDF text extraction
│   └── text_extractor.py         # TXT extraction
├── qa/
│   ├── question_answering.py     # LLM Q&A logic
│   └── openai_client.py          # OpenAI client
└── evaluator/
    └── answer_evaluator.py       # Answer evaluation logic

```

---

## 🧱 Architecture / Reasoning Flow

### Modules:


 - **main.py** – User interface (Streamlit) and backend interaction
 - **logic.py** - Core logic and LLM/document processing
 - **utils.py** - Helper and utility functions

### Flow:

1. Launches the Streamlit app.
2. Manages file upload, mode selection, and user inputs.
3. Calls functions from logic.py and displays results.
4. Handles text extraction from PDF/TXT.
5. Splits text into chunks and generates embeddings.
6. Performs semantic search and context retrieval.
7. Interfaces with the LLM for Q&A, summarization, and challenge generation
8. Text chunking and formatting utilities.
9. Prompt construction helpers.
10. Answer evaluation and scoring functions.

---

## 🧪 Tech Stack

- Python 3.10+
- Streamlit
- sentence-transformers
- PyMuPDF (pip install pymupdf)
- penAI Python SDK
- See requirements.txt for full list

---

## 🎥 Demo Photo/Video 



📹 Loom: [https://www.loom.com/share/your-demo-link](https://www.loom.com/share/31957017e6bb4e25acc374133c3927db)

---

## 🧑‍💻 Author

**Irshad Alam**  
[GitHub](https://github.com/IR980)


Built with ❤️ using Gemini + Streamlit By Irshad
