# Incident Report — sample_07.txt
**Date Analysed:** 2026-03-24 18:58
**Analyst:** Mauricio Zortea
**Severity:** Critical

---

## Executive Summary
This email is a targeted phishing attempt impersonating the Human Resources department of NorthBridge Financial Services, sent from a lookalike domain entirely unaffiliated with the legitimate organisation. It lures recipients into opening a macro-enabled Word document (`.docm`) via an embedded URL, which is a well-established delivery mechanism for malware payloads such as ransomware, infostealers, or remote access trojans. Given that it was distributed to the entire staff mailing list and exploits urgency around employment consequences, this represents a high-impact, organisation-wide threat requiring immediate containment.

---

## Indicators of Compromise (IOCs)
- **Sender email:** `hr-documents@northbridge-hr-portal.com`
- **Suspicious URLs:** `http://northbridge-hr-documents.com/handbook2026.docm`
- **Suspicious attachments:** `handbook2026.docm` — macro-enabled Microsoft Word document delivered via external URL; `.docm` format is commonly used to execute malicious VBA macros upon opening
- **Spoofed domain:** `northbridge-hr-portal.com` and `northbridge-hr-documents.com` — both are lookalike domains impersonating the legitimate `northbridgefinancial.co.uk`; neither matches the organisation's verified domain

---

## Phishing Techniques Identified

- **Domain Spoofing / Lookalike Domains:** The sender domain (`northbridge-hr-portal.com`) and the payload-hosting domain (`northbridge-hr-documents.com`) are crafted to visually mimic the legitimate corporate domain `northbridgefinancial.co.uk`, exploiting brand familiarity to reduce suspicion
- **Authority & Impersonation:** The email impersonates an internal HR department — a highly trusted function — and invokes the authority of the organisation itself to compel action
- **Urgency & Threat of Consequences:** The deadline of Friday 28 March and the explicit warning that *"failure to sign by the deadline may affect your employment record"* are designed to pressure employees into acting quickly without scrutiny
- **Broad Targeting (Spray Phishing):** The email is addressed to `all-staff@northbridgefinancial.co.uk`, maximising the potential victim pool and increasing the probability of at least one user executing the payload
- **Plausible Pretext (Lure Relevance):** The use of a routine, believable HR activity (annual handbook update) makes the request appear mundane and legitimate, lowering the recipient's defensive instinct
- **Malicious Macro Document Delivery:** Directing users to open a `.docm` file is a classic technique to bypass email attachment filters by hosting the payload on an external domain, while leveraging Microsoft Office macro execution to deploy malware
- **HTTP (Non-HTTPS) Link:** The payload URL uses unencrypted `http://`, which is inconsistent with legitimate enterprise document portals and may indicate a hastily assembled infrastructure

---

## Verdict
**Classification:** Phishing
**Confidence:** High
**Reasoning:** Multiple high-confidence indicators converge to confirm this as a malicious phishing email. The sender domain does not match the organisation's legitimate domain. The payload is hosted on a second unrelated lookalike domain over unencrypted HTTP. The file format (`.docm`) is a well-documented malware delivery vehicle. The social engineering is sophisticated — combining authority impersonation, urgency, and a plausible HR pretext — consistent with a deliberate, targeted campaign rather than opportunistic spam. No legitimate enterprise HR process would direct employees to download and open macro-enabled documents from an external URL.

---

## Recommended Actions
1. **Immediately quarantine and block** the email across the organisation's mail gateway; prevent delivery to any recipients who have not yet received it and flag/pull it from inboxes where it has already landed
2. **Block all associated IOCs** at the perimeter — blacklist the domains `northbridge-hr-portal.com` and `northbridge-hr-documents.com` and the full URL `http://northbridge-hr-documents.com/handbook2026.docm` at the DNS, proxy, and firewall levels
3. **Issue an urgent all-staff advisory** warning employees not