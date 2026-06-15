#!/usr/bin/env python3
"""EOW1 U2 My World - Grammar 1+2 worksheet.
Matches PAS reference layout: white page, black rounded-bold type,
black circle badges, dotted dividers, simple flat nature icons.
Scope: EOW1 Unit 2 only - to be (is/are); Where + in/on.
"""
import os, math
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

GF = "/usr/share/fonts/truetype/google-fonts"
pdfmetrics.registerFont(TTFont("Pop",  f"{GF}/Poppins-Regular.ttf"))
pdfmetrics.registerFont(TTFont("PopB", f"{GF}/Poppins-Bold.ttf"))
pdfmetrics.registerFont(TTFont("PopM", f"{GF}/Poppins-Medium.ttf"))

W, H = A4
INK  = HexColor("#111111")
GREY = HexColor("#333333")

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "EOW1 U2 My World.pdf")
c = canvas.Canvas(OUT, pagesize=A4)

# ---------------- layout helpers ----------------
def badge(x, y, r, txt, fs):
    c.setFillColor(INK); c.circle(x, y, r, fill=1, stroke=0)
    c.setFillColor(white); c.setFont("PopB", fs)
    c.drawCentredString(x, y - fs*0.36, txt)
    c.setFillColor(INK)

def dotted_h(x0, x1, y):
    c.setStrokeColor(INK); c.setLineWidth(1.4); c.setDash(1.5, 3.5)
    c.line(x0, y, x1, y); c.setDash()

def wline(x0, x1, y):
    c.setStrokeColor(INK); c.setLineWidth(1.2); c.setDash(2.5, 2.5)
    c.line(x0, y, x1, y); c.setDash()

def num(x, y, n):
    badge(x, y, 11, str(n), 13)

def header(page, total, title="My World"):
    c.setFillColor(white); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(INK); c.setFont("PopB", 13)
    c.drawString(36, H-52, "NAME:")
    c.setLineWidth(1.6); c.setStrokeColor(INK)
    c.line(92, H-54, 320, H-54)
    c.drawString(380, H-52, "DATE:")
    c.line(432, H-54, 560, H-54)
    fs = 34
    tw = pdfmetrics.stringWidth(title, "PopB", fs)
    bx = max(110, W/2 - (tw + 52)/2)
    badge(bx + 20, H-100, 20, "2", 24)
    c.setFillColor(INK); c.setFont("PopB", fs)
    c.drawString(bx + 52, H-100 - fs*0.36, title)
    c.setFont("PopM", 10)
    c.drawRightString(W-30, H-76, "EOW1 · Unit 2 · My World")
    c.drawRightString(W-30, H-91, f"Page {page} / {total}")
    return H - 150

def section(y, letter, label, instr):
    badge(52, y, 14, letter, 16)
    c.setFillColor(INK); c.setFont("PopB", 19)
    c.drawString(78, y-7, label)
    if instr:
        c.setFillColor(GREY); c.setFont("Pop", 11.5)
        c.drawString(78, y-26, instr)
    c.setFillColor(INK)
    return y - (48 if instr else 30)

def value_footer():
    c.setFont("PopM", 10.5); c.setFillColor(GREY)
    c.drawCentredString(W/2, 34, "Value: Enjoy nature.")
    c.setFillColor(INK)

# ---------------- simple flat nature icons (centered at x,y) ----------------
def i_sun(x, y, s):
    r = s*0.28
    c.setStrokeColor(INK); c.setLineWidth(2)
    for k in range(8):
        a = k*math.pi/4
        c.line(x+math.cos(a)*r*1.5, y+math.sin(a)*r*1.5,
               x+math.cos(a)*r*2.1, y+math.sin(a)*r*2.1)
    c.setFillColor(INK); c.circle(x, y, r, fill=1, stroke=0)

def i_moon(x, y, s):
    r = s*0.34
    c.saveState()
    p = c.beginPath(); p.circle(x, y, r); c.clipPath(p, stroke=0, fill=0)
    c.setFillColor(INK); c.circle(x, y, r, fill=1, stroke=0)
    c.setFillColor(white); c.circle(x+r*0.55, y+r*0.35, r, fill=1, stroke=0)
    c.restoreState(); c.setFillColor(INK)

def i_star(x, y, s):
    r = s*0.36; pts=[]
    for k in range(5):
        a = math.pi/2 + k*2*math.pi/5
        pts.append((x+math.cos(a)*r, y+math.sin(a)*r))
        a2 = a + math.pi/5
        pts.append((x+math.cos(a2)*r*0.45, y+math.sin(a2)*r*0.45))
    p = c.beginPath(); p.moveTo(*pts[0])
    for pt in pts[1:]: p.lineTo(*pt)
    p.close(); c.setFillColor(INK); c.drawPath(p, fill=1, stroke=0)

def i_cloud(x, y, s):
    c.setFillColor(INK)
    c.circle(x-s*0.22, y, s*0.20, fill=1, stroke=0)
    c.circle(x+s*0.06, y+s*0.05, s*0.26, fill=1, stroke=0)
    c.circle(x+s*0.30, y, s*0.18, fill=1, stroke=0)
    c.roundRect(x-s*0.40, y-s*0.20, s*0.80, s*0.22, 4, fill=1, stroke=0)

def i_tree(x, y, s):
    c.setFillColor(HexColor("#5a3b1a"))
    c.rect(x-s*0.06, y-s*0.40, s*0.12, s*0.34, fill=1, stroke=0)
    c.setFillColor(INK)
    c.circle(x, y+s*0.10, s*0.30, fill=1, stroke=0)
    c.circle(x-s*0.22, y-s*0.02, s*0.20, fill=1, stroke=0)
    c.circle(x+s*0.22, y-s*0.02, s*0.20, fill=1, stroke=0)
    c.setFillColor(INK)

def i_bush(x, y, s):
    c.setFillColor(INK)
    c.circle(x-s*0.20, y-s*0.05, s*0.18, fill=1, stroke=0)
    c.circle(x+s*0.20, y-s*0.05, s*0.18, fill=1, stroke=0)
    c.circle(x, y+s*0.08, s*0.24, fill=1, stroke=0)
    c.roundRect(x-s*0.40, y-s*0.22, s*0.80, s*0.20, 4, fill=1, stroke=0)

def i_bird(x, y, s):
    c.setStrokeColor(INK); c.setLineWidth(2.4)
    c.setFillColor(INK)
    c.ellipse(x-s*0.20, y-s*0.14, x+s*0.18, y+s*0.14, fill=1, stroke=0)  # body
    c.circle(x+s*0.20, y+s*0.10, s*0.10, fill=1, stroke=0)               # head
    p = c.beginPath(); p.moveTo(x+s*0.28, y+s*0.10)
    p.lineTo(x+s*0.40, y+s*0.14); p.lineTo(x+s*0.28, y+s*0.05); p.close()
    c.drawPath(p, fill=1, stroke=0)                                       # beak
    # wing
    c.setStrokeColor(white); c.setLineWidth(1.6)
    c.arc(x-s*0.10, y-s*0.06, x+s*0.14, y+s*0.16, startAng=200, extent=120)
    c.setStrokeColor(INK); c.setFillColor(INK)

def i_flower(x, y, s):
    r = s*0.13
    c.setStrokeColor(HexColor("#5a3b1a")); c.setLineWidth(2)
    c.line(x, y-s*0.05, x, y-s*0.40)
    c.setFillColor(INK)
    for k in range(6):
        a = k*math.pi/3
        c.circle(x+math.cos(a)*r*1.2, y+math.sin(a)*r*1.2, r, fill=1, stroke=0)
    c.setFillColor(white); c.circle(x, y, r*0.9, fill=1, stroke=0)
    c.setFillColor(INK); c.circle(x, y, r*0.5, fill=1, stroke=0)

def i_butterfly(x, y, s):
    c.setFillColor(INK)
    c.ellipse(x-s*0.05, y-s*0.22, x+s*0.05, y+s*0.22, fill=1, stroke=0)  # body
    for sx in (-1, 1):
        c.circle(x+sx*s*0.18, y+s*0.12, s*0.15, fill=1, stroke=0)
        c.circle(x+sx*s*0.18, y-s*0.12, s*0.12, fill=1, stroke=0)
    c.setStrokeColor(INK); c.setLineWidth(1.8)
    c.line(x, y+s*0.20, x-s*0.10, y+s*0.34)
    c.line(x, y+s*0.20, x+s*0.10, y+s*0.34)

def i_rock(x, y, s):
    c.setFillColor(GREY)
    c.roundRect(x-s*0.34, y-s*0.18, s*0.68, s*0.34, 10, fill=1, stroke=0)
    c.setFillColor(INK)
    c.roundRect(x-s*0.10, y-s*0.18, s*0.30, s*0.30, 8, fill=1, stroke=0)
    c.setFillColor(INK)

def i_river(x, y, s):
    c.setStrokeColor(INK); c.setLineWidth(2.4)
    for off in (-s*0.10, s*0.08):
        p = c.beginPath(); p.moveTo(x-s*0.36, y+off)
        p.curveTo(x-s*0.12, y+off+s*0.12, x+s*0.12, y+off-s*0.12, x+s*0.36, y+off)
        c.drawPath(p, fill=0, stroke=1)

ICON = dict(sun=i_sun, moon=i_moon, star=i_star, cloud=i_cloud, tree=i_tree,
            bush=i_bush, bird=i_bird, flower=i_flower, butterfly=i_butterfly,
            rock=i_rock, river=i_river)

def icon_group(name, x, y, s, count=1):
    if count == 1:
        ICON[name](x, y, s); return
    step = s*0.62
    start = x - step*(count-1)/2
    for k in range(count):
        ICON[name](start + k*step, y, s*0.82)

# ================= PAGE 1 =================
y = header(1, 3)

# Part A - Circle is / are
y = section(y, "A", "Circle: is / are",
            "Look at the picture. Circle is or are.  (one = is, more = are)")
itemsA = [  # (icon, count, "left text", "right text", answer)
    ("sun",   1, "The sun",        "in the sky.",  "is"),
    ("bird",  3, "Three birds",    "in the tree.", "are"),
    ("flower",1, "The flower",     "on the rock.", "is"),
    ("star",  2, "Two stars",      "in the sky.",  "are"),
    ("cloud", 2, "The clouds",     "in the sky.",  "are"),
    ("moon",  1, "The moon",       "in the sky.",  "is"),
]
rowA = 50; topA = y - 14
for i,(ic,ct,lt,rt,ans) in enumerate(itemsA):
    cy = topA - i*rowA
    num(48, cy, i+1)
    icon_group(ic, 96, cy, 34, ct)
    c.setFillColor(INK); c.setFont("PopM", 13)
    c.drawString(140, cy-5, lt)
    lx = 140 + pdfmetrics.stringWidth(lt+" ", "PopM", 13)
    c.setFont("PopB", 13)
    c.drawString(lx, cy-5, "( is  /  are )")
    cx = lx + pdfmetrics.stringWidth("( is  /  are ) ", "PopB", 13)
    c.setFont("PopM", 13)
    c.drawString(cx, cy-5, rt)
y = topA - (len(itemsA)-1)*rowA - 34
dotted_h(36, W-36, y)

# Part B - Write is / are
y = section(y-22, "B", "Write: is / are", "Write the correct word on the line.")
c.setFont("PopB", 11.5); c.setFillColor(INK)
c.drawString(392, y+44, "word bank")
c.setFont("PopM", 13); c.drawString(392, y+26, "is        are")
c.setLineWidth(1.4); c.setStrokeColor(INK); c.setDash(1.5,3.5)
c.roundRect(378, y+16, 150, 46, 8, fill=0, stroke=1); c.setDash()
itemsB = [
    ("bird",   1, "The bird", "on the bush."),
    ("flower", 2, "Two flowers", "on the tree."),
    ("sun",    1, "The sun", "in the sky."),
    ("rock",   2, "The rocks", "in the river."),
]
rowB = 52; topB = y - 16
for i,(ic,ct,lt,rt) in enumerate(itemsB):
    cy = topB - i*rowB
    num(48, cy, i+1)
    icon_group(ic, 96, cy, 32, ct)
    c.setFillColor(INK); c.setFont("PopM", 13)
    c.drawString(140, cy-5, lt)
    bx0 = 140 + pdfmetrics.stringWidth(lt+" ", "PopM", 13)
    wline(bx0, bx0+66, cy-8)
    c.drawString(bx0+74, cy-5, rt)
value_footer(); c.showPage()

# ================= PAGE 2 =================
y = header(2, 3)

# Part C - Where is/are
y = section(y, "C", "Where is / are ...?",
            "Answer the question. Use in or on.")
c.setFont("PopB", 11.5); c.setFillColor(INK)
c.drawString(392, y+44, "word bank")
c.setFont("PopM", 13); c.drawString(392, y+26, "in        on")
c.setLineWidth(1.4); c.setStrokeColor(INK); c.setDash(1.5,3.5)
c.roundRect(378, y+16, 150, 46, 8, fill=0, stroke=1); c.setDash()
itemsC = [
    ("bird",      "Where is the bird?",     "It is"),
    ("flower",    "Where is the flower?",   "It is"),
    ("star",      "Where are the stars?",   "They are"),
    ("butterfly", "Where is the butterfly?","It is"),
]
rowC = 84; topC = y - 18
for i,(ic,q,frame) in enumerate(itemsC):
    cy = topC - i*rowC
    num(48, cy, i+1)
    ICON[ic](96, cy, 38)
    c.setFillColor(INK); c.setFont("PopM", 14)
    c.drawString(140, cy+8, q)
    c.setFont("PopM", 13)
    c.drawString(140, cy-18, frame)
    fx = 140 + pdfmetrics.stringWidth(frame+" ", "PopM", 13)
    wline(fx, 545, cy-21)
y = topC - (len(itemsC)-1)*rowC - 44
dotted_h(36, W-36, y)

# Part D - Circle in / on
y = section(y-22, "D", "Circle: in / on", "Look at the picture. Circle in or on.")
itemsD = [
    ("cloud",     "The cloud is", "the sky.",  "in"),
    ("flower",    "The flower is","the rock.", "on"),
    ("bird",      "The bird is",  "the tree.", "in"),
    ("butterfly", "The butterfly is","the bush.","on"),
]
rowD = 50; topD = y - 14
for i,(ic,lt,rt,ans) in enumerate(itemsD):
    cy = topD - i*rowD
    num(48, cy, i+1)
    ICON[ic](96, cy, 32)
    c.setFillColor(INK); c.setFont("PopM", 13)
    c.drawString(140, cy-5, lt)
    lx = 140 + pdfmetrics.stringWidth(lt+" ", "PopM", 13)
    c.setFont("PopB", 13); c.drawString(lx, cy-5, "( in  /  on )")
    cx = lx + pdfmetrics.stringWidth("( in  /  on ) ", "PopB", 13)
    c.setFont("PopM", 13); c.drawString(cx, cy-5, rt)
value_footer(); c.showPage()

# ================= PAGE 3 : ANSWER KEY =================
y = header(3, 3, title="Answer Key")
rows = [
    ("A", "Circle: is / are", "1. is    2. are    3. is    4. are    5. are    6. is"),
    ("B", "Write: is / are",  "1. is    2. are    3. is    4. are"),
    ("C", "Where is / are ...?",
        "1. It is on the tree.   2. It is in the bush.   3. They are in the sky.   4. It is on the flower."),
    ("D", "Circle: in / on",  "1. in    2. on    3. in    4. on"),
]
for letter, label, ans in rows:
    y = section(y, letter, label, "")
    c.setFillColor(INK); c.setFont("PopM", 12.5)
    c.drawString(78, y+8, ans)
    y -= 40
    dotted_h(36, W-36, y+20); y -= 6

c.setFont("PopB", 12.5); c.setFillColor(INK)
c.drawString(78, y-6, "Teacher notes")
c.setFont("Pop", 11)
c.drawString(78, y-26, "Patterns: WS-002 / WS-003 / WS-006")
c.drawString(78, y-44, "Scope: EOW1 Unit 2 only — to be (is/are); Where + in/on. Prepositions limited to in/on.")
c.drawString(78, y-62, "Vocabulary strategy: ending -s (plural drives is/are).")
c.drawString(78, y-80, "Value: Enjoy nature.")
c.save()
print("done ->", OUT)
