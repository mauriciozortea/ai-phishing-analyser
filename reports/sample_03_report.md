# Incident Report — sample_03.txt
**Date Analysed:** 2026-03-24 19:00
**Analyst:** Mauricio Zortea
**Severity:** Critical

---

## Executive Summary
This email is a malicious phishing attempt masquerading as a legitimate invoice from a fabricated company ("Invoice Processing UK Ltd"), targeting the finance team of Northbridge Financial. The email employs urgency-based social engineering tactics to pressure the recipient into downloading a weaponised executable file hosted on a suspicious Russian-registered domain. If executed, the attachment is highly likely to deliver malware — such as a banking trojan, ransomware, or remote access tool — posing a critical risk to the organisation's systems and financial data.

---

## Indicators of Compromise (IOCs)
- **Sender email:** `accounts@invoice-processing-uk.com`
- **Suspicious URLs:** `http://invoice-secure-download.ru/INV-2026-4492.exe`
- **Suspicious attachments:** `INV-2026-4492.exe` — Windows executable file masquerading as an invoice document, hosted remotely rather than attached directly
- **Spoofed domain:** `invoice-processing-uk.com` — likely crafted to impersonate a legitimate UK invoicing or accounting service; no verifiable association with any known registered business

---

## Phishing Techniques Identified

- **Urgency and pressure tactics:** The subject line states "Payment Due Today" and the body demands immediate payment to avoid an 8% late fee, creating a false sense of time pressure to bypass rational scrutiny
- **Financial lure:** Use of a plausible invoice number (`INV-2026-4492`) and a specific, credible-looking amount (£12,500.00) to appear legitimate and prompt action without verification
- **Malicious executable disguised as a document:** The download link points to a `.exe` file, not a PDF or standard invoice format — a clear indicator of malware delivery masquerading as a business document
- **Untrusted foreign-hosted download link:** The download URL uses a `.ru` (Russia) top-level domain, entirely inconsistent with a claimed UK-based company, and delivered over unencrypted HTTP rather than HTTPS
- **Deflection from reply-chain scrutiny:** The email instructs recipients *not* to reply to the sender address and to contact a different address (`billing@invoice-processing-uk.com`) instead — a tactic used to prevent easy domain verification and reduce the chance of the fraud being discovered through normal correspondence
- **Lookalike sender identity:** The "From" name and signature ("Accounts Department, Invoice Processing UK Ltd") are designed to appear as a routine B2B supplier, targeting finance staff who regularly process invoices
- **No actual attachment — remote payload delivery:** By hosting the malicious file remotely rather than attaching it directly, the attacker attempts to bypass email gateway attachment scanning controls

---

## Verdict
**Classification:** Phishing
**Confidence:** High
**Reasoning:** Multiple high-confidence malicious indicators are present simultaneously. The download link points to a `.exe` file hosted on a `.ru` domain — entirely incongruent with a legitimate UK business invoice. The sender domain (`invoice-processing-uk.com`) has no verifiable legitimacy and is constructed to appear plausible at a glance. The instruction to avoid replying to the sender, combined with aggressive urgency framing and a financial threat (late fees), are textbook business email compromise (BEC) and malware delivery tactics. No legitimate invoicing workflow delivers payment instructions via a remotely hosted executable file. This email presents a critical threat and should be treated as a confirmed malicious phishing attempt.

---

## Recommended Actions
1. **Quarantine and block immediately:** Remove the email from all recipient inboxes and quarantine it at the email gateway. Block the sender domain `invoice-processing-uk.com` and the URL `invoice-secure-download.ru` at the web proxy/firewall level.
2. **Assess exposure:** Determine whether any user clicked the download link or executed the file. If execution is suspected, isolate the affected endpoint immediately, initiate forensic investigation, and escalate to Tier 2/3 SOC and the Incident Response team.
3. **User awareness notification:** Alert the finance team and broader staff with a targeted advisory warning them of this specific campaign style (invoice-themed malware via executable downloads). Reinforce that legitimate invoices are never delivered as `.exe` files and that any unexpected payment requests must be