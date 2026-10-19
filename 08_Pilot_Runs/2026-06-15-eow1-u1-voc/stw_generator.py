#!/usr/bin/env python3
"""EOW1 U1 vocabulary worksheet, Super Teacher Worksheets style:
clean, color, one page per vocab group, Look-Trace-Write + word bank.
No matching. Uses real art from 09_Image_Library."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

GF="/usr/share/fonts/truetype/google-fonts"
pdfmetrics.registerFont(TTFont("Pop",f"{GF}/Poppins-Regular.ttf"))
pdfmetrics.registerFont(TTFont("PopB",f"{GF}/Poppins-Bold.ttf"))
pdfmetrics.registerFont(TTFont("PopM",f"{GF}/Poppins-Medium.ttf"))

W,H=A4
INK=HexColor("#222222"); GREY=HexColor("#9aa0a6"); SOFT=HexColor("#e7eef7")
BLUE=HexColor("#2f6fb0"); LINE=HexColor("#b9c2cc")
HERE=os.path.dirname(os.path.abspath(__file__))
LIB="/sessions/epic-confident-ride/mnt/PAS Curriculum Wiki/09_Image_Library/words"

c=canvas.Canvas(os.path.join(HERE,"EOW1 U1 Vocabulary (STW-style, color).pdf"),pagesize=A4)

def page(num, words, title):
    c.setFillColor(white); c.rect(0,0,W,H,fill=1,stroke=0)
    # name/date row
    c.setFillColor(INK); c.setFont("Pop",11)
    c.drawString(40,H-50,"Name: ______________________")
    c.drawRightString(W-40,H-50,"Date: ____________")
    # title bar
    c.setFillColor(BLUE); c.setFont("PopB",24)
    c.drawCentredString(W/2,H-92,title)
    c.setFillColor(GREY); c.setFont("PopM",11.5)
    c.drawCentredString(W/2,H-110,"Look at the picture.  Trace the word.  Then write it.")
    # word bank
    bx0,bx1,by=40,W-40,H-160
    c.setStrokeColor(BLUE); c.setLineWidth(1.6); c.setDash(2,3)
    c.roundRect(bx0,by-34,bx1-bx0,46,10,fill=0,stroke=1); c.setDash()
    c.setFillColor(BLUE); c.setFont("PopB",11); c.drawString(bx0+12,by-2,"WORD BANK")
    c.setFillColor(INK); c.setFont("PopM",12.5)
    c.drawCentredString(W/2,by-22,"   ".join(words))
    # cards
    cols=2; gap=20; cw=(W-80-gap)/2; ch=118
    top=by-58
    for i,wd in enumerate(words):
        col=i%cols; r=i//cols
        x=40+col*(cw+gap); y=top-r*(ch+14)
        c.setStrokeColor(SOFT); c.setLineWidth(1.4); c.setDash()
        c.roundRect(x,y-ch,cw,ch,12,fill=0,stroke=1)
        # picture
        c.drawImage(f"{LIB}/{wd}/{wd}-v1-color.png",x+12,y-ch+18,84,84,
                    preserveAspectRatio=True,mask='auto')
        # trace word (light grey, to write over) — auto-fit width
        tx=x+112; avail=(x+cw-16)-tx
        fs=30
        while fs>14 and pdfmetrics.stringWidth(wd,"PopB",fs)>avail: fs-=1
        c.setFillColor(HexColor("#cfd6de")); c.setFont("PopB",fs)
        c.drawString(tx,y-46,wd)
        # write line
        c.setStrokeColor(LINE); c.setLineWidth(1.3); c.setDash(3,3)
        c.line(tx,y-ch+30,x+cw-16,y-ch+30); c.setDash()
        c.setFillColor(GREY); c.setFont("Pop",9); c.drawString(tx,y-ch+16,"write it")
        c.setFillColor(INK)
    # footer
    c.setFillColor(GREY); c.setFont("PopM",10)
    c.drawString(40,30,"EOW1 · Unit 1 · My Classroom")
    c.drawRightString(W-40,30,"Value: Work hard in school.")
    c.setFillColor(INK)
    c.showPage()

page(1,["clock","computer","crayon","map","paper","pen","pencil"],"My Classroom — Words 1")
page(2,["book","chair","desk","eraser","picture"],"My Classroom — Words 2")
c.save(); print("saved")
