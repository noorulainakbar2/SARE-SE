import pandas as pd

df = pd.read_csv("final_comparison_dataset.csv")

def clean_text(x):
    return str(x).lower()

def assign_gold_category(row):
    text = clean_text(row["requirement_text"])
    source = str(row["source"]).lower()

    # PURE: use keyword-independent semantic/security mapping
    if source == "pure":
        security_terms = [
            "secure", "security", "privacy", "confidential", "encrypt",
            "authentication", "authorization", "access", "permission",
            "audit", "log", "monitor", "risk", "safe", "safety"
        ]
        if any(term in text for term in security_terms):
            return "Security"
        return "Non-Security"

    # Dronology: safety/security operational requirements
    if source == "dronology":
        return "Security"

    # GitHub: map security-related project requirements
    github_security_terms = [
        "secure", "security", "ssh", "ssl", "https", "credential",
        "firewall", "permission", "validate", "validation", "risk",
        "monitor", "configuration", "access", "protection"
    ]
    if any(term in text for term in github_security_terms):
        return "Security"
    return "Non-Security"


def assign_gold_complexity(row):
    text = clean_text(row["requirement_text"])
    word_count = len(text.split())

    if word_count <= 10:
        return "Simple"
    elif word_count <= 18:
        return "Moderate"
    else:
        return "Complex"


df["gold_category"] = df.apply(assign_gold_category, axis=1)
df["gold_complexity"] = df.apply(assign_gold_complexity, axis=1)

df.to_csv("final_comparison_with_gold_labels.csv", index=False)

print("Gold labels added successfully!")
print("Total rows:", len(df))
print("\nGold category distribution:")
print(df["gold_category"].value_counts())
print("\nGold complexity distribution:")
print(df["gold_complexity"].value_counts())