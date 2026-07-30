import pandas as pd
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

df = pd.read_csv("final_evaluation_dataset.csv")

def clean_label(x):
    x = str(x).strip().lower()
    if "non-security" in x or "non security" in x:
        return "Non-Security"
    if "security" in x:
        return "Security"
    return "Non-Security"

df["gold_category_clean"] = df["gold_category"].apply(clean_label)
df["baseline_clean"] = df["baseline_prediction"].apply(clean_label)
df["single_clean"] = df["single_agent_prediction"].apply(clean_label)
df["multi_clean"] = df["multi_agent_security"].apply(clean_label)

labels = ["Non-Security", "Security"]

def evaluate(name, y_pred):
    print(f"\n========== {name} RESULTS ==========")
    print("Accuracy:", accuracy_score(df["gold_category_clean"], y_pred))
    print("\nClassification Report:")
    print(classification_report(df["gold_category_clean"], y_pred, labels=labels))
    print("\nConfusion Matrix:")
    print(confusion_matrix(df["gold_category_clean"], y_pred, labels=labels))

evaluate("BASELINE", df["baseline_clean"])
evaluate("SINGLE-AGENT", df["single_clean"])
evaluate("MULTI-AGENT", df["multi_clean"])

df.to_csv("final_evaluation_dataset_cleaned.csv", index=False)
print("\nCleaned evaluation dataset saved.")
