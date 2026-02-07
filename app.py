import streamlit as st
from src.contract_loader import load_contract
from src.preprocessing import preprocess_text
from src.clause_splitter import split_clauses
from src.risk_analyzer import analyze_risk
from src.ml_classifier import ClauseMLClassifier

st.set_page_config(
    page_title="AI Contract Risk Analyzer",
    layout="wide"
)

st.title("📄 AI Contract Risk Analyzer")
st.write("Upload or paste a legal contract to analyze risk using rules + ML")

# Input section
contract_text = st.text_area(
    "📑 Paste Contract Text Here",
    height=300,
    placeholder="Paste NDA / Agreement / Contract text..."
)

uploaded_file = st.file_uploader(
    "📤 Or upload a .txt contract file",
    type=["txt"]
)

analyze_button = st.button("🔍 Analyze Contract")

if analyze_button:
    if uploaded_file:
        contract_text = uploaded_file.read().decode("utf-8")

    if not contract_text.strip():
        st.warning("Please upload or paste a contract.")
    else:
        with st.spinner("Analyzing contract..."):
            text = preprocess_text(contract_text)
            clauses = split_clauses(text)
            rule_results = analyze_risk(clauses)

            ml_classifier = ClauseMLClassifier()
            ml_labels = ml_classifier.predict(clauses)

        st.success("Analysis completed!")

        # Display results
        st.subheader("📊 Risk Analysis Results")

        for item, ml_label in zip(rule_results, ml_labels):
            col1, col2, col3 = st.columns([1, 2, 6])

            with col1:
                if item["risk_level"] == "HIGH":
                    st.error("HIGH")
                elif item["risk_level"] == "MEDIUM":
                    st.warning("MEDIUM")
                else:
                    st.success("LOW")

            with col2:
                st.write(f"**Score:** {item['risk_score']}")
                st.write(f"**ML Category:** {ml_label}")

            with col3:
                st.write(item["clause"])

            st.divider()
