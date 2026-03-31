#!/usr/bin/env python3
"""Generate 3 Edulink Kerala Science Coaching flyer designs."""

from PIL import Image, ImageDraw, ImageFont
import math

FREG  = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
FBOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FW    = 1080
FH    = 1440

# Brand colours
RED   = "#E8001D"
BLUE  = "#0033CC"
GRAY  = "#555555"
WHITE = "#FFFFFF"
BLACK = "#0A0A0A"

def font(size, bold=False):
    return ImageFont.truetype(FBOLD if bold else FREG, size)

def draw_logo(draw, x, y, scale=1.0):
    """Draw EDU(red) LINK(blue) text logo."""
    sz = int(72 * scale)
    sub = int(22 * scale)
    draw.text((x, y),       "EDU",    font=font(sz, bold=True), fill=RED)
    draw.text((x + int(148*scale), y), "LINK",   font=font(sz, bold=True), fill=BLUE)
    draw.text((x + int(250*scale), y + int(48*scale)), "KERALA", font=font(sub, bold=True), fill=GRAY)

def draw_star_bg(draw, w, h, color, count=18, alpha=30):
    """Draw subtle dot grid as science atmosphere."""
    for i in range(count):
        for j in range(count):
            cx = int(w * i / count)
            cy = int(h * j / count)
            r = 2
            draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color)

def rounded_rect(draw, x0, y0, x1, y1, r=20, fill=None, outline=None, width=2):
    draw.rounded_rectangle([x0,y0,x1,y1], radius=r, fill=fill, outline=outline, width=width)

def program_box(draw, x, y, w, h, tag, name, desc, tag_bg, tag_fg, border_col):
    rounded_rect(draw, x, y, x+w, y+h, r=18, fill=WHITE, outline=border_col, width=3)
    # Tag pill
    rounded_rect(draw, x+20, y+20, x+20+len(tag)*18+20, y+54, r=14, fill=tag_bg)
    draw.text((x+30, y+26), tag, font=font(22, bold=True), fill=tag_fg)
    draw.text((x+20, y+66), name, font=font(26, bold=True), fill=BLACK)
    # wrap desc
    words = desc.split()
    lines, line = [], ""
    for w2 in words:
        test = (line + " " + w2).strip()
        if font(18).getlength(test) < w - 50:
            line = test
        else:
            lines.append(line); line = w2
    lines.append(line)
    for k, ln in enumerate(lines[:4]):
        draw.text((x+20, y+100+k*26), ln, font=font(18), fill="#444444")

# ═══════════════════════════════════════════════════════════════════
# FLYER 1 — Clean White Professional
# ═══════════════════════════════════════════════════════════════════
def flyer1():
    img  = Image.new("RGB", (FW, FH), "#F8F9FF")
    draw = ImageDraw.Draw(img)

    # Top accent bar
    draw.rectangle([0, 0, FW, 10], fill=RED)
    draw.rectangle([0, 10, FW, 18], fill=BLUE)

    # Subtle dot grid
    for i in range(0, FW, 55):
        for j in range(0, FH, 55):
            draw.ellipse([i-2,j-2,i+2,j+2], fill="#DDDDEE")

    # Logo
    draw_logo(draw, 60, 40, scale=1.0)

    # Hero headline
    draw.rectangle([0, 155, FW, 165], fill="#EEEEEE")
    draw.text((60, 185), "Science & Physics", font=font(72, bold=True), fill=BLUE)
    draw.text((60, 265), "Coaching", font=font(72, bold=True), fill=RED)
    draw.text((60, 355), "Classes 5 to 10", font=font(36, bold=True), fill=GRAY)

    # Tagline banner
    draw.rectangle([0, 415, FW, 485], fill=BLUE)
    tagline = "From Good to Great.  From Great to Exceptional."
    draw.text((FW//2, 450), tagline, font=font(26, bold=True), fill=WHITE, anchor="mm")

    # Highlights row
    highlights = [("🎓","Industry\nProfessionals"), ("🔬","Analytical &\nApplied Focus"), ("🏆","Competitive\nChampions")]
    for i,(ic,lb) in enumerate(highlights):
        bx = 40 + i*340
        rounded_rect(draw, bx, 505, bx+300, 625, r=16, fill=WHITE, outline="#CCDDFF", width=2)
        draw.text((bx+150, 530), ic, font=font(32), fill=BLUE, anchor="mm")
        for k,ln in enumerate(lb.split("\n")):
            draw.text((bx+150, 566+k*24), ln, font=font(19, bold=True), fill="#222244", anchor="mm")

    # Program cards
    draw.text((60, 650), "Our Programs", font=font(34, bold=True), fill=BLACK)
    draw.line([(60,690),(400,690)], fill=RED, width=3)

    program_box(draw, 40, 710, 470, 240, "CORE", "Complete Curriculum",
        "In-depth coverage of every topic in the school syllabus. Build strong "
        "fundamentals with clarity and confidence.",
        RED, WHITE, RED)
    program_box(draw, 560, 710, 470, 240, "BEYOND", "Beyond the Classroom",
        "Designed for future scientists and competitive exam champions. Advanced "
        "concepts, problem solving and research thinking.",
        BLUE, WHITE, BLUE)

    # Class grid
    draw.text((60, 975), "Available for Classes", font=font(28, bold=True), fill=BLACK)
    classes = ["Class 5","Class 6","Class 7","Class 8","Class 9","Class 10"]
    for i,cl in enumerate(classes):
        col,row = i%3, i//2
        bx = 40 + col*340; by = 1015 + row*82
        rounded_rect(draw, bx, by, bx+300, by+66, r=12,
                     fill=BLUE if i%2==0 else RED, outline=None)
        draw.text((bx+150, by+33), cl, font=font(22, bold=True), fill=WHITE, anchor="mm")

    # Tagline bottom
    draw.rectangle([0, 1215, FW, 1310], fill="#0A0A2A")
    draw.text((FW//2, 1252), "Transforming Students.", font=font(34, bold=True), fill=WHITE, anchor="mm")
    draw.text((FW//2, 1291), "Shaping Future Scientists & Champions.", font=font(24), fill="#AABBFF", anchor="mm")

    # Contact / CTA
    rounded_rect(draw, 40, 1330, FW-40, 1400, r=20, fill=RED)
    draw.text((FW//2, 1365), "Enrol Now  |  Online Classes  |  Edulink Kerala", font=font(26, bold=True), fill=WHITE, anchor="mm")

    # Bottom bar
    draw.rectangle([0, FH-12, FW, FH], fill=BLUE)

    img.save("/home/user/Sample_1_visitor-management/edulink-flyers/flyer1_clean_white.png", dpi=(150,150))
    print("Saved flyer1_clean_white.png")

# ═══════════════════════════════════════════════════════════════════
# FLYER 2 — Dark Navy Premium
# ═══════════════════════════════════════════════════════════════════
def flyer2():
    img  = Image.new("RGB", (FW, FH), "#06081A")
    draw = ImageDraw.Draw(img)

    # Star field dots
    import random; random.seed(42)
    for _ in range(200):
        x,y = random.randint(0,FW), random.randint(0,FH)
        r   = random.choice([1,1,1,2])
        draw.ellipse([x-r,y-r,x+r,y+r], fill="#FFFFFF22")

    # Top gradient band
    for i in range(120):
        t = i/119
        r2 = int(0x0+(0x0)*t); g2 = int(0x08+0x10*t); b2 = int(0x1A+0x60*t)
        draw.line([(0,i),(FW,i)], fill=(r2,g2,b2,255))

    # Logo on dark
    draw.text((60, 32), "EDU",    font=font(72, bold=True), fill=RED)
    draw.text((208, 32), "LINK",   font=font(72, bold=True), fill="#4488FF")
    draw.text((310, 80), "KERALA", font=font(22, bold=True), fill="#AAAAAA")

    # Glowing circle accent
    for r3 in range(160, 60, -8):
        alpha = int(255*(1-(r3-60)/100)*0.06)
        draw.ellipse([FW-r3-80, 30-r3+80, FW+r3-80, 30+r3+80],
                     outline=(68,136,255,alpha) if alpha>0 else None)

    # Main headline
    draw.text((60, 155), "Science &", font=font(80, bold=True), fill=WHITE)
    draw.text((60, 243), "Physics", font=font(80, bold=True), fill="#4488FF")
    draw.text((60, 331), "Coaching", font=font(80, bold=True), fill=RED)
    draw.text((62, 426), "Classes 5 — 10  |  Online", font=font(30), fill="#AABBCC")

    # Separator line
    draw.line([(60,475),(FW-60,475)], fill="#4488FF", width=2)

    # Tagline
    draw.text((FW//2, 510), '"From Good to Great.', font=font(30, bold=True), fill="#FFDD88", anchor="mm")
    draw.text((FW//2, 548), 'From Great to Exceptional."', font=font(30, bold=True), fill="#FFDD88", anchor="mm")

    # Feature chips
    chips = ["Industry Professionals", "Exceptional Academics",
             "Analytical Focus", "Applied Learning",
             "Competitive Champions", "Future Scientists"]
    cols  = ["#FF3355","#4488FF","#FF3355","#4488FF","#FF3355","#4488FF"]
    for i,(ch,col3) in enumerate(zip(chips,cols)):
        cx,cy = 40 + (i%2)*530, 590 + (i//2)*64
        rounded_rect(draw, cx, cy, cx+490, cy+50, r=25, fill=col3+"33", outline=col3, width=2)
        draw.text((cx+245, cy+25), ch, font=font(22, bold=True), fill=WHITE, anchor="mm")

    # Program cards dark
    draw.text((60, 800), "Choose Your Program", font=font(30, bold=True), fill=WHITE)
    for i,(tag,name,desc,col4) in enumerate([
        ("CORE","Complete Curriculum",
         "Full syllabus coverage in depth — every concept explained clearly for strong academic performance.",
         RED),
        ("BEYOND","Beyond the Curriculum",
         "Advanced physics concepts, research thinking, and competitive exam preparation for future champions.",
         "#4488FF")]):
        bx = 40 + i*520; by = 848
        rounded_rect(draw, bx, by, bx+480, by+230, r=18,
                     fill="#10152E", outline=col4, width=3)
        rounded_rect(draw, bx+20, by+18, bx+20+len(tag)*16+24, by+52, r=12, fill=col4)
        draw.text((bx+32, by+24), tag, font=font(22, bold=True), fill=WHITE)
        draw.text((bx+20, by+62), name, font=font(24, bold=True), fill=WHITE)
        words = desc.split(); lines2=[]; ln2=""
        for w3 in words:
            t2=(ln2+" "+w3).strip()
            if font(17).getlength(t2)<440: ln2=t2
            else: lines2.append(ln2); ln2=w3
        lines2.append(ln2)
        for k,l2 in enumerate(lines2[:4]):
            draw.text((bx+20, by+96+k*28), l2, font=font(17), fill="#AABBCC")

    # Class badges
    draw.text((60,1100), "Classes", font=font(28, bold=True), fill=WHITE)
    cls2 = ["5","6","7","8","9","10"]
    for i,cl2 in enumerate(cls2):
        cx2 = 60+i*160; cy2 = 1140
        draw.ellipse([cx2,cy2,cx2+80,cy2+80],
                     fill=RED if i%2==0 else "#4488FF")
        draw.text((cx2+40,cy2+40), cl2, font=font(26,bold=True), fill=WHITE, anchor="mm")
        draw.text((cx2+40,cy2+90), "Class", font=font(16), fill="#AAAAAA", anchor="mm")

    # Bottom CTA
    draw.rectangle([0,1260,FW,1440], fill="#0D1035")
    draw.line([(0,1260),(FW,1260)], fill="#4488FF", width=3)
    draw.text((FW//2,1300), "Edulink Kerala", font=font(44, bold=True), fill=WHITE, anchor="mm")
    draw.text((FW//2,1354), "Online Science & Physics Coaching", font=font(26), fill="#AABBCC", anchor="mm")
    rounded_rect(draw, FW//2-180,1385, FW//2+180, 1430, r=22, fill=RED)
    draw.text((FW//2,1407), "Enrol Now", font=font(28, bold=True), fill=WHITE, anchor="mm")

    img.save("/home/user/Sample_1_visitor-management/edulink-flyers/flyer2_dark_premium.png", dpi=(150,150))
    print("Saved flyer2_dark_premium.png")

# ═══════════════════════════════════════════════════════════════════
# FLYER 3 — Bold Gradient Energy
# ═══════════════════════════════════════════════════════════════════
def flyer3():
    img  = Image.new("RGB", (FW, FH), WHITE)
    draw = ImageDraw.Draw(img)

    # Gradient top half
    for i in range(560):
        t = i/559
        r4 = int(0x00 + (0x00)*t)
        g4 = int(0x10 + (0x50)*t)
        b4 = int(0x80 + (0x60)*t)
        draw.line([(0,i),(FW,i)], fill=(r4,g4,b4))

    # Diagonal accent
    draw.polygon([(0,380),(FW,300),(FW,560),(0,560)], fill="#F8F9FF")
    draw.polygon([(0,400),(FW,320),(FW,560),(0,560)], fill=WHITE)

    # Logo white on gradient
    draw.text((55, 38), "EDU",    font=font(72, bold=True), fill="#FF4466")
    draw.text((203, 38), "LINK",   font=font(72, bold=True), fill=WHITE)
    draw.text((305, 86), "KERALA", font=font(22, bold=True), fill="#BBDDFF")

    # Tagline strip on gradient
    draw.text((55, 145), "Transform Average to Good.", font=font(34, bold=True), fill=WHITE)
    draw.text((55, 188), "Transform Good to the Best.", font=font(34, bold=True), fill="#FFEE88")

    # Science atom decoration (top right)
    cx5,cy5 = 920,115
    draw.ellipse([cx5-8,cy5-8,cx5+8,cy5+8], fill=WHITE)
    for angle in [0,60,120]:
        rad = math.radians(angle)
        ex,ey = cx5+int(75*math.cos(rad)), cy5+int(35*math.sin(rad))
        draw.ellipse([ex-60,ey-25,ex+60,ey+25], outline=WHITE, width=2)
        draw.ellipse([cx5-75,cy5-35,cx5+75,cy5+35], outline="#FFFFFF44", width=2)
    for a2 in [30,120,210,300]:
        r5 = math.radians(a2)
        ex2,ey2 = cx5+int(72*math.cos(r5)),cy5+int(33*math.sin(r5))
        draw.ellipse([ex2-5,ey2-5,ex2+5,ey2+5], fill="#FFEE88")

    # Main subject block
    draw.text((55, 240), "Science &", font=font(78, bold=True), fill=WHITE)
    draw.text((55, 326), "Physics", font=font(78, bold=True), fill="#FFEE88")

    # White section
    draw.text((55, 590), "Online Coaching  |  Classes 5 to 10", font=font(30, bold=True), fill=BLUE)

    # USP row
    usps = [("🏛","By Industry\nProfessionals"), ("📊","Analytical &\nApplied Skills"), ("🚀","Built for\nFuture Champions")]
    for i,(ic,lb) in enumerate(usps):
        bx2 = 40+i*343
        rounded_rect(draw, bx2, 650, bx2+316, 778, r=18,
                     fill=["#FFF0F3","#F0F4FF","#FFF8E8"][i],
                     outline=[RED,BLUE,"#D97706"][i], width=2)
        draw.text((bx2+158,680), ic, font=font(28), fill="black", anchor="mm")
        for k2,ln3 in enumerate(lb.split("\n")):
            draw.text((bx2+158,715+k2*28), ln3, font=font(19,bold=True),
                      fill=[RED,BLUE,"#A05000"][i], anchor="mm")

    # Divider
    draw.line([(55,800),(FW-55,800)], fill="#DDDDDD", width=2)

    # Programs — side by side bold cards
    draw.text((55,820), "Our Signature Programs", font=font(32, bold=True), fill=BLACK)

    cards = [
        (40,  870, RED,   BLUE,  "CORE",
         "Complete Curriculum",
         ["Full syllabus — every chapter,","every concept in depth.",
          "Build unshakeable fundamentals","for board exams and beyond."]),
        (560, 870, BLUE,  RED,   "BEYOND",
         "Beyond Curriculum",
         ["Advanced physics concepts for","competitive exam champions.",
          "Research thinking, applied","problem solving & innovation."]),
    ]
    for bx3,by2,pill_col,name_col,tag2,name2,lines3 in cards:
        rounded_rect(draw, bx3,by2, bx3+470, by2+290, r=20, fill=WHITE,
                     outline=pill_col, width=3)
        rounded_rect(draw, bx3+20,by2+18, bx3+20+len(tag2)*20+24, by2+56, r=14, fill=pill_col)
        draw.text((bx3+32,by2+24), tag2, font=font(24,bold=True), fill=WHITE)
        draw.text((bx3+20,by2+68), name2, font=font(25,bold=True), fill=name_col)
        draw.line([(bx3+20,by2+100),(bx3+450,by2+100)], fill="#EEEEEE", width=1)
        for k3,ln4 in enumerate(lines3):
            draw.text((bx3+20,by2+112+k3*38), ln4, font=font(20), fill="#333333")

    # Class tags
    draw.text((55,1185), "Enrol for:", font=font(26, bold=True), fill=BLACK)
    cls3 = ["Class 5","Class 6","Class 7","Class 8","Class 9","Class 10"]
    pill_cols = [RED,BLUE,RED,BLUE,RED,BLUE]
    for i,(cl3,pc) in enumerate(zip(cls3,pill_cols)):
        bx4 = 40+(i%3)*343; by3 = 1220+(i//3)*62
        rounded_rect(draw, bx4,by3, bx4+316,by3+50, r=25, fill=pc)
        draw.text((bx4+158,by3+25), cl3, font=font(22,bold=True), fill=WHITE, anchor="mm")

    # Bottom CTA strip
    draw.rectangle([0,1368,FW,1440], fill="#06081A")
    draw.text((FW//2,1395), "Edulink Kerala — Online Science & Physics Coaching", font=font(23,bold=True), fill=WHITE, anchor="mm")
    draw.text((FW//2,1428), "Enrol Now  |  Classes 5 to 10  |  Core & Beyond Programs", font=font(19), fill="#AABBCC", anchor="mm")

    img.save("/home/user/Sample_1_visitor-management/edulink-flyers/flyer3_gradient_energy.png", dpi=(150,150))
    print("Saved flyer3_gradient_energy.png")

# Run all
flyer1()
flyer2()
flyer3()
print("All 3 flyers generated successfully.")
