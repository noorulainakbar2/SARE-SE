import pandas as pd

df = pd.read_csv("final_expanded_dataset.csv")

security_keywords = [
    "authentication", "authorization", "password", "access control",
    "encryption", "privacy", "secure", "security", "monitoring",
    "validation", "firewall", "risk", "safety", "audit", "logging",
    "ssh", "ssl", "https", "credential", "permission"
]

def classify_requirement(text):
    text = str(text).lower()
    for keyword in security_keywords:
        if keyword in text:
            return "Security"
    return "Non-Security"

df["baseline_prediction"] = df["requirement_text"].apply(classify_requirement)

df.to_csv("baseline_full_results.csv", index=False)

print("Full baseline run completed successfully!")
print("Total rows processed:", len(df))