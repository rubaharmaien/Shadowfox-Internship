import streamlit as st
from transformers import pipeline

# Load QA pipeline once (not per request)
@st.cache_resource
def load_model():
    return pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

qa_pipeline = load_model()

# Streamlit UI
st.title("AI Question Answering App 🤖")
st.write("Ask me anything! I'll try to give you close-to-accurate answers (not stories).")

# User inputs
context = st.text_area("📘 Provide context (e.g., a paragraph, article, or notes):", height=150)
question = st.text_input("❓ Ask your question:")

if st.button("Get Answer"):
    if context.strip() == "" or question.strip() == "":
        st.warning("Please provide both context and a question.")
    else:
        # Run QA pipeline
        result = qa_pipeline(question=question, context=context)
        st.success(f"**Answer:** {result['answer']}")
        st.caption(f"(Confidence: {result['score']:.2f})")
