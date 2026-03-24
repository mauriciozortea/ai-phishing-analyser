# Incident Report — sample_02.txt
**Date Analysed:** 2026-03-24 18:59
**Analyst:** Mauricio Zortea
**Severity:** High

---

## Executive Summary
This email is a phishing attempt impersonating Barclays Bank UK, targeting an employee at Northbridge Financial via a fraudulent security alert about a suspicious transaction. The email attempts to manipulate the recipient into clicking a malicious link designed to harvest banking credentials through a spoofed login page. The threat poses significant risk of financial loss and credential compromise to both the individual recipient and potentially the broader organisation.

---

## Indicators of Compromise (IOCs)
- **Sender email:** secure-alerts@barclays-verify.com
- **Suspicious URLs:** http://barclays-secure-verify.net/dispute/login
- **Suspicious attachments:** None identified
- **Spoofed domain:** barclays-verify.com *(sender)* / barclays-secure-verify.net *(link)* — both impersonating the legitimate barclays.co.uk domain

---

## Phishing Techniques Identified

- **Brand Impersonation:** The email mimics Barclays Bank's visual language, tone, and even includes a legitimate-looking physical address (1 Churchill Place, London E14 5HP) to establish false credibility.
- **Urgency and Artificial Time Pressure:** The 2-hour response window with threat of permanent fund transfer is a classic pressure tactic designed to override the recipient's critical thinking.
- **Fear Induction / Threat of Financial Loss:** Citing a specific, large transaction amount (£3,847.00) to a crypto exchange creates alarm and emotional distress, increasing the likelihood of impulsive action.
- **Specificity as a Trust Mechanism:** Inclusion of precise transaction details (amount, merchant name, location, timestamp) lends false legitimacy to the claim.
- **Lookalike Domain Abuse (Typosquatting):** Both domains — `barclays-verify.com` and `barclays-secure-verify.net` — are constructed to visually resemble the authentic Barclays domain while operating entirely outside Barclays' infrastructure.
- **HTTP (Non-Encrypted) Link:** The malicious URL uses plain `http://` rather than `https://`, indicating a lack of proper security infrastructure consistent with a hastily constructed phishing page.
- **Generic Salutation:** The greeting "Dear Barclays Customer" rather than the recipient's name suggests a mass-phishing campaign rather than a targeted, account-aware communication.

---

## Verdict
**Classification:** Phishing
**Confidence:** High
**Reasoning:** Multiple converging indicators confirm this as a phishing email. The sending domain (`barclays-verify.com`) is not affiliated with Barclays Bank, whose legitimate domain is `barclays.co.uk`. The embedded link routes to a second unrelated lookalike domain (`barclays-secure-verify.net`) over an unencrypted HTTP connection — consistent with a credential harvesting page. The combination of urgency tactics, fear-based messaging, brand spoofing, and fraudulent infrastructure leaves no reasonable doubt as to the malicious intent of this email.

---

## Recommended Actions
1. **Quarantine and Block:** Immediately quarantine the email across all mailboxes and block both domains (`barclays-verify.com` and `barclays-secure-verify.net`) at the email gateway and web proxy/firewall level.
2. **Notify the Recipient:** Contact m.thompson@northbridgefinancial.co.uk directly to confirm whether the link was clicked or any credentials were entered. If interaction occurred, escalate to Tier 2/3 SOC and initiate credential reset procedures immediately.
3. **Threat Intelligence Sharing & Reporting:** Submit both IOC domains and the sender address to your threat intelligence platform (e.g., MISP), report the phishing attempt to the NCSC's Suspicious Email Reporting Service (SERS) at report@phishing.gov.uk, and notify Barclays' fraud team so they may take action against the abusive domains.

---

## MITRE ATT&CK Mapping
- **T1566.002 — Phishing: Spearphishing Link**
  The email delivers a malicious URL intended to redirect the victim to a credential harvesting page, consistent with this sub-technique