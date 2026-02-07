🧠 AI Contract Risk Analyzer

An AI-powered system to analyze legal contracts and identify risk levels using a hybrid approach combining rule-based logic and machine learning classification.

This project helps users quickly understand high-risk, medium-risk, and low-risk clauses in legal agreements such as NDAs, service contracts, and employment agreements.

🚀 Features

📄 Upload or paste a legal contract

✂️ Automatically split contract into clauses

⚖️ Rule-based risk scoring (LOW / MEDIUM / HIGH)

🤖 Machine Learning clause classification

📊 Risk analysis report with scores & categories

🧩 Modular, extensible architecture

🌐 Optional Streamlit web UI

🏗️ Project Architecture
ai-contract-risk-analyzer/
│
├── src/
│   ├── contract_loader.py      # Load contract text
│   ├── preprocessing.py        # Clean and normalize text
│   ├── clause_splitter.py      # Split text into clauses
│   ├── risk_analyzer.py        # Rule-based risk scoring
│   ├── ml_classifier.py        # ML model loader & predictor
│
├── data/
│   ├── raw_contracts/
│   │   └── nda_sample.txt
│   └── training_data.csv       # Labeled training dataset
│
├── models/
│   └── clause_classifier.pkl   # Pre-trained ML model
│
├── notebooks/                  # Model training (Colab)
├── app.py                      # Streamlit UI (optional)
├── main.py                     # Entry point
├── requirements.txt
└── README.md

🧠 How It Works
1️⃣ Contract Processing

Loads contract text

Cleans and normalizes content

Splits text into individual clauses

2️⃣ Rule-Based Risk Engine

Uses keyword and pattern matching to assign:

Risk Score (1–5)

Risk Level

LOW

MEDIUM

HIGH

Examples:

Unlimited liability → HIGH

Immediate termination → MEDIUM

Standard confidentiality → LOW

3️⃣ Machine Learning Classifier

A trained ML model classifies each clause into categories such as:

Confidentiality

Liability

Termination

Intellectual Property

General

📊 Sample Output
[HIGH] Score: 5 | RuleCat: Liability | MLCat: Liability
Unlimited Liability The Contractor agrees to indemnify...

[MEDIUM] Score: 3 | RuleCat: Termination | MLCat: Termination
The Company may terminate this Agreement immediately...

[LOW] Score: 1 | RuleCat: General | MLCat: Confidentiality
The Contractor shall implement reasonable safeguards...

⚙️ Installation & Setup
1️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Linux / Mac

source venv/bin/activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Analyzer
python main.py

📦 requirements.txt
pandas
scikit-learn
numpy
joblib
streamlit

🤖 Machine Learning Model

Trained in Google Colab

Saved as clause_classifier.pkl

Uses:

TF-IDF Vectorization

Logistic Regression

Loaded locally using joblib

⚠️ Note:
Ensure the scikit-learn version used locally matches the version used during training to avoid warnings.

🌐 Optional Streamlit UI

Run the web interface:

streamlit run app.py


Features:

Upload or paste contract text

Visual risk cards (LOW / MEDIUM / HIGH)

Clause-wise breakdown

🎯 Use Cases

Legal contract review

NDA risk analysis

Startup legal compliance checks

Educational / academic demonstrations

🧪 Current Limitations

ML model trained on a synthetic dataset

Rule-based engine relies on predefined keywords

Not a substitute for legal advice

🔮 Future Enhancements

Larger real-world legal datasets

Transformer-based models (BERT / LegalBERT)

PDF & DOCX upload support

Clause highlighting in UI

Risk mitigation suggestions

📚 Academic Note

This project demonstrates:

NLP preprocessing

Hybrid AI systems

Practical ML deployment

Real-world problem solving in LegalTech

🧑‍💻 Author

AI Contract Risk Analyzer
Developed as an academic / learning project.
