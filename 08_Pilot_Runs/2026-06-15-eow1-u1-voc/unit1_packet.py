#!/usr/bin/env python3
"""EOW1 Unit 1 (My Classroom) — complete, fun, colourful worksheet packet.
Super Teacher Worksheets style. Color. Uses real art from 09_Image_Library.
Pages: Vocab1 trace, Vocab2 trace, Match, Circle, How many, What/Is it, Word Search, Answer Key.
"""
import os, random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

random.seed(11)
GF="/usr/share/fonts/truetype/google-fonts"
pdfmetrics.registerFont(TTFont("Pop",f"{GF}/Poppins-Regular.ttf"))
pdfmetrics.registerFont(TTFont("PopB",f"{GF}/Poppins-Bold.ttf"))
pdfmetrics.registerFont(TTFont("PopM",f"{GF}/Poppins-Medium.ttf"))

W,H=A4
INK=HexColor("#2b2b2b"); GREY=HexColor("#8a929b"); LINE=HexColor("#b9c2cc")
TRACE=HexColor("#d2dae3")
HERE=os.path.dirname(os.path.abspath(__file__))
LIB="/sessions/epic-confident-ride/mnt/PAS Curriculum Wiki/09_Image_Library/words"
PAL={"blue":"#3f8ed0","green":"#54b06a","orange":"#ef9b41","purple":"#8a6fc0",
     "teal":"#2fb3a8","pink":"#e87aa6","red":"#e36a5e","slate":"#6c7a89"}

c=canvas.Canvas(os.path.join(HERE,"EOW1 U1 My Classroom — Packet (color).pdf"),pagesize=A4)
V1=["clock","computer","crayon","map","paper","pen","pencil"]
V2=["book","chair","desk","eraser","picture"]
ALL=V1+V2

def img(word,x,y,s):
    c.drawImage(f"{LIB}/{word}/{word}-v1-color.png",x,y,s,s,preserveAspectRatio=True,mask='auto')
def star(x,y,r,col):
    c.setFillColor(HexColor(col))
    import math
    pts=[]
    for k in range(5):
        a=math.pi/2+k*2*math.pi/5; pts.append((x+math.cos(a)*r,y+math.sin(a)*r))
        a2=a+math.pi/5; pts.append((x+math.cos(a2)*r*0.45,y+math.sin(a2)*r*0.45))
    p=c.beginPath(); p.moveTo(*pts[0])
    for q in pts[1:]: p.lineTo(*q)
    p.close(); c.drawPath(p,fill=1,stroke=0)
def header(title,instr,col,page):
    c.setFillColor(white); c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(INK); c.setFont("Pop",11)
    c.drawString(40,H-46,"Name: _____________________")
    c.drawRightString(W-40,H-46,"Date: ____________")
    C=HexColor(PAL[col])
    c.setFillColor(C); c.roundRect(40,H-104,W-80,40,12,fill=1,stroke=0)
    star(60,H-84,9,"#ffffff"); star(W-60,H-84,9,"#ffffff")
    c.setFillColor(white); c.setFont("PopB",21); c.drawCentredString(W/2,H-92,title)
    c.setFillColor(GREY); c.setFont("PopM",11.5); c.drawCentredString(W/2,H-122,instr)
    return H-150
def footer(page):
    c.setFillColor(GREY); c.setFont("PopM",9.5)
    c.drawString(40,28,"EOW1 · Unit 1 · My Classroom")
    c.drawCentredString(W/2,28,"Work hard in school!")
    c.drawRightString(W-40,28,f"page {page}")
    c.setFillColor(INK)
def wordbank(words,col,y):
    C=HexColor(PAL[col])
    c.setStrokeColor(C); c.setLineWidth(1.6); c.setDash(2,3)
    c.roundRect(40,y-30,W-80,44,10,fill=0,stroke=1); c.setDash()
    c.setFillColor(C); c.setFont("PopB",10.5); c.drawString(52,y,"WORD BANK")
    c.setFillColor(INK); c.setFont("PopM",12.5); c.drawCentredString(W/2,y-18,"   ".join(words))

# ---- PAGE 1 & 2 : trace & write ----
def trace_page(words,title,col,page):
    y=header(title,"Look at the picture.  Trace the word.  Then write it.",col,page)
    wordbank(words,col,y);
    cols=2; gap=18; cw=(W-80-gap)/2; ch=112; top=y-54
    for i,wd in enumerate(words):
        cc=i%cols; r=i//cols; x=40+cc*(cw+gap); yy=top-r*(ch+12)
        c.setStrokeColor(HexColor("#e8eef5")); c.setLineWidth(1.4)
        c.roundRect(x,yy-ch,cw,ch,12,fill=0,stroke=1)
        img(wd,x+12,yy-ch+16,82)
        tx=x+108; avail=(x+cw-16)-tx; fs=30
        while fs>14 and pdfmetrics.stringWidth(wd,"PopB",fs)>avail: fs-=1
        c.setFillColor(TRACE); c.setFont("PopB",fs); c.drawString(tx,yy-44,wd)
        c.setStrokeColor(LINE); c.setLineWidth(1.3); c.setDash(3,3)
        c.line(tx,yy-ch+28,x+cw-16,yy-ch+28); c.setDash()
        c.setFillColor(GREY); c.setFont("Pop",9); c.drawString(tx,yy-ch+14,"write it"); c.setFillColor(INK)
    footer(page); c.showPage()

LETT="abcdefghijklmnopqrstuvwxyz"
def hw(x0,x1,y,gap=20):
    # 3-line primary handwriting ruling: bottom & top solid, middle dashed
    c.setStrokeColor(LINE); c.setLineWidth(1.2); c.setDash()
    c.line(x0,y,x1,y)            # baseline (solid)
    c.line(x0,y+gap,x1,y+gap)    # top line (solid)
    c.setStrokeColor(HexColor("#cdd6df")); c.setDash(2.5,3)
    c.line(x0,y+gap/2,x1,y+gap/2)  # mid line (dashed)
    c.setDash()
def hide(w):
    w=w.lower(); s=[random.choice(LETT) for _ in range(len(w)+4)]
    p=random.randint(0,len(s)-len(w)); s[p:p+len(w)]=list(w); return "  ".join(s)
def scramble(w):
    l=list(w)
    for _ in range(30):
        random.shuffle(l)
        if "".join(l)!=w: break
    return "  ".join(l)

def abc_page(page):
    y=header("ABC Order","Write the 12 words in ABC order (A to Z).","blue",page)
    sh=ALL[:]; random.shuffle(sh); wordbank(sh,"blue",y)
    top=y-62; rowh=46
    for i in range(12):
        col=0 if i<6 else 1; r=i%6; x=70+col*250; yy=top-r*rowh
        c.setFillColor(INK); c.setFont("PopB",13); c.drawString(x,yy-3,f"{i+1}.")
        hw(x+26,x+200,yy-8)
    footer(page); c.showPage()

def hunt_page(page):
    y=header("Word Hunt","Circle the word hidden in each row.","red",page)
    top=y-12; rowh=(top-70)/11
    for i,w in enumerate(ALL):
        cy=top-i*rowh
        c.setFillColor(INK); c.setFont("PopB",13); c.drawString(48,cy-4,f"{i+1}.")
        img(w,78,cy-18,30)
        c.setFont("PopM",14); c.drawString(118,cy-4,w)
        c.setFillColor(HexColor("#3a3a3a")); c.setFont("PopM",15.5); c.drawString(235,cy-4,hide(w))
    footer(page); c.showPage()

def scram_page(page):
    y=header("Scrambled Spelling","Unscramble the letters. Write the word.","orange",page)
    top=y-22; rowh=66
    for i,w in enumerate(ALL):
        col=0 if i<6 else 1; r=i%6; x=64+col*250; yy=top-r*rowh
        c.setFillColor(INK); c.setFont("PopB",14); c.drawString(x,yy,f"{i+1}.")
        c.setFillColor(HexColor("#444")); c.setFont("PopM",15); c.drawString(x+30,yy,scramble(w))
        hw(x+30,x+205,yy-18)
    wordbank(sorted(ALL),"orange",104)
    footer(page); c.showPage()

def write_twice_page(page):
    y=header("Write It Twice","Write each word two times in your best handwriting.","green",page)
    top=y-14; rowh=(top-58)/(len(ALL)-1)
    for i,w in enumerate(ALL):
        cy=top-i*rowh
        c.setFillColor(INK); c.setFont("PopB",13); c.drawString(48,cy-4,f"{i+1}.")
        img(w,76,cy-16,28)
        c.setFillColor(INK); c.setFont("PopM",16); c.drawString(116,cy-4,w)
        hw(210,360,cy-8); hw(382,540,cy-8)
    footer(page); c.showPage()

write_twice_page(1)
abc_page(2)
hunt_page(3)
scram_page(4)

# ---- PAGE 3 : Match ----
def match_page(page):
    y=header("Match It!","Draw a line from each picture to its word.","orange",page)
    pics=ALL[:]; random.shuffle(pics)
    words=ALL[:]; random.shuffle(words)
    n=len(ALL); top=y-6; row=(top-70)/ (n-1)
    for i in range(n):
        cy=top-i*row
        img(pics[i],90,cy-20,40)
        c.setFillColor(INK); c.circle(210,cy,3.2,fill=1,stroke=0)
        c.circle(360,cy,3.2,fill=1,stroke=0)
        c.setFont("PopM",14); c.drawString(385,cy-5,words[i])
    footer(page); c.showPage()
    return pics,words
mp_pics,mp_words=match_page(5)

# ---- PAGE 4 : Circle the word ----
def circle_page(page):
    y=header("Circle the Word","Look at the picture. Circle the correct word.","purple",page)
    items=[("clock","clock","crayon"),("computer","computer","chair"),("desk","desk","book"),
           ("pen","pen","pencil"),("eraser","eraser","paper"),("map","map","picture"),
           ("crayon","crayon","clock"),("chair","chair","desk")]
    cols=2; gap=18; cw=(W-80-gap)/2; ch=96; top=y-10
    for i,(pic,a,b) in enumerate(items):
        cc=i%cols; r=i//cols; x=40+cc*(cw+gap); yy=top-r*(ch+12)
        c.setStrokeColor(HexColor("#ece7f5")); c.setLineWidth(1.4); c.roundRect(x,yy-ch,cw,ch,12,fill=0,stroke=1)
        img(pic,x+10,yy-ch+14,70)
        c.setFillColor(INK); c.setFont("PopM",15); c.drawString(x+96,yy-ch/2-5,f"{a}    {b}")
    footer(page); c.showPage()
circle_page(6)

# ---- PAGE 5 : How many ----
def howmany_page(page):
    y=header("Count and Write","Count the pictures. Write how many.","teal",page)
    wordbank(["one","two","three","four","five"],"teal",y); top=y-56
    items=[("book",3),("pencil",5),("crayon",2),("chair",4),("clock",1)]
    rowh=84
    for i,(pic,nq) in enumerate(items):
        cy=top-i*rowh
        for k in range(nq): img(pic,52+k*60,cy-26,52)
        c.setFillColor(INK); c.setFont("PopM",14.5); c.drawString(380,cy-2,f"How many {pic}s?")
        c.setStrokeColor(LINE); c.setLineWidth(1.3); c.setDash(3,3); c.line(382,cy-20,560,cy-20); c.setDash()
    footer(page); c.showPage()
howmany_page(7)

# ---- PAGE 6 : What is it / Is it ----
def whatis_page(page):
    y=header("What Is It?","Write the word. Then circle Yes or No.","pink",page)
    P=HexColor(PAL["pink"])
    # Section A
    c.setFillColor(P); c.setFont("PopB",13.5); c.drawString(40,y,"A.   What is it?   Write:  It is a ________.")
    c.setFillColor(INK)
    wi=[("clock","clock"),("desk","desk"),("map","map")]
    topA=y-52; rowh=60
    for i,(pic,ans) in enumerate(wi):
        cy=topA-i*rowh; img(pic,48,cy-24,48); c.setFillColor(INK); c.setFont("PopM",14); c.drawString(112,cy-4,"It is a")
        c.setStrokeColor(LINE); c.setLineWidth(1.3); c.setDash(3,3); c.line(176,cy-8,380,cy-8); c.setDash()
    yB=topA-(len(wi)-1)*rowh-44
    # Section B
    c.setFillColor(P); c.setFont("PopB",13.5); c.drawString(40,yB,"B.   Is it a ___?   Circle Yes or No.")
    c.setFillColor(INK)
    isit=[("pen","Is it a pen?"),("book","Is it a chair?"),("computer","Is it a computer?"),("clock","Is it a map?")]
    topB=yB-52; rowh2=58
    for i,(pic,q) in enumerate(isit):
        cy=topB-i*rowh2; img(pic,48,cy-24,48); c.setFillColor(INK); c.setFont("PopM",14); c.drawString(112,cy-6,q)
        c.setFont("PopB",14); c.drawString(380,cy-6,"Yes"); c.drawString(450,cy-6,"No")
        c.setStrokeColor(HexColor("#cfd6de")); c.setLineWidth(1.2)
        c.circle(392,cy-1,16,fill=0,stroke=1); c.circle(459,cy-1,16,fill=0,stroke=1)
    footer(page); c.showPage()
whatis_page(8)

# ---- PAGE 7 : Word Search ----
def wordsearch_page(page):
    y=header("Word Search","Find and circle the 12 classroom words!","red",page)
    N=13; grid=[[None]*N for _ in range(N)]
    dirs=[(1,0),(0,1),(1,1)]
    def place(w):
        w=w.upper()
        for _ in range(300):
            d=random.choice(dirs); dx,dy=d
            x=random.randint(0,N-1-(dx*(len(w)-1))); yy=random.randint(0,N-1-(dy*(len(w)-1)))
            ok=True
            for k in range(len(w)):
                cx,cy=x+dx*k,yy+dy*k
                if grid[cy][cx] not in (None,w[k]): ok=False; break
            if ok:
                for k in range(len(w)):
                    grid[yy+dy*k][x+dx*k]=w[k]
                return True
        return False
    for w in sorted(ALL,key=len,reverse=True): place(w)
    import string
    for r in range(N):
        for col in range(N):
            if grid[r][col] is None: grid[r][col]=random.choice(string.ascii_uppercase)
    # draw grid
    gx,gy0=70,y-12; cell=30
    c.setFont("PopM",14)
    for r in range(N):
        for col in range(N):
            cx=gx+col*cell; cy=gy0-r*cell
            c.setFillColor(INK); c.drawCentredString(cx+cell/2,cy-cell+9,grid[r][col])
    # word list WITH pictures (uses the empty space below the grid)
    ly=gy0-N*cell-26
    c.setFillColor(HexColor(PAL["red"])); c.setFont("PopB",12); c.drawString(50,ly,"FIND THESE WORDS:")
    cols=3; cw=172; iconS=34; rowh=52; sx=52; sy=ly-30
    for i,w in enumerate(ALL):
        cc=i%cols; rr=i//cols
        x=sx+cc*cw; yy=sy-rr*rowh
        # checkbox
        c.setStrokeColor(HexColor(PAL["red"])); c.setLineWidth(1.3)
        c.roundRect(x,yy-iconS+8,14,14,3,fill=0,stroke=1)
        # picture
        img(w, x+22, yy-iconS+2, iconS)
        # word
        c.setFillColor(INK); c.setFont("PopM",13)
        c.drawString(x+22+iconS+8, yy-iconS/2-1, w)
    footer(page); c.showPage()
wordsearch_page(9)

def reading_page(page):
    y=header("Read and Answer","Read the story. Then answer the questions.","teal",page)
    # passage box
    px0,px1=40,W-40; ptop=y; ph=150
    c.setFillColor(HexColor("#eef7f6")); c.setStrokeColor(HexColor(PAL["teal"])); c.setLineWidth(1.4)
    c.roundRect(px0,ptop-ph,px1-px0,ph,12,fill=1,stroke=1)
    c.setFillColor(HexColor(PAL["teal"])); c.setFont("PopB",16); c.drawString(px0+18,ptop-26,"My Classroom")
    passage=["Look at my classroom!","It is a desk.  It is a chair.",
             "It is a pen.  It is a book.","What is it?  It is a clock.","Work hard in school!"]
    c.setFillColor(INK); c.setFont("PopM",14)
    for i,ln in enumerate(passage):
        c.drawString(px0+18, ptop-52-i*20, ln)
    img("desk",px1-150,ptop-ph+18,60); img("clock",px1-80,ptop-ph+18,60)
    # questions
    qy=ptop-ph-30
    c.setFillColor(INK); c.setFont("PopB",13); c.drawString(44,qy,"1.  The story is about a ...")
    c.setFont("PopM",13)
    for j,(lab,opt) in enumerate([("a","park"),("b","classroom"),("c","kitchen")]):
        c.drawString(80,qy-22-j*20,f"{lab}.  {opt}")
    qy2=qy-90
    c.setFont("PopB",13); c.drawString(44,qy2,"2.  What is it?"); img("clock",250,qy2-10,34)
    c.setFont("PopM",13); c.drawString(90,qy2-26,"It is a"); hw(150,360,qy2-30)
    qy3=qy2-66
    c.setFont("PopB",13); c.drawString(44,qy3,"3.  Is it a book?"); img("book",250,qy3-10,34)
    c.setFont("PopB",14); c.drawString(320,qy3-4,"Yes"); c.drawString(400,qy3-4,"No")
    c.setStrokeColor(HexColor("#cfd6de")); c.setLineWidth(1.2)
    c.circle(333,qy3,16,fill=0,stroke=1); c.circle(409,qy3,16,fill=0,stroke=1)
    footer(page); c.showPage()
reading_page(10)

def answer_page(page):
    y=header("Answer Key","For the teacher.","slate",page)
    c.setFillColor(INK); c.setFont("PopM",11.5); yy=y-2
    lines=[
      "Write It Twice: copy each word two times.",
      "ABC Order: book, chair, clock, computer, crayon, desk, eraser, map, paper, pen, pencil, picture.",
      "Word Hunt: circle each word inside its letter row.",
      "Scrambled Spelling: clock, computer, crayon, map, paper, pen, pencil, book, chair, desk, eraser, picture.",
      "Match It!: each picture connects to its own word.",
      "Circle the Word: 1 clock  2 computer  3 desk  4 pen  5 eraser  6 map  7 crayon  8 chair.",
      "Count and Write: 1 three books  2 five pencils  3 two crayons  4 four chairs  5 one clock.",
      "What is it?: A1 It is a clock.  A2 It is a desk.  A3 It is a map.   Is it: B1 Yes  B2 No  B3 Yes  B4 No.",
      "Word Search: all 12 unit words are hidden (across / down / diagonal).",
      "Read and Answer: 1 b (classroom)   2 It is a clock.   3 Yes.",
    ]
    for ln in lines:
        c.drawString(44,yy,ln); yy-=21
    c.setFillColor(GREY); c.setFont("Pop",10)
    c.drawString(44,yy-6,"Patterns: WS-001/002/003/006/016/018/019/020/023.  Scope: EOW1 Unit 1 only (passage is original, in-scope).")
    c.drawString(44,yy-22,"Art: 09_Image_Library (hand-drawn).  Number words for How many are unavoidable for the task.")
    footer(page); c.showPage()
answer_page(11)

c.save(); print("saved packet")
