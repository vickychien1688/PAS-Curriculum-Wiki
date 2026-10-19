#!/usr/bin/env python3
"""EOW2 U4 Fun in the Sun — colourful worksheet.
Variety mix: P1 match (sports) + write-with-wordbox (ball actions);
P2 Yes/No Q&A 'Do you like to...?'; P3 unscramble 'Let's ...'; P4 key.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import eow2lib as L
from eow2lib import (W,H,NAVY,PINK,BLUE,GREEN,ORANGE,PURPLE,GREY,RED)

HERE=os.path.dirname(os.path.abspath(__file__))
C=L.setup(HERE,"EOW2 U4 Fun in the Sun (colorful).pdf")
BADGE="EOW2 · Unit 4"

# ---------------- Page 1: Vocabulary ----------------
y=L.header(BADGE,[("Fun in the ",NAVY),("Sun",ORANGE)])
aTop=y; aH=372; aBot=aTop-aH
yc=L.card(40,aTop,W-80,aH,PINK,"A","Sports — match","Match each picture to the words.")
L.R_match(yc,aBot+14,[("fly-a-kite","fly a kite"),("jump-rope","jump rope"),
                      ("play-baseball","play baseball"),("play-basketball","play basketball"),
                      ("play-soccer","play soccer"),("ride-a-bike","ride a bike")],PINK)
bTop=aBot-14; bBot=38; bH=bTop-bBot
yc=L.card(40,bTop,W-80,bH,BLUE,"B","Write the action","Write the action under each picture. Use the Word Box.")
L.wordbox(54,yc-2,W-108,["throw a ball","catch a ball","bounce a ball","play tag","watch a game"],BLUE)
L.R_write(yc-58,bBot,[("throw-a-ball","throw a ball"),("catch-a-ball",None),
                      ("bounce-a-ball",None),("play-tag",None),("watch-a-game",None)],
          BLUE,prefix="",suffix="",picsize=52,prefix_font=14)
C.showPage()

# ---------------- Page 2: Grammar 1 ----------------
y=L.header(BADGE,[("Do you ",NAVY),("like to...?",GREEN)])
y=L.rule_box(y,[("Do you like to play baseball?  ",NAVY),("Yes, I do.",GREEN),("/ No, I don't.",RED)],
             sub="Answer about yourself. Number 1 is done for you.")
yc=L.card(40,y,W-80,y-50,GREEN,"1","Answer about you","Write Yes, I do. or No, I don't.")
L.R_qa_write(yc,44,[
  ("Do you like to play baseball?","Yes, I do.","play-baseball"),
  ("Do you like to ride a bike?",None,"ride-a-bike"),
  ("Do you like to jump rope?",None,"jump-rope"),
  ("Do you like to play soccer?",None,"play-soccer"),
  ("Do you like to fly a kite?",None,"fly-a-kite"),
],GREEN)
C.showPage()

# ---------------- Page 3: Grammar 2 ----------------
y=L.header(BADGE,[("Let's ",NAVY),("play!",PURPLE)])
y=L.rule_box(y,[("Let's throw a ball.  ",NAVY),("OK! What fun!",PURPLE)],
             sub="Put the words in order. Write the sentence. Add the end mark.")
yc=L.card(40,y,W-80,y-70,PURPLE,"1","Make the sentence","Write the sentence on the line.")
L.R_unscramble(yc,80,[
  ("throw-a-ball",["a","ball","Let's","throw"],". ?"),
  ("catch-a-ball",["catch","Let's","a","ball"],". ?"),
  ("play-tag",["play","Let's","tag"],". ?"),
  ("bounce-a-ball",["a","Let's","ball","bounce"],". ?"),
  ("play-a-game",["a","game","Let's","play"],". ?"),
],PURPLE)
C.showPage()

# ---------------- Page 4: Answer Key ----------------
L.answer_key(BADGE,[
  (PINK,"A","Sports — match",["fly a kite, jump rope, play baseball, play basketball, play soccer, ride a bike"]),
  (BLUE,"1","Write the action",["throw a ball, catch a ball, bounce a ball, play tag, watch a game"]),
  (GREEN,"1","Do you like to...?",["Answers will vary. Example: 1. Yes, I do.  2.-5. Yes, I do. / No, I don't."]),
  (PURPLE,"1","Let's ... (make the sentence)",
   ["1. Let's throw a ball.   2. Let's catch a ball.   3. Let's play tag.",
    "4. Let's bounce a ball.   5. Let's play a game."]),
],"Scope: EOW2 Unit 4 only.  Art: 09_Image_Library.  Value: Be a good sport.")
L.save()
