#!/usr/bin/env python3
"""EOW2 Reading Base 1 Story 1 "Do You Play?" — companion worksheet (2 pages).
Worksheet accompanies the reader; child reads the story in the reader, then answers here.
Title: "EOW2 Reading Base 1 Story 1"  /  "Read the story and answer the question."
P1 Questions: Do you play with the {animal}? circle Yes/No + write the FULL answer (詳答)
P2 Answer Key
Content from Canva reader (03_Reading_Base/eow2-unit-01.md), not invented.
Animals: one GPT grid image sliced into 8 de-backgrounded icons (animals/).
"""
import os, math, random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

GF="/usr/share/fonts/truetype/google-fonts"
pdfmetrics.registerFont(TTFont("Pop",f"{GF}/Poppins-Regular.ttf"))
pdfmetrics.registerFont(TTFont("PopB",f"{GF}/Poppins-Bold.ttf"))
pdfmetrics.registerFont(TTFont("PopM",f"{GF}/Poppins-Medium.ttf"))
pdfmetrics.registerFont(TTFont("PopSB",f"{GF}/Poppins-Bold.ttf"))

W,H=A4
NAVY=HexColor("#3a4a86"); BG=HexColor("#fffdf7"); INK=HexColor("#3a3d45"); GREY=HexColor("#8b909c")
PINK=HexColor("#d76f96"); BLUE=HexColor("#5f97cd"); GREEN=HexColor("#5cae67"); PURPLE=HexColor("#9e85c6")
BLUET=HexColor("#f1f6fb"); PURPLET=HexColor("#f6f2fb")
GOLD=HexColor("#e6c266"); LBLUE=HexColor("#a9c7e8")
HERE=os.path.dirname(os.path.abspath(__file__)); ANI=os.path.join(HERE,"animals")
OUT=os.path.join(HERE,"EOW2 RB U1 Story1 Do You Play.pdf")
ML,MR=42,W-42
c=canvas.Canvas(OUT,pagesize=A4)

STORY=[("rabbit","Yes"),("lion","No"),("goat","Yes"),("bear","No"),
       ("lamb","Yes"),("alligator","No"),("fawn","Yes"),("rhino","No")]

def aimg(name,cx,cy,s):
    p=os.path.join(ANI,name+".png")
    if os.path.exists(p): c.drawImage(p,cx-s/2,cy-s/2,s,s,preserveAspectRatio=True,mask='auto')

def star(cx,cy,r,fill=GOLD,stroke=None):
    pts=[]
    for k in range(5):
        a=math.radians(-90+k*72); pts.append((cx+math.cos(a)*r,cy+math.sin(a)*r))
        a2=math.radians(-90+k*72+36); pts.append((cx+math.cos(a2)*r*0.45,cy+math.sin(a2)*r*0.45))
    p=c.beginPath(); p.moveTo(*pts[0])
    for q in pts[1:]: p.lineTo(*q)
    p.close(); c.setFillColor(fill)
    if stroke: c.setStrokeColor(stroke); c.setLineWidth(1.4); c.drawPath(p,fill=1,stroke=1)
    else: c.drawPath(p,fill=1,stroke=0)
    c.setFillColor(INK)

def pencil(cx,cy,s,ang=0):
    c.saveState(); c.translate(cx,cy); c.rotate(ang)
    c.setFillColor(HexColor("#f4c430")); c.roundRect(-s*0.5,-s*0.12,s*0.8,s*0.24,3,fill=1,stroke=0)
    c.setFillColor(HexColor("#f0a8b8")); c.roundRect(-s*0.62,-s*0.12,s*0.13,s*0.24,3,fill=1,stroke=0)
    p=c.beginPath(); p.moveTo(s*0.3,-s*0.12); p.lineTo(s*0.5,0); p.lineTo(s*0.3,s*0.12); p.close()
    c.setFillColor(HexColor("#f0d8a0")); c.drawPath(p,fill=1,stroke=0)
    p=c.beginPath(); p.moveTo(s*0.44,-s*0.05); p.lineTo(s*0.5,0); p.lineTo(s*0.44,s*0.05); p.close()
    c.setFillColor(INK); c.drawPath(p,fill=1,stroke=0); c.restoreState(); c.setFillColor(INK)

def header(parts, subtitle):
    c.setFillColor(BG); c.rect(0,0,W,H,fill=1,stroke=0)
    c.setStrokeColor(HexColor("#d9c9a8")); c.setLineWidth(2); c.roundRect(16,16,W-32,H-32,18,fill=0,stroke=1)
    star(40,H-46,11,fill=GOLD,stroke=HexColor("#e0a800")); pencil(W-66,H-46,38,ang=-20)
    rl=70; rr=W-92; tot=lambda f: sum(pdfmetrics.stringWidth(t,"PopB",f) for t,_ in parts); fs=27
    while fs>16 and tot(fs)>(rr-rl): fs-=1
    x=(rl+rr)/2-tot(fs)/2
    for t,col in parts:
        c.setFillColor(col); c.setFont("PopB",fs); c.drawString(x,H-54,t); x+=pdfmetrics.stringWidth(t,"PopB",fs)
    c.setFillColor(GREY); c.setFont("PopM",12.5); c.drawCentredString(W/2,H-76,subtitle)
    c.setStrokeColor(LBLUE); c.setLineWidth(1.4); c.line(ML,H-90,MR,H-90)
    c.setFillColor(INK); return H-110

TITLE=[("EOW2 Reading Base 1  ",NAVY),("Story 1",PINK)]

# ================= PAGE 1 : Questions =================
y=header(TITLE,"Read the story and answer the question.")
HAND=HexColor("#2f6fb0")  # "filled-in" handwriting colour for the example
top=y-6; pitch=(top-58)/len(STORY)
for i,(an,ans) in enumerate(STORY):
    cyc=top-pitch*(i+0.5); example=(i==0)
    if i%2==0:
        c.setFillColor(BLUET); c.roundRect(ML,cyc-pitch/2+4,MR-ML,pitch-8,10,fill=1,stroke=0)
    # badge (gold "Ex" for example, else number 1..7)
    if example:
        c.setFillColor(GOLD); c.circle(ML+26,cyc+18,13,fill=1,stroke=0)
        c.setFillColor(white); c.setFont("PopB",10.5); c.drawCentredString(ML+26,cyc+14,"Ex")
    else:
        c.setFillColor(BLUE); c.circle(ML+26,cyc+18,12,fill=1,stroke=0)
        c.setFillColor(white); c.setFont("PopB",12); c.drawCentredString(ML+26,cyc+14,str(i))
    aimg(an,ML+76,cyc+6,56)
    c.setFillColor(NAVY); c.setFont("PopSB",14); c.drawString(ML+114,cyc+14,"Do you play with the "+an+"?")
    yx=MR-150
    c.setFillColor(GREEN); c.setFont("PopB",14); c.drawString(yx,cyc+14,"Yes")
    c.setFillColor(GREY); c.setFont("PopM",14); c.drawString(yx+42,cyc+14,"/")
    c.setFillColor(PINK); c.setFont("PopB",14); c.drawString(yx+60,cyc+14,"No")
    liney=cyc-22
    c.setStrokeColor(LBLUE); c.setLineWidth(1.5); c.line(ML+114,liney,MR-20,liney); c.setStrokeColor(INK)
    if example:
        # circle "Yes"
        c.setStrokeColor(GREEN); c.setLineWidth(2); c.ellipse(yx-7,cyc+8,yx+37,cyc+30,fill=0,stroke=1); c.setStrokeColor(INK)
        # write the full answer on the line
        c.setFillColor(HAND); c.setFont("PopM",13); c.drawString(ML+118,liney+4,"Yes, I do. I like to play with the rabbit.")
        c.setFillColor(INK)
c.showPage()

# ===== Build an 11x11 word search (words go right, left, down, and diagonal) =====
N=11; random.seed(5)
DIRS=[(0,1),(1,0),(1,1),(1,-1)]  # right, down, diag-down-right, diag-down-left (NO right-to-left)
grid=[[None]*N for _ in range(N)]; placements={}
def can_place(w,r,cc,dr,dc):
    for k,ch in enumerate(w):
        rr,c2=r+dr*k,cc+dc*k
        if not(0<=rr<N and 0<=c2<N): return False
        if grid[rr][c2] not in (None,ch): return False
    return True
def place(w):
    for _ in range(900):
        dr,dc=random.choice(DIRS); r=random.randint(0,N-1); cc=random.randint(0,N-1)
        if can_place(w,r,cc,dr,dc):
            for k,ch in enumerate(w): grid[r+dr*k][cc+dc*k]=ch
            placements[w]=(r,cc,dr,dc,len(w)); return True
    return False
for w in sorted([a for a,_ in STORY],key=len,reverse=True): place(w)
for r in range(N):
    for cc in range(N):
        if grid[r][cc] is None: grid[r][cc]=random.choice('abcdefghijklmnopqrstuvwxyz')

def grid_box(gtop,cs,gx):
    c.setStrokeColor(HexColor("#d3e3d3")); c.setLineWidth(1)
    for i in range(N+1):
        c.line(gx,gtop-cs*i,gx+cs*N,gtop-cs*i); c.line(gx+cs*i,gtop,gx+cs*i,gtop-cs*N)
    c.setStrokeColor(GREEN); c.setLineWidth(1.6); c.roundRect(gx-2,gtop-cs*N-2,cs*N+4,cs*N+4,8,fill=0,stroke=1)
def grid_letters(gtop,cs,gx,col=NAVY):
    c.setFont("PopB",cs*0.46); c.setFillColor(col)
    for r in range(N):
        for cc in range(N):
            c.drawCentredString(gx+cs*(cc+0.5),gtop-cs*(r+0.5)-cs*0.16,grid[r][cc].upper())

# ================= PAGE 2 : Word search =================
y=header([("Find the ",NAVY),("words.",GREEN)],"Find the 8 animal words. They go right, down and diagonal.")
CS=40.0; GX=(W-CS*N)/2; gtop=y-6
grid_box(gtop,CS,GX); grid_letters(gtop,CS,GX)
gbot=gtop-CS*N
# WORD BANK with a picture for each word, BELOW the grid
ptop=gbot-16; pbot=66
c.setFillColor(HexColor("#f1f7f1")); c.roundRect(40,pbot,W-80,ptop-pbot,12,fill=1,stroke=0)
c.setStrokeColor(GREEN); c.setLineWidth(1.1); c.setDash(2,3); c.roundRect(40,pbot,W-80,ptop-pbot,12,fill=0,stroke=1); c.setDash(1,0)
c.setFillColor(GREEN); c.setFont("PopB",10); c.drawString(56,ptop-16,"WORD BANK")
words8=[a for a,_ in STORY]; cols=4; cw=(W-80-16)/cols; areatop=ptop-28
rowh=(areatop-(pbot+10))/2
for i,an in enumerate(words8):
    col=i%cols; r=i//cols
    cx=48+cw*(col+0.5); ccy=areatop-rowh*(r+0.5)
    aimg(an,cx,ccy+12,50)
    c.setFillColor(NAVY); c.setFont("PopSB",13.5); c.drawCentredString(cx,ccy-26,an)
c.showPage()

# ================= PAGE 3 : Answer Key =================
y=header([("Answer ",NAVY),("Key",PINK)],"EOW2 Reading Base 1 · Story 1 · Do You Play?")
c.setFillColor(INK); c.setFont("PopM",10.5); yy=y-4
for i,(an,ans) in enumerate(STORY):
    tag="Ex" if i==0 else str(i)
    if ans=="Yes": line=f"{tag}. Do you play with the {an}?   Yes, I do. I like to play with the {an}."
    else:          line=f"{tag}. Do you play with the {an}?   No, I don't. I don't like the {an}."
    c.drawString(48,yy,line); yy-=17
# solved word search with coloured capsules over each word
cs2=29.0; gx2=(W-cs2*N)/2; gtop2=yy-16
COLS=[PINK,BLUE,GREEN,PURPLE,GOLD,HexColor("#5f97cd"),HexColor("#d76f96"),HexColor("#5cae67")]
for ci,(w,(r,cc,dr,dc,ln)) in enumerate(placements.items()):
    x1=gx2+cs2*(cc+0.5); y1=gtop2-cs2*(r+0.5)
    x2=gx2+cs2*(cc+dc*(ln-1)+0.5); y2=gtop2-cs2*(r+dr*(ln-1)+0.5)
    c.saveState(); c.setStrokeColor(COLS[ci%len(COLS)]); c.setLineWidth(cs2*0.74); c.setLineCap(1)
    c.setStrokeAlpha(0.32); c.line(x1,y1,x2,y2); c.restoreState()
grid_box(gtop2,cs2,gx2); grid_letters(gtop2,cs2,gx2)
c.setFillColor(GREY); c.setFont("Pop",9.5)
c.drawString(40,52,"Source: Canva EOW 2-UNIT 1 READER (Story 1).  Yes: rabbit/goat/lamb/fawn.  No: lion/bear/alligator/rhino.")
c.showPage()
c.save(); print("done ->",OUT)
