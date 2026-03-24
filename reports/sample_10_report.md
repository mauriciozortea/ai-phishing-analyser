# Incident Report — sample_10.txt
**Date Analysed:** 2026-03-24 18:57
**Analyst:** Mauricio Zortea
**Severity:** High

---

## Executive Summary
This email is a financial phishing attack impersonating an internal "NorthBridge Wealth Management Division," targeting employees of NorthBridge Financial with a fraudulent cryptocurrency investment scheme. The email employs multiple social engineering tactics to lure recipients into clicking a malicious link hosted on a Russian-registered domain (`.ru`), likely designed to harvest credentials, personal data, or financial information. The promise of guaranteed high returns and zero risk is a hallmark of investment fraud, posing a significant financial and reputational risk to both the organisation and its employees.

---

## Indicators of Compromise (IOCs)
- **Sender email:** `investment-opportunities@northbridge-wealth.com`
- **Suspicious URLs:** `http://northbridge-wealth-invest.ru/exclusive/staff`
- **Suspicious attachments:** None detected
- **Spoofed domain:** `northbridge-wealth.com` impersonating the legitimate organisation domain `northbridgefinancial.co.uk`; redirect destination registered under `.ru` (Russian ccTLD)

---

## Phishing Techniques Identified

- **Domain Spoofing / Lookalike Domain:** The sender domain `northbridge-wealth.com` is crafted to appear affiliated with the legitimate organisation (`northbridgefinancial.co.uk`), exploiting brand familiarity to lower the recipient's guard.
- **False Authority / Impersonation:** The email claims to originate from an internal "NorthBridge Wealth Management Division," implying organisational legitimacy and insider access.
- **Exclusivity & Urgency (Scarcity Principle):** Phrases such as *"exclusively to NorthBridge staff"* and *"closes on Sunday"* are designed to pressure the recipient into acting quickly without due diligence.
- **Social Proof Manipulation:** The claim that *"over 200 NorthBridge colleagues have already joined"* fabricates peer participation to build false trust and reduce scepticism.
- **Too-Good-To-Be-True Financial Incentive:** A guaranteed 340% return with "zero risk" and "fully protected capital" is economically implausible and consistent with advance-fee fraud and investment scam patterns.
- **Malicious Link Obfuscation:** The call-to-action URL (`http://northbridge-wealth-invest.ru`) mimics the organisation's branding while routing to a foreign-registered domain, likely hosting a credential harvesting page or malware payload.
- **Trusted Context Exploitation:** Framing the offer as an "employee benefits programme" exploits the recipient's relationship with their employer to bypass natural suspicion.

---

## Verdict
**Classification:** Phishing
**Confidence:** High
**Reasoning:** This email exhibits a high concentration of well-documented phishing and financial fraud indicators. The sender domain does not match the organisation's legitimate domain, the embedded URL resolves to a `.ru` ccTLD entirely inconsistent with a UK financial institution, and the investment offer (340% guaranteed return, zero risk) is financially fraudulent by definition — no regulated investment product can legally make such guarantees. The combination of domain spoofing, urgency, false social proof, and a malicious foreign-hosted link leaves no credible interpretation other than a targeted phishing campaign.

---

## Recommended Actions
1. **Block and quarantine immediately** — Block the sender domain `northbridge-wealth.com` and the URL `http://northbridge-wealth-invest.ru` at the email gateway and web proxy. Quarantine any instances of this email across the organisation's mailboxes.
2. **Issue an internal user alert** — Notify all NorthBridge employees via a trusted internal channel (e.g., IT Security bulletin) warning them of this campaign, advising them not to click the link, and reminding them that no legitimate investment offer will be communicated via unsolicited email.
3. **Identify and assess exposed users** — Query email gateway logs to identify all recipients of this message. Follow up with anyone who clicked the link, initiating a containment and investigation workflow including credential resets, endpoint scans, and a review of any financial data potentially submitted.
4. **Report externally** — Submit the phishing URL and sender domain to the UK National Cyber Security Centre (NCSC) via the Suspicious Email Reporting Service