def analyze_risk(clauses):
    report = []

    for clause in clauses:
        risk_score = 1
        category = "General"

        if "terminate" in clause.lower():
            risk_score = 3
            category = "Termination"

        if "liable" in clause.lower() or "liability" in clause.lower():
            risk_score = 5
            category = "Liability"

        risk_level = (
            "HIGH" if risk_score >= 4 else
            "MEDIUM" if risk_score >= 2 else
            "LOW"
        )

        report.append({
            "clause": clause,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "category": category
        })

    return report

