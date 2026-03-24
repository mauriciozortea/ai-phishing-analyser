# Incident Report — sample_09.txt
**Date Analysed:** 2026-03-24 19:01
**Analyst:** Mauricio Zortea
**Severity:** Critical

---

## Executive Summary
This email is a targeted spearphishing attack impersonating the NorthBridge Financial Services payroll department, designed to harvest sensitive banking and personal identity information from employees. The threat actor has constructed a convincing lookalike domain and is exploiting an imminent payroll deadline to pressure recipients into submitting their bank account details, sort code, and National Insurance number to an attacker-controlled website. If successful, this attack could result in direct financial fraud, salary diversion, and identity theft affecting the targeted employee.

---

## Indicators of Compromise (IOCs)
- **Sender email:** `payroll-update@northbridge-payroll.net`
- **Suspicious URLs:** `http://northbridge-payroll-secure.com/update/banking`
- **Suspicious attachments:** None identified
- **Spoofed domain:** `northbridge-payroll.net` and `northbridge-payroll-secure.com` — both impersonating the legitimate domain `northbridgefinancial.co.uk`

---

## Phishing Techniques Identified

- **Domain Spoofing / Lookalike Domain:** The sender domain `northbridge-payroll.net` and the linked domain `northbridge-payroll-secure.com` mimic the legitimate company domain (`northbridgefinancial.co.uk`) but are entirely separate, attacker-registered domains. The inclusion of the word *"secure"* in the URL is a common trust-building tactic.
- **Urgency and Artificial Deadline:** The email imposes a hard deadline of 28 March — just one day after the email date — pressuring the recipient to act quickly without verifying legitimacy.
- **Fear-Based Coercion:** The threat of a "delay of up to 14 working days" in salary payment is designed to provoke financial anxiety and override the recipient's critical judgement.
- **Spearphishing (Targeted Attack):** The email addresses the recipient by their first name ("Dear Mauricio") and references their specific employer, indicating the attacker has performed prior reconnaissance.
- **Credential and PII Harvesting:** The request for sort code, account number, employee ID, and National Insurance number constitutes a multi-vector data harvesting attempt targeting both financial and identity credentials.
- **Pretexting:** The attacker fabricates a plausible and routine business scenario — an "annual payroll system migration" — to lower the recipient's suspicion and provide a believable reason for the unusual request.
- **Unencrypted HTTP Link:** The malicious URL uses `http://` rather than `https://`, indicating no SSL certificate — a notable security red flag for any page requesting sensitive financial data.
- **Minimisation of Effort ("less than 2 minutes"):** This is a classic social engineering technique to reduce perceived friction and encourage immediate compliance before the recipient second-guesses the request.

---

## Verdict
**Classification:** Phishing
**Confidence:** High
**Reasoning:** The email displays multiple unambiguous indicators of a phishing attack. The sender domain (`northbridge-payroll.net`) does not match the legitimate organisation domain (`northbridgefinancial.co.uk`), and the linked URL (`northbridge-payroll-secure.com`) is similarly a lookalike domain with no affiliation to the genuine employer. Legitimate payroll departments would never solicit bank account re-confirmation via an unsolicited email link, particularly to an external domain. The combination of urgency, financial coercion, PII harvesting, and domain impersonation conclusively identifies this as a deliberate, targeted phishing campaign.

---

## Recommended Actions
1. **Do not click the link** — The URL `http://northbridge-payroll-secure.com/update/banking` should be treated as malicious. If the link has already been visited, escalate immediately to Tier 2/3 for endpoint inspection and potential credential reset.
2. **Block and quarantine** — Submit both domains (`northbridge-payroll.net` and `northbridge-payroll-secure.com`) to the security team for DNS/proxy blacklisting and email gateway blocking. Quarantine any further emails originating from the sender address.
3. **Notify and alert the wider organisation** — Inform the IT Security team and distribute an internal user