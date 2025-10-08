import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st 
from src.model import load_QA_answerer

@st.cache_resource(show_spinner=False)
def get_model():
    return load_QA_answerer()

def main():
    try:
        st.set_page_config(page_title="QA with DistilBERT", page_icon="🤖", layout="wide")
    except:
        pass
    
    st.title("🤖 Question Answering with DistilBERT")
    
    with st.spinner("🤖 Loading DistilBERT model... This may take a few moments."):
        question_answerer = get_model()
    
    with st.sidebar:
        st.markdown("## 📋 About")
        st.markdown("🎯 This app uses DistilBERT to answer questions based on provided context.")
        st.markdown("📊 **Performance on SQuAD v1.1:**")
        st.markdown("• **F1 Score:** 86.60%")
        st.markdown("• **Exact Match (EM):** 79.03%")
        st.markdown("## 🔗 Links")
        st.markdown("🤖 [Pretrained Model](https://huggingface.co/distilbert-base-uncased-distilled-squad)")
        st.markdown("📚 [SQuAD v1.1 Dataset](https://datarepository.wolframcloud.com/resources/SQuAD-v1.1)")
        st.markdown("[📂 GitHub Repository](https://github.com/ahmedxnov/QA-DistilBERT)")
        st.markdown("---")
        st.markdown("**👨‍💻 Developer:** [Ahmad Khaled](https://www.linkedin.com/in/ahmad-khaled-hamed/)")
    
    context = st.text_area("📄 Context", height=200, placeholder="Enter the context paragraph here...")
    question = st.text_input("❓ Question", placeholder="Enter your question here...")
    
    if st.button("🔍 Get Answer"):
        if context.strip() == "" or question.strip() == "":
            st.warning("Please provide both context and question.")
        else:
            with st.spinner("Generating answer..."):
                result = question_answerer(question=question, context=context)
                answer = result.get("answer", "No answer found.")
            st.markdown("### 💡 Answer")
            st.success(answer)
            st.markdown(f"**Confidence Score:** {result.get('score', 0):.4f}")
            

if __name__ == "__main__":
    main()
        