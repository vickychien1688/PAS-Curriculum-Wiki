#!/usr/bin/env python3
"""EOW2 U1 Animal Friends — COLORFUL 'Lesson-series' worksheet (4 pages).
Bright house style, roomy (not cramped), Poppins font. Scene art from GPT pipeline.
P1 Vocabulary: animals match + action circle (vocab 1 & 2 on one page)
P2 Grammar: What are they doing? (They are ___ing, scene images)
P3 Grammar: Put the words in order (scrambled sentences, scene images)
P4 Answer Key
"""
import os, math
from PIL import Image, ImageDraw
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

GF="/usr/share/fonts/truetype/google-fonts"
pdfmetrics.registerFont(TTFont("Pop",  f"{GF}/Poppins-Regular.ttf"))
pdfmetrics.registerFont(TTFont("PopB", f"{GF}/Poppins-Bold.ttf"))
pdfmetrics.registerFont(TTFont("PopM", f"{GF}/Poppins-Medium.ttf"))
pdfmetrics.registerFont(TTFont("PopSB", f"{GF}/Poppins-Bold.ttf"))

W,H=A4
# softer, calmer palette (less saturated than v1 — "too colourful" feedback)
NAVY=HexColor("#3a4a86"); BG=HexColor("#fffdf7"); INK=HexColor("#3a3d45"); GREY=HexColor("#8b909c")
PINK=HexColor("#d989aa"); BLUE=HexColor("#6ba0cf"); GREEN=HexColor("#7fb985"); ORANGE=HexColor("#e3a86a"); PURPLE=HexColor("#9e85c6")
PINKT=HexColor("#fbf2f6"); BLUET=HexColor("#f1f6fb"); GREENT=HexColor("#f2f8f3"); ORANGET=HexColor("#fdf6ee"); PURPLET=HexColor("#f6f2fb")
CREAM=HexColor("#fdf7e3"); GOLD=HexColor("#e6c266"); RED=HexColor("#dd9290"); LBLUE=HexColor("#a9c7e8")
HERE=os.path.dirname(os.path.abspath(__file__))
LIB=os.path.normpath(os.path.join(HERE,"..","..","09_Image_Library","words"))
SCENES=os.path.join(HERE,"scenes")
OUT=os.path.join(HERE,"EOW2 U1 Animal Friends (colorful).pdf")
c=canvas.Canvas(OUT,pagesize=A4)
CACHE=os.path.join(HERE,"_trans"); os.makedirs(CACHE,exist_ok=True)

def transparent(word,thresh=60):
    out=os.path.join(CACHE,f"{word}.png")
    if os.path.exists(out): return out
    im=Image.open(f"{LIB}/{word}/{word}-v1-color.png").convert("RGB")
    w,h=im.size; S=(1,2,3)
    for cn in ((0,0),(w-1,0),(0,h-1),(w-1,h-1)):
        if im.getpixel(cn)[0]>200: ImageDraw.floodfill(im,cn,S,thresh=thresh)
    px=im.load(); rg=im.convert("RGBA"); rp=rg.load()
    for y in range(h):
        for x in range(w):
            if px[x,y]==S: rp[x,y]=(255,255,255,0)
    bb=rg.split()[3].getbbox()
    if bb:
        l,t,r,b=bb; rg=rg.crop((max(0,l-6),max(0,t-6),min(w,r+6),min(h,b+6)))
    rg.save(out); return out

def img(word,cx,cy,s): c.drawImage(transparent(word),cx-s/2,cy-s/2,s,s,preserveAspectRatio=True,mask='auto')
def scene(name,x,cyc,s):
    p=os.path.join(SCENES,name)
    if not os.path.exists(p): return
    c.drawImage(p,x,cyc-s/2,s,s,preserveAspectRatio=True,mask='auto')
    c.setStrokeColor(white); c.setLineWidth(3); c.roundRect(x,cyc-s/2,s,s,8,fill=0,stroke=1)
    c.setStrokeColor(HexColor("#d8e0ea")); c.setLineWidth(1.4); c.roundRect(x,cyc-s/2,s,s,8,fill=0,stroke=1)

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

def crown(cx,cy,s):
    c.setFillColor(GOLD); base_y=cy-s*0.28
    p=c.beginPath(); p.moveTo(cx-s*0.5,base_y)
    p.lineTo(cx-s*0.5,cy+s*0.05); p.lineTo(cx-s*0.25,cy-s*0.15); p.lineTo(cx,cy+s*0.28)
    p.lineTo(cx+s*0.25,cy-s*0.15); p.lineTo(cx+s*0.5,cy+s*0.05); p.lineTo(cx+s*0.5,base_y); p.close()
    c.drawPath(p,fill=1,stroke=0)
    c.setFillColor(HexColor("#f0a500")); c.roundRect(cx-s*0.5,base_y-s*0.16,s,s*0.18,2,fill=1,stroke=0)
    for dx,col in ((-0.25,RED),(0.0,BLUE),(0.25,GREEN)):
        c.setFillColor(col); c.circle(cx+dx*s,cy+s*0.02,s*0.07,fill=1,stroke=0)
    c.setFillColor(INK)

def pencil(cx,cy,s,ang=0):
    c.saveState(); c.translate(cx,cy); c.rotate(ang)
    c.setFillColor(HexColor("#f4c430")); c.roundRect(-s*0.5,-s*0.12,s*0.8,s*0.24,3,fill=1,stroke=0)
    c.setFillColor(HexColor("#f0a8b8")); c.roundRect(-s*0.62,-s*0.12,s*0.13,s*0.24,3,fill=1,stroke=0)
    p=c.beginPath(); p.moveTo(s*0.3,-s*0.12); p.lineTo(s*0.5,0); p.lineTo(s*0.3,s*0.12); p.close()
    c.setFillColor(HexColor("#f0d8a0")); c.drawPath(p,fill=1,stroke=0)
    p=c.beginPath(); p.moveTo(s*0.44,-s*0.05); p.lineTo(s*0.5,0); p.lineTo(s*0.44,s*0.05); p.close()
    c.setFillColor(INK); c.drawPath(p,fill=1,stroke=0); c.restoreState(); c.setFillColor(INK)

def page_frame():
    c.setFillColor(BG); c.rect(0,0,W,H,fill=1,stroke=0)
    c.setStrokeColor(HexColor("#d9c9a8")); c.setLineWidth(2); c.setDash(1,0)
    c.roundRect(16,16,W-32,H-32,18,fill=0,stroke=1)

def lesson_badge(x,y,text,col=PURPLE):
    tw=pdfmetrics.stringWidth(text,"PopB",10.5)
    star(x+8,y,9,fill=GOLD,stroke=HexColor("#e0a800"))
    c.setFillColor(col); c.roundRect(x+20,y-11,tw+26,22,11,fill=1,stroke=0)
    c.setFillColor(white); c.setFont("PopB",10.5); c.drawString(x+34,y-4,text)
    c.setFillColor(INK); return x+20+tw+26

def header(unit_badge, parts):
    page_frame()
    bxr=lesson_badge(34,H-44,unit_badge)
    pencil(W-72,H-44,38,ang=-20)
    rl=bxr+16; rr=W-100
    tot=lambda f: sum(pdfmetrics.stringWidth(t,"PopB",f) for t,_ in parts)
    fs=30
    while fs>18 and tot(fs)>(rr-rl): fs-=1
    x=(rl+rr)/2-tot(fs)/2
    for t,col in parts:
        c.setFillColor(col); c.setFont("PopB",fs); c.drawString(x,H-54,t); x+=pdfmetrics.stringWidth(t,"PopB",fs)
    c.setFillColor(INK); return H-92

def card(x,y,w,h,color,tint,n,label,instr=""):
    c.setFillColor(tint); c.roundRect(x,y-h,w,h,16,fill=1,stroke=0)
    c.setStrokeColor(color); c.setLineWidth(1.1); c.setDash(1,0); c.roundRect(x,y-h,w,h,16,fill=0,stroke=1)
    lw=pdfmetrics.stringWidth(label,"PopB",13.5); hbw=lw+(66 if n else 32)
    c.setFillColor(color); c.roundRect(x+16,y-14,hbw,28,14,fill=1,stroke=0)
    if n:
        c.setFillColor(white); c.circle(x+34,y,11,fill=1,stroke=0)
        c.setFillColor(color); c.setFont("PopB",12); c.drawCentredString(x+34,y-4,str(n)); tx=x+50
    else: tx=x+30
    c.setFillColor(white); c.setFont("PopB",13.5); c.drawString(tx,y-4.5,label)
    cy=y-30
    if instr:
        c.setFillColor(GREY); c.setFont("PopM",10.5); c.drawString(x+20,y-26,instr); cy=y-44
    c.setFillColor(INK); return cy

def wline_colored(x0,x1,base):
    c.setStrokeColor(LBLUE); c.setLineWidth(1.5); c.setDash(1,0); c.line(x0,base,x1,base)
    c.setStrokeColor(INK)

def footer_check(items):
    pass  # footer band removed per Vicky

# ===================== PAGE 1 : Vocabulary (two cards) =====================
y=header("EOW2 · Unit 1",[("Animal ",NAVY),("Friends",ORANGE)])
# Card A : animals match (top) — split into groups of 5 + 4 (words shuffled within each group)
aTop=y; aH=474; aBot=aTop-aH
yc=card(40,aTop,W-80,aH,PINK,PINKT,"A","Animals — match","Match 5 pictures in each group to the words.")
groups=[(["cat","chicken","cow","dog","duck"], ["a duck","a cat","a dog","a cow","a chicken"]),
        (["goat","horse","sheep","turtle"],    ["a turtle","a goat","a sheep","a horse"])]
gapg=18; top=yc-6; pitch=(top-(aBot+14)-gapg)/9; cy=top
for gi,(gan,gw) in enumerate(groups):
    if gi>0:
        c.setStrokeColor(HexColor("#eccada")); c.setLineWidth(1); c.setDash(2,3); c.line(70,cy-2,W-70,cy-2); c.setDash(1,0); cy-=gapg
    for j in range(len(gan)):
        ccy=cy-pitch/2
        img(gan[j],118,ccy,46)
        c.setFillColor(PINK); c.circle(178,ccy,4.5,fill=1,stroke=0); c.circle(W-250,ccy,4.5,fill=1,stroke=0)
        word=gw[j]; tw=pdfmetrics.stringWidth(word,"PopSB",13)
        c.setFillColor(white); c.setStrokeColor(PINK); c.setLineWidth(1.4); c.roundRect(W-236,ccy-13,tw+26,26,8,fill=1,stroke=1)
        c.setFillColor(NAVY); c.setFont("PopSB",13); c.drawString(W-223,ccy-4,word)
        cy-=pitch
# Card B : action circle (bottom) — tighter, reaches near page bottom (no big white gap)
bTop=aBot-14; bBot=38; bH=bTop-bBot
yc=card(40,bTop,W-80,bH,BLUE,BLUET,"B","Action words — circle","Look at the picture. Circle the correct word.")
vrows=[("climb",["climb","swim","fly"]),("crawl",["fly","crawl","swim"]),
       ("fly",["swim","climb","fly"]),("swim",["crawl","swim","climb"])]
optx=[210,330,450]; top=yc-2; pitch=(top-(bBot+12))/len(vrows)
for i,(slug,opts) in enumerate(vrows):
    cy=top-pitch*(i+0.5)
    c.setFillColor(BLUE); c.circle(70,cy,11,fill=1,stroke=0)
    c.setFillColor(white); c.setFont("PopB",12); c.drawCentredString(70,cy-4,str(i+1))
    img(slug,128,cy,50)
    c.setFont("PopSB",14)
    for k,opt in enumerate(opts):
        c.setFillColor(NAVY); c.drawString(optx[k],cy-5,opt)
footer_check([])
c.showPage()

# ===================== PAGE 2 : What are they doing? =====================
y=header("EOW2 · Unit 1",[("What are they ",NAVY),("doing?",GREEN)])
c.setFillColor(CREAM); c.setStrokeColor(GOLD); c.setLineWidth(1.6); c.roundRect(40,y-56,W-80,56,12,fill=1,stroke=1)
crown(72,y-26,30)
c.setFillColor(NAVY); c.setFont("PopB",13); c.drawString(100,y-20,"Rule")
c.setFillColor(INK); c.setFont("PopM",12.5); c.drawString(150,y-20,"They are  +  verb-ing")
c.setFillColor(GREEN); c.setFont("PopB",12.5); c.drawString(305,y-20,"They are swimming.")
c.setFillColor(GREY); c.setFont("PopM",10.5); c.drawString(150,y-40,"Word bank:  climbing   crawling   flying   swimming")
y=y-90
yc=card(40,y,W-80,y-86,GREEN,GREENT,"1","Look and write","Look at the picture. Write the -ing verb.")
rows=[("cats-climbing.png",),("turtles-crawling.png",),("birds-flying.png",),("ducks-swimming.png",)]
top=yc-6; pitch=(top-94)/len(rows)
for i,(sc,) in enumerate(rows):
    cy=top-pitch*(i+0.5)
    c.setFillColor(GREEN); c.circle(70,cy,12,fill=1,stroke=0)
    c.setFillColor(white); c.setFont("PopB",12); c.drawCentredString(70,cy-4,str(i+1))
    scene(sc,96,cy,92)
    tx=206; c.setFillColor(NAVY); c.setFont("PopSB",16); c.drawString(tx,cy-4,"They are")
    sx=tx+pdfmetrics.stringWidth("They are  ","PopSB",16)
    wline_colored(sx,W-150,cy-8)
    c.setFillColor(NAVY); c.setFont("PopSB",16); c.drawString(W-144,cy-4,".")
footer_check([("Big letter",PINK),("are",BLUE),("Dot",GREEN)])
c.showPage()

# ===================== PAGE 3 : Put the words in order =====================
y=header("EOW2 · Unit 1",[("Put the words ",NAVY),("in order",PURPLE)])
yc=card(40,y,W-80,y-86,PURPLE,PURPLET,"1","Make the sentence","Write the sentence on the line. Add the end mark ( .  or  ? ).")
scram=[("cats-climbing.png",["climbing","the","cats","are"]),
       ("ducks-swimming.png",["the","ducks","are","swimming"]),
       ("turtles-crawling.png",["crawling","the","turtles","are"]),
       ("goats.png",["doing","what","are","the","goats"]),
       ("birds-flying.png",["flying","the","birds","are"])]
top=yc-4; pitch=(top-94)/len(scram)
for i,(sc,toks) in enumerate(scram):
    cmid=top-pitch*(i+0.5)
    c.setFillColor(PURPLE); c.circle(66,cmid,12,fill=1,stroke=0)
    c.setFillColor(white); c.setFont("PopB",12); c.drawCentredString(66,cmid-4,str(i+1))
    scene(sc,90,cmid,86)
    cx=190; c.setFont("PopSB",12.5)
    for t in toks:
        tw=pdfmetrics.stringWidth(t,"PopSB",12.5)
        c.setFillColor(white); c.setStrokeColor(PURPLE); c.setLineWidth(1.3); c.roundRect(cx,cmid+8,tw+16,24,7,fill=1,stroke=1)
        c.setFillColor(NAVY); c.drawString(cx+8,cmid+15,t); cx+=tw+16+7
    liney=cmid-22; wline_colored(190,W-86,liney)
    c.setStrokeColor(PURPLE); c.setLineWidth(1.2); c.setDash(2,2); c.roundRect(W-78,liney-5,24,26,5,fill=0,stroke=1); c.setDash(1,0)
    c.setFillColor(GREY); c.setFont("Pop",8); c.drawCentredString(W-66,liney-15,". ?"); c.setFillColor(INK)
footer_check([("Big letter",PINK),("Dot",GREEN),("end mark",ORANGE)])
c.showPage()

# ===================== PAGE 4 : Answer Key =====================
y=header("EOW2 · Unit 1",[("Answer ",NAVY),("Key",PINK)])
def keycard(y,color,tint,tag,label,lines):
    h=28+len(lines)*18+14
    yc=card(40,y,W-80,h,color,tint,tag,label)
    c.setFillColor(INK); c.setFont("PopM",12); yy=yc-6
    for ln in lines:
        c.drawString(60,yy,ln); yy-=18
    return y-h-12
y=keycard(y,PINK,PINKT,"A","Animals — match",
    ["cat = a cat,  chicken = a chicken,  cow = a cow,  dog = a dog,  duck = a duck,",
     "goat = a goat,  horse = a horse,  sheep = a sheep,  turtle = a turtle"])
y=keycard(y,BLUE,BLUET,"B","Action words — circle",
    ["1. climb   2. crawl   3. fly   4. swim"])
y=keycard(y,GREEN,GREENT,"1","What are they doing?",
    ["1. climbing   2. crawling   3. flying   4. swimming"])
y=keycard(y,PURPLE,PURPLET,"1","Put the words in order",
    ["1. The cats are climbing.   2. The ducks are swimming.   3. The turtles are crawling.",
     "4. What are the goats doing?   5. The birds are flying."])
c.setFillColor(GREY); c.setFont("Pop",10)
c.drawString(40,70,"Scope: EOW2 Unit 1 only.  Art: 09_Image_Library + GPT scenes.  Value: Be good to animals.")
footer_check([("Big letter",PINK),("Dot",GREEN)])
c.showPage()
c.save(); print("done ->",OUT)
