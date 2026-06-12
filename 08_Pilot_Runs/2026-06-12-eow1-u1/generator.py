#!/usr/bin/env python3
"""EOW1 U1 My Classroom — v3, matches PAS reference layout:
white page, black rounded-bold type, black circle badges, dotted dividers,
realistic flat icons."""
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import icons2  # classroom icon library (same folder)
ICON = icons2.ICONS

GF = "/usr/share/fonts/truetype/google-fonts"
pdfmetrics.registerFont(TTFont("Pop",  f"{GF}/Poppins-Regular.ttf"))
pdfmetrics.registerFont(TTFont("PopB", f"{GF}/Poppins-Bold.ttf"))
pdfmetrics.registerFont(TTFont("PopM", f"{GF}/Poppins-Medium.ttf"))

W, H = A4
INK = HexColor("#111111")
GREY = HexColor("#333333")

c = canvas.Canvas(
    "/sessions/epic-elegant-einstein/mnt/GitHub/PAS Curriculum Wiki/08_Pilot_Runs/2026-06-12-eow1-u1/EOW1 U1 My Classroom.pdf",
    pagesize=A4)

def badge(x, y, r, txt, fs):
    c.setFillColor(INK); c.circle(x, y, r, fill=1, stroke=0)
    c.setFillColor(white); c.setFont("PopB", fs)
    c.drawCentredString(x, y - fs*0.36, txt)
    c.setFillColor(INK)

def dotted_h(x0, x1, y):
    c.setStrokeColor(INK); c.setLineWidth(1.4); c.setDash(1.5, 3.5)
    c.line(x0, y, x1, y); c.setDash()

def dotted_v(x, y0, y1):
    c.setStrokeColor(INK); c.setLineWidth(1.4); c.setDash(1.5, 3.5)
    c.line(x, y0, x, y1); c.setDash()

def header(page, total, title="My Classroom"):
    c.setFillColor(white); c.rect(0, 0, W, H, fill=1, stroke=0)
    # NAME / DATE
    c.setFillColor(INK); c.setFont("PopB", 13)
    c.drawString(36, H-52, "NAME:")
    c.setLineWidth(1.6); c.setStrokeColor(INK)
    c.line(92, H-54, 320, H-54)
    c.drawString(380, H-52, "DATE:")
    c.line(432, H-54, 560, H-54)
    # title (centered block: badge + text, auto-shrinks to avoid the meta block)
    fs = 34
    max_right = W - 220
    while fs > 20:
        tw = pdfmetrics.stringWidth(title, "PopB", fs)
        bx = W/2 - (tw + 52)/2
        if bx + 52 + tw <= max_right and bx >= 110: break
        fs -= 1
    tw = pdfmetrics.stringWidth(title, "PopB", fs)
    bx = max(110, W/2 - (tw + 52)/2)
    badge(bx + 20, H-100, 20, str(1), 24)
    c.setFillColor(INK); c.setFont("PopB", fs)
    c.drawString(bx + 52, H-100 - fs*0.36, title)
    # meta top right
    c.setFont("PopM", 10)
    c.drawRightString(W-30, H-76, "EOW1 · Unit 1 · My Classroom")
    c.drawRightString(W-30, H-91, f"Page {page} / {total}")
    return H - 150

def section(y, letter, label, instr):
    badge(52, y, 14, letter, 16)
    c.setFillColor(INK); c.setFont("PopB", 19)
    c.drawString(78, y-7, label)
    c.setFillColor(GREY); c.setFont("Pop", 11.5)
    c.drawString(78, y-26, instr)
    c.setFillColor(INK)
    return y - 48

def num(x, y, n):
    badge(x, y, 11, str(n), 13)

def wline(x0, x1, y):
    c.setStrokeColor(INK); c.setLineWidth(1.2); c.setDash(2.5, 2.5)
    c.line(x0, y, x1, y); c.setDash()

# ================= PAGE 1 =================
y = header(1, 3)
y = section(y, "A", "Match", "Draw a line from the picture to the word.")

pics  = ["pencil", "clock", "computer", "book", "desk", "chair"]
words = ["book", "chair", "clock", "computer", "desk", "pencil"]
row = 64; topA = y - 24
for i, p in enumerate(pics):
    cy = topA - i*row
    num(48, cy, i+1)
    ICON[p](c, 145, cy, 72)
    c.setFillColor(INK); c.circle(250, cy, 3.2, fill=1, stroke=0)
for i, wd in enumerate(words):
    cy = topA - i*row
    c.setFillColor(INK); c.circle(420, cy, 3.2, fill=1, stroke=0)
    c.setFont("PopM", 16); c.drawString(465, cy-6, wd)
y = topA - 5*row - 48
dotted_h(36, W-36, y)

# B section
y = section(y - 24, "B", "Circle the correct word", "Look at the picture. Circle the word.")
items_b = [("pencil","pen","pencil"), ("book","book","chair"),
           ("clock","clock","computer"), ("chair","desk","chair")]
cell_w = (W-72)/2
b_top = y - 2
row_b = 76
for i, (pic, w1, w2) in enumerate(items_b):
    col = i % 2; r_ = i // 2
    x0 = 36 + col*cell_w
    cy = b_top - r_*row_b - 34
    num(x0+12, cy+14, i+1)
    ICON[pic](c, x0+74, cy, 58)
    c.setFillColor(INK); c.setFont("PopM", 13.5)
    c.drawString(x0+126, cy-5, f"{w1}  /  {w2}")
dotted_v(36+cell_w, b_top-2, b_top-2*row_b+10)
dotted_h(60, W-60, b_top-row_b+6)
c.showPage()

# ================= PAGE 2 =================
y = header(2, 3)
y = section(y, "C", "How many?", "Count. Write the number word.")
# word bank
c.setFont("PopB", 12); c.setFillColor(INK)
c.drawString(380, y+40, "word bank:")
c.setFont("PopM", 12.5)
c.drawString(380, y+22, "two   three   four   five")
c.setLineWidth(1.4); c.setStrokeColor(INK); c.setDash(1.5,3.5)
c.roundRect(366, y+8, 178, 50, 8, fill=0, stroke=1); c.setDash()

items_c = [("book",3), ("pencil",5), ("clock",2), ("chair",4)]
topC = y - 36
for i,(pic,n) in enumerate(items_c):
    ry = topC - i*86
    num(48, ry, i+1)
    for k in range(n):
        ICON[pic](c, 105 + k*62, ry, 56)
    c.setFillColor(INK); c.setFont("PopM", 14.5)
    c.drawString(388, ry+8, f"How many {pic}s?")
    wline(390, 548, ry-16)
y = topC - 3*86 - 60
dotted_h(36, W-36, y)

# D section
y = section(y-28, "D", "What is it?", "Write the answer.")
qs = [("clock", "What is it?    It is a", True),
      ("book",  "What is it?    It is a", True),
      ("desk",  "Is it a desk?", False)]
for i,(pic,q,mid) in enumerate(qs):
    ry = y - 36 - i*78
    num(48, ry, i+1)
    ICON[pic](c, 115, ry, 64)
    c.setFillColor(INK); c.setFont("PopM", 15)
    c.drawString(168, ry-5, q)
    if mid:
        wline(330, 500, ry-9); c.drawString(506, ry-5, ".")
    else:
        wline(268, 380, ry-9); c.drawString(386, ry-5, ", it is.")
c.showPage()

# ================= PAGE 3 : ANSWER KEY =================
y = header(3, 3, title="Answer Key")
rows = [
    ("A", "Match", "1-pencil   2-clock   3-computer   4-book   5-desk   6-chair"),
    ("B", "Circle the correct word", "1. pencil    2. book    3. clock    4. chair"),
    ("C", "How many?", "1. three books    2. five pencils    3. two clocks    4. four chairs"),
    ("D", "What is it?", "1. It is a clock.    2. It is a book.    3. Yes, it is."),
]
for letter, label, ans in rows:
    y = section(y, letter, label, "")
    c.setFillColor(INK); c.setFont("PopM", 13.5)
    c.drawString(78, y+10, ans)
    y -= 44
    dotted_h(36, W-36, y+22)
    y -= 8

c.setFont("PopB", 12.5); c.setFillColor(INK)
c.drawString(78, y-6, "Teacher notes")
c.setFont("Pop", 11)
c.drawString(78, y-26, "Patterns: WS-001 / WS-002 / WS-003 / WS-006")
c.drawString(78, y-44, "Scope: EOW1 Unit 1 only — Yes/No questions with it's; What / How many")
c.drawString(78, y-62, "Value: Work hard in school.")
c.save()
print("done")
