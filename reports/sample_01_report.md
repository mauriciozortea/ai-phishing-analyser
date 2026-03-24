# Incident Report — sample_01.txt
**Date Analysed:** 2026-03-24 19:00
**Analyst:** Mauricio Zortea
**Severity:** High

---

## Executive Summary
This email is a credential-harvesting phishing attempt impersonating Microsoft's security team, targeting an employee at Northbridge Financial. The threat actor employs urgency-based social engineering and a typosquatted domain to lure the recipient into submitting their Microsoft 365 credentials via a malicious Russian-hosted URL. If successful, this attack could result in account compromise, unauthorised access to sensitive financial data, and potential lateral movement within the organisation.

---

## Indicators of Compromise (IOCs)
- **Sender email:** security-alert@micros0ft-support.com
- **Suspicious URLs:** http://micros0ft-account-verify.ru/secure/login
- **Suspicious attachments:** None identified
- **Spoofed domain:** micros0ft-support.com (typosquat of microsoft.com); micros0ft-account-verify.ru (Russian-registered TLD, .ru)
- **Referenced IP address:** 197.210.84.33 (Lagos, Nigeria — used as a social engineering lure, not necessarily a confirmed attacker IP)

---

## Phishing Techniques Identified

1. **Typosquatting / Domain Spoofing** — The sender domain `micros0ft-support.com` replaces the letter "o" with the numeral "0" to visually mimic a legitimate Microsoft domain and evade casual inspection.
2. **Urgency & Fear Creation** — The subject line ("URGENT: Your Microsoft 365 account will be suspended in 24 hours") and body text manufacture a false sense of crisis to pressure the recipient into acting without rational evaluation.
3. **Brand Impersonation** — The email replicates Microsoft's visual identity, including the copyright notice, corporate address (One Microsoft Way, Redmond, WA 98052), and the "Microsoft Security Team" sign-off to appear legitimate.
4. **Artificial Countdown / Expiry Threat** — A 24-hour deadline is imposed to limit the recipient's time to verify authenticity or consult IT.
5. **Threatening Consequences** — Threatening permanent deletion of emails and files amplifies psychological pressure and discourages inaction.
6. **Geolocation Lure** — Citing a specific location (Lagos, Nigeria) and IP address adds false credibility and personalisation, making the threat feel real and targeted.
7. **Malicious Hyperlink Masquerading as Legitimate Action** — The call-to-action button/link ("VERIFY MY ACCOUNT NOW") directs to a non-Microsoft, Russian-registered domain designed to harvest credentials.

---

## Verdict
**Classification:** Phishing
**Confidence:** High
**Reasoning:** Multiple high-confidence indicators converge to confirm this as a phishing email. The sender domain uses deliberate character substitution (`0` for `o`) — a classic typosquatting technique. The destination URL is hosted on a `.ru` (Russia) domain with no affiliation to Microsoft. Legitimate Microsoft communications originate from `@microsoft.com` and direct users to `microsoft.com` or `login.microsoftonline.com`. The email contains no personalisation beyond a generic "Dear Microsoft 365 User," inconsistent with genuine security alerts. The combination of urgency, fear-based language, impersonation, and a deceptive link constitute a textbook credential-phishing campaign. No legitimate indicators are present.

---

## Recommended Actions

1. **Quarantine and block the email** — Immediately quarantine this message across all mailboxes via the email security gateway (e.g., Microsoft Defender for Office 365 / Mimecast) and block the sender domain `micros0ft-support.com` at the mail filter level.
2. **Block malicious URLs and domains at the network perimeter** — Submit `micros0ft-account-verify.ru` and `micros0ft-support.com` to the web proxy / DNS firewall for blocking. Check proxy and firewall logs to determine whether any users have already accessed the URL.
3. **Alert and educate the targeted employee** — Notify `employee@northbridgefinancial.co.uk` that this email is malicious, instruct them not to click the link, and confirm whether they interacted with it