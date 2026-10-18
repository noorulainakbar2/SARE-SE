import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("multi_agent_full_results_v2.csv")

def clean_label(x):
    x = str(x).strip().lower()

    if "non-security" in x:
        return "Non-Security"

    if "security" in x:
        return "Security"

    return "Unknown"

gold = df["gold_category"].apply(clean_label)
pred = df["multi_agent_security"].apply(clean_label)

print("\nAccuracy:")
print(round(accuracy_score(gold, pred), 4))

print("\nClassification Report:")
print(classification_report(gold, pred))