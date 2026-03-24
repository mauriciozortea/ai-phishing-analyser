# Incident Report — sample_04.txt
**Date Analysed:** 2026-03-24 18:58
**Analyst:** Mauricio Zortea
**Severity:** Critical

---

## Executive Summary
This email is a highly targeted Business Email Compromise (BEC) / CEO Fraud attempt, impersonating the CEO of NorthBridge Financial Services and instructing the finance team to process an unauthorised wire transfer of £47,000. The threat actor is exploiting authority, urgency, and secrecy to bypass standard financial controls and approval processes. If acted upon, this attack would result in direct and likely irrecoverable financial loss to the organisation.

---

## Indicators of Compromise (IOCs)
- **Sender email:** `j.hartwell@northbridgefinancial-corp.co.uk`
- **Suspicious URLs:** None detected
- **Suspicious attachments:** None detected
- **Spoofed domain:** `northbridgefinancial-corp.co.uk` — typosquatting the legitimate domain `northbridgefinancial.co.uk` via insertion of `-corp` subdomain segment; the legitimate CEO email would be expected to originate from `@northbridgefinancial.co.uk`

---

## Phishing Techniques Identified

- **Domain Spoofing / Typosquatting:** The sender domain `northbridgefinancial-corp.co.uk` closely mimics the legitimate company domain `northbridgefinancial.co.uk`. A casual reader is unlikely to detect the discrepancy, particularly under time pressure.
- **CEO / Executive Impersonation:** The attacker poses as James Hartwell, CEO, leveraging positional authority to compel compliance from a subordinate in the finance team — a classic BEC pattern.
- **Artificial Urgency:** A hard deadline of 3:00 PM is imposed to prevent the recipient from following standard verification procedures or seeking managerial sign-off.
- **Phone Unavailability Pretext:** Claiming to be in a board meeting and unable to speak by phone is a deliberate social engineering tactic designed to pre-emptively block the most reliable verification method (a voice call).
- **Confidentiality / Isolation Instruction:** The explicit instruction *"do not discuss this with anyone else in the office"* is a major red flag — it is designed to isolate the target, suppress internal scrutiny, and prevent fraud controls from being invoked.
- **Plausible Business Pretext:** References to "Project Aurora — Q1 Settlement" and a confidential acquisition add a veneer of legitimacy and discourage the recipient from questioning the request.
- **Mobile Device Claim ("Sent from iPhone"):** Intended to excuse any brevity or informality in the message while adding a humanising, plausible touch to the impersonation.
- **Reply-Based Confirmation Request:** Requesting email confirmation rather than a formal approval chain bypasses standard financial authorisation workflows.

---

## Verdict
**Classification:** Phishing (Business Email Compromise — CEO Fraud)
**Confidence:** High
**Reasoning:** The combination of a spoofed lookalike domain, executive impersonation, an unsolicited high-value wire transfer request, artificial urgency, phone unavailability, and an explicit instruction to maintain secrecy are all hallmark indicators of a BEC/CEO fraud attack. No legitimate financial instruction of this nature would bypass dual-authorisation controls, arrive via an unverified external domain, or explicitly prohibit internal discussion. The beneficiary name "Meridian Consulting Partners Ltd" and account details cannot be verified against approved supplier records and should be treated as attacker-controlled. There are no legitimate business indicators present that would justify treating this email as authentic.

---

## Recommended Actions
1. **Do not process the transfer** — immediately notify the finance team member who received this email that they must take no action; quarantine the email and flag it within the email security platform.
2. **Verify out-of-band with the real CEO** — contact James Hartwell directly using a known, trusted phone number (not any contact details supplied in the email) to confirm he did not send this request.
3. **Preserve and escalate evidence** — retain full email headers, sender IP information, and the original message for forensic review; escalate to Tier 2/3 SOC and notify the IT Security Manager and relevant stakeholders per the IR playbook.
4. **Block the malicious domain** —