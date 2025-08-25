Advanced NLP Project: Question Answering with DistilBERT & RoBERTa

📌 Overview

This project explores and deploys Question Answering (QA) Language Models using Hugging Face Transformers.
It consists of two main parts:

Analysis Notebook (Advance_Level_final.ipynb) — in-depth exploration and comparison of DistilBERT and RoBERTa.

Streamlit App (streamlit_app.py) — interactive demo that allows users to input context and questions, and receive model-generated answers.

The project aligns with advanced NLP/ML tasks: implementation, exploration, visualization, research questions, and deployment.

⚙️ Models Used

DistilBERT → distilbert-base-cased-distilled-squad

RoBERTa → deepset/roberta-base-squad2

Both are extractive QA models fine-tuned on the SQuAD dataset.

🚀 How to Run
1. Notebook (Analysis)

Run the notebook in Google Colab or locally:

pip install -r requirements.txt
jupyter notebook Advance_Level_final.ipynb


Or open directly in Google Colab:
👉 Open Advance_Level_final.ipynb in Colab

2. Streamlit App (Deployment)

Run locally:

pip install -r requirements.txt
streamlit run streamlit_app.py


Deploy on Streamlit Cloud
 or Hugging Face Spaces
.

🔎 Research Questions Explored

Which model is more confident overall?
→ RoBERTa is usually more confident.

Do models give consistent answers?
→ Both identify lunar maria and lava correctly, though phrasing may differ.

How do models handle myth-based questions?
→ Both can extract text about legends (e.g., people once believed the Moon had figures).

📊 Key Insights

DistilBERT: Lightweight, fast, but less nuanced.

RoBERTa: Stronger, more confident, but heavier.

Both are limited to extractive QA (they can’t invent answers beyond context).

Applications: education, research, quick knowledge retrieval.

Future: hybrid systems combining extractive + generative models.

🙌 Credits

Hugging Face Transformers

Streamlit

PyTorch
