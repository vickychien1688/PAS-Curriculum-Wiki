#!/usr/bin/env python3
"""EOW2 U3 Boots and Bathing Suits — colourful worksheet.
Variety mix: P1 match (weather) + circle (clothes); P2 look&write It's ___ (weather);
P3 multiple-choice imperatives; P4 answer key.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import eow2lib as L
from eow2lib import (W,H,NAVY,PINK,BLUE,GREEN,ORANGE,PURPLE,GREY,RED)

HERE=os.path.dirname(os.path.abspath(__file__))
C=L.setup(HERE,"EOW2 U3 Boots and Bathing Suits (colorful).pdf")
BADGE="EOW2 · Unit 3"

# ---------------- Page 1: Vocabulary ----------------
y=L.header(BADGE,[("Boots and ",NAVY),("Bathing Suits",ORANGE)])
aTop=y; aH=372; aBot=aTop-aH
yc=L.card(40,aTop,W-80,aH,PINK,"A","Weather — match","Match each picture to the weather word.")
L.R_match(yc,aBot+14,[("sunny","sunny"),("cloudy","cloudy"),("rainy","rainy"),
                      ("hot","hot"),("cold","cold")],PINK)
bTop=aBot-14; bBot=38; bH=bTop-bBot
yc=L.card(40,bTop,W-80,bH,BLUE,"B","Clothes — circle","Look at the picture. Circle the correct word.")
L.R_circle(yc,bBot,[("coat",["a coat","a cap","a sock"]),
                    ("jeans",["boots","jeans","shorts"]),
                    ("shorts",["shorts","jeans","a coat"]),
                    ("sneakers",["a hat","boots","sneakers"]),
                    ("umbrella",["an umbrella","a raincoat","a coat"])],BLUE,optx=(220,330,445))
C.showPage()

# ---------------- Page 2: Grammar 1 ----------------
y=L.header(BADGE,[("What's the weather ",NAVY),("like?",GREEN)])
y=L.rule_box(y,[("What's the weather like?  ",NAVY),("It's rainy.",GREEN)],
             sub="Word bank:  sunny   cloudy   rainy   hot   cold")
yc=L.card(40,y,W-80,y-86,GREEN,"1","Look and write","Look at the picture. Write the weather. Number 1 is done for you.")
L.R_write(yc,90,[("sunny","sunny"),("rainy",None),("cloudy",None),("hot",None),("cold",None)],
          GREEN,prefix="It's",suffix=".")
C.showPage()

# ---------------- Page 3: Grammar 2 ----------------
y=L.header(BADGE,[("Put on your ",NAVY),("coat!",PURPLE)])
y=L.rule_box(y,[("It's cold.  ",NAVY),("Put on your coat.",PURPLE)],
             sub="Read the weather. Choose the best thing to do.")
yc=L.card(40,y,W-80,y-60,PURPLE,"1","Choose the best one","Circle a or b.")
L.R_mc(yc,46,[
  ("It's cold.",[("a","Put on your coat."),("b","Put on your shorts.")],"a","cold"),
  ("It's rainy.",[("a","Forget your umbrella."),("b","Take your umbrella.")],"b","rainy"),
  ("It's hot.",[("a","Put on your bathing suit."),("b","Put on your boots.")],"a","hot"),
  ("It's sunny.",[("a","Wear your raincoat."),("b","Wear your shorts.")],"b","sunny"),
],PURPLE)
C.showPage()

# ---------------- Page 4: Answer Key ----------------
L.answer_key(BADGE,[
  (PINK,"A","Weather — match",["sunny, cloudy, rainy, hot, cold  (match each to its picture)"]),
  (BLUE,"B","Clothes — circle",["1. a coat   2. jeans   3. shorts   4. sneakers   5. an umbrella"]),
  (GREEN,"1","What's the weather like?",["1. It's sunny.   2. It's rainy.   3. It's cloudy.   4. It's hot.   5. It's cold."]),
  (PURPLE,"1","Choose the best one",["1. a   2. b   3. a   4. b"]),
],"Scope: EOW2 Unit 3 only.  Art: 09_Image_Library.  Value: Dress for the weather.")
L.save()
