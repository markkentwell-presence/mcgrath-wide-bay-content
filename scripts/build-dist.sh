#!/usr/bin/env bash
# Rebuild the installable zips and the combined ChatGPT/Copilot file from the plugin source (needs only python3).
set -euo pipefail
cd "$(dirname "$0")/.."
python3 - <<'PY'
import os, re, shutil, zipfile
NAME = "mcgrath-wide-bay-content"
# 1. keep shared references in sync (hook bank and scorecard live in piece-to-camera)
src = "skills/mcgrath-piece-to-camera/references"
for f, dests in {"hook-bank.md": ["mcgrath-carousel", "mcgrath-content-intake"], "scorecard.md": ["mcgrath-carousel"]}.items():
    for d in dests: shutil.copy(f"{src}/{f}", f"skills/{d}/references/{f}")
# 2. combined instructions for ChatGPT, Copilot and other assistants
order = [("mcgrath-content-intake", ["references/goal-playbooks.md", "profiles/TEMPLATE-agent-profile.md"]),
         ("mcgrath-piece-to-camera", ["references/hook-bank.md", "references/scorecard.md", "references/film-it-guide.md"]),
         ("mcgrath-carousel", ["references/brand.md", "references/carousel-templates.md", "references/canva-build-guide.md"]),
         ("mcgrath-video-edit", []), ("mcgrath-compliance-check", ["references/banned-phrases.md"]), ("mcgrath-weekly-ideas", [])]
ver = re.search(r'"version":\s*"([^"]+)"', open(".claude-plugin/plugin.json").read()).group(1)
out = [f"# McGrath Wide Bay content system (combined instructions for ChatGPT, Copilot, Gemini and other assistants)\n\nVersion {ver}. This one file holds every skill in the plugin. Where a section says \"use the X skill\", read the section with that name here. Scripts (lint.py, hooks.py) are optional; apply the same rules by reading.\n\n---\n\n<!-- OFFICE-PROFILE.md (defaults; an uploaded OFFICE-PROFILE.md overrides this) -->\n" + re.sub(r"^(#+) ", r"#\1 ", open("OFFICE-PROFILE.md").read(), flags=re.M)]
for s, refs in order:
    t = re.sub(r"^---\n.*?\n---\n", "", open(f"skills/{s}/SKILL.md").read(), flags=re.S)
    out.append(f"\n\n---\n\n<!-- SKILL: {s} -->\n" + re.sub(r"^# ", f"# [{s}] ", t, count=1, flags=re.M))
    for r in refs:
        out.append(f"\n\n<!-- {s}/{r} -->\n" + re.sub(r"^(#+) ", r"#\1 ", open(f"skills/{s}/{r}").read(), flags=re.M))
out.append("\n\n---\n\n<!-- examples/EXAMPLES.md -->\n" + re.sub(r"^(#+) ", r"#\1 ", open("examples/EXAMPLES.md").read(), flags=re.M))
open("chatgpt/MCGRATH-WIDE-BAY-CONTENT-INSTRUCTIONS.md", "w").write("".join(out))
# 3. zips
shutil.rmtree("dist", ignore_errors=True); os.makedirs("dist/skills")
def add(z, path, arc):
    for root, _, files in os.walk(path):
        for f in files:
            if f == ".DS_Store" or f.endswith(".pyc") or "__pycache__" in root: continue
            p = os.path.join(root, f); z.write(p, os.path.join(arc, os.path.relpath(p, path)))
with zipfile.ZipFile(f"dist/{NAME}-plugin.zip", "w", zipfile.ZIP_DEFLATED) as z:
    add(z, ".claude-plugin", f"{NAME}/.claude-plugin"); add(z, "skills", f"{NAME}/skills"); add(z, "examples", f"{NAME}/examples")
    for f in ["README.md", "CHANGELOG.md", "OFFICE-PROFILE.md", "LICENSE"]: z.write(f, f"{NAME}/{f}")
for s in sorted(os.listdir("skills")):
    with zipfile.ZipFile(f"dist/skills/{s}.zip", "w", zipfile.ZIP_DEFLATED) as z:
        add(z, f"skills/{s}", s); z.write("OFFICE-PROFILE.md", f"{s}/OFFICE-PROFILE.md")
for f in os.listdir("chatgpt"): shutil.copy(f"chatgpt/{f}", "dist/")
shutil.copy("OFFICE-PROFILE.md", "dist/")
print("Built", ver, sorted(os.listdir("dist")))
PY
