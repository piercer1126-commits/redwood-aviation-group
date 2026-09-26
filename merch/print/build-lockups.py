"""Build Redwood Aviation Group apparel lockups from the master mark.

Input:  merch/print/mark-only.png  (transparent pine-cluster mark, 1343x1134)
Output: the stacked and horizontal lockups plus sized variants and proofs.

Fonts (SIL Open Font License). Fetch once, then point FONT_DIR at them
(defaults to /tmp):

  curl -sSL -o /tmp/PlayfairDisplay.ttf \
    "https://raw.githubusercontent.com/google/fonts/main/ofl/playfairdisplay/PlayfairDisplay%5Bwght%5D.ttf"

Usage:
  FONT_DIR=/path python3 build-lockups.py
"""
import os
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ART   = Path(__file__).resolve().parent
FONTS = Path(os.environ.get("FONT_DIR", "/tmp"))
PF    = str(FONTS/"PlayfairDisplay.ttf")

GOLD = (240,192,64,255)

def font(px):
    f = ImageFont.truetype(PF, px); f.set_variation_by_axes([700]); return f
def wof(t,f,tr): return sum(f.getlength(c) for c in t)+tr*(len(t)-1)
def fit(text, target_w, track_em):
    lo, hi = 10, 1400
    for _ in range(60):
        mid=(lo+hi)/2; f=font(int(round(mid)))
        if wof(text,f,track_em*mid) < target_w: lo=mid
        else: hi=mid
    s=int(round(lo)); return font(s), track_em*s
def tracked(d,cx,baseline,text,f,tr,fill):
    x = cx - wof(text,f,tr)/2
    for ch in text:
        d.text((x,baseline),ch,font=f,fill=fill,anchor="ls"); x+=f.getlength(ch)+tr
def cap(f): b=f.getbbox("H"); return b[3]-b[1]

mark = Image.open(ART/"mark-only.png").convert("RGBA")

def clean_pale(img):
    """Drop near-white unsaturated pixels. Resampling can ring at high-contrast
    edges and reintroduce pale fringe, so this runs after every rescale."""
    a = np.asarray(img).astype(np.float32)
    rgb, al = a[...,:3], a[...,3]
    mn = rgb.min(axis=2); chroma = rgb.max(axis=2)-mn
    ramp = lambda v,lo,hi: np.clip((v-lo)/(hi-lo),0,1)
    factor = ramp(mn,140,200)*(1.0-ramp(chroma,40,80))
    return Image.fromarray(np.dstack([rgb, al*(1.0-factor)]).astype(np.uint8),"RGBA")

def scaled(img,w):
    if w==img.width: return img
    return clean_pale(img.resize((w,round(img.height*w/img.width)),Image.LANCZOS))

def stacked(mark_w):
    m = scaled(mark, mark_w); W = mark_w
    f1,t1 = fit("REDWOOD",        0.88*W, 0.10)
    f2,t2 = fit("AVIATION GROUP", 0.86*W, 0.22)
    c1,c2 = cap(f1), cap(f2)
    GAP, LGAP = int(0.045*W), int(0.42*c2)
    CW, CH = W+2, m.height+GAP+c1+LGAP+c2+int(0.02*W)
    c = Image.new("RGBA",(CW,CH),(0,0,0,0))
    c.alpha_composite(m,((CW-W)//2,0))
    d = ImageDraw.Draw(c)
    b1 = m.height+GAP+c1
    tracked(d,CW/2,b1,"REDWOOD",f1,t1,GOLD)
    tracked(d,CW/2,b1+LGAP+c2,"AVIATION GROUP",f2,t2,GOLD)
    return c.crop(c.getbbox())

def horizontal():
    MW,MH = mark.width, mark.height
    f1,t1 = fit("REDWOOD",        0.95*MW, 0.10)
    f2,t2 = fit("AVIATION GROUP", 0.93*MW, 0.22)
    c1,c2 = cap(f1), cap(f2)
    LG = int(0.42*c2); tb_h = c1+LG+c2
    tb_w = int(max(wof("REDWOOD",f1,t1), wof("AVIATION GROUP",f2,t2)))
    GAP = int(0.06*MW)
    CW,CH = MW+GAP+tb_w+4, max(MH,tb_h)+4
    c = Image.new("RGBA",(CW,CH),(0,0,0,0))
    c.alpha_composite(mark,(0,(CH-MH)//2))
    d = ImageDraw.Draw(c)
    top = (CH-tb_h)//2; cx = MW+GAP+tb_w/2
    tracked(d,cx,top+c1,"REDWOOD",f1,t1,GOLD)
    tracked(d,cx,top+c1+LG+c2,"AVIATION GROUP",f2,t2,GOLD)
    return c.crop(c.getbbox())

if __name__=="__main__":
    big = stacked(2400)                      # 8in wide @300dpi
    big.save(ART/"lockup-8in-300dpi.png")
    stacked(mark.width).save(ART/"lockup-native.png")
    scaled(big,1050).save(ART/"lockup-leftchest-3.5in.png")

    h = horizontal()
    h.save(ART/"lockup-horizontal.png")
    scaled(h,1350).save(ART/"lockup-horizontal-cap-4.5in.png")

    for name,bg in (("black","#101014"),("charcoal","#2f3033")):
        p = int(big.width*0.10)
        s = Image.new("RGBA",(big.width+2*p,big.height+2*p),bg)
        s.alpha_composite(big,(p,p))
        s.convert("RGB").save(ART/f"proof-{name}.png")

    print("stacked 8in :", big.size)
    print("horizontal  :", h.size, "(%.2f:1)"%(h.width/h.height))
    print("all lockups rebuilt from mark-only.png")
