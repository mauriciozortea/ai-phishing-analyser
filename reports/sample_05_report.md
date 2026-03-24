# Incident Report — sample_05.txt
**Date Analysed:** 2026-03-24 18:58
**Analyst:** Mauricio Zortea
**Severity:** High

---

## Executive Summary
This email is a credential harvesting phishing attempt impersonating LinkedIn's Trust & Safety team, targeting Mauricio Zortea at Northbridge Financial. The email employs urgency, fear-based messaging, and a convincing but fraudulent domain to trick the recipient into clicking a malicious link designed to steal account credentials. Given the financial sector context of the target organisation, a successful compromise could expose sensitive corporate or client data beyond the LinkedIn account itself.

---

## Indicators of Compromise (IOCs)
- **Sender email:** notifications@linkedln-secure.com *(note the deliberate misspelling: "linkedln" instead of "linkedin")*
- **Suspicious URLs:** `http://linkedln-account-verify.com/restore/secure` *(unencrypted HTTP, typosquatted domain, non-LinkedIn infrastructure)*
- **Suspicious attachments:** None identified
- **Spoofed domain:** `linkedln-secure.com` and `linkedln-account-verify.com` — both typosquatting the legitimate `linkedin.com` domain, substituting the letter "i" with a lowercase "L" (`ln` vs `in`)

---

## Phishing Techniques Identified
- **Typosquatting / Domain Spoofing:** The sender domain (`linkedln-secure.com`) and redirect domain (`linkedln-account-verify.com`) closely mimic the legitimate LinkedIn domain to deceive a casual reader
- **Urgency and Artificial Time Pressure:** The 12-hour verification deadline is designed to prevent the recipient from thinking critically or verifying legitimacy through official channels
- **Fear-Based Messaging / Intimidation:** Threatens severe consequences — hidden profile, removal of all connections, and loss of a Premium subscription without refund — to coerce immediate action
- **Brand Impersonation:** Replicates LinkedIn's tone, team name ("LinkedIn Trust & Safety Team"), and even the correct corporate address (1000 W Maude Ave, Sunnyvale, CA 94085) to appear credible
- **Legitimacy Anchoring:** Including a real-world IP address (103.45.67.89) and a plausible geolocation (Bucharest, Romania) adds false credibility and creates a sense of a concrete, verifiable threat
- **Unsecured Link Delivery:** The malicious URL uses `http://` rather than `https://`, indicating a lack of proper infrastructure and reducing trust in the destination

---

## Verdict
**Classification:** Phishing
**Confidence:** High
**Reasoning:** Multiple high-confidence indicators confirm this is a phishing email. The sender domain and linked URL both contain a deliberate and consistent typosquat of `linkedin.com` (`linkedln` vs `linkedin`). The destination URL is entirely external to LinkedIn's infrastructure. The use of plaintext HTTP for a supposed "secure verification" page is inconsistent with any legitimate corporate communication. The combination of urgency, fear-based threats, brand impersonation, and fabricated technical details (IP address, geolocation) are textbook phishing social engineering techniques. No legitimate indicators of authenticity were identified.

---

## Recommended Actions
1. **Do not click the link** — The URL `http://linkedln-account-verify.com/restore/secure` should be treated as malicious. It must not be opened on any corporate or personal device.
2. **Quarantine and block** — Escalate to Tier 2/3 SOC to quarantine this email organisation-wide, and submit `linkedln-secure.com` and `linkedln-account-verify.com` to the email gateway and web proxy blocklists immediately.
3. **Verify account status directly** — Advise Mauricio Zortea to navigate directly to `https://www.linkedin.com` (manually typed, not via any link in this email) to confirm whether any genuine restriction has been applied to the account.
4. **Report and submit IOCs** — Report the phishing email to LinkedIn's official abuse team (safety@linkedin.com) and submit the domains and sender address to threat intelligence platforms (e.g., VirusTotal, URLhaus, PhishTank) for broader community protection.
5. **User Awareness Reminder** — Issue a brief awareness reminder to Northbridge Financial staff regarding typos