#!/usr/bin/env python3
"""EOW2 U8 Awesome Animals — colourful worksheet.
Variety mix: P1 word hunt (animals) + match (animal parts);
P2 can/can't True-False; P3 'Does ... have ...?' Yes/No Q&A; P4 key.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import eow2lib as L
from eow2lib import (W,H,NAVY,PINK,BLUE,GREEN,ORANGE,PURPLE,GREY,RED)

HERE=os.path.dirname(os.path.abspath(__file__))
C=L.setup(HERE,"EOW2 U8 Awesome Animals (colorful).pdf")
BADGE="EOW2 · Unit 8"

# ---------------- Page 1: Vocabulary ----------------
y=L.header(BADGE,[("Awesome ",NAVY),("Animals",ORANGE)])
aTop=y; aH=400; aBot=aTop-aH
yc=L.card(40,aTop,W-80,aH,PINK,"A","Find and circle the animal","Each line hides one animal. Circle the word you see.")
L.R_wordhunt(yc,aBot+8,[("lion","k l i o n e"),("tiger","p t i g e r s"),("zebra","u z e b r a m"),
                        ("panda","x p a n d a t"),("hippo","s h i p p o r"),
                        ("giraffe","a g i r a f f e n")],PINK)
bTop=aBot-14; bBot=38; bH=bTop-bBot
yc=L.card(40,bTop,W-80,bH,BLUE,"B","Animal parts — match","Match each picture to the words.")
L.R_match(yc,bBot,[("big-teeth","big teeth"),("sharp-claws","sharp claws"),
                   ("long-trunk","a long trunk"),("colorful-feathers","colorful feathers"),
                   ("short-tail","a short tail")],BLUE)
C.showPage()

# ---------------- Page 2: Grammar 1 (can / can't) ----------------
y=L.header(BADGE,[("What can they ",NAVY),("do?",GREEN)])
y=L.rule_box(y,[("Penguins can swim.  ",GREEN),("Penguins can't fly.",RED)],
             sub="Read each sentence. Circle True or False.")
yc=L.card(40,y,W-80,y-50,GREEN,"1","True or False?","Look and circle True or False.")
L.R_truefalse(yc,44,[
  ("A penguin can swim.","T","penguin"),
  ("A penguin can fly.","F","penguin"),
  ("A kangaroo can hop.","T","kangaroo"),
  ("A tiger can fly.","F","tiger"),
  ("A lion can run.","T","lion"),
],GREEN)
C.showPage()

# ---------------- Page 3: Grammar 2 (Does ... have ...?) ----------------
y=L.header(BADGE,[("Does it ",NAVY),("have...?",PURPLE)])
y=L.rule_box(y,[("Does a tiger have sharp claws?  ",NAVY),("Yes, it does.",GREEN),("/ No, it doesn't.",RED)],
             sub="Answer the question. Number 1 is done for you.")
yc=L.card(40,y,W-80,y-50,PURPLE,"1","Answer the question","Write Yes, it does. or No, it doesn't.")
L.R_qa_write(yc,44,[
  ("Does a tiger have sharp claws?","Yes, it does.","tiger"),
  ("Does a lion have big teeth?",None,"lion"),
  ("Does a panda have a short tail?",None,"panda"),
  ("Does a zebra have a long trunk?",None,"zebra"),
  ("Does a giraffe have sharp claws?",None,"giraffe"),
],PURPLE)
C.showPage()

# ---------------- Page 4: Answer Key ----------------
L.answer_key(BADGE,[
  (PINK,"A","Find and circle",["1. lion  2. tiger  3. zebra  4. panda  5. hippo  6. giraffe"]),
  (BLUE,"B","Animal parts — match",["big teeth, sharp claws, a long trunk, colorful feathers, a short tail"]),
  (GREEN,"1","True or False?",["1. True  2. False  3. True  4. False  5. True"]),
  (PURPLE,"1","Does it have...?",["1. Yes, it does.  2. Yes, it does.  3. Yes, it does.",
                                  "4. No, it doesn't.  5. No, it doesn't."]),
],"Scope: EOW2 Unit 8 only.  Art: 09_Image_Library.  Value: Respect animals.")
L.save()
