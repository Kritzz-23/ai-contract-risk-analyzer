CLAUSE_CATEGORIES = {
    "Confidentiality": ["confidential", "disclosure"],
    "Termination": ["terminate", "termination"],
    "Liability": ["liability", "indemnity"],
    "Governing Law": ["governing law", "jurisdiction"],
}

def classify_clause(clause: str) -> str:
    for category, keywords in CLAUSE_CATEGORIES.items():
        if any(k in clause.lower() for k in keywords):
            return category
    return "General"
if __name__ == "__main__":
    test_clause = "This agreement shall terminate upon breach."
    print(classify_clause(test_clause))
