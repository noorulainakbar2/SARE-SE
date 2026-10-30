import pandas as pd

# Load datasets
pure_df = pd.read_csv("pure_sampled_345.csv")
dronology_df = pd.read_csv("dronology_requirements.csv")
github_df = pd.read_csv("github_requirements.csv")

# Keep only consistent columns
pure_df = pure_df[["id", "requirement_text", "source"]]

# Merge all datasets
merged_df = pd.concat([
    pure_df,
    dronology_df,
    github_df
], ignore_index=True)

# Save merged dataset
merged_df.to_csv(
    "final_expanded_dataset.csv",
    index=False
)

print("Datasets merged successfully!")
print("Total requirements:", len(merged_df))