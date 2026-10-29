# McGrath Wide Bay content plugin

Six skills that help McGrath Knight Frank Wide Bay & Fraser Coast agents and property managers decide what to post, then write it, film it, design it, edit it and check it. Every hook is about the viewer's money, decision or inside knowledge, never a feature list. Works as a Claude plugin, as Claude.ai skills, and in ChatGPT or Microsoft Copilot through one instructions file.

Version: see `.claude-plugin/plugin.json`. Changes: `CHANGELOG.md`. Licence: MIT.

## What it does

Tell it who is presenting, what the post is for and what the property or topic is. It does the rest.

| Skill | What it is for |
| --- | --- |
| `mcgrath-content-intake` | Start here. Four questions (presenter, goal, property or topic, format), presenter profiles, routes to the right playbook. |
| `mcgrath-piece-to-camera` | Talking-to-camera scripts: viewer-first hook, promise, proof, payoff with a "so what" on every beat, an insider tip, a platform-native CTA. Teleprompter Pro and kit guide. |
| `mcgrath-carousel` | Premium 1080 x 1350 carousels in the office brand, with a cover hook rule, slide copy limits and a Canva build guide. |
| `mcgrath-video-edit` | Premium edit recipes (CapCut, TikTok, Instagram and Edits) and an AI-edit brief. |
| `mcgrath-compliance-check` | QLD and Australian advertising basics, anti-slop phrase list, per-platform checklist, offline `lint.py` and `hooks.py`. |
| `mcgrath-weekly-ideas` | Four posts a week across the five goals that are not listing replicas. |

The five goals: (1) buyers to a listing, (2) tenants to a rental, (3) landlords for the rent roll, (4) sellers and listings, (5) personal and community brand.

## Install

### Claude Code (one line)
```bash
/plugin marketplace add markkentwell-presence/mcgrath-wide-bay-content
/plugin install mcgrath-wide-bay-content@mcgrath-wide-bay
```

### Claude desktop app or Claude.ai (Cowork plugins)
1. Download `mcgrath-wide-bay-content-plugin.zip` from the [latest release](https://github.com/markkentwell-presence/mcgrath-wide-bay-content/releases/latest) (also in `dist/`).
2. In Claude: **Customize > Plugins > Add > Upload plugin**, choose the zip.
3. Or add it as a marketplace: **Customize > Plugins > Add marketplace**, enter `markkentwell-presence/mcgrath-wide-bay-content`.

Team or Enterprise owners can add it for everyone under **Organization settings > Plugins & skills**.

### Claude.ai skills only (if plugins are not on your plan)
1. Turn on **Settings > Capabilities > Code execution and file creation**.
2. **Customize > Skills**, upload each zip from `dist/skills/` (six small zips) and turn them on.
3. Make a Claude Project called "McGrath content" and add your edited `OFFICE-PROFILE.md` to its knowledge.

### ChatGPT (Custom GPT or Project)
- **Custom GPT:** Explore GPTs > Create > Configure. Paste `chatgpt/CORE-INSTRUCTIONS.md` into **Instructions**. Upload `chatgpt/MCGRATH-WIDE-BAY-CONTENT-INSTRUCTIONS.md` and your `OFFICE-PROFILE.md` under **Knowledge**.
- **Project:** New project, paste `CORE-INSTRUCTIONS.md` into the instructions, add the two files as project files.

### Microsoft 365 Copilot
1. **Create an agent** (Agent Builder). Paste `chatgpt/CORE-INSTRUCTIONS.md` into **Instructions**.
2. Add `MCGRATH-WIDE-BAY-CONTENT-INSTRUCTIONS.md` and `OFFICE-PROFILE.md` under **Knowledge**.
3. Share the agent with the team.

### Gemini, Perplexity or anything else
Paste `CORE-INSTRUCTIONS.md` as custom instructions and attach the other two files.

## Edit your office details (one file)

All office details live in **`OFFICE-PROFILE.md`**: agency name, phone, licensee, licence number, whether to show a licensee line, brand colours, fonts, sign-off and standard lines.

1. Open `OFFICE-PROFILE.md` in any text editor (TextEdit, Notepad, or the pencil icon on GitHub).
2. Change the words after each colon. Leave anything you do not use blank.
3. Save it, then use it in the place you work:
   - **Claude Project, ChatGPT or Copilot:** upload it to the project or agent knowledge. Replace the old file when you change it.
   - **Claude Code:** keep a copy named `OFFICE-PROFILE.md` in your working folder. It overrides the built-in one, and plugin updates will not overwrite it.
   - **Plugin zip:** edit the file inside the folder before you zip and upload, or just upload the edited file to your project.
4. Or ask: *"Update our office profile: our licence number is 1234567."* The assistant gives you the new file to save.

**Licensee line:** off by default. Queensland's Property Occupations Act 2014 s 95(1) only requires the particulars set by regulation, and the current Property Occupations Regulation 2014 sets none for advertisements, so a licence number is not required on social posts. The agency name stays on every post. If McGrath head office asks for more, set "Show licensee line on posts" to yes, or put the licensee details once in each platform bio. Not legal advice.

## How good is "good"

- **Hooks:** a feature list, address, greeting or bare stat as the first line is a FAIL. `python3 skills/mcgrath-compliance-check/scripts/hooks.py --hook "your first line"`.
- **Scorecard:** every script and carousel is scored out of 10 (`skills/mcgrath-piece-to-camera/references/scorecard.md`) and only handed back at 8.5 or better.
- **Examples:** `examples/EXAMPLES.md` has a full listing script, a seller market script, captions and cover lines with placeholder details.

## Working with REMAP's setup
- **Humanizer:** run captions through Humanizer if you have it, then run `mcgrath-compliance-check` again.
- **Postiz:** schedule finished posts through Postiz. Nothing in this plugin posts anything by itself.
- **Canva tiles:** keep the automated just-listed and open-home tiles. This plugin covers the rest of the week.

## Maintaining it
- Edit the skill files, bump `version` in `.claude-plugin/plugin.json`, add a line to `CHANGELOG.md`.
- Rebuild the zips: `bash scripts/build-dist.sh`.
- Brand and compliance notes carry a "checked on" date. Recheck at least every six months.

Not legal advice. Check McGrath head office brand and compliance guidelines and your licensee-in-charge for anything borderline.
