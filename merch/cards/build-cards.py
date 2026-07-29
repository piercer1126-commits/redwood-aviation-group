"""Build Redwood Aviation Group business cards (3.5x2in, 0.125in bleed, 600 DPI).

Fonts (SIL Open Font License, fetched to /tmp before running):

  curl -sSL -o /tmp/PlayfairDisplay.ttf \
    "https://raw.githubusercontent.com/google/fonts/main/ofl/playfairdisplay/PlayfairDisplay%5Bwght%5D.ttf"
  curl -sSL -o /tmp/Inter.ttf \
    "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter%5Bopsz,wght%5D.ttf"

Usage:
  python3 build-cards.py '[{"slug":"rob","name":"...","title":"...",
                            "phone":"...","email":"..."}]'
"""
from PIL import Image, ImageDraw, ImageFont

DPI   = 600
PT    = DPI/72.0
BLEED = int(0.125*DPI)                 # 75px
TRIM_W, TRIM_H = int(3.5*DPI), int(2.0*DPI)
CW, CH = TRIM_W+2*BLEED, TRIM_H+2*BLEED
SAFE  = BLEED + int(0.125*DPI)         # 150px from canvas edge

BLACK=(10,10,12,255); GOLD=(240,192,64,255); WHITE=(255,255,255,255)
INK=(232,228,221,255); SOFT=(150,146,140,255)

PF="/tmp/PlayfairDisplay.ttf"; IN="/tmp/Inter.ttf"
def playfair(pt,w=700):
    f=ImageFont.truetype(PF,int(round(pt*PT))); f.set_variation_by_axes([w]); return f
def inter(pt,w=400):
    f=ImageFont.truetype(IN,int(round(pt*PT))); f.set_variation_by_axes([14,w]); return f

def wof(t,f,tr): return sum(f.getlength(c) for c in t)+tr*(len(t)-1)
def tracked(d,x,base,t,f,tr,fill,anchor="l"):
    w=wof(t,f,tr)
    if anchor=="c": x-=w/2
    elif anchor=="r": x-=w
    for ch in t:
        d.text((x,base),ch,font=f,fill=fill,anchor="ls"); x+=f.getlength(ch)+tr
    return w
def cap(f): b=f.getbbox("H"); return b[3]-b[1]

mark=Image.open("/tmp/logo-2000-transparent.png").convert("RGBA")
lockh=Image.open("/home/user/redwood-aviation-group/merch/print/lockup-horizontal.png").convert("RGBA")

def fit_w(img,inches):
    w=int(inches*DPI); return img.resize((w,round(img.height*w/img.width)),Image.LANCZOS)

# ---------------- BACK ----------------
def build_back():
    c=Image.new("RGBA",(CW,CH),BLACK); d=ImageDraw.Draw(c)
    lk=fit_w(lockh,2.45)
    ly=int(CH*0.5 - lk.height*0.5 - 0.085*DPI)
    c.alpha_composite(lk,((CW-lk.width)//2, ly))
    TAG="AIRCRAFT LEASEBACK PARTNERSHIPS"
    # size the tagline so it optically matches the lockup width above it
    target=2.05*DPI; lo,hi=3.0,12.0
    for _ in range(40):
        mid=(lo+hi)/2; f=inter(mid,600)
        if wof(TAG,f,0.22*f.size)<target: lo=mid
        else: hi=mid
    f=inter(lo,600)
    tracked(d,CW/2, ly+lk.height+int(0.20*DPI), TAG, f, 0.22*f.size, GOLD, "c")
    return c

# ---------------- FRONT ----------------
def build_front(name,title,phone,email,site="redwoodaviationgroup.com"):
    c=Image.new("RGBA",(CW,CH),BLACK); d=ImageDraw.Draw(c)
    # mark, right side, vertically centered
    mk=fit_w(mark,1.02)
    mx=CW-SAFE-mk.width
    c.alpha_composite(mk,(mx,(CH-mk.height)//2))

    x=SAFE
    fn=playfair(11.5,700); ft=inter(5.8,600); fc=inter(6.9,400); fs=inter(6.9,500)
    cn,ct,cc=cap(fn),cap(ft),cap(fc)
    line_gap=int(0.052*DPI)
    rule_gap=int(0.075*DPI)

    block_h = cn + int(0.055*DPI) + ct + rule_gap + 4 + rule_gap + cc*3 + line_gap*2
    y = (CH-block_h)//2 + cn

    tracked(d,x,y,name.upper(),fn,0.055*fn.size,WHITE)
    y += int(0.055*DPI) + ct
    tracked(d,x,y,title.upper(),ft,0.20*ft.size,GOLD)
    y += rule_gap
    d.rectangle([x,y,x+int(0.62*DPI),y+3],fill=GOLD)
    y += 3 + rule_gap + cc
    for txt,fnt,col in ((phone,fc,INK),(email,fc,INK),(site,fs,GOLD)):
        tracked(d,x,y,txt,fnt,0.012*fnt.size,col)
        y += cc + line_gap
    return c

def guides(card):
    g=card.copy(); d=ImageDraw.Draw(g)
    d.rectangle([BLEED,BLEED,CW-BLEED-1,CH-BLEED-1],outline=(255,60,60,255),width=4)
    d.rectangle([SAFE,SAFE,CW-SAFE-1,CH-SAFE-1],outline=(80,200,255,255),width=3)
    return g

if __name__=="__main__":
    import sys, json
    people=json.loads(sys.argv[1])
    out="/home/user/redwood-aviation-group/merch/cards"
    back=build_back(); back.save(f"{out}/card-back.png")
    print("back:", back.size)
    for p in people:
        slug=p["slug"]
        fr=build_front(p["name"],p["title"],p["phone"],p["email"])
        fr.save(f"{out}/card-front-{slug}.png")
        guides(fr).save(f"/tmp/guide-{slug}.png")
        print("front:",slug,fr.size)
    guides(back).save("/tmp/guide-back.png")
    print("canvas %dx%d px = %.2fx%.2f in @%d DPI (incl. bleed)"%(CW,CH,CW/DPI,CH/DPI,DPI))
