#!/usr/bin/env python3
"""Flat side-view farm-animal icons, reference-worksheet style (outline + fill, no faces)."""
from reportlab.lib.colors import HexColor, white

OUT = HexColor("#1A1A1A")
def _pen(c, lw): c.setStrokeColor(OUT); c.setLineWidth(lw)
def _eye(c, x, y, r):
    c.setFillColor(OUT); c.circle(x, y, r, fill=1, stroke=0)

def duck(c, x, y, s):
    _pen(c, s*0.03)
    c.setFillColor(HexColor("#F5D442"))
    c.ellipse(x-s*0.34, y-s*0.26, x+s*0.26, y+s*0.10, fill=1, stroke=1)      # body
    c.circle(x+s*0.20, y+s*0.16, s*0.15, fill=1, stroke=1)                    # head
    c.setFillColor(HexColor("#E8862E"))
    p=c.beginPath(); p.moveTo(x+s*0.33, y+s*0.18); p.lineTo(x+s*0.48, y+s*0.13); p.lineTo(x+s*0.33, y+s*0.10); p.close()
    c.drawPath(p, stroke=1, fill=1)                                           # beak
    c.setFillColor(HexColor("#E8C32E"))
    c.ellipse(x-s*0.22, y-s*0.16, x+s*0.04, y+s*0.02, fill=1, stroke=1)       # wing
    _eye(c, x+s*0.24, y+s*0.19, s*0.022)
    c.setStrokeColor(HexColor("#5FA8D9")); c.setLineWidth(s*0.025)
    for i in range(3):                                                         # water
        xx = x - s*0.38 + i*s*0.30
        p=c.beginPath(); p.moveTo(xx, y-s*0.32); p.curveTo(xx+s*0.07, y-s*0.27, xx+s*0.15, y-s*0.37, xx+s*0.22, y-s*0.32)
        c.drawPath(p, stroke=1, fill=0)

def turtle(c, x, y, s):
    _pen(c, s*0.03)
    c.setFillColor(HexColor("#5F9C5C"))
    p=c.beginPath(); p.moveTo(x-s*0.32, y-s*0.10)
    p.curveTo(x-s*0.30, y+s*0.26, x+s*0.30, y+s*0.26, x+s*0.32, y-s*0.10); p.close()
    c.drawPath(p, stroke=1, fill=1)                                           # shell
    c.setStrokeColor(HexColor("#3E6B3C")); c.setLineWidth(s*0.02)
    c.line(x-s*0.16, y-s*0.09, x-s*0.10, y+s*0.12); c.line(x+s*0.16, y-s*0.09, x+s*0.10, y+s*0.12)
    c.line(x-s*0.10, y+s*0.12, x+s*0.10, y+s*0.12)
    _pen(c, s*0.03)
    c.setFillColor(HexColor("#8FBF6B"))
    c.circle(x+s*0.40, y-s*0.06, s*0.10, fill=1, stroke=1)                    # head
    for lx in (-s*0.20, s*0.16):                                              # legs
        c.ellipse(x+lx-s*0.06, y-s*0.24, x+lx+s*0.06, y-s*0.08, fill=1, stroke=1)
    _eye(c, x+s*0.43, y-s*0.03, s*0.02)

def cat(c, x, y, s):
    _pen(c, s*0.03)
    orange = HexColor("#E8975A")
    c.setFillColor(orange)
    c.ellipse(x-s*0.30, y-s*0.26, x+s*0.18, y+s*0.06, fill=1, stroke=1)       # body
    c.circle(x+s*0.22, y+s*0.12, s*0.15, fill=1, stroke=1)                    # head
    for ex in (s*0.12, s*0.32):                                               # ears
        p=c.beginPath(); p.moveTo(x+ex, y+s*0.24); p.lineTo(x+ex+s*0.05, y+s*0.38); p.lineTo(x+ex+s*0.10, y+s*0.24); p.close()
        c.drawPath(p, stroke=1, fill=1)
    c.setStrokeColor(OUT); c.setLineWidth(s*0.028)
    p=c.beginPath(); p.moveTo(x-s*0.30, y-s*0.10)                             # tail
    p.curveTo(x-s*0.46, y-s*0.04, x-s*0.46, y+s*0.16, x-s*0.36, y+s*0.20)
    c.drawPath(p, stroke=1, fill=0)
    c.setLineWidth(s*0.015)
    for wy in (s*0.10, s*0.06):                                               # whiskers
        c.line(x+s*0.34, y+wy, x+s*0.46, y+wy+s*0.02)
    _eye(c, x+s*0.26, y+s*0.15, s*0.022)
    c.setLineWidth(s*0.02)
    for lx in (-s*0.18, -s*0.02):                                             # legs
        c.line(x+lx, y-s*0.26, x+lx, y-s*0.36)

def dog(c, x, y, s):
    _pen(c, s*0.03)
    brown = HexColor("#B07B4F")
    c.setFillColor(brown)
    c.ellipse(x-s*0.30, y-s*0.24, x+s*0.18, y+s*0.08, fill=1, stroke=1)       # body
    c.circle(x+s*0.24, y+s*0.14, s*0.15, fill=1, stroke=1)                    # head
    c.setFillColor(HexColor("#8A5A33"))
    c.ellipse(x+s*0.10, y+s*0.02, x+s*0.20, y+s*0.26, fill=1, stroke=1)       # floppy ear
    c.setFillColor(OUT); c.circle(x+s*0.40, y+s*0.12, s*0.025, fill=1, stroke=0)  # nose
    c.setStrokeColor(OUT); c.setLineWidth(s*0.028)
    p=c.beginPath(); p.moveTo(x-s*0.30, y-s*0.02)                             # tail up
    p.curveTo(x-s*0.42, y+s*0.06, x-s*0.44, y+s*0.18, x-s*0.40, y+s*0.22)
    c.drawPath(p, stroke=1, fill=0)
    _eye(c, x+s*0.28, y+s*0.18, s*0.022)
    c.setLineWidth(s*0.02)
    for lx in (-s*0.18, -s*0.02, s*0.10):
        c.line(x+lx, y-s*0.24, x+lx, y-s*0.36)

def sheep(c, x, y, s):
    _pen(c, s*0.03)
    wool = HexColor("#F2EDE3")
    c.setFillColor(wool)
    for (dx,dy,r) in [(-0.20,0.02,0.14),(0.0,0.08,0.16),(0.18,0.02,0.14),(-0.10,-0.10,0.15),(0.10,-0.10,0.15),(0.0,-0.02,0.18)]:
        c.circle(x+dx*s, y+dy*s, r*s, fill=1, stroke=1)
    c.setFillColor(wool); c.circle(x, y-s*0.01, s*0.20, fill=1, stroke=0)     # smooth core
    c.setFillColor(HexColor("#6B6B6B"))
    c.circle(x+s*0.30, y+s*0.10, s*0.11, fill=1, stroke=1)                    # head
    c.ellipse(x+s*0.18, y+s*0.14, x+s*0.28, y+s*0.22, fill=1, stroke=1)       # ear
    _eye(c, x+s*0.33, y+s*0.13, s*0.02)
    c.setStrokeColor(OUT); c.setLineWidth(s*0.02)
    for lx in (-s*0.14, 0, s*0.14):
        c.line(x+lx, y-s*0.22, x+lx, y-s*0.36)

def cow(c, x, y, s):
    _pen(c, s*0.03)
    c.setFillColor(white)
    c.ellipse(x-s*0.32, y-s*0.24, x+s*0.20, y+s*0.10, fill=1, stroke=1)       # body
    c.setFillColor(OUT)
    c.ellipse(x-s*0.18, y-s*0.12, x-s*0.02, y+s*0.04, fill=1, stroke=0)       # spot
    c.ellipse(x+s*0.02, y-s*0.20, x+s*0.14, y-s*0.08, fill=1, stroke=0)       # spot
    c.setFillColor(white)
    c.circle(x+s*0.26, y+s*0.14, s*0.14, fill=1, stroke=1)                    # head
    c.setFillColor(HexColor("#E8B4B8"))
    c.ellipse(x+s*0.28, y+s*0.02, x+s*0.44, y+s*0.12, fill=1, stroke=1)       # muzzle
    c.setFillColor(HexColor("#D9D9D9"))
    for hx in (s*0.16, s*0.32):                                               # horns
        p=c.beginPath(); p.moveTo(x+hx, y+s*0.26); p.lineTo(x+hx+s*0.03, y+s*0.36); p.lineTo(x+hx+s*0.07, y+s*0.26); p.close()
        c.drawPath(p, stroke=1, fill=1)
    _eye(c, x+s*0.30, y+s*0.18, s*0.022)
    c.setStrokeColor(OUT); c.setLineWidth(s*0.02)
    for lx in (-s*0.20, -s*0.04, s*0.10):
        c.line(x+lx, y-s*0.24, x+lx, y-s*0.38)

def horse(c, x, y, s):
    _pen(c, s*0.03)
    body = HexColor("#A8763E")
    c.setFillColor(body)
    c.ellipse(x-s*0.30, y-s*0.22, x+s*0.16, y+s*0.08, fill=1, stroke=1)       # body
    p=c.beginPath(); p.moveTo(x+s*0.08, y+s*0.04)                             # neck+head
    p.lineTo(x+s*0.26, y+s*0.30); p.lineTo(x+s*0.40, y+s*0.26); p.lineTo(x+s*0.44, y+s*0.16)
    p.lineTo(x+s*0.30, y+s*0.10); p.lineTo(x+s*0.20, y-s*0.02); p.close()
    c.drawPath(p, stroke=1, fill=1)
    c.setFillColor(HexColor("#5C3A1E"))
    p=c.beginPath(); p.moveTo(x+s*0.10, y+s*0.06)                             # mane
    p.curveTo(x+s*0.16, y+s*0.22, x+s*0.22, y+s*0.30, x+s*0.28, y+s*0.32)
    p.lineTo(x+s*0.24, y+s*0.18); p.close()
    c.drawPath(p, stroke=1, fill=1)
    p=c.beginPath(); p.moveTo(x-s*0.30, y-s*0.04)                             # tail
    p.curveTo(x-s*0.42, y-s*0.10, x-s*0.40, y-s*0.26, x-s*0.36, y-s*0.30)
    c.setStrokeColor(HexColor("#5C3A1E")); c.setLineWidth(s*0.05)
    c.drawPath(p, stroke=1, fill=0)
    _eye(c, x+s*0.33, y+s*0.22, s*0.022)
    c.setStrokeColor(OUT); c.setLineWidth(s*0.022)
    for lx in (-s*0.20, -s*0.06, s*0.08):
        c.line(x+lx, y-s*0.22, x+lx, y-s*0.38)

def zzz(c, x, y, s):
    c.setFillColor(OUT); c.setFont("Helvetica-Bold", s*0.16)
    for i,(dx,dy,f) in enumerate([(0.0,0.0,0.16),(0.10,0.10,0.12),(0.18,0.20,0.09)]):
        c.setFont("Helvetica-Bold", s*f); c.drawString(x+dx*s, y+dy*s, "Z")

ICONS = {"duck": duck, "turtle": turtle, "cat": cat, "dog": dog,
         "sheep": sheep, "cow": cow, "horse": horse}
