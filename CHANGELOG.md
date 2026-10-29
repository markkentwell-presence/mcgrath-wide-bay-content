# Changelog: mcgrath-wide-bay-content

Bump `version` in `.claude-plugin/plugin.json` with every change, then add a line here.
Rebuild the zips with `bash scripts/build-dist.sh` after any edit.

## 1.1.0 (2026-10-29)

- **Hooks rebuilt.** A feature-led opener (features, beds, baths, land size, address, greeting, or a stat with no stake) is now a hard FAIL in `mcgrath-piece-to-camera` and `mcgrath-carousel`. New hook patterns: value, timing, insider, call-out, mistake list, your money, contrarian, decision.
- New `references/hook-bank.md` (by goal: buyers, tenants, landlords, sellers, community) and `references/scorecard.md` (10 points, ship at 8.5 or better).
- New `mcgrath-compliance-check/scripts/hooks.py` hook linter; `lint.py` now runs it on the first line.
- "So what for the viewer" check on every beat and every slide. Storytelling section (sell the life and the decision, not the specs; pattern interrupt, insider angle, payoff).
- **Office profile.** New `OFFICE-PROFILE.md` at the top of the plugin: agency name, licensee, licence number, brand colours, sign-off. Every skill reads it.
- **Licensee line now optional (default off).** Property Occupations Act 2014 (Qld) s 95(1) only requires the particulars prescribed by regulation, and the Property Occupations Regulation 2014 (current as at 1 July 2022) prescribes none for advertisements (reg 9 covers s 95(2), the auctioneer's name at an auction). Agency name stays; licensee details are a profile setting or a bio line.
- `examples/` with placeholder scripts, carousel copy and captions.
- Public mirror: github.com/markkentwell-presence/mcgrath-wide-bay-content. Licence changed to MIT.

## 1.0.0 (2026-10-29)

- First release, prepared by Mark Kentwell for Ashley's office (McGrath Knight Frank Wide Bay & Fraser Coast) after the 29 Oct 2026 McGrath x REMAP.ai call.
- Six skills: `mcgrath-content-intake` (router), `mcgrath-piece-to-camera`, `mcgrath-carousel`, `mcgrath-video-edit`, `mcgrath-compliance-check`, `mcgrath-weekly-ideas`.
- Five goal playbooks: buyers to a listing, tenants to a rental, landlords for the rent roll, sellers and listings, personal and community brand.
- Brand reference taken from the live mcgrathwidebay.com.au theme (charcoal #11181C, orange #E67200, warm off-white #F1F0ED, Centra No2 and Recife Display). Check against McGrath head office guidelines before wider use.
- QLD compliance notes from the Property Occupations Act 2014 (current as at 1 Aug 2025 on legislation.qld.gov.au) and the Queensland Government property advertising page, checked 29 Oct 2026.
- Offline lint script (`mcgrath-compliance-check/scripts/lint.py`) for banned phrases, em dashes, long paragraphs, hashtag walls and (optionally) a missing licence number.
- ChatGPT, Copilot and other-LLM path: `chatgpt/MCGRATH-WIDE-BAY-CONTENT-INSTRUCTIONS.md`.
- Test pack (two carousels and two scripts on a live listing) kept in the private master copy only.
