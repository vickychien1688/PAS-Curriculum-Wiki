#!/usr/bin/env python3
"""EOW2 Unit 1 - Animal Friends : Vocabulary + Grammar worksheet.
Agreed 大題:
  P1 Vocabulary - Animals : matching picture<->word
  P2 Vocabulary - Action verbs : matching picture<->word
  P3 Grammar    - Present progressive: They're ___ing (fill in, word bank)
  P4 Grammar    - Scrambled sentences (write the sentence, single line)
  P5 Answer Key
De-backgrounded art, single write line, roomy. Scope: EOW2 Unit 1 ONLY.
Value: Be good to animals.
"""
import os
from PIL import Image, ImageDraw
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

GF = "/usr/share/fonts/truetype/google-fonts"
pdfmetrics.registerFont(TTFont("Pop",  f"{GF}/Poppins-Regular.ttf"))
pdfmetrics.registerFont(TTFont("PopB", f"{GF}/Poppins-Bold.ttf"))
pdfmetrics.registerFont(TTFont("PopM", f"{GF}/Poppins-Medium.ttf"))

W, H = A4
INK  = HexColor("#1b1b1b"); GREY = HexColor("#6b7280")
ACC  = HexColor("#2f6fb0"); ACCL = HexColor("#eef4fb")
CARD = HexColor("#dbe4ee"); RULE = HexColor("#9aa3ad")
HERE = os.path.dirname(os.path.abspath(__file__))
LIB  = os.path.normpath(os.path.join(HERE, "..", "..", "09_Image_Library", "words"))
OUT  = os.path.join(HERE, "EOW2 U1 Animal Friends.pdf")
UNIT_TAG = "EOW2 · Unit 1 · Animal Friends"
VALUE = "Value: Be good to animals."
ML, MR = 42, W-42
TOTAL = 5
c = canvas.Canvas(OUT, pagesize=A4)

CACHE = os.path.join(HERE, "_trans"); os.makedirs(CACHE, exist_ok=True)
def transparent(word, thresh=60):
    out = os.path.join(CACHE, f"{word}.png")
    if os.path.exists(out): return out
    im = Image.open(f"{LIB}/{word}/{word}-v1-color.png").convert("RGB")
    w, h = im.size; SENT = (1, 2, 3)
    for cn in ((0,0),(w-1,0),(0,h-1),(w-1,h-1)):
        if im.getpixel(cn)[0] > 200:
            ImageDraw.floodfill(im, cn, SENT, thresh=thresh)
    px = im.load(); rgba = im.convert("RGBA"); rp = rgba.load()
    for y in range(h):
        for x in range(w):
            if px[x, y] == SENT: rp[x, y] = (255,255,255,0)
    # auto-crop to the subject so every animal fills its box consistently (fixes small cow)
    bbox = rgba.split()[3].getbbox()
    if bbox:
        pad = 6
        l, t, r, b = bbox
        rgba = rgba.crop((max(0,l-pad), max(0,t-pad), min(w,r+pad), min(h,b+pad)))
    rgba.save(out); return out

def img(word, cx, cy, s):
    c.drawImage(transparent(word), cx-s/2, cy-s/2, s, s, preserveAspectRatio=True, mask='auto')

SCENES = os.path.join(HERE, "scenes")
def scene_thumb(name, x, cyc, s):
    """square scene illustration with a soft border; x = left edge, cyc = vertical center."""
    p = os.path.join(SCENES, name)
    if not os.path.exists(p):
        return False
    c.drawImage(p, x, cyc-s/2, s, s, preserveAspectRatio=True, mask='auto')
    c.setStrokeColor(CARD); c.setLineWidth(1.3); c.setDash()
    c.roundRect(x, cyc-s/2, s, s, 6, fill=0, stroke=1)
    c.setStrokeColor(INK)
    return True

def badge(cx, cy, r, txt, fs, fill=ACC):
    c.setFillColor(fill); c.circle(cx, cy, r, fill=1, stroke=0)
    c.setFillColor(white); c.setFont("PopB", fs)
    c.drawCentredString(cx, cy-fs*0.36, txt); c.setFillColor(INK)

def dot(x, y, r=4, fill=ACC):
    c.setFillColor(fill); c.circle(x, y, r, fill=1, stroke=0); c.setFillColor(INK)

def dotted_h(x0, x1, y, col=CARD):
    c.setStrokeColor(col); c.setLineWidth(1.3); c.setDash(1.5, 3.5)
    c.line(x0, y, x1, y); c.setDash(); c.setStrokeColor(INK)

def wline(x0, x1, base):
    c.setStrokeColor(RULE); c.setLineWidth(1.5); c.setDash()
    c.line(x0, base, x1, base); c.setStrokeColor(INK)

def header(page, title):
    c.setFillColor(white); c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(INK); c.setFont("PopB", 11.5)
    c.drawString(ML, H-48, "NAME:"); c.setLineWidth(1.4); c.setStrokeColor(INK)
    c.line(ML+50, H-50, ML+260, H-50)
    c.drawString(ML+300, H-48, "DATE:"); c.line(ML+346, H-50, MR, H-50)
    fs=27; tw=pdfmetrics.stringWidth(title,"PopB",fs); bx=W/2-(tw+46)/2
    badge(bx+17, H-92, 17, "1", 21)
    c.setFillColor(INK); c.setFont("PopB", fs); c.drawString(bx+46, H-92-fs*0.36, title)
    c.setFont("PopM", 9.5); c.setFillColor(GREY)
    c.drawRightString(MR, H-71, UNIT_TAG); c.drawRightString(MR, H-84, f"Page {page} / {TOTAL}")
    c.setStrokeColor(ACC); c.setLineWidth(2); c.line(ML, H-112, MR, H-112); c.setFillColor(INK)
    return H-134

def section(y, letter, label, instr=""):
    badge(ML+12, y, 13, letter, 15)
    c.setFillColor(INK); c.setFont("PopB", 17); c.drawString(ML+34, y-6, label)
    if instr:
        c.setFillColor(GREY); c.setFont("Pop", 10.5); c.drawString(ML+34, y-23, instr)
    c.setFillColor(INK)
    return y-(40 if instr else 26)

def word_bank(y, words):
    c.setFillColor(ACCL); c.setStrokeColor(ACC); c.setLineWidth(1.4); c.setDash(2,3)
    c.roundRect(ML, y-34, MR-ML, 46, 10, fill=1, stroke=1); c.setDash()
    c.setFillColor(ACC); c.setFont("PopB", 10); c.drawString(ML+12, y-2, "WORD BANK")
    c.setFillColor(INK); c.setFont("PopM", 12.5)
    c.drawCentredString(W/2, y-22, "      ".join(words)); c.setFillColor(INK)
    return y-50

def footer():
    c.setStrokeColor(CARD); c.setLineWidth(1); c.line(ML, 42, MR, 42)
    c.setFillColor(GREY); c.setFont("PopM", 9)
    c.drawString(ML, 29, UNIT_TAG); c.drawRightString(MR, 29, VALUE); c.setFillColor(INK)

# ============================================================
# MATCHING PAGE  (連連看)
# ============================================================
def matching_page(page, letter, label, left_items, right_words):
    """left_items: [(slug,label)] in order; right_words: shuffled labels."""
    y = header(page, "Animal Friends")
    y = section(y, letter, label, "Draw a line from each picture to the correct word.")
    n = len(left_items)
    pitch = (y - 66)/n; top = y - 6
    picx = ML+78; ldotx = ML+170; rdotx = MR-210; wordx = MR-196
    for i in range(n):
        cyL = top - pitch*(i+0.5)
        slug,_lab = left_items[i]
        img(slug, picx, cyL, min(66, pitch-8))
        dot(ldotx, cyL)
        # right word in a pill
        cyR = top - pitch*(i+0.5)
        word = right_words[i]
        dot(rdotx, cyR)
        tw = pdfmetrics.stringWidth(word, "PopM", 14)
        c.setFillColor(white); c.setStrokeColor(CARD); c.setLineWidth(1.4); c.setDash()
        c.roundRect(wordx, cyR-15, tw+28, 30, 8, fill=1, stroke=1)
        c.setFillColor(INK); c.setFont("PopM", 14); c.drawString(wordx+14, cyR-5, word)
    footer(); c.showPage()

animals = [("cat","a cat"),("chicken","a chicken"),("cow","a cow"),("dog","a dog"),
           ("duck","a duck"),("goat","a goat"),("horse","a horse"),("sheep","a sheep"),
           ("turtle","a turtle")]
animals_right = ["a duck","a horse","a cat","a goat","a turtle","a cow","a chicken","a sheep","a dog"]
matching_page(1, "A", "Animals — match", animals, animals_right)

# Page 2 : Action words — circle the correct word (different type from P1 matching)
y = header(2, "Animal Friends")
y = section(y, "B", "Action words — circle the correct word",
            "Look at the picture. Circle the word that matches.")
vrows = [
    ("climb", ["climb","swim","fly"]),
    ("crawl", ["fly","crawl","swim"]),
    ("fly",   ["swim","climb","fly"]),
    ("swim",  ["crawl","swim","climb"]),
]
optx = [ML+160, ML+300, ML+440]
pitch = (y - 70)/len(vrows); top = y
for i,(slug,opts) in enumerate(vrows):
    cy = top - pitch*(i+0.5)
    if i % 2 == 0:
        c.setFillColor(ACCL); c.roundRect(ML, cy-pitch/2+8, MR-ML, pitch-16, 10, fill=1, stroke=0)
    c.setFillColor(INK)
    badge(ML+22, cy, 13, str(i+1), 14)
    img(slug, ML+92, cy, 92)
    c.setFont("PopM", 15)
    for k,opt in enumerate(opts):
        c.setFillColor(INK); c.drawString(optx[k], cy-6, opt)
footer(); c.showPage()

# ============================================================
# PAGE 3 : They're ___ing  (present progressive fill-in)
# ============================================================
y = header(3, "Animal Friends")
y = section(y, "A", "What are they doing?",
            "Look at the action. Write the -ing verb on the line.")
y = word_bank(y, ["climbing","crawling","flying","swimming"])
rows = [("cats-climbing.png","They are"), ("turtles-crawling.png","They are"),
        ("birds-flying.png","They are"),  ("ducks-swimming.png","They are")]
pitch = (y - 70)/len(rows); top = y
for i,(scenef,stem) in enumerate(rows):
    cy = top - pitch*(i+0.5)
    if i % 2 == 0:
        c.setFillColor(ACCL); c.roundRect(ML, cy-pitch/2+8, MR-ML, pitch-16, 10, fill=1, stroke=0)
    c.setFillColor(INK)
    badge(ML+20, cy, 13, str(i+1), 14)                     # number at the front of the row
    s = 96; scene_thumb(scenef, ML+46, cy, s)              # big scene illustration of the action
    tx = ML+46 + s + 20
    c.setFillColor(INK); c.setFont("PopM", 16); c.drawString(tx, cy-6, stem)
    sx = tx + pdfmetrics.stringWidth(stem+" ", "PopM", 16)
    wline(sx, MR-44, cy-9)
    c.setFont("PopM", 16); c.drawString(MR-38, cy-6, ".")
footer(); c.showPage()

# ============================================================
# PAGE 4 : Scrambled sentences
# ============================================================
y = header(4, "Animal Friends")
y = section(y, "A", "Put the words in order",
            "Look at the picture. Write the sentence on the line. Add the end mark ( .  or  ? ).")
scram = [   # (subject animal, action, scrambled tokens)
    ("cat",    "climb", ["climbing","the","cats","are"]),
    ("duck",   "swim",  ["the","ducks","are","swimming"]),
    ("turtle", "crawl", ["crawling","the","turtles","are"]),
    ("goat",   None,     ["doing","what","are","the","goats"]),
    ("bird",   "fly",   ["flying","the","birds","are"]),
]
scene_files = ["cats-climbing.png","ducks-swimming.png","turtles-crawling.png",
               "goats.png","birds-flying.png"]
pitch = (y - 50)/len(scram); top = y
for i,(animal, action, toks) in enumerate(scram):
    cellTop = top - pitch*i
    cmid = cellTop - pitch/2
    if i % 2 == 0:
        c.setFillColor(ACCL); c.roundRect(ML, cellTop-pitch+8, MR-ML, pitch-12, 10, fill=1, stroke=0)
    c.setFillColor(INK)
    badge(ML+20, cmid, 12, str(i+1), 13)                    # number at the front of the row
    s = 96
    scene_thumb(scene_files[i], ML+46, cmid, s)             # big scene matching the sentence
    chipx = ML+46 + s + 18
    # chips (upper row)
    cx = chipx; c.setFont("PopM", 12.5)
    for t in toks:
        tw = pdfmetrics.stringWidth(t, "PopM", 12.5)
        c.setFillColor(white); c.setStrokeColor(ACC); c.setLineWidth(1.2); c.setDash()
        c.roundRect(cx, cmid+10, tw+16, 24, 7, fill=1, stroke=1)
        c.setFillColor(INK); c.drawString(cx+8, cmid+18, t)
        cx += tw+16+7
    # write line (lower) + end-mark slot right after it — extra gap above for writing
    liney = cmid - 42
    wline(chipx, MR-54, liney)
    c.setStrokeColor(ACC); c.setLineWidth(1.2); c.setDash(2,2)
    c.roundRect(MR-46, liney-5, 24, 26, 5, fill=0, stroke=1); c.setDash()
    c.setFillColor(GREY); c.setFont("Pop", 8); c.drawCentredString(MR-34, liney-15, ". ?"); c.setFillColor(INK)
footer(); c.showPage()

# ============================================================
# PAGE 5 : Answer Key
# ============================================================
y = header(5, "Answer Key")
def keyrow(y, tag, label, lines):
    badge(ML+14, y, 14, tag, 11)
    c.setFillColor(INK); c.setFont("PopB", 14); c.drawString(ML+40, y-5, label)
    c.setFont("PopM", 11.5); yy = y-24
    for ln in lines:
        c.drawString(ML+40, yy, ln); yy -= 17
    yy -= 10; dotted_h(ML, MR, yy+15); return yy-4

y = keyrow(y, "1", "Animals — match (picture → word)",
    ["cat→a cat, chicken→a chicken, cow→a cow, dog→a dog, duck→a duck,",
     "goat→a goat, horse→a horse, sheep→a sheep, turtle→a turtle"])
y = keyrow(y, "2", "Action words — circle the correct word",
    ["1. climb   2. crawl   3. fly   4. swim"])
y = keyrow(y, "3", "What are they doing? (-ing)",
    ["1. climbing   2. crawling   3. flying   4. swimming"])
y = keyrow(y, "4", "Put the words in order",
    ["1. The cats are climbing.   2. The ducks are swimming.",
     "3. The turtles are crawling.   4. What are the goats doing?",
     "5. The birds are flying."])

c.setFont("PopB", 12); c.setFillColor(INK); c.drawString(ML+40, y-6, "Teacher notes")
c.setFont("Pop", 10.5); c.setFillColor(GREY)
c.drawString(ML+40, y-24, "Patterns: WS-001 / WS-022 / WS-017.  Single write line; de-backgrounded art.")
c.drawString(ML+40, y-40, "Scope: EOW2 Unit 1 only. Present progressive uses in-scope verbs only.")
c.drawString(ML+40, y-56, "Art: 09_Image_Library (color).  Source: 01_EOW/EOW2/unit-01.")
c.drawString(ML+40, y-72, VALUE); c.setFillColor(INK)
c.save(); print("done ->", OUT)
