#!/usr/bin/env python3
"""EOW2 U7 How Are You? — colourful worksheet.
Variety mix: P1 phonics-build (feelings) + match (face actions);
P2 'He/She looks ___' choose; P3 plurals (write the plural); P4 key.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import eow2lib as L
from eow2lib import (W,H,NAVY,PINK,BLUE,GREEN,ORANGE,PURPLE,GREY,RED,white)
from reportlab.pdfbase import pdfmetrics

HERE=os.path.dirname(os.path.abspath(__file__))
C=L.setup(HERE,"EOW2 U7 How Are You (colorful).pdf")
BADGE="EOW2 · Unit 7"
L.CHUNKS={
 "angry":["an","gry"], "bored":["b","or","ed"], "hungry":["hun","gry"],
 "scared":["sc","are","d"], "surprised":["sur","pri","sed"], "thirsty":["th","ir","sty"],
 "tired":["t","ire","d"],
}

# ---------------- Page 1: Vocabulary ----------------
y=L.header(BADGE,[("How Are ",NAVY),("You?",ORANGE)])
aTop=y; aH=400; aBot=aTop-aH
yc=L.card(40,aTop,W-80,aH,PINK,"A","Build the word from sound chunks","Put the sound chunks in order. Write the word.")
L.R_phonics(yc,aBot+8,["angry","bored","hungry","scared","surprised","thirsty","tired"],PINK)
bTop=aBot-14; bBot=38; bH=bTop-bBot
yc=L.card(40,bTop,W-80,bH,BLUE,"B","Faces — match","Match each picture to the word.")
L.R_match(yc,bBot,[("smiling","smiling"),("laughing","laughing"),("crying","crying"),
                   ("frowning","frowning"),("yawning","yawning")],BLUE)
C.showPage()

# ---------------- Page 2: Grammar (looks + plurals on one page) ----------------
y=L.header(BADGE,[("Looks ",NAVY),("and plurals",GREEN)])
# Card 1: How does he look? (choose)
aTop=y; aH=356; aBot=aTop-aH
yc=L.card(40,aTop,W-80,aH,GREEN,"1","How does he look?","Look at the face. Circle a or b.")
L.R_mc(yc,aBot+12,[
  ("He looks ___.",[("a","angry"),("b","happy")],"a","angry"),
  ("She looks ___.",[("a","tired"),("b","hungry")],"a","tired"),
  ("He looks ___.",[("a","scared"),("b","bored")],"a","scared"),
  ("She looks ___.",[("a","thirsty"),("b","surprised")],"b","surprised"),
],GREEN)
# Card 2: Write the plural
bTop=aBot-16; bBot=40; bH=bTop-bBot
yc=L.card(40,bTop,W-80,bH,PURPLE,"2","Write the plural","one child -> two children.  Number 1 is done for you.")
plur=[("one book  ->  two","books"),("one parent  ->  two","parents"),
      ("one child  ->  two","children"),("one person  ->  three","people"),
      ("one foot  ->  two","feet")]
top=yc-4; bot=bBot+6; pitch=(top-bot)/len(plur)
for i,(stem,ans) in enumerate(plur):
    cy=top-pitch*(i+0.5)
    C.setFillColor(PURPLE); C.circle(66,cy,11,fill=1,stroke=0)
    C.setFillColor(white); C.setFont("PopB",12); C.drawCentredString(66,cy-4,str(i+1))
    C.setFillColor(NAVY); C.setFont("PopSB",15); C.drawString(96,cy-5,stem)
    sx=96+pdfmetrics.stringWidth(stem+"  ","PopSB",15)
    L.wline(sx,sx+170,cy-9)
    if i==0:
        C.setFillColor(PURPLE); C.setFont("PopSB",15); C.drawString(sx+8,cy-5,ans)
        C.setFillColor(GREY); C.setFont("PopM",8.5); C.drawString(sx+8,cy-20,"(example)")
C.setFillColor(L.INK)
C.showPage()

# ---------------- Page 4: Answer Key ----------------
L.answer_key(BADGE,[
  (PINK,"A","Build the word",["1. angry  2. bored  3. hungry  4. scared  5. surprised  6. thirsty  7. tired"]),
  (BLUE,"B","Faces — match",["smiling, laughing, crying, frowning, yawning"]),
  (GREEN,"1","How does he look?",["1. a (angry)  2. a (tired)  3. a (scared)  4. b (surprised)"]),
  (PURPLE,"1","Write the plural",["1. books  2. parents  3. children  4. people  5. feet"]),
],"Scope: EOW2 Unit 7 only.  Art: 09_Image_Library.  Value: Be kind.")
L.save()
