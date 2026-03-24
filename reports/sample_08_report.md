# Incident Report — sample_08.txt
**Date Analysed:** 2026-03-24 19:00
**Analyst:** Mauricio Zortea
**Severity:** Critical

---

## Executive Summary
This email is a credential harvesting phishing attack impersonating the IT Support team of NorthBridge Financial Services. It employs urgency-driven social engineering to coerce staff into clicking a malicious link hosted on a spoofed domain, where victims are prompted to submit their current credentials. If successful, this attack could result in account compromise, unauthorised access to internal systems, and a potential breach of sensitive financial data.

---

## Indicators of Compromise (IOCs)
- **Sender email:** `it-support@northbridgefinancial-helpdesk.com`
- **Suspicious URLs:** `http://northbridge-it-portal.net/password/reset`
- **Suspicious attachments:** None identified
- **Spoofed domain:** `northbridgefinancial-helpdesk.com` (spoofing the legitimate `northbridgefinancial.co.uk`); `northbridge-it-portal.net` (fraudulent portal domain)

---

## Phishing Techniques Identified

- **Domain Spoofing / Lookalike Domain:** The sender domain `northbridgefinancial-helpdesk.com` is crafted to appear affiliated with the legitimate organisation (`northbridgefinancial.co.uk`). It uses a `.com` TLD and appends `-helpdesk` to deceive recipients into trusting its origin.
- **Artificial Urgency:** The subject line *"URGENT: Your password expires in 2 hours"* and body content create a false time pressure designed to override the recipient's critical thinking and prompt immediate, unconsidered action.
- **Fear of Loss / Access Deprivation:** The email explicitly lists high-value resources (Email, Microsoft 365, VPN, shared drives) the victim stands to lose, amplifying anxiety and increasing the likelihood of compliance.
- **Credential Harvesting via Malicious Link:** The call-to-action directs users to a fraudulent portal (`northbridge-it-portal.net`) and explicitly instructs them to *"enter your current password to authenticate"* — a classic credential theft mechanism. Legitimate password reset workflows never require submission of the current password.
- **Authority Impersonation:** The email poses as the internal IT Support Team, a figure of authority that staff are conditioned to trust and comply with regarding system access matters.
- **Plausible Deniability Clause:** The line *"If you have already updated your password today, please ignore this email"* is a social engineering technique used to add legitimacy and reduce suspicion among recipients who might otherwise question the email's authenticity.
- **Unencrypted HTTP Link:** The reset URL uses `http://` rather than `https://`, indicating no SSL/TLS encryption — a significant red flag for any purported internal IT portal handling credentials.
- **Generic Salutation:** The greeting *"Dear NorthBridge Staff Member"* lacks personalisation, consistent with a broad phishing campaign targeting multiple recipients rather than a legitimate internal communication.

---

## Verdict
**Classification:** Phishing
**Confidence:** High
**Reasoning:** Multiple high-confidence indicators conclusively identify this as a credential phishing email. The sender domain does not match the organisation's legitimate domain (`northbridgefinancial.co.uk`), and the embedded link directs users to an entirely unrelated external domain (`northbridge-it-portal.net`) over unencrypted HTTP. The explicit instruction to enter a *current* password is a hallmark of credential harvesting and directly contradicts standard IT security practices. The combination of urgency, authority impersonation, lookalike domains, and a fraudulent portal leaves no reasonable basis to classify this as legitimate.

---

## Recommended Actions
1. **Quarantine and block immediately:** Isolate this email across all staff mailboxes using the email security gateway. Block both domains (`northbridgefinancial-helpdesk.com` and `northbridge-it-portal.net`) at the DNS, proxy, and email filtering layers to prevent further exposure.
2. **Issue an organisation-wide staff alert:** Notify all NorthBridge Financial staff immediately via a verified internal communication channel (e.g., official intranet or confirmed internal email) warning them not to click the link, not to submit credentials, and to report if they have