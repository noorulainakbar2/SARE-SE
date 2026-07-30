import os
import time
import pandas as pd
from openai import OpenAI

INPUT_FILE = "final_comparison_with_gold_labels.csv"
OUTPUT_FILE = "multi_agent_refined_full_results.csv"

df = pd.read_csv(INPUT_FILE)

if os.path.exists(OUTPUT_FILE):
    out_df = pd.read_csv(OUTPUT_FILE)
    print(f"Resuming from existing file: {OUTPUT_FILE}")
else:
    out_df = df.copy()
    out_df["multi_agent_security"] = ""
    out_df["multi_agent_complexity"] = ""
    out_df["verification_result"] = ""

client = OpenAI(timeout=40, max_retries=2)

def ask_model(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.1,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()

def multi_agent_analysis(requirement):
    security_prompt = f"""
You are a strict security requirements classification agent.

Classify the following software requirement as Security or Non-Security.

Use Security only if the requirement explicitly states or clearly implies a security control, protection mechanism, restriction, audit requirement, encryption, authentication, authorization, access-control rule, credential protection, secure communication, firewall protection, risk control, safety-critical protection, or prevention of unauthorized access.

Use Non-Security if the requirement is mainly about normal functionality, usability, workflow, content display, recommendation, scheduling, storage duration, administrative process, regulatory description, payment workflow, or general system operation without a direct security control requirement.

Mentioning data, users, system, processing, information, access, password, or payment is not sufficient by itself. Classify as Security only when the requirement imposes a clear security-related protection, restriction, monitoring, audit, authentication, authorization, encryption, or risk-control requirement.

Requirement:
{requirement}

Return exactly one label:
Security
Non-Security
"""
    security_result = ask_model(security_prompt)

    complexity_prompt = f"""
You are a software requirements complexity analysis agent.

Analyze the following requirement and estimate its complexity level.

Requirement:
{requirement}

Return exactly one label:
Simple
Moderate
Complex
"""
    complexity_result = ask_model(complexity_prompt)

    verification_prompt = f"""
You are a verifier agent for security requirements classification.

Requirement:
{requirement}

Initial Security Classification:
{security_result}

Complexity Classification:
{complexity_result}

Check whether the initial security classification is reasonable.

Return exactly one label:
Verified
Needs Review
"""
    verification_result = ask_model(verification_prompt)

    final_security_result = security_result

    if "needs review" in verification_result.lower():
        refinement_prompt = f"""
You are a senior security requirements reviewer.

Requirement:
{requirement}

Initial Security Classification:
{security_result}

The verifier flagged this classification for review.

Re-evaluate the requirement carefully.

Classify as Security only if the requirement explicitly specifies a security control, authentication, authorization, encryption, audit logging, monitoring for security, access restriction, privacy protection, integrity protection, credential protection, secure communication, firewall protection, risk control, safety-critical protection, or prevention of unauthorized access.

Classify as Non-Security if the requirement is mainly about normal functionality, usability, workflow, content display, recommendation, scheduling, storage duration, administrative process, regulatory description, payment workflow, or general system operation without a direct security control requirement.

Mentioning data, users, system, processing, information, access, password, or payment is not sufficient by itself.

Return exactly one label:
Security
Non-Security
"""
        final_security_result = ask_model(refinement_prompt)

    return final_security_result, complexity_result, verification_result

for index, row in out_df.iterrows():
    already_done = str(row.get("multi_agent_security", "")).strip()

    if already_done and already_done.lower() != "nan":
        continue

    req = row["requirement_text"]
    print(f"Processing requirement {index + 1}/{len(out_df)}")

    try:
        security_result, complexity_result, verification_result = multi_agent_analysis(req)

        out_df.at[index, "multi_agent_security"] = security_result
        out_df.at[index, "multi_agent_complexity"] = complexity_result
        out_df.at[index, "verification_result"] = verification_result

        out_df.to_csv(OUTPUT_FILE, index=False)
        time.sleep(0.3)

    except Exception as e:
        print(f"Error at row {index + 1}: {e}")
        out_df.to_csv(OUTPUT_FILE, index=False)
        break

print("Refined multi-agent TEST run saved.")
print("Completed rows:", out_df["multi_agent_security"].astype(str).str.strip().ne("").sum())
print("Total rows:", len(out_df))

print("\nVerification distribution:")
print(out_df["verification_result"].value_counts())

print("\nSecurity prediction distribution:")
print(out_df["multi_agent_security"].value_counts())