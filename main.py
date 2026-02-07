from src.contract_loader import load_contract
from src.preprocessing import preprocess_text
from src.clause_splitter import split_clauses
from src.risk_analyzer import analyze_risk
from src.ml_classifier import ClauseMLClassifier


def main():
    # 1. Load contract
    text = load_contract("data/raw_contracts/nda_sample.txt")

    # 2. Preprocess text
    text = preprocess_text(text)

    # 3. Split into clauses
    clauses = split_clauses(text)

    # 4. Rule-based risk analysis
    report = analyze_risk(clauses)

    # 5. ML-based classification (LOAD MODEL, NO TRAINING)
    ml_classifier = ClauseMLClassifier()
    ml_labels = ml_classifier.predict(clauses)

    # 6. Display results
    print("\n--- AI Contract Risk Analysis Report ---\n")

    for item, ml_label in zip(report[:10], ml_labels[:10]):
        print(
            f"[{item['risk_level']}] "
            f"Score: {item['risk_score']} | "
            f"RuleCat: {item['category']} | "
            f"MLCat: {ml_label} | "
            f"{item['clause'][:60]}"
        )


if __name__ == "__main__":
    main()
