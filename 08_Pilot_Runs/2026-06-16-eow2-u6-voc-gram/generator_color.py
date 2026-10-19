#!/usr/bin/env python3
"""EOW2 U6 Day by Day — colourful worksheet.
P1 two matches: daily routines (9) + times of day (4, framed);
P2 grammar: telling the time (5 clocks) + how often (4 choose);
P3 answer key.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import eow2lib as L
from eow2lib import (W,H,NAVY,PINK,BLUE,GREEN,ORANGE,PURPLE,GREY,RED,white)
from reportlab.pdfbase import pdfmetrics

HERE=os.path.dirname(os.path.abspath(__file__))
C=L.setup(HERE,"EOW2 U6 Day by Day (colorful).pdf")
BADGE="EOW2 · Unit 6"

# ---------------- Page 1: two matches (routines + times of day) ----------------
y=L.header(BADGE,[("Day by ",NAVY),("Day",ORANGE)])
aTop=y; aH=442; aBot=aTop-aH
yc=L.card(40,aTop,W-80,aH,PINK,"A","Daily routines — match","Draw a line from each picture to the words.")
L.R_match(yc,aBot+10,[("get-up","get up"),("brush-my-teeth","brush my teeth"),
                      ("get-dressed","get dressed"),("eat-breakfast","eat breakfast"),
                      ("eat-lunch","eat lunch"),("eat-dinner","eat dinner"),
                      ("go-to-school","go to school"),("play-with-friends","play with friends"),
                      ("go-to-bed","go to bed")],PINK,picsize=40)
bTop=aBot-16; bBot=40; bH=bTop-bBot
yc=L.card(40,bTop,W-80,bH,BLUE,"B","Times of day — match","Draw a line from each picture to the words.")
L.R_match(yc,bBot,[("in-the-morning","in the morning"),("in-the-afternoon","in the afternoon"),
                   ("in-the-evening","in the evening"),("at-night","at night")],BLUE,frame=True,picsize=38)
C.showPage()

# ---------------- Page 2: grammar (telling time + how often) ----------------
y=L.header(BADGE,[("Time ",NAVY),("and how often",GREEN)])
aTop=y; aH=352; aBot=aTop-aH
yc=L.card(40,aTop,W-80,aH,GREEN,"1","What time is it?","Look at the clock. Write the time. Number 1 is done for you.")
clocks=[(7,"7:00"),(12,"12:00"),(3,"3:00"),(6,"6:00"),(9,"9:00")]
top=yc-2; bot=aBot+12; pitch=(top-bot)/len(clocks)
for i,(hr,ans) in enumerate(clocks):
    cy=top-pitch*(i+0.5)
    C.setFillColor(GREEN); C.circle(64,cy,11,fill=1,stroke=0)
    C.setFillColor(white); C.setFont("PopB",12); C.drawCentredString(64,cy-4,str(i+1))
    L.clock(132,cy,25,hr)
    tx=196; C.setFillColor(NAVY); C.setFont("PopSB",15); C.drawString(tx,cy-5,"It's")
    sx=tx+pdfmetrics.stringWidth("It's  ","PopSB",15)
    L.wline(sx,sx+150,cy-9)
    C.setFillColor(NAVY); C.setFont("PopSB",15); C.drawString(sx+158,cy-5,".")
    if i==0:
        C.setFillColor(GREEN); C.setFont("PopSB",15); C.drawCentredString(sx+75,cy-5,ans)
        C.setFillColor(GREY); C.setFont("PopM",8.5); C.drawString(sx,cy-20,"(example)")
C.setFillColor(L.INK)
bTop=aBot-16; bBot=40; bH=bTop-bBot
yc=L.card(40,bTop,W-80,bH,PURPLE,"2","How often?","always / every day / never.  Circle a or b.")
L.R_mc(yc,bBot+6,[
  ("I ___ get up in the morning.",[("a","always"),("b","never")],"a","get-up"),
  ("I ___ eat dinner in the morning.",[("a","always"),("b","never")],"b","eat-dinner"),
  ("I go to school ______ .",[("a","every day"),("b","at night")],"a","go-to-school"),
  ("I ___ go to bed at night.",[("a","always"),("b","never")],"a","go-to-bed"),
],PURPLE)
C.showPage()

# ---------------- Page 3: Answer Key ----------------
L.answer_key(BADGE,[
  (PINK,"A","Daily routines — match",["get up, brush my teeth, get dressed, eat breakfast, eat lunch,",
                                      "eat dinner, go to school, play with friends, go to bed"]),
  (BLUE,"B","Times of day — match",["in the morning, in the afternoon, in the evening, at night"]),
  (GREEN,"1","What time is it?",["1. It's 7:00.  2. It's 12:00.  3. It's 3:00.  4. It's 6:00.  5. It's 9:00."]),
  (PURPLE,"2","How often?",["1. a (always)  2. b (never)  3. a (every day)  4. a (always)"]),
],"Scope: EOW2 Unit 6 only.  Art: 09_Image_Library.  Value: Be on time.")
L.save()
