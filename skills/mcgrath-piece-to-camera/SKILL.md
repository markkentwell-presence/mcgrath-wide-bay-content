---
name: mcgrath-piece-to-camera
description: Write a short piece-to-camera (talking to the phone) script for a McGrath Wide Bay agent or property manager. Opens with a value, curiosity or contrarian hook tied to the viewer's outcome (never a feature list), then promise, proof, payoff with a "so what for you" on every beat, an insider tip and a platform-native soft CTA. Includes a hook bank per goal, a scorecard (ship at 8.5/10 or better), a hook linter, a film-it guide and Teleprompter Pro setup. Use for Reels, TikToks, Facebook video, YouTube Shorts, walk-and-talks, market updates, how-we-work and suburb videos.
---

# Piece-to-camera scripts

Run `mcgrath-content-intake` first if you do not yet know the presenter, goal, property or topic. Then write the script here and finish with `mcgrath-compliance-check`.

## The one law: never open on features

The first line is about **the viewer's outcome**, not the property's specs. "Two acres, a pool and the coast" is a portal listing, not a hook. People stop scrolling for money, a decision, a mistake or a secret.

**Hard FAIL** if the first spoken line or first on-screen line:
- only states features, beds, baths, cars, land size, finishes or views
- opens with the address, the agent's name or "Hi everyone"
- opens with a bare stat and no stake for the viewer ("Prices rose 11.9%.")

Check it: `python3 ../mcgrath-compliance-check/scripts/hooks.py --hook "{line}"`. It rejects feature-only, greeting and stake-less openers.

## Hook patterns (pick one, make it specific)

| Pattern | Example |
| --- | --- |
| Value / price reveal | "Here's what $X buys you in {suburb} right now." |
| Timing | "Why this is the best time to buy something like this." (only with a dated, sourced reason) |
| Insider | "What you won't see on realestate.com.au about this one." |
| Call-out | "If you're paying rent in Bundaberg, watch this." |
| Mistake list | "Three things buyers miss at open homes here." |
| Your money | "What your neighbour's sale means for your price." |
| Contrarian | "{Suburb}'s up {x}%. Don't put that number on your house." |
| Decision | "Most {suburb} buyers think you have to choose. {A} or {B}." |

More in `references/hook-bank.md`, by goal: buyers, tenants, landlords, sellers, community.

## The shape (every script)

| Beat | Time | Job |
| --- | --- | --- |
| Hook | 0 to 3 s | Pattern interrupt about the viewer's money, decision or mistake. 8 words or fewer. Same idea on screen in 6 words. |
| Promise | 3 to 6 s | The specific thing they get by the end. "Here's what actually sets your price." |
| Proof | by 8 s | A price, number, rule or result that makes the promise credible. |
| Payoff | 6 to 35 s | Each beat is **fact + so what for you**. Sell the life and the decision, not the specs. |
| Insider | one beat | What only a local agent would tell you: what to check, ask or avoid. |
| Soft CTA | last 3 to 5 s | One ask, native to the platform. Echo a word from the hook so it loops. |

Length: 30 to 45 seconds, roughly 75 to 105 words at a calm pace. No single line longer than about 4 seconds spoken.

## "So what for the viewer" check (every beat)

For every line ask: *so what, for the person watching?* If the answer is not in the script, add it or cut the line.

| Portal feature | Script line (fact + so what) |
| --- | --- |
| Butler's pantry with dishwasher | "A butler's pantry with its own dishwasher. So Christmas mess stays out of sight." |
| Three extra-high shed bays | "Tow a boat? That's your Saturday back." |
| Main bedroom in its own wing | "With a full house, you still get quiet." |
| Median up 11.9% | "Don't put that number on your house. Here's why." |
| Fixed rent, no bidding (QLD) | "The advertised rent is the rent. Nobody can outbid you." |

## Storytelling (premium agent-creator style)

Think Ryan Serhant and the best US agent-creators on TikTok, delivered in a calm Australian voice:
- **Sell the life and the decision, not the specs.** Who lives here, what their Saturday looks like, which trade-off this home removes.
- **Fast pattern interrupt, insider angle, payoff.** Hook in 3 seconds, one thing outsiders do not know, then deliver.
- **Specific beats general.** "$2.28 million", "three extra-high bays", "Saturday at nine" beat "spacious", "ample", "soon".
- **Sophisticated, never plain, never silly.** No skits, trends, fake urgency or hype words. Confidence comes from specifics.

## Writing rules

- Write for the ear. Short sentences, contractions, no adjective lists.
- Name and brand go in the caption and lower third, not the first line.
- Use the presenter's real voice from their profile. A calm principal does not say "OMG".
- Facts only from the listing, the agent or a dated source. Placeholders for anything unconfirmed. Never invent a distance, buyer count or result.
- One idea per video. Two ideas, two videos.
- Never read out the full address of a rental with tenants in place, and never mention vendor circumstances (divorce, deceased estate, financial stress).

## Scorecard (ship at 8.5 or better)

Score every script out of 10 with `references/scorecard.md`: hook about the viewer, proof early, specific promise, insider or plan, so-what on every beat, life and decision over specs, open loop paid off, a reason to save or share, platform-native CTA, clean tone and compliance. Below 8.5, rewrite the weakest beats and score again. Show the score with a one-line reason for each lost point.

## Platform-native CTAs (never cross them)

- **Instagram / Facebook:** "Inspection details in the caption." "Save this for your weekend list." "Message us for the recent sales on your street." A comment keyword only if the office has a live automation for it.
- **TikTok:** land the point cleanly. "Open home is Saturday at nine." "Follow for more from Bargara." Never "link in bio", never "comment X and we'll DM you", never Instagram references.
- **YouTube Shorts:** "Subscribe for more Wide Bay market updates." No comment keywords.
- **LinkedIn video:** a question for peers or a one-line takeaway. No hard sell.

## Formats with templates

### A. Listing walk-and-talk (buyers)
```
HOOK (value or decision, never features): "Here's what ${price} buys in {suburb}." or "Most {suburb} buyers think you have to choose. {A} or {B}."
PROMISE: "This one is both." / "Here's what you actually get for it."
PAYOFF, one stop per beat, each = fact + so what:
  "{Feature}. {What that changes about their week}."
  "{Feature}. {What that changes about their week}."
  "{Feature}. {The trade-off it removes}."
INSIDER: "Before you fall for the {obvious feature}, check {the thing that decides it}."
CTA: "Open home {day} at {time}. Save this for the drive."
```
Film tip: hook to camera at the best view, then walk slowly to each stop. Grab B-roll of every named feature after the talking take.

### B. Market update (sellers, landlords, community)
```
HOOK (contrarian or your money): "{Suburb}'s up {x}%. Don't put that number on your house."
PROMISE: "Here's what actually sets your price."
PROOF: the stat, source on screen.
PAYOFF: what the number really means, the cost of getting it wrong, what really counts.
INSIDER: a QLD rule or a question to ask ("an agent's price opinion must come with evidence").
CTA: "Want your street's sales, not the suburb's number? Message our team." No predictions stated as fact.
```

### C. How we work (sellers, landlords)
```
HOOK: "This is what happens in the first {14 days / week} after you list with us."
PROMISE: "Step by step, in thirty seconds."
PAYOFF: Day 1 ... Day 3 ... Day 7 ... (real office process only)
CTA: "If you're thinking about selling next year, save this."
```

### D. Suburb guide (buyers, community)
```
HOOK: "Three things locals know about {suburb} that the brochures skip."
PROMISE: implied.
PAYOFF: a place, a practical fact, a lifestyle detail (all verifiable).
CTA: "Follow for more from {region}."
```

### E. Rental tour (tenants)
```
HOOK: "{Rent} a week in {suburb}. Here's what you get."
PAYOFF: the one standout feature + so what, then pets / parking / air con as applicable, each with what it means for their week.
CTA: "Book a viewing through the listing."
```

### F. Ask the agent (community, all goals)
```
HOOK: "A {buyer / seller / tenant} asked me this week: {question}?"
PAYOFF: the honest answer in three lines.
CTA: "Got a question? Send it in and I'll answer it next week."
```

## Output format (hand this back)

1. **Teleprompter version:** spoken lines only, one sentence per line, blank line between beats. No stage directions. This is what goes into Teleprompter Pro.
2. **Director's version:** the same script with `[ON SCREEN: ...]` and `[B-ROLL: ...]` notes for the editor.
3. **Captions:** Instagram/Facebook caption, TikTok caption (no IG CTA), LinkedIn if relevant.
4. **Three alternate hooks** to film straight after the main take.
5. **On-screen text plan:** beat by beat, 6 words or fewer per card, plus lower third and end card.
6. **Scorecard:** the 10-point score and what lost points. Only hand back at 8.5 or better.
7. **Placeholders to confirm.**

## Film it (send this with the script)

See `references/film-it-guide.md` for the full kit and Teleprompter Pro guide. The short version:

- Phone at eye level, 9:16 vertical, rear camera if someone is filming, front camera if alone. Clean the lens.
- Light in front of you, window or sun over the camera's shoulder. Avoid midday overhead sun.
- Audio matters more than picture: a clip-on or handheld mic, wired EarPods, or AirPods.
- Teleprompter Pro (free to try, optional one-off lifetime upgrade) scrolls the script next to the lens so you keep eye contact. It is a safety net, not a script to read like a robot. Know the three beats, glance for the next line, look back at the lens.
- Film the main take three times, then the three alternate hooks, then 6 to 10 B-roll clips of the features you mentioned.
