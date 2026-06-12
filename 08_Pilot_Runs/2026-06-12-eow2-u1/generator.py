#!/usr/bin/env python3
"""EOW2 U1 Animal Friends — 3-page worksheet, PAS reference layout."""
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import icons_animals as IA
ICON = IA.ICONS

GF = "/usr/share/fonts/truetype/google-fonts"
pdfmetrics.registerFont(TTFont("Pop",  f"{GF}/Poppins-Regular.ttf"))
pdfmetrics.registerFont(TTFont("PopB", f"{GF}/Poppins-Bold.ttf"))
pdfmetrics.registerFont(TTFont("PopM", f"{GF}/Poppins-Medium.ttf"))

W, H = A4
INK = HexColor("#111111"); GREY = HexColor("#333333")
OUTDIR = "/sessions/epic-elegant-einstein/mnt/GitHub/PAS Curriculum Wiki/08_Pilot_Runs/2026-06-12-eow2-u1"
import os; os.makedirs(OUTDIR, exist_ok=True)
c = canvas.Canvas(f"{OUTDIR}/EOW2 U1 Animal Friends.pdf", pagesize=A4)

def badge(x, y, r, txt, fs):
    c.setFillColor(INK); c.circle(x, y, r, fill=1, stroke=0)
    c.setFillColor(white); c.setFont("PopB", fs)
    c.drawCentredString(x, y - fs*0.36, txt); c.setFillColor(INK)

def dotted_h(x0, x1, y):
    c.setStrokeColor(INK); c.setLineWidth(1.4); c.setDash(1.5, 3.5)
    c.line(x0, y, x1, y); c.setDash()

def dotted_v(x, y0, y1):
    c.setStrokeColor(INK); c.setLineWidth(1.4); c.setDash(1.5, 3.5)
    c.line(x, y0, x, y1); c.setDash()

def header(page, total, title="Animal Friends"):
    c.setFillColor(white); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(INK); c.setFont("PopB", 13)
    c.drawString(36, H-52, "NAME:")
    c.setLineWidth(1.6); c.setStrokeColor(INK)
    c.line(92, H-54, 320, H-54)
    c.drawString(380, H-52, "DATE:"); c.line(432, H-54, 560, H-54)
    fs = 34
    max_right = W - 220          # keep clear of top-right meta block
    while fs > 20:
        tw = pdfmetrics.stringWidth(title, "PopB", fs)
        bx = W/2 - (tw + 52)/2
        if bx + 52 + tw <= max_right and bx >= 110: break
        fs -= 1
    tw = pdfmetrics.stringWidth(title, "PopB", fs)
    bx = max(110, W/2 - (tw + 52)/2)
    badge(bx + 20, H-100, 20, "1", 24)
    c.setFillColor(INK); c.setFont("PopB", fs); c.drawString(bx + 52, H-100 - fs*0.36, title)
    c.setFont("PopM", 10)
    c.drawRightString(W-30, H-76, "EOW2 · Unit 1 · Animal Friends")
    c.drawRightString(W-30, H-91, f"Page {page} / {total}")
    return H - 150

def section(y, letter, label, instr):
    badge(52, y, 14, letter, 16)
    c.setFillColor(INK); c.setFont("PopB", 19); c.drawString(78, y-7, label)
    c.setFillColor(GREY); c.setFont("Pop", 11.5); c.drawString(78, y-26, instr)
    c.setFillColor(INK)
    return y - 48

def num(x, y, n): badge(x, y, 11, str(n), 13)

def wline(x0, x1, y):
    c.setStrokeColor(INK); c.setLineWidth(1.2); c.setDash(2.5, 2.5)
    c.line(x0, y, x1, y); c.setDash()

# ================= PAGE 1 =================
y = header(1, 3)
y = section(y, "A", "Match", "Draw a line from the picture to the word.")
pics  = ["duck", "cat", "sheep", "cow", "turtle", "dog"]
words = ["cat", "cow", "dog", "duck", "sheep", "turtle"]   # alphabetical
row = 64; topA = y - 24
for i, p in enumerate(pics):
    cy = topA - i*row
    num(48, cy, i+1)
    ICON[p](c, 145, cy, 64)
    c.setFillColor(INK); c.circle(250, cy, 3.2, fill=1, stroke=0)
for i, wd in enumerate(words):
    cy = topA - i*row
    c.setFillColor(INK); c.circle(420, cy, 3.2, fill=1, stroke=0)
    c.setFont("PopM", 16); c.drawString(465, cy-6, wd)
y = topA - 5*row - 48
dotted_h(36, W-36, y)

y = section(y - 24, "B", "Circle the correct word", "Look at the picture. Circle the word.")
items_b = [("duck","duck","chicken"), ("cat","cat","dog"),
           ("sheep","sheep","goat"), ("cow","cow","horse")]
cell_w = (W-72)/2; b_top = y - 2; row_b = 76
for i, (pic, w1, w2) in enumerate(items_b):
    col = i % 2; r_ = i // 2
    x0 = 36 + col*cell_w
    cy = b_top - r_*row_b - 34
    num(x0+12, cy+14, i+1)
    ICON[pic](c, x0+74, cy, 52)
    c.setFillColor(INK); c.setFont("PopM", 13.5)
    c.drawString(x0+126, cy-5, f"{w1}  /  {w2}")
dotted_v(36+cell_w, b_top-2, b_top-2*row_b+10)
dotted_h(60, W-60, b_top-row_b+6)
c.showPage()

# ================= PAGE 2 =================
y = header(2, 3)
y = section(y, "C", "What are they doing?", "Look. Write the word.")
c.setFont("PopB", 12); c.setFillColor(INK)
c.drawString(360, y+40, "word bank:")
c.setFont("PopM", 11.5)
c.drawString(360, y+22, "climbing  crawling  sleeping  swimming")
c.setLineWidth(1.4); c.setStrokeColor(INK); c.setDash(1.5,3.5)
c.roundRect(348, y+8, 212, 50, 8, fill=0, stroke=1); c.setDash()

items_c = [("duck", "ducks", "swim"), ("turtle", "turtles", "crawl"),
           ("cat", "cats", "climb"), ("sheep", "sheep", "sleep")]
topC = y - 40
for i,(pic, plural, verb) in enumerate(items_c):
    ry = topC - i*92
    num(48, ry+10, i+1)
    for k in range(2):
        ICON[pic](c, 105 + k*66, ry+10, 56)
    if verb == "sleep": IA.zzz(c, 188, ry+28, 56)
    c.setFillColor(INK); c.setFont("PopM", 13.5)
    c.drawString(252, ry+22, f"What are the {plural} doing?")
    c.drawString(252, ry-4, "They are")
    wline(316, 440, ry-8)
    c.setFont("Pop", 12); c.drawString(448, ry-4, f". ({verb})")
y = topC - 3*92 - 60
dotted_h(36, W-36, y)

y = section(y - 24, "D", "What do you want to do?", "Write the answer.")
ICON["horse"](c, 100, y-30, 60)
c.setFillColor(INK); c.setFont("PopM", 13.5)
c.drawString(150, y-24, "Do you want to ride the horse?   Yes, I")
wline(400, 470, y-28); c.drawString(476, y-24, ".")
ICON["duck"](c, 100, y-88, 56)
c.drawString(150, y-82, "What do you want to do?  I want to")
wline(382, 452, y-86); c.drawString(458, y-82, "the ducks. (see)")
ICON["sheep"](c, 100, y-146, 56)
c.drawString(150, y-140, "She")
wline(184, 254, y-144); c.drawString(260, y-140, "to see the sheep. (want)")
for i in range(3): num(48, y-30-58*i, i+1)
c.showPage()

# ================= PAGE 3 =================
y = header(3, 3)
y = section(y, "E", "Unscramble the words", "Put the letters in order. Write the word.")
items_e = [("cat","t a c"), ("dog","g d o"), ("duck","k c d u"),
           ("cow","w o c"), ("sheep","h p e e s"), ("turtle","l e t r u t")]
cell_w = (W-72)/2; e_top = y - 6; row_e = 92
for i,(word, scr) in enumerate(items_e):
    col = i % 2; r_ = i // 2
    x0 = 36 + col*cell_w
    cy = e_top - r_*row_e - 40
    num(x0+12, cy+16, i+1)
    ICON[word](c, x0+74, cy+6, 54)
    c.setFillColor(INK); c.setFont("PopB", 15)
    c.drawString(x0+126, cy+14, scr)
    wline(x0+126, x0+240, cy-16)
dotted_v(36+cell_w, e_top-6, e_top-3*row_e+18)
for r_ in (1,2):
    dotted_h(60, W-60, e_top-r_*row_e+14)
y = e_top - 3*row_e - 6
dotted_h(36, W-36, y)

# Answer key
c.setFillColor(INK); c.circle(52, y-26, 14, fill=1, stroke=0)
c.setFillColor(white); c.setFont("ZapfDingbats", 14); c.drawCentredString(52, y-31, "4")
c.setFillColor(INK); c.setFont("PopB", 19); c.drawString(78, y-33, "Answer Key")
y = y - 74
c.setFillColor(INK)
rows = [
 ("A. Match", "1-duck  2-cat  3-sheep  4-cow  5-turtle  6-dog"),
 ("B. Circle", "1. duck   2. cat   3. sheep   4. cow"),
 ("C. What are they doing?", "1. swimming   2. crawling   3. climbing   4. sleeping"),
 ("D. Want to", "1. do   2. see   3. wants"),
 ("E. Unscramble", "1. cat  2. dog  3. duck  4. cow  5. sheep  6. turtle"),
 ("Teacher notes", "WS-001/002/003/006/016 · Scope: EOW2 U1 · Be good to animals."),
]
ty = y + 4
for label, ans in rows:
    c.setFont("PopB", 11.5); c.drawString(52, ty, label)
    c.setFont("Pop", 11); c.drawString(230, ty, ans)
    ty -= 22
c.save()
print("done")
