# Incident Report — sample_06.txt

**Date Analysed:** 2026-03-24 18:59
**Analyst:** Mauricio Zortea
**Severity:** High

---

## Executive Summary

This email is a smishing/phishing attempt impersonating DHL Express, a globally recognised parcel delivery brand, targeting an employee at Northbridge Financial. The email uses a fabricated failed-delivery scenario and an artificial 24-hour deadline to pressure the recipient into clicking a malicious link and submitting a payment of £2.99, likely designed to harvest banking credentials or payment card details. If acted upon, this attack could result in financial fraud and/or the compromise of sensitive personal and corporate payment information.

---

## Indicators of Compromise (IOCs)

- **Sender email:** `delivery-notification@dhl-express-uk.net`
- **Suspicious URLs:** `http://dhl-redelivery-uk.com/pay/reschedule`
- **Suspicious attachments:** None detected
- **Spoofed domain:** `dhl-express-uk.net` (spoofing the legitimate `dhl.com`); `dhl-redelivery-uk.com` (fraudulent lookalike domain — note use of unencrypted HTTP rather than HTTPS)

---

## Phishing Techniques Identified

- **Brand impersonation:** The email closely mimics DHL Express branding, using recognisable language, formatting conventions, and a plausible tracking number (`JD014600008985076532`) to appear legitimate.
- **Urgency and artificial deadline:** The recipient is warned that payment must be made within 24 hours or the parcel will be returned, creating pressure to act quickly without scrutiny.
- **Lookalike/typosquatted domains:** Both the sender domain (`dhl-express-uk.net`) and the linked domain (`dhl-redelivery-uk.com`) are crafted to visually resemble official DHL infrastructure while being entirely unaffiliated.
- **Low-cost lure ("smishing-style" micropayment):** The nominal fee of £2.99 is deliberately small to reduce the victim's suspicion and lower the psychological barrier to payment, while the true goal is likely credential or card data harvesting.
- **False legitimacy through parcel details:** Fabricated but plausible parcel metadata (weight, origin, delivery attempt count) is included to add credibility to the scenario.
- **Unencrypted link (HTTP):** The redelivery link uses plain HTTP rather than HTTPS, a red flag indicating a low-effort or quickly stood-up fraudulent page.
- **Generic greeting:** The use of "Dear Customer" rather than the recipient's name indicates a mass-distributed phishing campaign rather than a targeted communication.

---

## Verdict

**Classification:** Phishing
**Confidence:** High
**Reasoning:** Multiple strong indicators confirm this is a phishing email. The sender domain (`dhl-express-uk.net`) is not an authorised DHL domain — all legitimate DHL communications originate from `@dhl.com` or verified regional subdomains. The embedded URL points to `dhl-redelivery-uk.com`, a clearly fraudulent lookalike domain with no association to DHL, served over unencrypted HTTP. The combination of brand impersonation, urgency tactics, a micropayment lure, generic salutation, and suspicious infrastructure is entirely consistent with a well-documented "missed delivery" phishing campaign typology. There are no indicators that this email is legitimate.

---

## Recommended Actions

1. **Quarantine and block immediately:** Remove the email from the recipient's inbox and any other mailboxes it may have reached. Block both domains (`dhl-express-uk.net` and `dhl-redelivery-uk.com`) at the email gateway and web proxy/firewall level.
2. **Verify recipient interaction:** Contact the employee to determine whether the link was clicked or any payment/card details were submitted. If credentials or payment information were entered, escalate to Tier 2/3 and initiate financial fraud and credential compromise response procedures without delay.
3. **User awareness notification:** Issue a brief advisory to all staff warning of this active campaign, reminding them that DHL will never request payment via unsolicited email links, and encouraging them to report similar emails via the official phishing reporting channel. Consider submitting the fraudulent domains to the NCSC's phishing reporting service (report@phishing.gov.uk