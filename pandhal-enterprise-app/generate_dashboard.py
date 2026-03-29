#!/usr/bin/env python3
"""Generate Pandhal Super Admin Dashboard as a high-resolution PNG."""

from PIL import Image, ImageDraw, ImageFont

SCALE = 2
W, H  = 390, 1700

img  = Image.new("RGB", (W*SCALE, H*SCALE), "#111827")
draw = ImageDraw.Draw(img)

FREG  = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
FBOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

def f(sz, bold=False):
    return ImageFont.truetype(FBOLD if bold else FREG, sz*SCALE)

def s(v): return int(v*SCALE)
def sp(xy): return (s(xy[0]), s(xy[1]))
def sb(xy): return [s(xy[0]), s(xy[1]), s(xy[2]), s(xy[3])]

def rr(x0,y0,x1,y1, r=12, fill=None, outline=None, lw=1):
    draw.rounded_rectangle(sb([x0,y0,x1,y1]), radius=s(r), fill=fill, outline=outline, width=s(lw))

def rx(x0,y0,x1,y1, fill=None):
    draw.rectangle(sb([x0,y0,x1,y1]), fill=fill)

def tx(x,y, txt, sz=12, bold=False, col="#0F172A", anc="la"):
    draw.text(sp([x,y]), str(txt), font=f(sz,bold), fill=col, anchor=anc)

def dot(cx,cy, r, fill):
    draw.ellipse([s(cx)-s(r), s(cy)-s(r), s(cx)+s(r), s(cy)+s(r)], fill=fill)

def vgrad(x0,y0,x1,y1, top, bot):
    ht = y1-y0
    r0,g0,b0 = int(top[1:3],16),int(top[3:5],16),int(top[5:7],16)
    r1,g1,b1 = int(bot[1:3],16),int(bot[3:5],16),int(bot[5:7],16)
    for i in range(ht):
        t = i/max(ht-1,1)
        clr=(int(r0+(r1-r0)*t), int(g0+(g1-g0)*t), int(b0+(b1-b0)*t))
        draw.rectangle([s(x0),s(y0+i),s(x1),s(y0+i+1)], fill=clr)

# ─────────────────────────────────────────────
# PHONE BACKGROUND
# ─────────────────────────────────────────────
rx(0,0,390,1460, fill="#EEF2F7")

# ─────────────────────────────────────────────
# STATUS BAR
# ─────────────────────────────────────────────
rx(0,0,390,38, fill="#0C1F4A")
tx(22,12, "9:41", sz=12, bold=True, col="white")
# battery outline
rr(334,13,358,25, r=3, outline="#FFFFFF88", fill=None, lw=1)
rx(335,14,354,24, fill="white")
rx(358,16,361,22, fill="#FFFFFF66")
# signal bars
for i,h in enumerate([4,6,8,10]):
    rx(295+i*6, 26-h, 299+i*6, 26, fill="white" if i<3 else "#FFFFFF55")

# ─────────────────────────────────────────────
# HERO HEADER
# ─────────────────────────────────────────────
vgrad(0,38,390,212, "#0C1F4A","#1A5FD4")
dot(355,60, 70, "#1A2F6A")   # decorative blobs
dot(28,185, 48, "#0E4AA8")

# Logo box
rr(20,53,54,87, r=8, fill="#FFFFFF22", outline="#FFFFFF33")
tx(37,70, "P", sz=15, bold=True, col="white", anc="mm")
tx(61,64, "PANDHAL", sz=13, bold=True, col="white")

# Notification bell
rr(320,53,356,87, r=10, fill="#FFFFFF18", outline="#FFFFFF22")
tx(338,70, "n", sz=14, bold=True, col="white", anc="mm")  # bell placeholder
# real bell shape via text approximation
tx(338,70, "Bell", sz=9, col="#FFFFFF99", anc="mm")
# badge
dot(354,53, 7, "#EF4444")
tx(354,53, "3", sz=8, bold=True, col="white", anc="mm")

# Avatar
rr(360,53,386,87, r=10, fill="#06B6D4")
tx(373,70, "SG", sz=11, bold=True, col="white", anc="mm")

# Role chip
rr(20,102,162,120, r=9, fill="#FFFFFF22", outline="#FFFFFF33")
dot(31,111, 4, "#34D399")
tx(40,111, "CEO   |   Super Admin", sz=9, bold=True, col="#FFFFFFDD", anc="lm")

# Greeting
tx(20,129, "Good morning, Sajan George.", sz=18, bold=True, col="white")
tx(20,154, "Friday, 27 March 2026   |   Pandhal Industries", sz=11, col="#FFFFFF88")

# ─────────────────────────────────────────────
# BODY (overlaps hero)
# ─────────────────────────────────────────────
BY = 180

# ── FIRE ALERT BANNER ──
rr(16,BY, 374,BY+62, r=12, fill="#FEF2F2", outline="#FECACA")
rx(16,BY,21,BY+62, fill="#DC2626")               # accent bar
rr(27,BY+9, 61,BY+53, r=9, fill="#DC2626")        # icon bg
tx(44,BY+31, "FIRE", sz=9, bold=True, col="white", anc="mm")
tx(69,BY+16, "Fire Sensor Alert  -  Zone B3, Packing Hall", sz=11, bold=True, col="#991B1B")
tx(69,BY+34, "Triggered 14 min ago  |  Status: Investigating  |  Tap to view", sz=10, col="#B91C1C")
tx(360,BY+31, ">", sz=18, bold=True, col="#DC2626", anc="mm")

# ── GLANCE STATS SECTION ──
SY = BY + 76
tx(16,SY, "Today at a Glance", sz=13, bold=True)
tx(374,SY, "27 Mar 2026", sz=11, col="#64748B", anc="ra")

SY2 = SY+20
CW2,CH2,GAP = 174,84,10

STATS = [
    ("#EFF6FF","#1A5FD4","14", "Visitors Today",    "+3 new","#D1FAE5","#059669"),
    ("#D1FAE5","#059669","38", "Machines Active",   "92%",   "#D1FAE5","#059669"),
    ("#FEE2E2","#DC2626","3",  "Active Alerts",     "1 crit","#FEE2E2","#DC2626"),
    ("#FEF3C7","#D97706","78%","Training Done",     "78%",   "#F1F5F9","#64748B"),
    ("#F0FDF4","#059669","2.84L","Outlet Sales Today","Today","#F0FDF4","#059669"),
    ("#F5F3FF","#6D28D9","142","Cust. Interactions","Today","#EDE9FE","#6D28D9"),
]
for i,(ibg,icol,val,lbl,pill,pbg,pcol) in enumerate(STATS):
    col,row = i%2, i//2
    cx = 16+col*(CW2+GAP)
    cy = SY2+row*(CH2+GAP)
    rr(cx,cy,cx+CW2,cy+CH2, r=14, fill="white")
    rr(cx+10,cy+10,cx+46,cy+46, r=10, fill=ibg)
    tx(cx+28,cy+28, val[:1], sz=13, bold=True, col=icol, anc="mm")  # small icon stand-in
    rr(cx+CW2-62,cy+10,cx+CW2-8,cy+27, r=8, fill=pbg)
    tx(cx+CW2-35,cy+18, pill, sz=9, bold=True, col=pcol, anc="mm")
    tx(cx+12,cy+52, val, sz=22, bold=True, col="#0F172A")
    tx(cx+12,cy+73, lbl, sz=10, col="#64748B")

# ── OPERATIONS MODULES ──
MY = SY2 + 3*(CH2+GAP) + 14
tx(16,MY, "Operations Modules", sz=13, bold=True)

MODS = [
  # (icon_txt, icon_bg, icon_col, title, desc, v1,l1,vc1, v2,l2,vc2, v3,l3,vc3, bar_col)
  ("VM","#EFF6FF","#1A5FD4",
   "Visitor Management",
   "14 visitors today  |  Production, QA & Admin  |  9 checked in  |  5 pending",
   "14","Scheduled","#0F172A",  "9","Checked In","#059669",  "5","Pending","#D97706",
   "#10B981"),

  ("SF","#EDE9FE","#6D28D9",
   "Shopfloor & Sensor Summary",
   "4,280 packs today  |  2 metal detection alerts  |  38 of 41 machines running",
   "4,280","Packs Today","#1A5FD4",  "2","Metal Alerts","#D97706",  "92%","Utilisation","#059669",
   "#F59E0B"),

  ("AL","#FEE2E2","#DC2626",
   "Alerts & Notifications",
   "1 critical fire sensor event  |  2 sensor warnings  |  Zone B3 under review",
   "1","Critical","#DC2626",  "2","Warnings","#D97706",  "18","Today Total","#0F172A",
   "#EF4444"),

  ("LM","#FEF3C7","#D97706",
   "Learning Management",
   "78% mandatory training complete  |  12 certifications due  |  6 departments",
   "78%","Completion","#0F172A",  "12","Certs Due","#D97706",  "34","Certified","#059669",
   "#1A5FD4"),

  ("OT","#F0FDF4","#059669",
   "Outlet Management",
   "Sales: Rs.2.84L today  |  142 customer interactions  |  Avg order Rs.320  |  8 outlets",
   "2.84L","Sales Today","#059669",  "142","Customers","#6D28D9",  "Rs.320","Avg Order","#0F172A",
   "#059669"),
]

mc_y = MY+18
MCH  = 116

for m in MODS:
    (itxt,ibg,icol, title,desc,
     v1,l1,vc1, v2,l2,vc2, v3,l3,vc3, bar) = m

    rr(16,mc_y,374,mc_y+MCH, r=16, fill="white")
    rx(16,mc_y+MCH-4,374,mc_y+MCH, fill=bar)      # color bottom bar
    rr(26,mc_y+12,66,mc_y+52, r=13, fill=ibg)
    tx(46,mc_y+32, itxt, sz=11, bold=True, col=icol, anc="mm")
    tx(74,mc_y+14, title, sz=13, bold=True)
    tx(74,mc_y+33, desc, sz=10, col="#64748B")
    rr(346,mc_y+13,368,mc_y+35, r=8, fill="#EEF2F7")
    tx(357,mc_y+24, ">", sz=14, bold=True, col="#94A3B8", anc="mm")

    # divider
    rx(16,mc_y+57,374,mc_y+58, fill="#E2E8F0")

    # 3-column stats
    cw3 = (374-16)//3
    for j,(val,lbl,vc) in enumerate([(v1,l1,vc1),(v2,l2,vc2),(v3,l3,vc3)]):
        sx = 16 + j*cw3 + cw3//2
        tx(sx,mc_y+74, val, sz=16, bold=True, col=vc, anc="mm")
        tx(sx,mc_y+95, lbl, sz=9,  bold=False, col="#64748B", anc="mm")
        if j < 2:
            rx(16+(j+1)*cw3, mc_y+60, 17+(j+1)*cw3, mc_y+MCH-7, fill="#E2E8F0")

    mc_y += MCH+10

# ── FUTURE MODULES ──
FY = mc_y+6
tx(16,FY, "Coming Soon", sz=13, bold=True)
tx(374,FY, "Future Modules", sz=11, col="#94A3B8", anc="ra")

FUTURE = [
    ("AST","Asset Management"),
    ("CMP","Compliance Mgmt"),
    ("ESG","ESG / Sustainability"),
    ("WRK","Workforce Analytics"),
    ("SCM","Supply Chain"),
    ("INC","Incident Reporting"),
]
FCW,FCH2 = 174,80
FY2 = FY+20
for i,(code,name) in enumerate(FUTURE):
    col,row = i%2, i//2
    fx = 16+col*(FCW+GAP)
    fy = FY2+row*(FCH2+GAP)
    rr(fx,fy,fx+FCW,fy+FCH2, r=13, fill="#FFFFFF", outline="#E2E8F0")
    rr(fx+10,fy+10,fx+44,fy+44, r=10, fill="#F1F5F9")
    tx(fx+27,fy+27, code, sz=9, bold=True, col="#94A3B8", anc="mm")
    tx(fx+12,fy+52, name, sz=11, bold=True, col="#64748B")
    rr(fx+10,fy+66,fx+82,fy+77, r=9, fill="#F1F5F9")
    tx(fx+46,fy+71, "COMING SOON", sz=7, bold=True, col="#94A3B8", anc="mm")

# ── BOTTOM NAV ──
NV = FY2+3*(FCH2+GAP)+12
rx(0,NV,390,NV+1, fill="#E2E8F0")
rx(0,NV+1,390,NV+75, fill="white")

NAV = [("Home","Dashboard",True),("Usr","Visitors",False),
       ("Fct","Shopfloor",False),("Bel","Alerts",False),("Bk","Learn",False)]
nw2 = 390//len(NAV)
for i,(ico,lbl,act) in enumerate(NAV):
    nx = i*nw2+nw2//2
    col="#1A5FD4" if act else "#94A3B8"
    rr(nx-16,NV+6,nx+16,NV+30, r=8, fill="#EFF6FF" if act else None)
    tx(nx,NV+18, ico, sz=9, bold=True, col=col, anc="mm")
    tx(nx,NV+38, lbl, sz=9, bold=act, col=col, anc="mm")
    if act:
        dot(nx,NV+58, 3, "#1A5FD4")

# ── CROP & SAVE ──
final_h = (NV+75)*SCALE
out_img = img.crop([0,0,W*SCALE, final_h])
out_path = "/home/user/Sample_1_visitor-management/pandhal-enterprise-app/dashboard.png"
out_img.save(out_path, "PNG", dpi=(144,144))
print(f"Saved: {out_path}  ({out_img.width} x {out_img.height} px @2x)")
