---
name: mcgrath-compliance-check
description: Final quality and compliance check before any McGrath Wide Bay post goes out. Covers Queensland and Australian real estate advertising basics (misleading claims, QLD auction price-guide rules, offers-over pricing, rent bidding, agency and licensee name, consent and privacy), an anti-AI-slop banned phrase list, Australian English and formatting rules, and a per-platform checklist. Use on every script, caption and carousel, and whenever someone asks "is this OK to post?"
---

# Compliance and quality check

Run this last, every time. It is a practical checklist, **not legal advice**. When something is borderline, ask the licensee-in-charge or principal before posting, and check McGrath head office brand and compliance guidelines.

## How to run it

1. Read the draft against every section below.
2. If you can run code, run `python3 scripts/lint.py <file>` on the caption or script for an automatic first pass.
3. Output a short report: **PASS** or **FIX**, then a numbered list of fixes with the corrected line.
4. Suggest: "If you have Humanizer installed, run it over the caption now, then run this check again." Humanizer rewrites for a natural voice, this check makes sure the rewrite has not added claims, hype or em dashes.

## 1. Truth and accuracy (Australian Consumer Law, applies everywhere)

- Every fact must be true and checkable: beds, baths, land size, features, distances, inspection times, prices, stats.
- No misleading impressions by omission. If a "two minutes to the beach" claim is by car, say so, or drop it.
- No "best", "number one", "record" or "top agent" claims without current proof you can show.
- No guaranteed outcomes: "we will sell it for", "guaranteed rent", "zero vacancy".
- Market statistics need a named source and date on the slide or in the caption.
- Testimonials and sold results only with the client's permission, and only real ones.

## 2. Queensland selling rules (Property Occupations Act 2014 and QLD Government guidance)

Sources checked 29 Oct 2026: Property Occupations Act 2014 (Qld) on legislation.qld.gov.au (current as at 1 Aug 2025), sections 214 to 216; Property Occupations Regulation 2014; Queensland Government "Property advertising" page (qld.gov.au).

- **Auctions: no price guides.** For a residential property going to auction, agents and auctioneers must not disclose a price guide, reserve or "likely" price to buyers. Do not hint at price in a script or caption for an auction listing ("expect bidding to start around..." is out). Listing portals may filter by a price bracket behind the scenes, with the prescribed statement on the listing.
- **Offers over / price.** An offers-over figure should be the minimum the seller is willing to accept. Advertising a price the seller will not accept is bait advertising and can be a false or misleading representation.
- **Price opinions to sellers.** If an agent gives a seller information about the likely selling price, they must also give a comparative market analysis or a written explanation of how they reached it (s 215). Fine to talk about this as a consumer right in content.
- **Agency and licensee identification.** Property Occupations Act 2014 s 95(1) says a principal licensee's business advertisements must state "the particulars prescribed under a regulation". The Property Occupations Regulation 2014 (current as at 1 July 2022, checked 29 Oct 2026) prescribes no particulars for s 95(1); it only covers displaying the auctioneer's name at an auction (s 95(2), reg 9). So Queensland law does not currently require a licensee name or licence number on social posts. What to do:
  - Make it clear who is advertising. The agency name in the account name, bio or caption is enough. Never imply an affiliation or approval you do not have (s 209(2)(a)).
  - Follow the "Show licensee line on posts" setting in `OFFICE-PROFILE.md` (default "no"). If "yes", add one short line at the end: `{Agency} · {Licensee} · Lic. {number}`.
  - The simplest tidy option is the licensee details once in each platform bio.
  - McGrath head office or franchise policy may ask for more. If it does, set the profile to "yes".
- **Ownership or interest.** If the agent or a related person owns or has an interest in the advertised property, disclose it.
- **Suburb accuracy.** Do not say a property is in a suburb it is not in.

## 3. Queensland rental rules (RTA)

Source checked 29 Oct 2026: Residential Tenancies Authority (rta.qld.gov.au) rent bidding and 6 June 2024 rental law changes pages.

- Rentals must be advertised at a fixed rent. No rent ranges, no rent auctions, no inviting or accepting offers above the advertised rent.
- No discriminatory wording (family status, age, race, disability and so on). Describe the property, not the ideal tenant.
- Do not show tenants, their belongings or anything identifying without written consent.

## 4. Financial and tax talk

- Stay general. No personal financial, tax or lending advice. Do not tell anyone they should buy, sell or refinance.
- Interest rate and price predictions only as attributed opinion from a named, dated source, never as fact.
- On market or investment posts, end the caption with: `General information only. Not financial advice.`

## 5. Privacy and consent

- Written OK from the vendor or landlord before filming inside a property.
- Anyone recognisable on camera (colleagues, buyers at an open home, neighbours, children) gives consent first. When in doubt, blur or leave them out.
- Remove personal photos, mail, medication, documents, security codes and number plates from shot.
- Never mention a seller's or tenant's personal circumstances.
- Music and photography must be licensed for the platform you post to.
- If AI is used to generate a voice or presenter, do not present it as the real agent. Label it.

## 6. Anti-slop and house style

- Australian English. No em dashes. Two sentences max per paragraph in captions and on screen.
- None of the banned words and phrases in `references/banned-phrases.md`.
- No hashtag walls. Zero to three relevant hashtags.
- One CTA per post. No fake urgency.
- Sounds like the presenter's profile, not like a brochure.
- Specific over generic: a street, a number, a feature, a local detail.

## 7. Platform checklist

**Instagram (Reel or carousel)**
- [ ] Hook in the first line of the caption, inside 125 characters
- [ ] Cover / slide 1 readable at thumbnail size
- [ ] On-screen text inside safe zones
- [ ] Alt text added for carousels
- [ ] CTA native to IG ("details in the caption", "save this", "message us")

**Facebook**
- [ ] Same as Instagram, plus the address and inspection time written in full for local search
- [ ] Community groups: follow each group's rules on real estate posts

**TikTok**
- [ ] No Instagram CTAs, no "link in bio", no comment-for-DM keywords
- [ ] Captions on, licensed sound only

**LinkedIn**
- [ ] Professional angle, no hard sell, a takeaway or question

**All platforms**
- [ ] Agency name clear (bio or caption); licensee line only if the office profile says yes
- [ ] Facts and placeholders confirmed
- [ ] Consent and privacy checked
- [ ] Principal or licensee-in-charge has approved anything borderline
- [ ] Checked against McGrath head office brand guidelines
