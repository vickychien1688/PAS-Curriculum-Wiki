#!/usr/bin/env python3
"""EOW2 U2 Fun in Class — COLORFUL 'Lesson-series' worksheet (4 pages).
Bright house style, roomy, Poppins. VARIED activity types (differ from U1):
P1 Vocabulary: A = Word Scramble (action words) + B = Word Hunt (classroom objects)
P2 Grammar 1: We're + verb-ing  (fill the blank with Word Bank, scene images)
P3 Grammar 2: Are there...? Yes, there are. / No, there aren't. (one desk scene, Yes/No)
P4 Answer Key
"""
import os, math, random
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
NAVY=HexColor("#3a4a86"); BG=HexColor("#fffdf7"); INK=HexColor("#3a3d45"); GREY=HexColor("#8b909c")
PINK=HexColor("#d989aa"); BLUE=HexColor("#6ba0cf"); GREEN=HexColor("#7fb985"); ORANGE=HexColor("#e3a86a"); PURPLE=HexColor("#9e85c6")
PINKT=HexColor("#fbf2f6"); BLUET=HexColor("#f1f6fb"); GREENT=HexColor("#f2f8f3"); ORANGET=HexColor("#fdf6ee"); PURPLET=HexColor("#f6f2fb")
CREAM=HexColor("#fdf7e3"); GOLD=HexColor("#e6c266"); RED=HexColor("#dd9290"); LBLUE=HexColor("#a9c7e8")
HERE=os.path.dirname(os.path.abspath(__file__))
LIB=os.path.normpath(os.path.join(HERE,"..","..","09_Image_Library","words"))
SCENES=os.path.join(HERE,"scenes")
OUT=os.path.join(HERE,"EOW2 U2 Fun in Class (colorful).pdf")
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
    if not os.path.exists(p): return False
    c.drawImage(p,x,cyc-s/2,s,s,preserveAspectRatio=True,mask='auto')
    c.setStrokeColor(white); c.setLineWidth(3); c.roundRect(x,cyc-s/2,s,s,8,fill=0,stroke=1)
    c.setStrokeColor(HexColor("#d8e0ea")); c.setLineWidth(1.4); c.roundRect(x,cyc-s/2,s,s,8,fill=0,stroke=1)
    return True

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

def wordbox(x,y,w,words,color,title="Word Box"):
    """A rounded Word Box band with the words, returns height used."""
    pad=12; th=20
    c.setFillColor(white); c.setStrokeColor(color); c.setLineWidth(1.4); c.setDash(1,0)
    h=44
    c.roundRect(x,y-h,w,h,12,fill=1,stroke=1)
    c.setFillColor(color); c.setFont("PopB",11); c.drawString(x+14,y-16,title)
    c.setFillColor(NAVY); c.setFont("PopSB",13)
    s="    ".join(words)
    c.drawCentredString(x+w/2, y-36, s)
    c.setFillColor(INK); return h

# PHONICS-CHUNK scramble: split into decoding units (onset blend / vowel grapheme /
# final consonant cluster / -ing), keep each chunk intact, shuffle the chunk ORDER.
# (Vicky: teach decoding by sound chunks, e.g. count = c-ou-nt.)
CHUNKS={
 "coloring":["c","o","l","or","ing"], "counting":["c","ou","nt","ing"],
 "cutting":["c","u","tt","ing"], "drawing":["dr","aw","ing"],
 "gluing":["gl","u","ing"], "talking":["t","al","k","ing"],
}
def scramble_syll(word, seed):
    chunks=CHUNKS[word][:];
    if len(chunks)==1: return chunks
    r=random.Random(seed)
    for _ in range(20):
        s=chunks[:]; r.shuffle(s)
        if s!=chunks: return s
    return chunks[::-1]

# ===================== PAGE 1 : Vocabulary (Scramble + Word Hunt) =====================
y=header("EOW2 · Unit 2",[("Fun in ",NAVY),("Class",ORANGE)])

# Card A : Word Scramble (action words)
aTop=y; aH=372; aBot=aTop-aH
yc=card(40,aTop,W-80,aH,PINK,PINKT,"A","Build the word from sound chunks","Put the sound chunks in the right order. Write the word.")
acts=["coloring","counting","cutting","drawing","gluing","talking"]
top=yc-6; rowsN=len(acts); pitch=(top-(aBot+62))/rowsN
for i,wd in enumerate(acts):
    cy=top-pitch*(i+0.5)
    c.setFillColor(PINK); c.circle(70,cy,11,fill=1,stroke=0)
    c.setFillColor(white); c.setFont("PopB",12); c.drawCentredString(70,cy-4,str(i+1))
    img(wd,120,cy,46)
    # syllable chunks shown as separate tiles (reassemble the syllables)
    chunks=scramble_syll(wd,i+11)
    tx=168
    for ch in chunks:
        lab=ch.lower(); tw=pdfmetrics.stringWidth(lab,"PopB",14)
        c.setFillColor(white); c.setStrokeColor(ORANGE); c.setLineWidth(1.4); c.setDash(1,0)
        c.roundRect(tx,cy-13,tw+18,26,7,fill=1,stroke=1)
        c.setFillColor(ORANGE); c.setFont("PopB",14); c.drawString(tx+9,cy-5,lab)
        tx+=tw+18+8
    wline_colored(tx+10,W-70,cy-8)
# word box
wordbox(40+14,aBot+50,W-80-28,["coloring","counting","cutting","drawing","gluing","talking"],PINK)

# Card B : Word Hunt (classroom objects) — circle the hidden word
bTop=aBot-14; bBot=38; bH=bTop-bBot
yc=card(40,bTop,W-80,bH,BLUE,BLUET,"B","Find and circle the word","Each line hides one word. Circle the word you see.")
objs=[("glue","t g l u e r"),("marker","b m a r k e r s"),("notebook","p n o t e b o o k a"),
      ("paintbrush","x p a i n t b r u s h e"),("scissors","u s c i s s o r s n")]
top=yc-2; pitch=(top-(bBot+12))/len(objs)
for i,(slug,strg) in enumerate(objs):
    cy=top-pitch*(i+0.5)
    c.setFillColor(BLUE); c.circle(70,cy,11,fill=1,stroke=0)
    c.setFillColor(white); c.setFont("PopB",12); c.drawCentredString(70,cy-4,str(i+1))
    img(slug,124,cy,48)
    c.setFillColor(NAVY); c.setFont("PopB",17); c.drawString(186,cy-6,strg.lower())
c.showPage()

# ===================== PAGE 2 : Grammar 1 — We're + verb-ing =====================
y=header("EOW2 · Unit 2",[("What are you ",NAVY),("doing?",GREEN)])
c.setFillColor(CREAM); c.setStrokeColor(GOLD); c.setLineWidth(1.6); c.roundRect(40,y-56,W-80,56,12,fill=1,stroke=1)
crown(72,y-26,30)
c.setFillColor(NAVY); c.setFont("PopB",13); c.drawString(100,y-20,"Rule")
c.setFillColor(INK); c.setFont("PopM",12.5); c.drawString(150,y-20,"We're  +  verb-ing")
c.setFillColor(GREEN); c.setFont("PopB",12.5); c.drawString(300,y-20,"We're counting crayons.")
c.setFillColor(GREY); c.setFont("PopM",10.5); c.drawString(150,y-40,"Word bank:  coloring   counting   cutting   drawing   gluing")
y=y-90
yc=card(40,y,W-80,y-86,GREEN,GREENT,"1","Look and write","Look at the picture. Write the -ing word on the line.")
rows=[("coloring.png","coloring"),("counting.png","counting"),("cutting.png","cutting"),
      ("drawing.png","drawing"),("gluing.png","gluing")]
top=yc-6; pitch=(top-94)/len(rows)
for i,(sc,ans) in enumerate(rows):
    cy=top-pitch*(i+0.5)
    c.setFillColor(GREEN); c.circle(70,cy,12,fill=1,stroke=0)
    c.setFillColor(white); c.setFont("PopB",12); c.drawCentredString(70,cy-4,str(i+1))
    if not scene(sc,96,cy,92):
        img(ans,96+46,cy,80)  # fallback to icon if scene missing
    tx=210; c.setFillColor(NAVY); c.setFont("PopSB",16); c.drawString(tx,cy-4,"We're")
    sx=tx+pdfmetrics.stringWidth("We're  ","PopSB",16)
    wline_colored(sx,W-150,cy-8)
    c.setFillColor(NAVY); c.setFont("PopSB",16); c.drawString(W-144,cy-4,".")
c.showPage()

# ===================== PAGE 3 : Grammar 2 — Are there...? =====================
y=header("EOW2 · Unit 2",[("Are there ",NAVY),("...?",PURPLE)])
c.setFillColor(CREAM); c.setStrokeColor(GOLD); c.setLineWidth(1.6); c.roundRect(40,y-58,W-80,58,12,fill=1,stroke=1)
crown(72,y-27,30)
c.setFillColor(NAVY); c.setFont("PopB",13); c.drawString(100,y-18,"Rule")
c.setFillColor(GREEN); c.setFont("PopSB",11.5); c.drawString(150,y-18,"Yes, there are. There are ten markers.")
c.setFillColor(RED); c.setFont("PopSB",11.5); c.drawString(150,y-38,"No, there aren't. There aren't any crayons.")
y=y-74
# desk scene (watercolour, GPT): countable — 10 markers, 4 notebooks, 5 paintbrushes, 4 glue sticks, 2 scissors
dp=os.path.join(SCENES,"desk.png")
dw,dh=252,202
if os.path.exists(dp):
    c.drawImage(dp,W/2-dw/2,y-dh,dw,dh,preserveAspectRatio=True,mask='auto')
    c.setStrokeColor(HexColor("#d8e0ea")); c.setLineWidth(1.4); c.roundRect(W/2-dw/2,y-dh,dw,dh,8,fill=0,stroke=1)
else:
    c.setFillColor(GREY); c.setFont("PopM",11); c.drawCentredString(W/2,y-dh/2,"[desk scene]")
y=y-dh-14
yc=card(40,y,W-80,y-46,PURPLE,PURPLET,"1","Look, count and write","Count the things. Write the full answer. Number 1 is done for you.")
qs=[("Are there any markers?","Yes, there are. There are ten markers."),
    ("Are there any crayons?","No, there aren't. There aren't any crayons."),
    ("Are there any notebooks?","Yes, there are. There are four notebooks."),
    ("Are there any erasers?","No, there aren't. There aren't any erasers."),
    ("Are there any paintbrushes?","Yes, there are. There are five paintbrushes.")]
top=yc-2; bot=42; pitch=(top-bot)/len(qs)
for i,(q,ans) in enumerate(qs):
    blk=top-pitch*i
    qy=blk-18
    c.setFillColor(PURPLE); c.circle(66,qy,11,fill=1,stroke=0)
    c.setFillColor(white); c.setFont("PopB",12); c.drawCentredString(66,qy-4,str(i+1))
    c.setFillColor(NAVY); c.setFont("PopSB",13.5); c.drawString(90,qy-5,q)
    ly=blk-pitch+22   # answer line low in block -> roomy gap from the question above
    wline_colored(90,W-70,ly)
    if i==0:
        c.setFillColor(GREEN); c.setFont("PopSB",13.5); c.drawString(96,ly+5,ans)
        c.setFillColor(GREY); c.setFont("PopM",9); c.drawString(W-150,ly+5,"(example)")
c.showPage()

# ===================== PAGE 4 : Reading — Paper Art =====================
y=header("EOW2 · Unit 2",[("Paper ",NAVY),("Art",GREEN)])
para=["This girl is making Chinese paper art. She is cutting paper to make a picture of a cat. She is using scissors.",
      "Some people make paper animals or flowers. In Mexico, people make paper art, too. People cut pictures of flowers, animals, and people."]
def _wrap(t,fz,maxw):
    out=[]; cur=""
    for w in t.split():
        s=(cur+" "+w).strip()
        if pdfmetrics.stringWidth(s,"PopM",fz)<=maxw: cur=s
        else: out.append(cur); cur=w
    if cur: out.append(cur)
    return out
fz=12; iw=120; innerw=(W-40-16-iw-16)-62; plines=[]
for p in para: plines+=_wrap(p,fz,innerw); plines.append("")
if plines and plines[-1]=="": plines.pop()
texth=len(plines)*18
ph=40+max(texth,iw)+16
c.setFillColor(GREENT); c.roundRect(40,y-ph,W-80,ph,14,fill=1,stroke=0)
c.setStrokeColor(GREEN); c.setLineWidth(1.2); c.setDash(1,0); c.roundRect(40,y-ph,W-80,ph,14,fill=0,stroke=1)
lbl="Paper Art"; tw=pdfmetrics.stringWidth(lbl,"PopB",13.5)
c.setFillColor(GREEN); c.roundRect(56,y-14,tw+30,28,14,fill=1,stroke=0)
c.setFillColor(white); c.setFont("PopB",13.5); c.drawString(70,y-4.5,lbl)
ix=W-40-16-iw; icy=y-ph/2-4
c.setFillColor(white); c.setStrokeColor(HexColor("#d8e0ea")); c.setLineWidth(1.3); c.roundRect(ix,icy-iw/2,iw,iw,10,fill=1,stroke=1)
img("cutting",ix+iw/2,icy,iw-14)
c.setFillColor(INK); c.setFont("PopM",fz); yy=y-44
for ln in plines:
    if ln: c.drawString(62,yy,ln)
    yy-=18
y=y-ph-14
yc=card(40,y,W-80,y-30,GREEN,GREENT,"1","Read and answer","Read. Then answer the questions. Number 1 is done for you.")
cx0=66; tx=92
def _bullet(n,yy):
    c.setFillColor(GREEN); c.circle(cx0,yy,11,fill=1,stroke=0)
    c.setFillColor(white); c.setFont("PopB",12); c.drawCentredString(cx0,yy-4,str(n))
def _tf(yy,stmt,ans,example=False):
    _bullet(_tf.n,yy); _tf.n+=1
    c.setFillColor(NAVY); c.setFont("PopSB",13); c.drawString(tx,yy-5,stmt)
    ax=W-212
    for opt,col in (("True",GREEN),("False",RED)):
        twd=pdfmetrics.stringWidth(opt,"PopSB",11.5); fillit=example and ((opt=="True")==(ans=="T"))
        c.setFillColor(col if fillit else white); c.setStrokeColor(col); c.setLineWidth(1.3)
        c.roundRect(ax,yy-12,twd+16,24,12,fill=1,stroke=1)
        c.setFillColor(white if fillit else col); c.setFont("PopSB",11.5); c.drawString(ax+8,yy-4,opt); ax+=twd+16+10
    if example: c.setFillColor(GREY); c.setFont("PopM",8.5); c.drawString(W-150,yy-22,"(example)")
    c.setFillColor(INK)
_tf.n=1
def _mc(yy,q,opts):
    _bullet(_mc.n,yy); _mc.n+=1
    c.setFillColor(NAVY); c.setFont("PopSB",13); c.drawString(tx,yy-5,q)
    ox=tx; oy=yy-30
    for lab,t in opts:
        s=f"{lab}) {t}"; twd=pdfmetrics.stringWidth(s,"PopSB",12)
        c.setFillColor(white); c.setStrokeColor(GREEN); c.setLineWidth(1.2); c.roundRect(ox,oy-13,twd+16,24,11,fill=1,stroke=1)
        c.setFillColor(NAVY); c.setFont("PopSB",12); c.drawString(ox+8,oy-5,s); ox+=twd+16+12
def _wr(yy,q):
    _bullet(_wr.n,yy); _wr.n+=1
    c.setFillColor(NAVY); c.setFont("PopSB",13); c.drawString(tx,yy-5,q)
    wline_colored(tx,W-80,yy-30)
_tf.n=1; _mc.n=6
cur=yc-12
_tf(cur,"The girl is making Chinese paper art.","T",example=True); cur-=38
_tf(cur,"She is cutting paper with a pencil.","F"); cur-=36
_tf(cur,"She is making a picture of a cat.","T"); cur-=36
_tf(cur,"People make paper art only in China.","F"); cur-=36
_tf(cur,"People make paper animals and flowers.","T"); cur-=46
_mc(cur,"What is the girl making?",[("a","a dog"),("b","a cat"),("c","a car")]); cur-=56
_mc(cur,"Where do people also make paper art?",[("a","Japan"),("b","Mexico"),("c","India")]); cur-=56
_mc(cur,"What does she use to cut paper?",[("a","a pencil"),("b","scissors"),("c","glue")]); cur-=56
_mc(cur,"What do people cut pictures of?",[("a","cars"),("b","flowers and animals"),("c","houses")]); cur-=56
_mc(cur,"Paper art is made with ______.",[("a","paper"),("b","wood"),("c","stone")]); cur-=50
c.setFillColor(INK)
c.showPage()

# ===================== PAGE 5 : Value Reading — Be Neat =====================
y=header("EOW2 · Unit 2",[("Be ",NAVY),("Neat",GREEN)])
vpara=["Be neat at school and at home. Put your books on the shelf. Put your pens in the box. Clean your desk.",
       "Put your toys away. A neat room is nice. When you are neat, you can find your things fast. Be neat every day!"]
fz=12; iw=120; innerw=(W-40-16-iw-16)-62; plines=[]
for p in vpara: plines+=_wrap(p,fz,innerw); plines.append("")
if plines and plines[-1]=="": plines.pop()
texth=len(plines)*18; ph=40+max(texth,iw)+16
c.setFillColor(GREENT); c.roundRect(40,y-ph,W-80,ph,14,fill=1,stroke=0)
c.setStrokeColor(GREEN); c.setLineWidth(1.2); c.setDash(1,0); c.roundRect(40,y-ph,W-80,ph,14,fill=0,stroke=1)
lbl="Be Neat"; tw=pdfmetrics.stringWidth(lbl,"PopB",13.5)
c.setFillColor(GREEN); c.roundRect(56,y-14,tw+30,28,14,fill=1,stroke=0)
c.setFillColor(white); c.setFont("PopB",13.5); c.drawString(70,y-4.5,lbl)
ix=W-40-16-iw; icy=y-ph/2-4
c.setFillColor(white); c.setStrokeColor(HexColor("#d8e0ea")); c.setLineWidth(1.3); c.roundRect(ix,icy-iw/2,iw,iw,10,fill=1,stroke=1)
img("cleaning",ix+iw/2,icy,iw-14)
c.setFillColor(INK); c.setFont("PopM",fz); yy=y-44
for ln in plines:
    if ln: c.drawString(62,yy,ln)
    yy-=18
y=y-ph-14
yc=card(40,y,W-80,y-30,GREEN,GREENT,"1","Read and answer","Read. Then answer the questions. Number 1 is done for you.")
_tf.n=1; _mc.n=6
cur=yc-12
_tf(cur,"Be neat at school and at home.","T",example=True); cur-=38
_tf(cur,"Put your books on the floor.","F"); cur-=36
_tf(cur,"A neat room is nice.","T"); cur-=36
_tf(cur,"You can find your things fast.","T"); cur-=36
_tf(cur,"Be neat only at school.","F"); cur-=46
_mc(cur,"Where do you put your books?",[("a","on the shelf"),("b","on the floor"),("c","in the trash")]); cur-=56
_mc(cur,"Where do you put your pens?",[("a","in the box"),("b","on the bed"),("c","in the sink")]); cur-=56
_mc(cur,"What do you clean?",[("a","your desk"),("b","the street"),("c","the car")]); cur-=56
_mc(cur,"A neat room is ______.",[("a","nice"),("b","bad"),("c","dirty")]); cur-=56
_mc(cur,"When are you neat?",[("a","every day"),("b","never"),("c","one day")]); cur-=50
c.setFillColor(INK)
c.showPage()

# ===================== PAGE 6 : Answer Key =====================
y=header("EOW2 · Unit 2",[("Answer ",NAVY),("Key",PINK)])
def keycard(y,color,tint,tag,label,lines):
    h=28+len(lines)*18+14
    yc=card(40,y,W-80,h,color,tint,tag,label)
    c.setFillColor(INK); c.setFont("PopM",12); yy=yc-6
    for ln in lines:
        c.drawString(60,yy,ln); yy-=18
    return y-h-12
y=keycard(y,PINK,PINKT,"A","Build the word from sound chunks",
    ["1. coloring  (c-o-l-or-ing)   2. counting  (c-ou-nt-ing)   3. cutting  (c-u-tt-ing)",
     "4. drawing  (dr-aw-ing)   5. gluing  (gl-u-ing)   6. talking  (t-al-k-ing)"])
y=keycard(y,BLUE,BLUET,"B","Find and circle the word",
    ["1. glue   2. marker   3. notebook   4. paintbrush   5. scissors"])
y=keycard(y,GREEN,GREENT,"1","We're + verb-ing",
    ["1. coloring   2. counting   3. cutting   4. drawing   5. gluing"])
y=keycard(y,PURPLE,PURPLET,"1","Are there...? (full answers)",
    ["1. Yes, there are. There are ten markers.   2. No, there aren't. There aren't any crayons.",
     "3. Yes, there are. There are four notebooks.   4. No, there aren't. There aren't any erasers.",
     "5. Yes, there are. There are five paintbrushes."])
y=keycard(y,GREEN,GREENT,"R","Paper Art (reading)",
    ["1. True   2. False   3. True   4. False   5. True",
     "6. b (a cat)   7. b (Mexico)   8. b (scissors)   9. b (flowers and animals)   10. a (paper)"])
y=keycard(y,GREEN,GREENT,"V","Be Neat (value reading)",
    ["1. True   2. False   3. True   4. True   5. False",
     "6. a (on the shelf)   7. a (in the box)   8. a (your desk)   9. a (nice)   10. a (every day)"])
c.setFillColor(GREY); c.setFont("Pop",10)
c.drawString(40,70,"Scope: EOW2 Unit 2 only.  Art: 09_Image_Library + GPT scenes.  Value: Be neat.")
c.showPage()
c.save(); print("done ->",OUT)
