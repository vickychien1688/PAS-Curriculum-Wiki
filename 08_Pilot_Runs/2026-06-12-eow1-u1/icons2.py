#!/usr/bin/env python3
"""Realistic flat classroom icons (no faces) — matches PAS reference worksheet style."""
import math
from reportlab.lib.colors import HexColor, white, black

OUT = HexColor("#1A1A1A")

def _pen(c, lw): c.setStrokeColor(OUT); c.setLineWidth(lw)

def pencil(c, x, y, s):
    """classic yellow pencil, diagonal, tip lower-left"""
    c.saveState(); c.translate(x, y); c.rotate(-18)
    L, t = s*0.92, s*0.16
    _pen(c, s*0.025)
    # body
    c.setFillColor(HexColor("#F5C842"))
    c.rect(-L/2+t*1.1, -t/2, L-t*2.2, t, fill=1, stroke=1)
    # body ridges
    c.setLineWidth(s*0.012)
    c.line(-L/2+t*1.1, -t/6, L/2-t*1.1, -t/6)
    c.line(-L/2+t*1.1,  t/6, L/2-t*1.1,  t/6)
    _pen(c, s*0.025)
    # wood tip
    c.setFillColor(HexColor("#F2DCB8"))
    p = c.beginPath(); p.moveTo(-L/2+t*1.1, -t/2); p.lineTo(-L/2, 0); p.lineTo(-L/2+t*1.1, t/2); p.close()
    c.drawPath(p, stroke=1, fill=1)
    # graphite
    c.setFillColor(OUT)
    p = c.beginPath(); p.moveTo(-L/2+t*0.4, -t*0.18); p.lineTo(-L/2, 0); p.lineTo(-L/2+t*0.4, t*0.18); p.close()
    c.drawPath(p, stroke=0, fill=1)
    # ferrule
    c.setFillColor(HexColor("#B8BfC6"))
    c.rect(L/2-t*1.6, -t/2, t*0.6, t, fill=1, stroke=1)
    # eraser
    c.setFillColor(HexColor("#F2A0A8"))
    c.roundRect(L/2-t*1.0, -t/2, t*1.0, t, t*0.3, fill=1, stroke=1)
    c.restoreState()

def clock(c, x, y, s):
    """wall clock with numerals 12/3/6/9, blue rim"""
    r = s*0.42
    _pen(c, s*0.035)
    c.setFillColor(HexColor("#2E6DA8")); c.circle(x, y, r*1.12, fill=1, stroke=1)
    c.setFillColor(white); c.circle(x, y, r*0.94, fill=1, stroke=1)
    c.setFillColor(OUT); c.setFont("Helvetica-Bold", s*0.11)
    c.drawCentredString(x, y+r*0.62, "12")
    c.drawCentredString(x+r*0.72, y-s*0.04, "3")
    c.drawCentredString(x, y-r*0.78, "6")
    c.drawCentredString(x-r*0.72, y-s*0.04, "9")
    c.setFont("Helvetica", s*0.08)
    for hh,(dx,dy) in {1:(0.38,0.62),2:(0.62,0.36),4:(0.62,-0.42),5:(0.36,-0.68),
                       7:(-0.36,-0.68),8:(-0.62,-0.42),10:(-0.62,0.36),11:(-0.38,0.62)}.items():
        c.drawCentredString(x+r*dx, y+r*dy-s*0.025, str(hh))
    # hands
    c.setLineWidth(s*0.035); c.setStrokeColor(OUT)
    c.line(x, y, x, y+r*0.52)                 # minute up
    c.line(x, y, x+r*0.36, y+r*0.10)          # hour
    c.setStrokeColor(HexColor("#D03B3B")); c.setLineWidth(s*0.015)
    c.line(x, y, x-r*0.30, y-r*0.45)          # red second
    c.setFillColor(OUT); c.circle(x, y, s*0.025, fill=1, stroke=0)

def computer(c, x, y, s):
    """monitor + keyboard + mouse"""
    _pen(c, s*0.03)
    # monitor
    c.setFillColor(HexColor("#22272E"))
    c.roundRect(x-s*0.36, y-s*0.02, s*0.62, s*0.42, s*0.02, fill=1, stroke=1)
    c.setFillColor(HexColor("#3D6FA8"))
    c.rect(x-s*0.32, y+s*0.02, s*0.54, s*0.34, fill=1, stroke=1)
    # screen shine
    c.setFillColor(HexColor("#5F8FC4"))
    p = c.beginPath(); p.moveTo(x-s*0.32, y+s*0.02); p.lineTo(x-s*0.05, y+s*0.36); p.lineTo(x-s*0.18, y+s*0.36); p.lineTo(x-s*0.32, y+s*0.16); p.close()
    c.drawPath(p, stroke=0, fill=1)
    # stand
    c.setFillColor(HexColor("#22272E"))
    c.rect(x-s*0.08, y-s*0.10, s*0.10, s*0.08, fill=1, stroke=1)
    c.roundRect(x-s*0.16, y-s*0.13, s*0.26, s*0.04, s*0.01, fill=1, stroke=1)
    # keyboard
    c.setFillColor(HexColor("#2B313A"))
    p = c.beginPath(); p.moveTo(x-s*0.40, y-s*0.30); p.lineTo(x+s*0.18, y-s*0.30); p.lineTo(x+s*0.22, y-s*0.18); p.lineTo(x-s*0.44, y-s*0.18); p.close()
    c.drawPath(p, stroke=1, fill=1)
    c.setStrokeColor(HexColor("#6A7280")); c.setLineWidth(s*0.01)
    for i in range(5):
        c.line(x-s*0.41+i*s*0.12, y-s*0.28, x-s*0.45+i*s*0.12+s*0.005, y-s*0.20)
    _pen(c, s*0.03)
    # mouse
    c.setFillColor(HexColor("#2B313A"))
    c.ellipse(x+s*0.30, y-s*0.30, x+s*0.42, y-s*0.16, fill=1, stroke=1)

def book(c, x, y, s):
    """green hardcover, slight 3D perspective"""
    _pen(c, s*0.03)
    w, h, d = s*0.72, s*0.42, s*0.12
    # pages block (right + bottom edge)
    c.setFillColor(HexColor("#F5EFD9"))
    p = c.beginPath()
    p.moveTo(x-w/2+d, y-h/2-d); p.lineTo(x+w/2+d, y-h/2-d); p.lineTo(x+w/2+d, y+h/2-d)
    p.lineTo(x+w/2, y+h/2); p.lineTo(x+w/2, y-h/2); p.lineTo(x-w/2+d, y-h/2); p.close()
    c.drawPath(p, stroke=1, fill=1)
    c.setLineWidth(s*0.012)
    for i in range(1,4):
        c.line(x-w/2+d*i/3.2, y-h/2-d*i/3.2, x+w/2+d*i/3.2, y-h/2-d*i/3.2)
    _pen(c, s*0.03)
    # cover
    c.setFillColor(HexColor("#2F7D4F"))
    c.roundRect(x-w/2, y-h/2, w, h, s*0.02, fill=1, stroke=1)
    # label
    c.setFillColor(HexColor("#EFE6C8"))
    c.rect(x-w*0.18, y+h*0.12, w*0.36, h*0.30, fill=1, stroke=1)
    # ribbon
    c.setFillColor(HexColor("#C0392B"))
    p = c.beginPath(); p.moveTo(x+w*0.18, y-h/2); p.lineTo(x+w*0.18, y-h/2-d*0.9)
    p.lineTo(x+w*0.13, y-h/2-d*0.55); p.lineTo(x+w*0.08, y-h/2-d*0.9); p.lineTo(x+w*0.08, y-h/2); p.close()
    c.drawPath(p, stroke=1, fill=1)

def desk(c, x, y, s):
    """school desk with open front shelf, metal legs"""
    _pen(c, s*0.03)
    # top (parallelogram)
    c.setFillColor(HexColor("#D9A05B"))
    p = c.beginPath()
    p.moveTo(x-s*0.30, y+s*0.16); p.lineTo(x+s*0.38, y+s*0.16)
    p.lineTo(x+s*0.30, y+s*0.30); p.lineTo(x-s*0.38, y+s*0.30); p.close()
    c.drawPath(p, stroke=1, fill=1)
    # top front edge
    c.setFillColor(HexColor("#C08A45"))
    c.rect(x-s*0.30, y+s*0.10, s*0.68, s*0.06, fill=1, stroke=1)
    # open shelf box
    c.setFillColor(HexColor("#3A3F46"))
    c.rect(x-s*0.24, y-s*0.08, s*0.52, s*0.16, fill=1, stroke=1)
    c.setFillColor(HexColor("#14171B"))
    c.rect(x-s*0.20, y-s*0.05, s*0.44, s*0.10, fill=1, stroke=1)
    # legs
    c.setStrokeColor(HexColor("#7A828C")); c.setLineWidth(s*0.045)
    c.line(x-s*0.24, y+s*0.10, x-s*0.30, y-s*0.42)
    c.line(x+s*0.30, y+s*0.10, x+s*0.36, y-s*0.42)
    c.setLineWidth(s*0.03)
    c.line(x-s*0.28, y-s*0.30, x+s*0.34, y-s*0.30)
    _pen(c, s*0.03)

def chair(c, x, y, s):
    """wooden school chair, metal legs"""
    _pen(c, s*0.03)
    wood = HexColor("#D9A05B")
    # back rest
    c.setFillColor(wood)
    c.roundRect(x-s*0.20, y+s*0.16, s*0.40, s*0.16, s*0.03, fill=1, stroke=1)
    # back posts
    c.setStrokeColor(HexColor("#7A828C")); c.setLineWidth(s*0.04)
    c.line(x-s*0.16, y+s*0.16, x-s*0.16, y-s*0.02)
    c.line(x+s*0.16, y+s*0.16, x+s*0.16, y-s*0.02)
    _pen(c, s*0.03)
    # seat
    c.setFillColor(wood)
    p = c.beginPath()
    p.moveTo(x-s*0.24, y-s*0.02); p.lineTo(x+s*0.24, y-s*0.02)
    p.lineTo(x+s*0.28, y-s*0.10); p.lineTo(x-s*0.28, y-s*0.10); p.close()
    c.drawPath(p, stroke=1, fill=1)
    # legs
    c.setStrokeColor(HexColor("#7A828C")); c.setLineWidth(s*0.045)
    c.line(x-s*0.22, y-s*0.10, x-s*0.26, y-s*0.46)
    c.line(x+s*0.22, y-s*0.10, x+s*0.26, y-s*0.46)
    c.setLineWidth(s*0.03)
    c.line(x-s*0.24, y-s*0.32, x+s*0.24, y-s*0.32)
    _pen(c, s*0.03)

def pen(c, x, y, s):
    """blue ballpoint pen, diagonal"""
    c.saveState(); c.translate(x, y); c.rotate(-18)
    L, t = s*0.9, s*0.12
    _pen(c, s*0.025)
    c.setFillColor(HexColor("#2E6DA8"))
    c.roundRect(-L/2+t*1.2, -t/2, L-t*2.4, t, t*0.3, fill=1, stroke=1)
    # tip cone
    c.setFillColor(HexColor("#B8BFC6"))
    p = c.beginPath(); p.moveTo(-L/2+t*1.2, -t/2); p.lineTo(-L/2, 0); p.lineTo(-L/2+t*1.2, t/2); p.close()
    c.drawPath(p, stroke=1, fill=1)
    # cap end + clip
    c.setFillColor(HexColor("#1F4E7A"))
    c.roundRect(L/2-t*1.4, -t/2, t*1.2, t, t*0.3, fill=1, stroke=1)
    c.setLineWidth(s*0.025); c.setStrokeColor(OUT)
    c.line(L/2-t*1.2, t/2, L/2-t*0.2, t*1.1)
    c.restoreState()

ICONS = {"pencil": pencil, "clock": clock, "computer": computer,
         "book": book, "desk": desk, "chair": chair, "pen": pen}
