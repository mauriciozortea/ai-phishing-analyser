import anthropic
import os
from datetime import datetime

client = anthropic.Anthropic(api_key="YOUR_API_KEY_HERE")

def analyse_phishing_email(email_content, sample_name):

    prompt = f"""You are a Tier 1 SOC Analyst investigating a suspicious email.
Analyse the following email and produce a structured incident report.

EMAIL CONTENT:
{email_content}

Produce a report with exactly these sections:

## Incident Report — {sample_name}
**Date Analysed:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Analyst:** Mauricio Zortea
**Severity:** [Critical / High / Medium / Low]

## Executive Summary
[2-3 sentences describing what this email is and the threat it poses]

## Indicators of Compromise (IOCs)
- Sender email:
- Suspicious URLs:
- Suspicious attachments:
- Spoofed domain:

## Phishing Techniques Identified
[List the social engineering tactics used]

## Verdict
**Classification:** [Phishing / Spam / Legitimate / Uncertain]
**Confidence:** [High / Medium / Low]
**Reasoning:** [Why you reached this conclusion]

## Recommended Actions
1.
2.
3.

## MITRE ATT&CK Mapping
- Technique: [e.g. T1566.001 — Spearphishing Attachment]
"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text


def process_sample(filename):

    sample_path = f"samples/{filename}"

    with open(sample_path, "r", encoding="utf-8") as f:
        email_content = f.read()

    print(f"Analysing: {filename}...")

    report = analyse_phishing_email(email_content, filename)

    report_name = filename.replace(".txt", "_report.md")
    report_path = f"reports/{report_name}"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Report saved: {report_path}")
    print("-" * 50)


if __name__ == "__main__":
    samples = os.listdir("samples")

    if not samples:
        print("No samples found in /samples folder.")
    else:
        for sample in samples:
            if sample.endswith(".txt"):
                process_sample(sample)