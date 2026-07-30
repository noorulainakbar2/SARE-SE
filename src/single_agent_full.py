import pandas as pd
from openai import OpenAI

# Load expanded dataset
df = pd.read_csv("final_expanded_dataset.csv")

# Initialize OpenAI client
client = OpenAI()

# Single-agent classification function
def classify_requirement(requirement):

    prompt = f"""
You are a security requirements analysis agent.

Analyze the following software requirement and classify whether it contains security-related concerns.

Requirement:
{requirement}

Return only one label:
- Security
- Non-Security
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.1,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

# Apply classification
results = []

for index, req in enumerate(df["requirement_text"]):

    print(f"Processing requirement {index + 1}/{len(df)}")

    prediction = classify_requirement(req)

    results.append(prediction)

# Save results
df["single_agent_prediction"] = results

df.to_csv(
    "single_agent_full_results.csv",
    index=False
)

print("Full single-agent run completed successfully!")
print("Total rows processed:", len(df))