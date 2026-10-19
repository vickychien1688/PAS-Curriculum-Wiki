#!/usr/bin/env python3
"""EOW2 Unit 3 - Boots and Bathing Suits : Vocabulary + Grammar worksheet (v4).
Agreed 大題:
  P1 Vocabulary - Weather: circle the correct word (roomy)
  P2 Vocabulary - Clothes: circle the correct word (roomy)
  P3 Grammar 1  - What's the weather like? It's ___ (single write line, word bank)
  P4 Grammar 2  - Imperatives: circle + sentence builder (single write line)
  P5 Answer Key
No tracing (EOW1-only). Single write line for EOW2/3 (no 3-line ruling).
Real art from 09_Image_Library. Scope: EOW2 Unit 3 ONLY. Value: Dress for the weather.
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
OUT  = os.path.join(HERE, "EOW2 U3 Boots and Bathing Suits.pdf")
UNIT_TAG = "EOW2 · Unit 3 · Boots and Bathing Suits"
VALUE = "Value: Dress for the weather."
ML, MR = 42, W-42
TOTAL = 5
c = canvas.Canvas(OUT, pagesize=A4)

CACHE = os.path.join(HERE, "_trans")
os.makedirs(CACHE, exist_ok=True)

def transparent(word, thresh=60):
    """Cache a version with the exterior white background flood-filled to transparent.
    Interior whites (snowflake, sneakers, etc.) are preserved."""
    out = os.path.join(CACHE, f"{word}.png")
    if os.path.exists(out):
        return out
    im = Image.open(f"{LIB}/{word}/{word}-v1-color.png").convert("RGB")
    w, h = im.size
    SENT = (1, 2, 3)
    for corner in ((0,0),(w-1,0),(0,h-1),(w-1,h-1)):
        if im.getpixel(corner)[0] > 200:  # only flood if corner is light
            ImageDraw.floodfill(im, corner, SENT, thresh=thresh)
    px = im.load()
    rgba = im.convert("RGBA"); rp = rgba.load()
    for y in range(h):
        for x in range(w):
            if px[x, y] == SENT:
                rp[x, y] = (255, 255, 255, 0)
    rgba.save(out)
    return out

def img(word, cx, cy, s):
    c.drawImage(transparent(word), cx-s/2, cy-s/2, s, s,
                preserveAspectRatio=True, mask='auto')

def badge(cx, cy, r, txt, fs, fill=ACC):
    c.setFillColor(fill); c.circle(cx, cy, r, fill=1, stroke=0)
    c.setFillColor(white); c.setFont("PopB", fs)
    c.drawCentredString(cx, cy-fs*0.36, txt); c.setFillColor(INK)

def dotted_h(x0, x1, y, col=CARD):
    c.setStrokeColor(col); c.setLineWidth(1.3); c.setDash(1.5, 3.5)
    c.line(x0, y, x1, y); c.setDash(); c.setStrokeColor(INK)

def wline(x0, x1, base):
    """single solid write line, baseline at `base`."""
    c.setStrokeColor(RULE); c.setLineWidth(1.5); c.setDash()
    c.line(x0, base, x1, base); c.setStrokeColor(INK)

def header(page, title):
    c.setFillColor(white); c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(INK); c.setFont("PopB", 11.5)
    c.drawString(ML, H-48, "NAME:"); c.setLineWidth(1.4); c.setStrokeColor(INK)
    c.line(ML+50, H-50, ML+260, H-50)
    c.drawString(ML+300, H-48, "DATE:"); c.line(ML+346, H-50, MR, H-50)
    fs=29; tw=pdfmetrics.stringWidth(title,"PopB",fs); bx=W/2-(tw+46)/2
    badge(bx+17, H-92, 17, "3", 21)
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
# VOCAB PAGE : circle the correct word (one section, roomy)
# ============================================================
def vocab_page(page, letter, label, items):
    y = header(page, "Boots & Bathing Suits")
    y = section(y, letter, label, "Look at the picture. Circle the word that matches.")
    optx = [ML+120, ML+272, ML+424]
    pitch = (y - 70)/len(items); top = y
    for i,(slug, opts) in enumerate(items):
        cy = top - pitch*(i+0.5)
        if i % 2 == 0:
            c.setFillColor(ACCL); c.roundRect(ML, cy-pitch/2+7, MR-ML, pitch-14, 10, fill=1, stroke=0)
        c.setFillColor(INK)
        badge(ML+24, cy, 12, str(i+1), 13)
        img(slug, ML+74, cy, 50)
        c.setFont("PopM", 13.5)
        for k,opt in enumerate(opts):
            c.setFillColor(INK); c.drawString(optx[k], cy-5, opt)
    footer(); c.showPage()

vocab_page(1, "A", "Weather — circle the correct word", [
    ("sunny",       ["sunny","rainy","cold"]),
    ("rainy",       ["hot","rainy","sunny"]),
    ("cloudy",      ["cloudy","sunny","hot"]),
    ("hot",         ["cold","hot","cloudy"]),
    ("cold",        ["cold","rainy","hot"]),
    ("bathing-suit",["a raincoat","a bathing suit","boots"]),
    ("boots",       ["boots","a coat","sneakers"]),
    ("raincoat",    ["a raincoat","an umbrella","shorts"]),
])
vocab_page(2, "B", "Clothes — circle the correct word", [
    ("coat",     ["a coat","jeans","shorts"]),
    ("jeans",    ["shorts","jeans","a coat"]),
    ("shorts",   ["shorts","sneakers","jeans"]),
    ("sneakers", ["boots","sneakers","a coat"]),
    ("umbrella", ["an umbrella","a raincoat","boots"]),
])

# ============================================================
# PAGE 3 : Grammar 1 - What's the weather like?
# ============================================================
y = header(3, "Boots & Bathing Suits")
y = section(y, "A", "What's the weather like?",
            "Look at the picture. Write the weather word on the line.")
y = word_bank(y, ["sunny","rainy","cloudy","hot","cold"])
items = ["sunny","rainy","cloudy","hot","cold"]
pitch = (y - 78)/len(items); top = y
for i,slug in enumerate(items):
    cy = top - pitch*(i+0.5)
    if i % 2 == 0:
        c.setFillColor(ACCL); c.roundRect(ML, cy-pitch/2+8, MR-ML, pitch-16, 10, fill=1, stroke=0)
    c.setFillColor(INK)
    badge(ML+24, cy, 13, str(i+1), 14)
    img(slug, ML+80, cy, 62)
    c.setFillColor(INK); c.setFont("PopM", 16); c.drawString(ML+128, cy-6, "It's")
    lx = ML+128 + pdfmetrics.stringWidth("It's  ", "PopM", 16)
    wline(lx, MR-58, cy-9)
    c.setFont("PopM", 16); c.drawString(MR-50, cy-6, ".")
footer(); c.showPage()

# ============================================================
# PAGE 4 : Grammar 2 - Imperatives
# ============================================================
y = header(4, "Boots & Bathing Suits")
y = section(y, "A", "Dress for the weather!",
            "Read. Look at the picture. Circle the best sentence.")
itemsC = [
    ("rainy", "It's rainy.", "Put on your raincoat.", "Put on your shorts."),
    ("cold",  "It's cold.",  "Put on your coat.",     "Put on your bathing suit."),
    ("hot",   "It's hot.",   "Put on your bathing suit.", "Put on your boots."),
    ("sunny", "It's sunny.", "Put on your sneakers.", "Put on your raincoat."),
]
topC = y; pitchC = 66
for i,(slug,cue,o1,o2) in enumerate(itemsC):
    cy = topC - pitchC*(i+0.5)
    if i % 2 == 0:
        c.setFillColor(ACCL); c.roundRect(ML, cy-pitchC/2+6, MR-ML, pitchC-12, 10, fill=1, stroke=0)
    c.setFillColor(INK)
    badge(ML+22, cy+8, 12, str(i+1), 13)
    img(slug, ML+70, cy+4, 48)
    c.setFillColor(INK); c.setFont("PopB", 13); c.drawString(ML+108, cy+14, cue)
    c.setFont("PopM", 12)
    c.drawString(ML+122, cy-9, "a)  " + o1)
    c.drawString(ML+322, cy-9, "b)  " + o2)
y = topC - pitchC*len(itemsC) - 6
dotted_h(ML, MR, y)
y = section(y-16, "B", "Finish the sentence",
            "Choose a word from the box. Write it on the line.")
y = word_bank(y, ["coat","boots","umbrella","sneakers"])
itemsD = [
    ("cold",  "It's cold.  Put on your"),
    ("rainy", "It's rainy.  Don't forget your"),
    ("hot",   "It's hot.  Put on your"),
]
pitchD = (y - 70)/len(itemsD); topD = y
for i,(slug,stem) in enumerate(itemsD):
    cy = topD - pitchD*(i+0.5)
    badge(ML+22, cy, 12, str(i+1), 13)
    img(slug, ML+70, cy, 48)
    c.setFillColor(INK); c.setFont("PopM", 13.5); c.drawString(ML+108, cy-6, stem)
    sx = ML+108 + pdfmetrics.stringWidth(stem+" ", "PopM", 13.5)
    wline(sx, MR-42, cy-9)
    c.setFont("PopM", 13.5); c.drawString(MR-36, cy-6, ".")
footer(); c.showPage()

# ============================================================
# PAGE 5 : Answer Key
# ============================================================
y = header(5, "Answer Key")
def keyrow(y, tag, label, lines):
    badge(ML+14, y, 14, tag, 11)
    c.setFillColor(INK); c.setFont("PopB", 14); c.drawString(ML+40, y-5, label)
    c.setFont("PopM", 12); yy = y-24
    for ln in lines:
        c.drawString(ML+40, yy, ln); yy -= 18
    yy -= 10; dotted_h(ML, MR, yy+16); return yy-4

y = keyrow(y, "1", "Weather — circle",
    ["1. sunny   2. rainy   3. cloudy   4. hot   5. cold",
     "6. a bathing suit   7. boots   8. a raincoat"])
y = keyrow(y, "2", "Clothes — circle",
    ["1. a coat   2. jeans   3. shorts   4. sneakers   5. an umbrella"])
y = keyrow(y, "3", "What's the weather like?",
    ["1. It's sunny.   2. It's rainy.   3. It's cloudy.   4. It's hot.   5. It's cold."])
y = keyrow(y, "4A", "Dress for the weather (circle)",
    ["1. a (Put on your raincoat.)   2. a (Put on your coat.)",
     "3. a (Put on your bathing suit.)   4. a (Put on your sneakers.)"])
y = keyrow(y, "4B", "Finish the sentence",
    ["1. Put on your coat.   2. Don't forget your umbrella.   3. Put on your sneakers."])

c.setFont("PopB", 12); c.setFillColor(INK); c.drawString(ML+40, y-6, "Teacher notes")
c.setFont("Pop", 10.5); c.setFillColor(GREY)
c.drawString(ML+40, y-24, "Patterns: WS-002 / WS-022 / WS-006.  No tracing; single write line (EOW2/3).")
c.drawString(ML+40, y-40, "Scope: EOW2 Unit 3 only.  Art: 09_Image_Library (color).  Source: 01_EOW/EOW2/unit-03.")
c.drawString(ML+40, y-56, VALUE); c.setFillColor(INK)
c.save(); print("done ->", OUT)
