---
name: mcgrath-carousel
description: Build premium, McGrath brand-compliant Instagram and Facebook carousels (1080 x 1350) for McGrath Wide Bay agents, in formats that hold attention: story, number-first, myth vs fact, before and after, suburb guide, listing deep-dive and seller-attention. Produces slide-by-slide copy with word limits, layout notes, captions and a Canva build guide. Use for any carousel, swipe post or multi-image post request.
---

# McGrath carousels

Run `mcgrath-content-intake` first if the goal, presenter or facts are unknown. Finish with `mcgrath-compliance-check`.

A carousel earns its swipes. Slide 1 stops the scroll, slide 2 pays the first part of the promise, every slide after gives a reason to keep going, and the last slide gives one clear action. People save and share carousels that teach or reveal something. They scroll past carousels that look like a listing brochure.

## Brand (read `references/brand.md` before designing)

- Charcoal `#11181C`, McGrath orange `#E67200` as the single accent, warm off-white `#F1F0ED`, white.
- Serif display headline (Recife Display on the McGrath site; in Canva use a refined serif such as Fraunces or Playfair Display if Recife is not in your brand kit) and a clean geometric sans for body (Centra No2 on site; Canva alternative DM Sans or Montserrat).
- Lots of space. One accent per slide. Real photography, never stock that pretends to be local.
- Use the office's supplied logo file only. Never recolour, stretch, outline or place it on a busy photo without a clear panel.
- Check against McGrath head office brand guidelines and any Knight Frank co-brand rules before wider rollout. This plugin's brand notes come from the live Wide Bay website, not the official guideline document.

## The cover law (slide 1)

Slide 1 is the hook. It must be about the viewer's money, decision, mistake or inside knowledge, never a feature list, an address or a bare stat. **Hard FAIL**: "Two acres, a pool and the coast close by." **Pass**: "Here's what $2.28m buys you in Bargara right now." Check it with `python3 ../mcgrath-compliance-check/scripts/hooks.py --hook "{cover headline}"`. Hook ideas by goal: `references/hook-bank.md`.

Every following slide is **fact + so what for the viewer**. The kicker names the viewer's situation ("If you tow anything", "If you host"), the headline gives the outcome ("Your Saturday just got easier."), the body gives the proof. One insider slide (what to check, ask or avoid) in every carousel. Last slide: one soft CTA plus a reason to save.

Score with `references/scorecard.md` and only hand back at 8.5 or better.

## Copy limits per slide

| Slide | Max words | Notes |
| --- | --- | --- |
| 1 Cover | 12 headline + 6 sub | The hook. Must make sense with the sound off and at thumbnail size. |
| 2 | 25 | Deliver something immediately: the number, the answer, the first fact. |
| Middle slides | 30 each | One idea each. Headline 3 to 8 words, body 15 to 25 words. |
| Last slide | 25 | One CTA, contact or inspection details with the right office's phone (from the office profile), agency name, source line if stats used. Licensee line only if the office profile says yes. |

5 to 8 slides is the sweet spot. 10 maximum.

## Formats (pick one, see `references/carousel-templates.md` for slide-by-slide templates)

1. **Listing deep-dive** (buyers): hook fact, the numbers, 3 to 5 feature slides with photos, who it suits, inspect.
2. **Seller-attention** (sellers): local stat with source, what it means, myth vs fact, questions to ask, appraisal CTA.
3. **Number-first** (any): one big verified number on slide 1, then unpack it.
4. **Myth vs fact** (sellers, landlords, tenants): 3 to 4 myths, each busted with a fact and source.
5. **Story** (community, sellers with consent): the situation, the challenge, what we did, the result, the lesson.
6. **Before and after** (sellers): styling or prep changes with real photos and the cost of each change.
7. **Suburb guide** (buyers, community): five things locals love, each with a photo and one practical fact.
8. **How we work** (sellers, landlords): the process step by step, one step per slide.

## Design rules that make it look premium

- Big serif headline, small sans body. Never more than two fonts.
- Left-aligned text, generous margins (at least 70 px on a 1080 px canvas).
- Photo slides: photo on the top 55 to 60 percent, text panel below on off-white. Or full-bleed photo with a dark gradient behind white text on the cover only.
- Data slides: one huge number in serif, a thin orange rule, a short label, a source line in small grey.
- Slide counter (02 / 07) top right in small grey. Logo small in a footer bar.
- No emoji on slides, no clip art, no drop shadows on text, no more than one orange element per slide.
- Last slide can flip to charcoal for contrast.

## Output (hand this back)

1. Slide-by-slide table: slide number, layout, headline, body, image to use, notes.
2. Caption: hook line within the first 125 characters, two to four short paragraphs, one CTA, the agency sign-off from `OFFICE-PROFILE.md`. No hashtag wall (zero to three relevant tags, or none).
3. Alt text for each slide (accessibility).
4. Canva build steps (see `references/canva-build-guide.md`).
5. Sources and placeholders.

If you can generate files (Claude with code execution, Claude Code, Cowork), you may also render the slides as 1080 x 1350 PNGs from HTML using the brand rules. Always view your output and fix overflow, orphan words and contrast before handing over.
