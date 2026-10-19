#!/usr/bin/env python3
"""EOW1 U2 sample page using REAL hand-drawn art from 09_Image_Library.
Outputs two PDFs: sample-with-art-color.pdf and sample-with-art-bw.pdf.
Proves the image library flows into the PAS worksheet layout.
"""
import os
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
INK = HexColor("#111111")
GREY = HexColor("#333333")
LIB = "/sessions/epic-confident-ride/mnt/PAS Curriculum Wiki/09_Image_Library/words"
HERE = os.path.dirname(os.path.abspath(__file__))

def build(mode):
    out = os.path.join(HERE, f"sample-with-art-{mode}.pdf")
    c = canvas.Canvas(out, pagesize=A4)
    def img(word, x, y, s):
        c.drawImage(f"{LIB}/{word}/{word}-v1-{mode}.png", x-s/2, y-s/2, s, s,
                    preserveAspectRatio=True, mask='auto')
    def badge(x, y, r, txt, fs):
        c.setFillColor(INK); c.circle(x, y, r, fill=1, stroke=0)
        c.setFillColor(white); c.setFont("PopB", fs)
        c.drawCentredString(x, y - fs*0.36, txt); c.setFillColor(INK)
    def dotted(x0, x1, y):
        c.setStrokeColor(INK); c.setLineWidth(1.4); c.setDash(1.5, 3.5)
        c.line(x0, y, x1, y); c.setDash()

    c.setFillColor(white); c.rect(0,0,W,H,fill=1,stroke=0)
    # header
    c.setFillColor(INK); c.setFont("PopB", 13)
    c.drawString(36, H-52, "NAME:"); c.setLineWidth(1.6); c.setStrokeColor(INK)
    c.line(92, H-54, 320, H-54); c.drawString(380, H-52, "DATE:"); c.line(432, H-54, 560, H-54)
    title="My World"
    tw=pdfmetrics.stringWidth(title,"PopB",30); bx=max(110,W/2-(tw+52)/2)
    badge(bx+18,H-100,18,"2",22); c.setFillColor(INK); c.setFont("PopB",30)
    c.drawString(bx+50,H-100-30*0.36,title)
    c.setFont("PopM",10); c.drawRightString(W-30,H-78,"EOW1 · Unit 2 · My World")
    c.drawRightString(W-30,H-92,f"sample · {mode}")

    # Section A
    y=H-150
    badge(52,y,14,"A",16); c.setFillColor(INK); c.setFont("PopB",19)
    c.drawString(78,y-7,"Circle: is / are")
    c.setFillColor(GREY); c.setFont("Pop",11.5)
    c.drawString(78,y-26,"Look at the picture. Circle is or are.")
    c.setFillColor(INK)
    items=[("sun","The sun","in the sky."),
           ("bird","The bird","in the tree."),
           ("tree","The trees","green and tall.")]
    top=y-70; row=92
    for i,(w,lt,rt) in enumerate(items):
        cy=top-i*row
        badge(48,cy,11,str(i+1),13)
        img(w,110,cy,64)
        c.setFillColor(INK); c.setFont("PopM",14); c.drawString(160,cy-5,lt)
        lx=160+pdfmetrics.stringWidth(lt+" ","PopM",14)
        c.setFont("PopB",14); c.drawString(lx,cy-5,"( is  /  are )")
        cx=lx+pdfmetrics.stringWidth("( is  /  are ) ","PopB",14)
        c.setFont("PopM",14); c.drawString(cx,cy-5,rt)
    y=top-2*row-60; dotted(36,W-36,y)

    # Section B
    badge(52,y-26,14,"B",16); c.setFillColor(INK); c.setFont("PopB",19)
    c.drawString(78,y-33,"Where is it?")
    c.setFillColor(GREY); c.setFont("Pop",11.5); c.drawString(78,y-52,"Answer. Use in or on.")
    c.setFillColor(INK)
    cy=y-120; badge(48,cy,11,"1",13); img("bird",110,cy,64)
    c.setFont("PopM",14); c.drawString(160,cy+8,"Where is the bird?")
    c.setFont("PopM",13); c.drawString(160,cy-18,"It is")
    c.setStrokeColor(INK); c.setLineWidth(1.2); c.setDash(2.5,2.5)
    c.line(196,cy-21,545,cy-21); c.setDash()

    c.setFont("PopM",10.5); c.setFillColor(GREY)
    c.drawCentredString(W/2,40,"Value: Enjoy nature.   —   art from 09_Image_Library (hand-drawn set)")
    c.save(); print("saved", out)

build("color")
build("bw")
