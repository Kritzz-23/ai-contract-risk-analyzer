RISK_WEIGHTS = {
    "liability": 3,
    "termination": 3,
    "penalty": 4,
    "indemnity": 5,
    "breach": 4,
    "damages": 3,
    "governing law": 2
}

def calculate_risk_score(clause: str) -> int:
    score = 0
    for keyword, weight in RISK_WEIGHTS.items():
        if keyword in clause.lower():
            score += weight
    return score

if __name__ == "__main__":
    test_clause = "The party shall be liable for breach and damages."
    score = calculate_risk_score(test_clause)
    print("Risk Score:", score)