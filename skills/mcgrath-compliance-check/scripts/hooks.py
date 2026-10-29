#!/usr/bin/env python3
"""Hook linter for McGrath Wide Bay scripts and carousel covers. Python 3 stdlib only.
Rejects openers that only state features, specs or an address, greetings, and stats with no stake for the viewer.
Usage: python3 hooks.py --hook "Here's what $2.28 million buys in Bargara."
       python3 hooks.py script.txt        (checks the first line)
       python3 hooks.py hooks.txt --each  (one hook per line)"""
import re, sys, argparse
FEATURES = r"\b(\d+\s*(bed|bdr|bedroom|bath|bathroom|car|cars|garage)s?|bed(room)?s?|bath(room)?s?|ensuite|acres?|hectares?|m2|m²|sqm|square metres?|block|land|pool|kitchen|butler'?s pantry|shed|sheds|garage|carport|views?|ocean views?|renovated|brand new|storey|deck|verandah|patio|air ?con|solar|island bench|stone benches?|timber floors?|open plan|living areas?|backyard|yard)\b"
VIEWER = r"(\byou\b|\byour\b|\byou're\b|\byou'll\b|\bhere's\b|\bwhy\b|\bwhat\b|\bhow\b|\bif\b|\bbefore\b|\bmost\b|\bmiss\b|\bmistake|\bwon't\b|\bdon't\b|\bnever\b|\bnobody\b|\bthinking of\b|\bbuys?\b|\bworth\b|\bcost|\bpaying\b|\bchoose\b|\bquestion\b|\bthree things\b|\bthe one\b|\bsecret\b|\binsider\b|\bwatch this\b|\bversus\b|\bvs\b)"
GREET = r"^(hi|hey|hello|g'?day|welcome|good (morning|afternoon)|it's [a-z]+ from|this is \d+|introducing|presenting|just listed|new listing|for sale)"
ADDRESS = r"^\d+\s+[a-z]+\s+(road|rd|street|st|avenue|ave|drive|dr|court|ct|parade|pde|crescent|cres|place|pl|lane|ln|esplanade)\b"
STAT = r"(\d+(\.\d+)?\s*(%|per ?cent)|median|\$\d)"
HYPE = r"\b(stunning|breathtaking|nestled|boasts?|must see|won't last|rare opportunity|sought[- ]after|dream home|oozes|hidden gem)\b"
def check(h):
    t=h.strip().lower().replace("’","'"); f=[]
    if not t: return ["Empty hook."]
    if re.search(GREET,t): f.append("Greeting or announcement opener. Start at the interesting sentence.")
    if re.search(ADDRESS,t): f.append("Address opener. Put the address in the caption or lower third.")
    feats=len(re.findall(FEATURES,t)); viewer=bool(re.search(VIEWER,t))
    if feats and not viewer: f.append(f"Feature-led opener ({feats} feature words, nothing about the viewer). Open on their money, decision, mistake or inside knowledge.")
    if re.search(STAT,t) and not viewer and not feats: f.append("Stat with no stake for the viewer. Add what it means for them (\"Don't put that number on your house.\").")
    if re.search(HYPE,t): f.append("Hype or cliché word in the hook.")
    if len(t.split())>14: f.append(f"{len(t.split())} words. Land the hook in 14 or fewer (8 is better).")
    return f
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("file",nargs="?"); ap.add_argument("--hook"); ap.add_argument("--each",action="store_true")
    a=ap.parse_args()
    if a.hook: hooks=[a.hook]
    else:
        lines=[l for l in open(a.file,encoding="utf-8").read().splitlines() if l.strip()]
        hooks=lines if a.each else lines[:1]
    bad=0
    for h in hooks:
        f=check(h); bad+=bool(f)
        print(("FAIL  " if f else "PASS  ")+h.strip())
        for x in f: print("      - "+x)
    sys.exit(1 if bad else 0)
if __name__=="__main__": main()
