#!/usr/bin/env python3
"""EOW2 U5 Inside Our House — colourful worksheet.
Variety mix: P1 phonics-build (furniture) + word hunt (house words);
P2 prepositions cloze with composed cat+table vignettes; P3 Where is/are...? (It's/They're);
P4 key.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import eow2lib as L
from eow2lib import (W,H,NAVY,PINK,BLUE,GREEN,ORANGE,PURPLE,GREY,RED,LBLUE,white,HexColor)
from reportlab.pdfbase import pdfmetrics

HERE=os.path.dirname(os.path.abspath(__file__))
C=L.setup(HERE,"EOW2 U5 Inside Our House (colorful).pdf")
BADGE="EOW2 · Unit 5"
L.CHUNKS={
 "bookcase":["book","case"], "rug":["r","u","g"], "shower":["sh","ow","er"],
 "stairs":["st","air","s"], "stove":["st","o","ve"], "table":["t","a","ble"], "tub":["t","u","b"],
}

# ---------------- Page 1: Vocabulary ----------------
y=L.header(BADGE,[("Inside Our ",NAVY),("House",ORANGE)])
aTop=y; aH=400; aBot=aTop-aH
yc=L.card(40,aTop,W-80,aH,PINK,"A","Build the word from sound chunks","Put the sound chunks in order. Write the word.")
L.R_phonics(yc,aBot+8,["bookcase","rug","shower","stairs","stove","table","tub"],PINK)
bTop=aBot-14; bBot=38; bH=bTop-bBot
yc=L.card(40,bTop,W-80,bH,BLUE,"B","Find and circle the word","Each line hides one word. Circle the word you see.")
L.R_wordhunt(yc,bBot,[("door","z d o o r p"),("phone","k p h o n e t"),
                      ("refrigerator","x r e f r i g e r a t o r"),
                      ("sink","u s i n k e"),("window","m w i n d o w s")],BLUE)
C.showPage()

# ---------------- Page 2: Grammar 1 (prepositions) ----------------
y=L.header(BADGE,[("Where is the ",NAVY),("cat?",GREEN)])
y=L.rule_box(y,[("Where is the cat?  ",NAVY),("It's on the table.",GREEN)],
             sub="Word bank:  on   under   next to   behind   in front of   between")
yc=L.card(40,y,W-80,y-40,GREEN,"1","Look and write","Write the place. Number 1 is done for you.")
preps=[("on","on","the table."),("under","under","the table."),("nextto","next to","the table."),
       ("behind","behind","the table."),("front","in front of","the table."),("between","between","the tables.")]
SC=os.path.join(HERE,"scenes")
top=yc-4; bot=44; pitch=(top-bot)/len(preps)
for i,(fn,ans,tail) in enumerate(preps):
    cy=top-pitch*(i+0.5)
    C.setFillColor(GREEN); C.circle(64,cy,11,fill=1,stroke=0)
    C.setFillColor(white); C.setFont("PopB",12); C.drawCentredString(64,cy-4,str(i+1))
    p=os.path.join(SC,fn+".png")
    if os.path.exists(p): C.drawImage(p,92,cy-36,118,72,preserveAspectRatio=True,mask='auto')
    tx=224; C.setFillColor(NAVY); C.setFont("PopSB",13.5); C.drawString(tx,cy-5,"The cat is")
    sx=tx+pdfmetrics.stringWidth("The cat is  ","PopSB",13.5)
    L.wline(sx,sx+108,cy-9)
    ax=sx+108+8; C.setFillColor(NAVY); C.setFont("PopSB",13.5); C.drawString(ax,cy-5,tail)
    if i==0:
        C.setFillColor(GREEN); C.setFont("PopSB",13.5); C.drawCentredString(sx+54,cy-5,ans)
        C.setFillColor(GREY); C.setFont("PopM",8.5); C.drawString(sx,cy-20,"(example)")
C.setFillColor(L.INK)
C.showPage()

# ---------------- Page 3: Grammar 2 (it / they) ----------------
y=L.header(BADGE,[("Where is ",NAVY),("it?",PURPLE)])
y=L.rule_box(y,[("Where is...? It's ...    ",GREEN),("Where are...? They're ...",PURPLE)],
             sub="Look at the room. One thing -> It's ...   Many things -> They're ...")
yc=L.card(40,y,W-80,y-46,PURPLE,"1","Look and answer","Look at the room. Write It's or They're and the place.")
rooms=[("room_phone","Where is the phone?","It's in the living room."),
       ("room_stove","Where is the stove?",None),
       ("room_bookcase","Where are the books?",None),
       ("room_tub","Where is the tub?",None),
       ("room_rug","Where is the rug?",None)]
SC=os.path.join(HERE,"scenes")
IW,IH=164,104; qx=262
top=yc-2; bot=40; pitch=(top-bot)/len(rooms)
for i,(fn,q,ans) in enumerate(rooms):
    blk=top-pitch*i
    ly=blk-pitch+30            # writing line near the block bottom
    iy=ly                      # image bottom-aligned to the writing line
    p=os.path.join(SC,fn+".png")
    if os.path.exists(p):
        C.drawImage(p,82,iy,IW,IH,preserveAspectRatio=True,mask='auto')
        C.setStrokeColor(HexColor("#d8e0ea")); C.setLineWidth(1.2); C.roundRect(82,iy,IW,IH,8,fill=0,stroke=1)
    qy=ly+IH-30                # question near the top of the image -> roomy gap down to the line
    C.setFillColor(PURPLE); C.circle(60,qy,11,fill=1,stroke=0)
    C.setFillColor(white); C.setFont("PopB",12); C.drawCentredString(60,qy-4,str(i+1))
    C.setFillColor(NAVY); C.setFont("PopSB",13.5); C.drawString(qx,qy-5,q)
    L.wline(qx,W-70,ly)
    if i==0 and ans:
        C.setFillColor(GREEN); C.setFont("PopSB",13.5); C.drawString(qx+6,ly+5,ans)
        C.setFillColor(GREY); C.setFont("PopM",9); C.drawString(W-150,ly+5,"(example)")
C.setFillColor(L.INK)
C.showPage()

# ---------------- Page 4: Answer Key ----------------
L.answer_key(BADGE,[
  (PINK,"A","Build the word",["1. bookcase  2. rug  3. shower  4. stairs  5. stove  6. table  7. tub"]),
  (BLUE,"B","Find and circle",["1. door  2. phone  3. refrigerator  4. sink  5. window"]),
  (GREEN,"1","Where is the cat?",["1. It's on the table.  2. under  3. next to  4. behind  5. in front of  6. between"]),
  (PURPLE,"1","Where is it?",["1. It's in the living room.  2. It's in the kitchen.  3. They're in the bedroom.",
                              "4. It's in the bathroom.  5. It's in the living room."]),
],"Scope: EOW2 Unit 5 only.  Art: 09_Image_Library.  Value: Help at home.")
L.save()
