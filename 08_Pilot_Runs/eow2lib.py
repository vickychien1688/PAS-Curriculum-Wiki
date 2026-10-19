#!/usr/bin/env python3
"""Shared library for EOW2 colourful 'Lesson-series' worksheets.
House style: rounded frame, lesson badge, big coloured title, crown Rule Box,
coloured title-tab cards, star/pencil decor. Soft palette, Poppins, NO footer.
Single-line handwriting (no tracing). Activity variety via the renderers below.
Art = 09_Image_Library single icons (watercolour). Scenes optional (scenes/<name>.png).
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
TINT={PINK:PINKT, BLUE:BLUET, GREEN:GREENT, ORANGE:ORANGET, PURPLE:PURPLET}

LIB=None; CACHE=None; SCENES=None; C=None  # set by setup()

def setup(here, out_name, lib_rel=("..","..","09_Image_Library","words")):
    global LIB,CACHE,SCENES,C,OUT
    LIB=os.path.normpath(os.path.join(here,*lib_rel))
    SCENES=os.path.join(here,"scenes")
    CACHE=os.path.join(here,"_trans"); os.makedirs(CACHE,exist_ok=True)
    OUT=os.path.join(here,out_name)
    C=canvas.Canvas(OUT,pagesize=A4)
    return C

def save():
    C.save(); print("done ->",OUT)

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

def img(word,cx,cy,s):
    C.drawImage(transparent(word),cx-s/2,cy-s/2,s,s,preserveAspectRatio=True,mask='auto')

# ---------- decorations ----------
def star(cx,cy,r,fill=GOLD,stroke=None):
    pts=[]
    for k in range(5):
        a=math.radians(-90+k*72); pts.append((cx+math.cos(a)*r,cy+math.sin(a)*r))
        a2=math.radians(-90+k*72+36); pts.append((cx+math.cos(a2)*r*0.45,cy+math.sin(a2)*r*0.45))
    p=C.beginPath(); p.moveTo(*pts[0])
    for q in pts[1:]: p.lineTo(*q)
    p.close(); C.setFillColor(fill)
    if stroke: C.setStrokeColor(stroke); C.setLineWidth(1.4); C.drawPath(p,fill=1,stroke=1)
    else: C.drawPath(p,fill=1,stroke=0)
    C.setFillColor(INK)

def crown(cx,cy,s):
    C.setFillColor(GOLD); base_y=cy-s*0.28
    p=C.beginPath(); p.moveTo(cx-s*0.5,base_y)
    p.lineTo(cx-s*0.5,cy+s*0.05); p.lineTo(cx-s*0.25,cy-s*0.15); p.lineTo(cx,cy+s*0.28)
    p.lineTo(cx+s*0.25,cy-s*0.15); p.lineTo(cx+s*0.5,cy+s*0.05); p.lineTo(cx+s*0.5,base_y); p.close()
    C.drawPath(p,fill=1,stroke=0)
    C.setFillColor(HexColor("#f0a500")); C.roundRect(cx-s*0.5,base_y-s*0.16,s,s*0.18,2,fill=1,stroke=0)
    for dx,col in ((-0.25,RED),(0.0,BLUE),(0.25,GREEN)):
        C.setFillColor(col); C.circle(cx+dx*s,cy+s*0.02,s*0.07,fill=1,stroke=0)
    C.setFillColor(INK)

def pencil(cx,cy,s,ang=0):
    C.saveState(); C.translate(cx,cy); C.rotate(ang)
    C.setFillColor(HexColor("#f4c430")); C.roundRect(-s*0.5,-s*0.12,s*0.8,s*0.24,3,fill=1,stroke=0)
    C.setFillColor(HexColor("#f0a8b8")); C.roundRect(-s*0.62,-s*0.12,s*0.13,s*0.24,3,fill=1,stroke=0)
    p=C.beginPath(); p.moveTo(s*0.3,-s*0.12); p.lineTo(s*0.5,0); p.lineTo(s*0.3,s*0.12); p.close()
    C.setFillColor(HexColor("#f0d8a0")); C.drawPath(p,fill=1,stroke=0)
    p=C.beginPath(); p.moveTo(s*0.44,-s*0.05); p.lineTo(s*0.5,0); p.lineTo(s*0.44,s*0.05); p.close()
    C.setFillColor(INK); C.drawPath(p,fill=1,stroke=0); C.restoreState(); C.setFillColor(INK)

def page_frame():
    C.setFillColor(BG); C.rect(0,0,W,H,fill=1,stroke=0)
    C.setStrokeColor(HexColor("#d9c9a8")); C.setLineWidth(2); C.setDash(1,0)
    C.roundRect(16,16,W-32,H-32,18,fill=0,stroke=1)

def lesson_badge(x,y,text,col=PURPLE):
    tw=pdfmetrics.stringWidth(text,"PopB",10.5)
    star(x+8,y,9,fill=GOLD,stroke=HexColor("#e0a800"))
    C.setFillColor(col); C.roundRect(x+20,y-11,tw+26,22,11,fill=1,stroke=0)
    C.setFillColor(white); C.setFont("PopB",10.5); C.drawString(x+34,y-4,text)
    C.setFillColor(INK); return x+20+tw+26

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
        C.setFillColor(col); C.setFont("PopB",fs); C.drawString(x,H-54,t); x+=pdfmetrics.stringWidth(t,"PopB",fs)
    C.setFillColor(INK); return H-92

def card(x,y,w,h,color,n,label,instr=""):
    tint=TINT.get(color,PINKT)
    C.setFillColor(tint); C.roundRect(x,y-h,w,h,16,fill=1,stroke=0)
    C.setStrokeColor(color); C.setLineWidth(1.1); C.setDash(1,0); C.roundRect(x,y-h,w,h,16,fill=0,stroke=1)
    lw=pdfmetrics.stringWidth(label,"PopB",13.5); hbw=lw+(66 if n else 32)
    C.setFillColor(color); C.roundRect(x+16,y-14,hbw,28,14,fill=1,stroke=0)
    if n:
        C.setFillColor(white); C.circle(x+34,y,11,fill=1,stroke=0)
        C.setFillColor(color); C.setFont("PopB",12); C.drawCentredString(x+34,y-4,str(n)); tx=x+50
    else: tx=x+30
    C.setFillColor(white); C.setFont("PopB",13.5); C.drawString(tx,y-4.5,label)
    cy=y-30
    if instr:
        C.setFillColor(GREY); C.setFont("PopM",10.5); C.drawString(x+20,y-26,instr); cy=y-44
    C.setFillColor(INK); return cy

def wline(x0,x1,base):
    C.setStrokeColor(LBLUE); C.setLineWidth(1.5); C.setDash(1,0); C.line(x0,base,x1,base)
    C.setStrokeColor(INK)

def wordbox(x,y,w,words,color,title="Word Box"):
    h=44
    C.setFillColor(white); C.setStrokeColor(color); C.setLineWidth(1.4); C.setDash(1,0)
    C.roundRect(x,y-h,w,h,12,fill=1,stroke=1)
    C.setFillColor(color); C.setFont("PopB",11); C.drawString(x+14,y-16,title)
    C.setFillColor(NAVY); C.setFont("PopSB",13); C.drawCentredString(x+w/2, y-36, "    ".join(words))
    C.setFillColor(INK); return h

def rule_box(y, segs, sub=None):
    """Crown rule box. segs = [(text,color),...] on line 1; sub = grey line 2."""
    hh=58 if sub else 44
    C.setFillColor(CREAM); C.setStrokeColor(GOLD); C.setLineWidth(1.6); C.roundRect(40,y-hh,W-80,hh,12,fill=1,stroke=1)
    crown(72,y-hh/2,30)
    C.setFillColor(NAVY); C.setFont("PopB",13); C.drawString(100,y-20,"Rule")
    x=150
    for t,col in segs:
        C.setFillColor(col); C.setFont("PopSB",12.5); C.drawString(x,y-20,t); x+=pdfmetrics.stringWidth(t,"PopSB",12.5)+10
    if sub:
        C.setFillColor(GREY); C.setFont("PopM",10.5); C.drawString(150,y-40,sub)
    C.setFillColor(INK); return y-hh-14

# ---------- phonics chunking ----------
def split_chunks(word):
    """Heuristic phonics chunks: onset blend / vowel(team) / final cons / -ing,-y.
    Override via CHUNKS dict where needed for accuracy."""
    if word in CHUNKS: return CHUNKS[word]
    return list(word)  # fallback: letters (callers should provide CHUNKS)
CHUNKS={}

def scramble_order(items, seed):
    if len(items)<2: return items
    r=random.Random(seed)
    for _ in range(30):
        s=items[:]; r.shuffle(s)
        if s!=items: return s
    return items[::-1]

# ================= RENDERERS (draw inside a card you already opened) =================
def R_match(yc, ybot, rows, color, picx=118, dotx2=None, seed=7, frame=False, picsize=46):
    """rows=[(slug, word_text)]. Pictures (in order) on the left, words SHUFFLED on the
    right so the child must draw connecting lines (a real matching task, not a labelled list).
    frame=True boxes each picture (for full-bleed scene icons)."""
    if dotx2 is None: dotx2=W-250
    pics=[r[0] for r in rows]; words=[r[1] for r in rows]
    swords=scramble_order(words, seed)
    n=len(rows); pitch=(yc-6-(ybot+12))/n; top=yc-6
    for i in range(n):
        cy=top-pitch*(i+0.5)
        if frame:
            s=picsize+10; C.setFillColor(white); C.setStrokeColor(HexColor("#d8e0ea")); C.setLineWidth(1.3)
            C.roundRect(picx-s/2,cy-s/2,s,s,8,fill=1,stroke=1)
        img(pics[i],picx,cy,picsize)
        C.setFillColor(color); C.circle(picx+60,cy,4.5,fill=1,stroke=0); C.circle(dotx2,cy,4.5,fill=1,stroke=0)
        word=swords[i]; tw=pdfmetrics.stringWidth(word,"PopSB",13)
        C.setFillColor(white); C.setStrokeColor(color); C.setLineWidth(1.4); C.roundRect(W-236,cy-13,tw+26,26,8,fill=1,stroke=1)
        C.setFillColor(NAVY); C.setFont("PopSB",13); C.drawString(W-223,cy-4,word)
    C.setFillColor(INK)

def R_circle(yc, ybot, rows, color, optx=(225,345,460), frame=False, picsize=50):
    """rows=[(slug,[opt1,opt2,opt3])]. picture + 3 word options to circle.
    frame=True draws a white rounded border around each picture (use for full-bleed
    scene icons like sky/time-of-day so they don't merge into one strip)."""
    n=len(rows); top=yc-2; pitch=(top-(ybot+12))/n
    for i,(slug,opts) in enumerate(rows):
        cy=top-pitch*(i+0.5)
        C.setFillColor(color); C.circle(70,cy,11,fill=1,stroke=0)
        C.setFillColor(white); C.setFont("PopB",12); C.drawCentredString(70,cy-4,str(i+1))
        if frame:
            s=picsize+10
            C.setFillColor(white); C.setStrokeColor(HexColor("#d8e0ea")); C.setLineWidth(1.3)
            C.roundRect(128-s/2,cy-s/2,s,s,8,fill=1,stroke=1)
        img(slug,128,cy,picsize)
        C.setFont("PopSB",14)
        for k,opt in enumerate(opts):
            C.setFillColor(NAVY); C.drawString(optx[k],cy-5,opt)
    C.setFillColor(INK)

def R_write(yc, ybot, rows, color, prefix="", suffix=".", picsize=70, prefix_font=15):
    """rows=[(slug, answer_or_None)]. picture + 'prefix ____ suffix' handwriting line.
    If answer given and it's row 0 we mark example."""
    n=len(rows); top=yc-6; pitch=(top-(ybot+8))/n
    for i,(slug,ans) in enumerate(rows):
        cy=top-pitch*(i+0.5)
        C.setFillColor(color); C.circle(66,cy,12,fill=1,stroke=0)
        C.setFillColor(white); C.setFont("PopB",12); C.drawCentredString(66,cy-4,str(i+1))
        img(slug,118,cy,picsize)
        tx=170; C.setFillColor(NAVY); C.setFont("PopSB",prefix_font)
        if prefix: C.drawString(tx,cy-5,prefix)
        sx=tx+pdfmetrics.stringWidth(prefix+" ","PopSB",prefix_font)
        wline(sx,W-150,cy-9)
        if suffix:
            C.setFillColor(NAVY); C.setFont("PopSB",prefix_font); C.drawString(W-144,cy-5,suffix)
        if i==0 and ans:
            C.setFillColor(GREEN); C.setFont("PopSB",prefix_font); C.drawString(sx+6,cy-5,ans)
            C.setFillColor(GREY); C.setFont("PopM",8.5); C.drawString(sx+6,cy-20,"(example)")
    C.setFillColor(INK)

def R_cloze(yc, ybot, rows, color, picsize=64):
    """rows=[(slug, before, after, ans)]. picture + 'before ___ after' line; row0 example."""
    n=len(rows); top=yc-6; pitch=(top-(ybot+8))/n
    for i,(slug,before,after,ans) in enumerate(rows):
        cy=top-pitch*(i+0.5)
        C.setFillColor(color); C.circle(66,cy,12,fill=1,stroke=0)
        C.setFillColor(white); C.setFont("PopB",12); C.drawCentredString(66,cy-4,str(i+1))
        img(slug,116,cy,picsize)
        tx=168; C.setFillColor(NAVY); C.setFont("PopSB",14); C.drawString(tx,cy-5,before)
        sx=tx+pdfmetrics.stringWidth(before+" ","PopSB",14)
        linew=92
        wline(sx,sx+linew,cy-9)
        ax=sx+linew+8
        if after: C.setFillColor(NAVY); C.setFont("PopSB",14); C.drawString(ax,cy-5,after)
        if i==0 and ans:
            C.setFillColor(GREEN); C.setFont("PopSB",14); C.drawCentredString(sx+linew/2,cy-5,ans)
            C.setFillColor(GREY); C.setFont("PopM",8.5); C.drawString(sx,cy-20,"(example)")
    C.setFillColor(INK)

def R_phonics(yc, ybot, words, color, seed0=11, picsize=46):
    """rows of words: picture + scrambled phonics-chunk tiles + write line."""
    n=len(words); top=yc-6; pitch=(top-(ybot+8))/n
    for i,wd in enumerate(words):
        cy=top-pitch*(i+0.5)
        C.setFillColor(color); C.circle(70,cy,11,fill=1,stroke=0)
        C.setFillColor(white); C.setFont("PopB",12); C.drawCentredString(70,cy-4,str(i+1))
        img(wd,120,cy,picsize)
        chunks=scramble_order(split_chunks(wd),seed0+i)
        tx=168
        for ch in chunks:
            lab=ch.lower(); tw=pdfmetrics.stringWidth(lab,"PopB",14)
            C.setFillColor(white); C.setStrokeColor(ORANGE); C.setLineWidth(1.4); C.roundRect(tx,cy-13,tw+18,26,7,fill=1,stroke=1)
            C.setFillColor(ORANGE); C.setFont("PopB",14); C.drawString(tx+9,cy-5,lab); tx+=tw+18+8
        wline(tx+10,W-70,cy-8)
    C.setFillColor(INK)

def R_wordhunt(yc, ybot, rows, color, picsize=48):
    """rows=[(slug, letterstring)] circle the word."""
    n=len(rows); top=yc-2; pitch=(top-(ybot+12))/n
    for i,(slug,strg) in enumerate(rows):
        cy=top-pitch*(i+0.5)
        C.setFillColor(color); C.circle(70,cy,11,fill=1,stroke=0)
        C.setFillColor(white); C.setFont("PopB",12); C.drawCentredString(70,cy-4,str(i+1))
        img(slug,124,cy,picsize)
        C.setFillColor(NAVY); C.setFont("PopB",17); C.drawString(186,cy-6,strg.lower())
    C.setFillColor(INK)

def R_unscramble(yc, ybot, rows, color, picsize=70):
    """rows=[(slug, [tokens], end_hint)]. word tiles to reorder + handwriting line."""
    n=len(rows); top=yc-4; pitch=(top-(ybot+8))/n
    for i,(slug,toks,end) in enumerate(rows):
        cmid=top-pitch*(i+0.5)
        C.setFillColor(color); C.circle(66,cmid,12,fill=1,stroke=0)
        C.setFillColor(white); C.setFont("PopB",12); C.drawCentredString(66,cmid-4,str(i+1))
        if slug: img(slug,108,cmid,picsize)
        cx=158; C.setFont("PopSB",12.5)
        for t in toks:
            tw=pdfmetrics.stringWidth(t,"PopSB",12.5)
            C.setFillColor(white); C.setStrokeColor(color); C.setLineWidth(1.3); C.roundRect(cx,cmid+8,tw+16,24,7,fill=1,stroke=1)
            C.setFillColor(NAVY); C.drawString(cx+8,cmid+15,t); cx+=tw+16+7
        wline(158,W-86,cmid-22)
        if end:
            C.setStrokeColor(color); C.setLineWidth(1.2); C.setDash(2,2); C.roundRect(W-78,cmid-27,24,26,5,fill=0,stroke=1); C.setDash(1,0)
            C.setFillColor(GREY); C.setFont("Pop",8); C.drawCentredString(W-66,cmid-37,end); C.setFillColor(INK)
    C.setFillColor(INK)

def R_mc(yc, ybot, rows, color, picslug_size=58):
    """rows=[(prompt, [(label,text)...], ans_label, slug_or_None)]. text prompt + lettered choices."""
    n=len(rows); top=yc-4; pitch=(top-(ybot+8))/n
    for i,(prompt,opts,ans,slug) in enumerate(rows):
        blk=top-pitch*i; qy=blk-18
        C.setFillColor(color); C.circle(66,qy,11,fill=1,stroke=0)
        C.setFillColor(white); C.setFont("PopB",12); C.drawCentredString(66,qy-4,str(i+1))
        if slug: img(slug,108,qy,picslug_size)
        C.setFillColor(NAVY); C.setFont("PopSB",13.5); C.drawString(150 if slug else 90,qy-5,prompt)
        oy=qy-30; ox=150 if slug else 90
        for lab,txt in opts:
            s=f"{lab}) {txt}"; tw=pdfmetrics.stringWidth(s,"PopSB",12)
            C.setFillColor(white); C.setStrokeColor(color); C.setLineWidth(1.2); C.roundRect(ox,oy-13,tw+18,24,11,fill=1,stroke=1)
            C.setFillColor(NAVY); C.setFont("PopSB",12); C.drawString(ox+9,oy-5,s); ox+=tw+18+12
    C.setFillColor(INK)

def R_qa_write(yc, ybot, rows, color, picsize=66):
    """Two-line Q&A handwriting: rows=[(question, answer, slug_or_None)]. row0 example.
    Roomy gap between question and its write line (Vicky pref)."""
    n=len(rows); top=yc-2; bot=ybot; pitch=(top-bot)/n
    for i,(q,ans,slug) in enumerate(rows):
        blk=top-pitch*i; qy=blk-18
        C.setFillColor(color); C.circle(66,qy,11,fill=1,stroke=0)
        C.setFillColor(white); C.setFont("PopB",12); C.drawCentredString(66,qy-4,str(i+1))
        if slug: img(slug,110,qy,picsize); qx=150
        else: qx=90
        C.setFillColor(NAVY); C.setFont("PopSB",13.5); C.drawString(qx,qy-5,q)
        ly=blk-pitch+22
        wline(90,W-70,ly)
        if i==0 and ans:
            C.setFillColor(GREEN); C.setFont("PopSB",13.5); C.drawString(96,ly+5,ans)
            C.setFillColor(GREY); C.setFont("PopM",9); C.drawString(W-150,ly+5,"(example)")
    C.setFillColor(INK)

def R_truefalse(yc, ybot, rows, color, picsize=58):
    """rows=[(statement, 'T'|'F', slug_or_None)]. statement + True/False chips to circle."""
    n=len(rows); top=yc-2; pitch=(top-(ybot+12))/n
    for i,(stmt,ans,slug) in enumerate(rows):
        cy=top-pitch*(i+0.5)
        C.setFillColor(color); C.circle(66,cy,11,fill=1,stroke=0)
        C.setFillColor(white); C.setFont("PopB",12); C.drawCentredString(66,cy-4,str(i+1))
        if slug: img(slug,112,cy,picsize); sx=150
        else: sx=90
        C.setFillColor(NAVY); C.setFont("PopSB",13.5); C.drawString(sx,cy-5,stmt)
        ax=W-220
        for opt,col in (("True",GREEN),("False",RED)):
            tw=pdfmetrics.stringWidth(opt,"PopSB",12)
            C.setFillColor(white); C.setStrokeColor(col); C.setLineWidth(1.3); C.roundRect(ax,cy-12,tw+18,24,12,fill=1,stroke=1)
            C.setFillColor(col); C.setFont("PopSB",12); C.drawString(ax+9,cy-4,opt); ax+=tw+18+12
    C.setFillColor(INK)

def clock(cx,cy,r,hour,minute=0):
    C.setFillColor(white); C.setStrokeColor(NAVY); C.setLineWidth(2.4); C.circle(cx,cy,r,fill=1,stroke=1)
    for h in range(12):
        a=math.radians(90-h*30); x1=cx+math.cos(a)*(r-6); y1=cy+math.sin(a)*(r-6); x2=cx+math.cos(a)*(r-2); y2=cy+math.sin(a)*(r-2)
        C.setStrokeColor(NAVY); C.setLineWidth(1.4); C.line(x1,y1,x2,y2)
    C.setFillColor(NAVY)
    # hour hand
    ah=math.radians(90-(hour%12+minute/60)*30); C.setLineWidth(3.2); C.setStrokeColor(NAVY)
    C.line(cx,cy,cx+math.cos(ah)*r*0.5,cy+math.sin(ah)*r*0.5)
    am=math.radians(90-(minute/60)*360); C.setLineWidth(2)
    C.line(cx,cy,cx+math.cos(am)*r*0.78,cy+math.sin(am)*r*0.78)
    C.circle(cx,cy,3,fill=1,stroke=0); C.setFillColor(INK)

def wrap_text(text, font, size, maxw):
    words=text.split(); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if pdfmetrics.stringWidth(t,font,size)<=maxw: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def passage_box(x,y,w,title,paragraphs,color,fontsize=12.5,lead=18):
    """Draw a reading passage in a rounded box. paragraphs = list of strings.
    Returns the y just below the box."""
    inner=w-44
    lines=[]
    for p in paragraphs:
        lines+=wrap_text(p,"PopM",fontsize,inner); lines.append("")
    if lines and lines[-1]=="": lines.pop()
    h=30+len(lines)*lead+18
    tint=TINT.get(color,CREAM)
    C.setFillColor(tint); C.roundRect(x,y-h,w,h,14,fill=1,stroke=0)
    C.setStrokeColor(color); C.setLineWidth(1.2); C.setDash(1,0); C.roundRect(x,y-h,w,h,14,fill=0,stroke=1)
    tw=pdfmetrics.stringWidth(title,"PopB",13.5)
    C.setFillColor(color); C.roundRect(x+16,y-14,tw+30,28,14,fill=1,stroke=0)
    C.setFillColor(white); C.setFont("PopB",13.5); C.drawString(x+30,y-4.5,title)
    C.setFillColor(INK); C.setFont("PopM",fontsize); yy=y-38
    for ln in lines:
        if ln: C.drawString(x+22,yy,ln)
        yy-=lead
    return y-h-14

def answer_key(unit_badge, blocks, footer_note):
    """blocks=[(color,tag,label,[lines])]."""
    y=header(unit_badge,[("Answer ",NAVY),("Key",PINK)])
    for color,tag,label,lines in blocks:
        h=28+len(lines)*18+14
        yc=card(40,y,W-80,h,color,tag,label)
        C.setFillColor(INK); C.setFont("PopM",12); yy=yc-6
        for ln in lines: C.drawString(60,yy,ln); yy-=18
        y=y-h-12
    C.setFillColor(GREY); C.setFont("Pop",10); C.drawString(40,70,footer_note)
    C.showPage()
