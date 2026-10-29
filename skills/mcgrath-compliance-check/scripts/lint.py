#!/usr/bin/env python3
"""Offline lint for McGrath Wide Bay captions and scripts. Python 3 stdlib only.
Usage: python3 lint.py caption.txt [--platform instagram|tiktok|facebook|linkedin] [--rental] [--auction] [--licensee-line]
Prints PASS or FIX with line-level findings. Never sends anything anywhere."""
import re, sys, argparse, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hooks import check as hook_check
BANNED = ["stunning","breathtaking","nestled","boasting","boasts","must see","won't last","rare opportunity","once in a lifetime",
 "entertainer's delight","oozes","sun-drenched","tightly held","priced to sell","motivated vendor","bring your offers","act fast",
 "don't miss out","the wait is over","hidden gem","slice of paradise","delve","dive into","deep dive","unlock","unleash","elevate",
 "embark","journey","seamless","game changer","next level","in today's fast-paced world","it's no secret","let's face it",
 "here's the thing","picture this","imagine waking up","look no further","more than just","testament to","a symphony of","tapestry",
 "realm","curated","leverage","utilise","utilize","robust","foster","showcase"]
RED = ["guaranteed","guarantee","risk-free","risk free","will sell for","will rent for","best agent","number one","#1 ","record price",
 "you should buy","you should sell","perfect for you","families only","professionals only","no kids","ideal for couples"]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("file"); ap.add_argument("--platform",default="instagram")
    ap.add_argument("--rental",action="store_true"); ap.add_argument("--auction",action="store_true")
    ap.add_argument("--licensee-line",action="store_true",help="office profile has Show licensee line: yes")
    a=ap.parse_args(); text=open(a.file,encoding="utf-8").read(); low=text.lower(); f=[]
    if "\u2014" in text or "\u2013 " in text: f.append("Em or en dash found. Replace with a full stop or comma.")
    for w in BANNED:
        if re.search(r"(?<![a-z])"+re.escape(w)+r"(?![a-z])",low): f.append(f"Banned / cliché phrase: '{w}'.")
    for w in RED:
        if w in low: f.append(f"COMPLIANCE red flag: '{w.strip()}'. Check with the licensee-in-charge.")
    for i,p in enumerate([p for p in re.split(r"\n\s*\n",text) if p.strip()],1):
        n=len(re.findall(r"[.!?](\s|$)",p.strip()))
        if n>2: f.append(f"Paragraph {i} has {n} sentences. Max two.")
    tags=re.findall(r"#\w+",text)
    if len(tags)>3: f.append(f"{len(tags)} hashtags. Use three or fewer.")
    first=text.strip().splitlines()[0] if text.strip() else ""
    if a.platform!="caption-body":
        for x in hook_check(first):
            if "words. Land the hook" not in x: f.append("Hook: "+x)
        s1=re.split(r"(?<=[.!?])\s",first.strip())[0]
        if len(s1.split())>14: f.append(f"Hook: first sentence is {len(s1.split())} words. Land it in 14 or fewer.")
    if len(first)>125: f.append(f"First line is {len(first)} characters. Land the hook inside 125.")
    if a.platform=="tiktok" and re.search(r"link in bio|instagram|\bdm\b|comment .* (below|and)",low): f.append("TikTok caption has an Instagram-style CTA. Remove it.")
    if a.rental and re.search(r"offers? (above|over)|rent range|\$\d+\s*-\s*\$?\d+\s*(pw|per week|a week)",low): f.append("Rental: QLD requires a fixed rent. No ranges or offers above.")
    if a.auction and re.search(r"price guide|expect(ed)? (to sell|bidding)|offers? (over|above)|\$\d",low): f.append("Auction listing: no price guide or price hints in QLD.")
    if a.licensee_line and not re.search(r"lic(ence|ense)?\.?\s*(no\.?)?\s*\d",low): f.append("Office profile says show the licensee line, but no licence number found.")
    if re.search(r"median|market|growth|per cent|%",low) and not re.search(r"source",low): f.append("Stat or market claim without a 'Source:' line.")
    if re.search(r"utilize|organize|color\b|neighbor|center\b",low): f.append("US spelling found. Use Australian English.")
    print("PASS" if not f else "FIX"); [print(f" {i}. {x}") for i,x in enumerate(f,1)]
    print("\nReminder: this is an automatic first pass, not legal advice. Run the full mcgrath-compliance-check checklist too.")
if __name__=="__main__": main()
