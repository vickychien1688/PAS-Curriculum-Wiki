#!/usr/bin/env python3
"""EOW1 Reading Base U1 Story 1 'What is it?' — reading companion worksheet."""
import math, os
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
INK = HexColor("#111111"); GREY = HexColor("#333333")
COL = {"red":"#D63B3B","blue":"#2E6DA8","yellow":"#F5C842","green":"#3E8E4E",
       "purple":"#7D4FA8","orange":"#E8862E","white":"#FFFFFF","black":"#1A1A1A"}

OUTDIR = "/sessions/epic-elegant-einstein/mnt/GitHub/PAS Curriculum Wiki/08_Pilot_Runs/2026-06-12-eow1-rb1-story1"
os.makedirs(OUTDIR, exist_ok=True)
c = canvas.Canvas(f"{OUTDIR}/EOW1 RB U1 Story1 What is it.pdf", pagesize=A4)

def shape(kind, color, x, y, s):
    c.setStrokeColor(INK); c.setLineWidth(s*0.045)
    c.setFillColor(HexColor(COL[color]))
    h = s/2
    if kind == "circle": c.circle(x, y, h*0.9, fill=1, stroke=1)
    elif kind == "square": c.rect(x-h*0.8, y-h*0.8, s*0.8, s*0.8, fill=1, stroke=1)
    elif kind == "rectangle": c.rect(x-h, y-h*0.6, s, s*0.6, fill=1, stroke=1)
    elif kind == "triangle":
        p=c.beginPath(); p.moveTo(x, y+h*0.9); p.lineTo(x+h*0.95, y-h*0.7); p.lineTo(x-h*0.95, y-h*0.7); p.close()
        c.drawPath(p, stroke=1, fill=1)
    elif kind == "star":
        p=c.beginPath()
        for i in range(10):
            r = h*0.95 if i%2==0 else h*0.42
            a = math.pi/2 + i*math.pi/5
            xx, yy = x+r*math.cos(a), y+r*math.sin(a)
            (p.moveTo if i==0 else p.lineTo)(xx, yy)
        p.close(); c.drawPath(p, stroke=1, fill=1)
    elif kind == "heart":
        p=c.beginPath(); p.moveTo(x, y-h*0.8)
        p.curveTo(x-h*1.3, y+h*0.15, x-h*0.55, y+h*0.95, x, y+h*0.25)
        p.moveTo(x, y-h*0.8)
        p.curveTo(x+h*1.3, y+h*0.15, x+h*0.55, y+h*0.95, x, y+h*0.25)
        c.drawPath(p, stroke=1, fill=1)
    elif kind == "oval": c.ellipse(x-h, y-h*0.6, x+h, y+h*0.6, fill=1, stroke=1)
    elif kind == "diamond":
        p=c.beginPath(); p.moveTo(x, y+h*0.95); p.lineTo(x+h*0.7, y); p.lineTo(x, y-h*0.95); p.lineTo(x-h*0.7, y); p.close()
        c.drawPath(p, stroke=1, fill=1)

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

def header(page, total, title="What is it?"):
    c.setFillColor(white); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(INK); c.setFont("PopB", 13)
    c.drawString(36, H-52, "NAME:"); c.setLineWidth(1.6); c.setStrokeColor(INK)
    c.line(92, H-54, 320, H-54)
    c.drawString(380, H-52, "DATE:"); c.line(432, H-54, 560, H-54)
    fs = 34; max_right = W - 220
    while fs > 20:
        tw = pdfmetrics.stringWidth(title, "PopB", fs)
        bx = W/2 - (tw + 52)/2
        if bx + 52 + tw <= max_right and bx >= 110: break
        fs -= 1
    tw = pdfmetrics.stringWidth(title, "PopB", fs)
    bx = max(110, W/2 - (tw + 52)/2)
    badge(bx + 20, H-100, 20, "1", 24)
    c.setFillColor(INK); c.setFont("PopB", fs)
    c.drawString(bx + 52, H-100 - fs*0.36, title)
    c.setFont("PopM", 10)
    c.drawRightString(W-30, H-76, "EOW1 · Reading Base U1 · Story 1")
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
y = section(y, "A", "Read and match", "Read the sentence. Draw a line to the shape.")
sents = [("red","circle"), ("blue","square"), ("yellow","triangle"),
         ("green","star"), ("purple","heart"), ("white","diamond")]
order  = [("green","star"), ("white","diamond"), ("red","circle"),
          ("purple","heart"), ("blue","square"), ("yellow","triangle")]
row = 64; topA = y - 24
for i,(col,shp) in enumerate(sents):
    cy = topA - i*row
    num(48, cy, i+1)
    art = "an" if col == "orange" else "a"
    c.setFillColor(INK); c.setFont("PopM", 14.5)
    c.drawString(76, cy-5, f"It's {art} {col} {shp}.")
    c.setFillColor(INK); c.circle(300, cy, 3.2, fill=1, stroke=0)
for i,(col,shp) in enumerate(order):
    cy = topA - i*row
    c.setFillColor(INK); c.circle(420, cy, 3.2, fill=1, stroke=0)
    shape(shp, col, 490, cy, 46)
y = topA - 5*row - 48
dotted_h(36, W-36, y)

y = section(y - 24, "B", "True or False", "Read. Look at the shape. Circle T or F.")
items_b = [("blue","square","It's a blue square.", True),
           ("orange","oval","It's an orange circle.", False),
           ("black","rectangle","It's a black rectangle.", True),
           ("yellow","triangle","It's a green triangle.", False)]
cell_w = (W-72)/2; b_top = y - 2; row_b = 78
for i,(col,shp,sent,ans) in enumerate(items_b):
    colx = i % 2; r_ = i // 2
    x0 = 36 + colx*cell_w
    cy = b_top - r_*row_b - 36
    num(x0+12, cy+14, i+1)
    shape(shp, col, x0+66, cy+4, 42)
    c.setFillColor(INK); c.setFont("PopM", 12)
    c.drawString(x0+104, cy+12, sent)
    c.setFont("PopB", 13)
    c.drawString(x0+104, cy-14, "T   /   F")
dotted_v(36+cell_w, b_top-2, b_top-2*row_b+8)
dotted_h(60, W-60, b_top-row_b+4)
c.showPage()

# ================= PAGE 2 =================
y = header(2, 3)
y = section(y, "C", "Circle the correct word", "Look at the shape. Circle the word.")
items_c = [("red","circle","red / blue"), ("green","star","green / purple"),
           ("purple","heart","heart / star"), ("white","diamond","diamond / oval")]
cell_w = (W-72)/2; c_top = y - 2; row_c = 68
for i,(col,shp,opts) in enumerate(items_c):
    colx = i % 2; r_ = i // 2
    x0 = 36 + colx*cell_w
    cy = c_top - r_*row_c - 36
    num(x0+12, cy+14, i+1)
    shape(shp, col, x0+70, cy+2, 44)
    c.setFillColor(INK); c.setFont("PopM", 13.5)
    c.drawString(x0+118, cy-2, opts)
dotted_v(36+cell_w, c_top-2, c_top-2*row_c+8)
dotted_h(60, W-60, c_top-row_c+4)
y = c_top - 2*row_c - 16
dotted_h(36, W-36, y)

y = section(y - 24, "D", "What is it?", "Write two words: the color and the shape.")
items_d = [("yellow","triangle"), ("blue","square"), ("orange","oval")]
for i,(col,shp) in enumerate(items_d):
    ry = y - 32 - i*56
    num(48, ry+6, i+1)
    shape(shp, col, 110, ry+2, 46)
    art = "an" if col == "orange" else "a"
    c.setFillColor(INK); c.setFont("PopM", 13.5)
    c.drawString(155, ry-2, f"What is it?   It's {art}")
    wline(330, 420, ry-6); wline(430, 540, ry-6)
    c.drawString(544, ry-2, ".")
y = y - 32 - 2*56 - 44
dotted_h(36, W-36, y)

y = section(y - 24, "E", "Unscramble the words", "Put the letters in order. Write the word.")
items_e = [("star","green","r a t s"), ("heart","purple","r e h a t"),
           ("circle","red","l e c r i c"), ("square","blue","r a u q e s")]
cell_w = (W-72)/2; e_top = y - 2; row_e = 70
for i,(word,col,scr) in enumerate(items_e):
    colx = i % 2; r_ = i // 2
    x0 = 36 + colx*cell_w
    cy = e_top - r_*row_e - 32
    num(x0+12, cy+14, i+1)
    shape(word, col, x0+66, cy+4, 40)
    c.setFillColor(INK); c.setFont("PopB", 14)
    c.drawString(x0+108, cy+10, scr)
    wline(x0+108, x0+225, cy-14)
dotted_v(36+cell_w, e_top-2, e_top-2*row_e+8)
dotted_h(60, W-60, e_top-row_e+4)
c.showPage()

# ================= PAGE 3 : ANSWER KEY =================
y = header(3, 3, title="Answer Key")
rows = [
 ("A. Read and match", "1-circle(3rd)  2-square(5th)  3-triangle(6th)  4-star(1st)  5-heart(4th)  6-diamond(2nd)"),
 ("B. True or False", "1. T   2. F (it's an orange oval)   3. T   4. F (it's a yellow triangle)"),
 ("C. Circle", "1. red   2. green   3. heart   4. diamond"),
 ("D. What is it?", "1. yellow triangle   2. blue square   3. orange oval (It's an...)"),
 ("E. Unscramble", "1. star   2. heart   3. circle   4. square"),
 ("Story source", "Reading Base 1, Book 1 My Classroom, Story 1 pages 1-6."),
 ("Teacher notes", "WS-001/002/004/006/016 · Grammar: What is it? It's a/an... · Value: Work hard in school."),
]
ty = y - 10
for label, ans in rows:
    c.setFillColor(INK); c.setFont("PopB", 11.5); c.drawString(52, ty, label)
    c.setFont("Pop", 10.5); c.drawString(210, ty, ans)
    ty -= 24
c.save()
print("done")
