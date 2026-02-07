def load_contract(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    print("✅ Contract loaded successfully!")
    return text

