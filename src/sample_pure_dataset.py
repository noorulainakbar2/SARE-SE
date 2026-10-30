import pandas as pd

# Load PURE dataset
df = pd.read_csv("pure_dataset.csv", encoding="latin1")

# Rename columns
df = df.rename(columns={
    "sentence": "requirement_text"
})

# Separate security and non-security requirements
security_df = df[df["security"] == 1]
non_security_df = df[df["security"] == 0]

# Sample balanced subset for 345 PURE requirements
security_sample = security_df.sample(n=230, random_state=42)
non_security_sample = non_security_df.sample(n=115, random_state=42)

# Combine samples
sampled_df = pd.concat([security_sample, non_security_sample])

# Add source column
sampled_df["source"] = "PURE"

# Select required columns
final_df = sampled_df[[
    "id",
    "requirement_text",
    "source",
    "security",
    "reliability",
    "NFR_boolean"
]]

# Save sampled dataset
final_df.to_csv(
    "pure_sampled_345.csv",
    index=False
)

print("PURE sampled dataset created successfully!")
print("Total rows:", len(final_df))