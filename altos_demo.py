"""ALTOS demo: /projects/altos-demo/ (Butch 2026-11-19, "Four-role tour").

A click-through copy of ALTOS that runs only in the visitor's browser: made-up LGU, officers, taxpayers and
amounts, no server, no database, nothing saved (reloading starts fresh). It copies the LOOK and the steps of
ALTOS (colours, sign-in panel, side menu, page colours per account) but none of the real ALTOS code.

Rules (project memory): label it a demo with sample data on every screen; ALTOS is only tested on the developer
side, never claim it is used in actual treasury work; never name a real LGU; no ads on this page, so the page is
written here on its own, without the site layout (the AdSense code lives in pages.layout).
The screens are drawn by static/altos-demo.js.
"""

import json
import math

import tags as t
from content import SITE
from tags import Raw

DEMO_URL = "/projects/altos-demo/"
DEMO_TITLE = "ALTOS Demo"
DEMO_DESCRIPTION = ("Try a demo of ALTOS, the Automated Local Treasury Operations System, with made-up data: issue an "
                    "official receipt, close the day's RCD, count the money, write a check and see the Cash Book.")

ALTOS_COLORS = ("#ffd27a", "#7cc2ff", "#4be3a8", "#ff8a8a", "#d1b6ff")  # the five letters, as on the ALTOS sign-in page
TINTS = {"col": "#7cc2ff", "lo": "#4be3a8", "do": "#ff8a8a", "sys": "#d1b6ff"}


def _arc(cx, cy, rr, start, ext):
    a1, a2 = math.radians(start), math.radians(start + ext)
    return (f"M{cx + rr * math.cos(a1):.2f},{cy - rr * math.sin(a1):.2f} A{rr},{rr} 0 {1 if abs(ext) > 180 else 0} "
            f"{0 if ext > 0 else 1} {cx + rr * math.cos(a2):.2f},{cy - rr * math.sin(a2):.2f}")


def _emblem_inner():
    """The peso sign and 360 degrees as two linked rings, the ALTOS emblem."""
    r, gap, ax, ay = 40, 64, 52, 52
    bx = ax + gap
    gold, em = ("#8a5a00", "#e0a800", "#ffe58a"), ("#06604a", "#19c18c", "#b8f5dc")

    def link(cx, cy, c, start=None, ext=None):
        out = ""
        for w, col in ((13, c[0]), (9, c[1])):
            out += (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}"/>' if start is None else
                    f'<path d="{_arc(cx, cy, r, start, ext)}" fill="none" stroke="{col}" stroke-width="{w}"/>')
        hs, he = (95, 110) if start is None else (start, ext)
        return out + f'<path d="{_arc(cx, cy, r - 2, hs, he)}" fill="none" stroke="{c[2]}" stroke-width="2"/>'

    th = math.degrees(math.acos(gap / 2 / r))
    cr, ccx, ccy = 21, bx + 8, ay
    a = math.radians(110 - 320)
    ex, ey = ccx + cr * math.cos(a), ccy - cr * math.sin(a)
    tx, ty, nx, ny = math.sin(a), math.cos(a), math.cos(a), -math.sin(a)
    tri = (f"{ex + tx * 7:.1f},{ey + ty * 7:.1f} {ex + nx * 5 - tx * 2:.1f},{ey + ny * 5 - ty * 2:.1f} "
           f"{ex - nx * 5 - tx * 2:.1f},{ey - ny * 5 - ty * 2:.1f}")
    return (f'<ellipse cx="{(ax + bx) / 2}" cy="{ay}" rx="{gap / 2 + r + 12}" ry="{r + 12}" fill="rgba(255,255,255,.10)"/>'
            f'<circle cx="{ax}" cy="{ay}" r="{r - 5}" fill="#fff8dc"/><circle cx="{bx}" cy="{ay}" r="{r - 5}" fill="#eafff6"/>'
            f'{link(ax, ay, gold)}{link(bx, ay, em)}{link(ax, ay, gold, -th - 16, 32)}'
            f'<text x="{ax - 12}" y="{ay + 12}" font-family="Helvetica,Arial,sans-serif" font-weight="bold" font-size="34" '
            f'text-anchor="middle" fill="#7a4f00">&#8369;</text>'
            f'<path d="{_arc(ccx, ccy, cr, 110, -320)}" fill="none" stroke="{em[0]}" stroke-width="3"/><polygon points="{tri}" fill="{em[0]}"/>'
            f'<text x="{ccx - 4}" y="{ccy + 5}" font-family="Helvetica,Arial,sans-serif" font-weight="bold" font-size="15" '
            f'text-anchor="middle" fill="#17418f">360</text>'
            f'<text x="{ccx + 14}" y="{ccy + 1}" font-family="Helvetica,Arial,sans-serif" font-weight="bold" font-size="17" '
            f'text-anchor="middle" fill="#0b1f4d">&#176;</text>')


def brand_svg():
    """The emblem with the word ALTOS in its five colours, joined by a band that ends in an arrow."""
    x, cy, base = 177, 52, 77.5
    uy, w = base + 7.8, 4
    starts = (0, 62, 108, 158, 230)
    end = x + 279 + 18
    sx, sy = 116 + 40 * math.cos(math.radians(38)), cy + 40 * math.sin(math.radians(38))
    shadow = "#0d244f"
    curve = f"M{sx:.1f},{sy:.1f} C{sx + 10:.1f},{uy - 1:.1f} {x - 6},{uy:.1f} {x + 2},{uy:.1f}"
    shade = f"M{sx + 2:.1f},{sy + 2:.1f} C{sx + 12:.1f},{uy + 1:.1f} {x - 4},{uy + 2:.1f} {x + 4},{uy + 2:.1f}"
    segs = ""
    for i, col in enumerate(ALTOS_COLORS):
        x1 = x + starts[i]
        x2 = (end - 12.8) if i == 4 else x + starts[i + 1]
        segs += f'<line x1="{x1}" y1="{uy:.1f}" x2="{x2:.1f}" y2="{uy:.1f}" stroke="{col}" stroke-width="{w}"/>'
    tip = (f'<polygon points="{end},{uy:.1f} {end - 14.4:.1f},{uy - 6.4:.1f} {end - 12.8:.1f},{uy:.1f} {end - 14.4:.1f},{uy + 6.4:.1f}" '
           f'fill="{ALTOS_COLORS[4]}"/>')
    font = ('font-family="\'Avenir Next\',Avenir,\'Segoe UI\',\'Helvetica Neue\',Helvetica,Arial,sans-serif" '
            'font-weight="700" font-size="80"')
    letters = "".join(f'<text x="{x + st + 3}" y="{base + 3}" fill="{shadow}" {font}>{ch}</text>' for ch, st in zip("ALTOS", starts))
    letters += "".join(f'<text x="{x + st}" y="{base}" fill="{col}" {font}>{ch}</text>'
                       for ch, st, col in zip("ALTOS", starts, ALTOS_COLORS))
    return (f'<svg viewBox="0 0 500 104" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="ALTOS">'
            f'{_emblem_inner()}<path d="{shade}" fill="none" stroke="{shadow}" stroke-width="{w + 3}" stroke-linecap="round"/>'
            f'<line x1="{x + 2}" y1="{uy + 2:.1f}" x2="{end + 2}" y2="{uy + 2:.1f}" stroke="{shadow}" stroke-width="{w + 1}"/>'
            f'<path d="{curve}" fill="none" stroke="#06604a" stroke-width="{w + 3}" stroke-linecap="round"/>'
            f'<path d="{curve}" fill="none" stroke="#19c18c" stroke-width="{w}" stroke-linecap="round"/>{segs}{tip}{letters}</svg>')


# The look of ALTOS (its web pages): page colour per account, navy side menu, flat panels, square fields,
# striped tables. On a phone the side menu becomes a row of tabs that scrolls sideways.
CSS = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:16px;color:#1d2433;background:#f3f6fc;line-height:1.45}
h1,h2,h3,label,th,button,.btn,.badge,.pill,.side,.tab,.total,.banner h1,.banner .pos{font-family:"Avenir Next","Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:#1a56c4}
.demo-bar{background:#f2c230;color:#1b1b1b;font:600 14px/1.35 "Avenir Next","Segoe UI",Roboto,Helvetica,Arial,sans-serif;padding:7px 14px;display:flex;align-items:center;gap:6px 12px;flex-wrap:wrap}
.demo-bar b{font-weight:800;letter-spacing:.04em}
.demo-bar a{margin-left:auto;color:#1b1b1b;font-weight:700;white-space:nowrap}
/* sign-in page, with role buttons instead of a username and password */
.lg{display:flex;min-height:calc(100vh - 34px)}
.lg .panel{flex:56;position:relative;overflow:hidden;background:linear-gradient(180deg,#17418f,#5a33a8);color:#fff;padding:40px 6.7vw;display:flex;flex-direction:column;justify-content:center}
.lg .c1,.lg .c2,.lg .c3{position:absolute;border-radius:50%;background:rgba(255,255,255,.09)}
.lg .c1{width:60vh;height:60vh;right:-18vh;top:-18vh}.lg .c2{width:76vh;height:76vh;left:-30vh;bottom:-36vh}
.lg .c3{width:28vh;height:28vh;right:6vh;bottom:8vh;background:rgba(255,255,255,.12)}
.lg .in{position:relative}
.lg .brand svg{width:min(494px,100%);height:auto;display:block}
.lg .ttl{font-family:Helvetica,Arial,sans-serif;font-weight:800;font-size:clamp(20px,2.2vw,30px);line-height:1.25;margin-top:24px}
.lg .bar4{display:flex;width:min(420px,70%);margin:16px 0 0}.lg .bar4 i{flex:1;height:6px;margin-right:4px}
.lg .tag{font-size:19px;color:#e3e9f8;margin-top:18px}
.lg .motto{font-style:italic;color:#ffd6e6;font-size:16px;margin-top:10px;line-height:1.45}
.dev{display:inline-block;margin-top:28px;padding:6px 10px 8px;border-radius:8px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.22);position:relative}
.dev .by{font-size:12px;color:#c9d3ea}
.dev .nm{font-size:11px;color:#ffd27a;display:inline-block;padding-bottom:3px;border-bottom:3px solid;border-image:linear-gradient(90deg,#7cc2ff 25%,#4be3a8 25% 50%,#ff8a8a 50% 75%,#d1b6ff 75%) 1}
.lg .side2{flex:44;background:#f3f6fc;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:30px 18px}
.lguh{text-align:center;margin:0 0 18px;font-family:"Avenir Next","Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.lguh .rp{color:#8a93a6;font-size:11px;font-weight:700;letter-spacing:.14em}.lguh .pv{color:#6b7385;font-size:14px;margin-top:3px}
.lguh .nm{color:#17418f;font-size:21px;font-weight:700;letter-spacing:.04em;margin-top:2px}
.lguh .of{color:#c2185b;font-size:15px;font-weight:700;margin-top:2px}
.lcard{background:#fff;border-radius:22px;box-shadow:6px 10px 0 #dde2ec,3px 6px 0 #d3d9e5;padding:34px 34px 30px;width:min(400px,100%)}
.lcard h1{color:#1d2433;margin:0;line-height:1.05;font:bold 30px Helvetica,Arial,sans-serif}
.lcard .acc4{display:flex;gap:3px;margin:6px 0 4px}.lcard .acc4 i{width:22px;height:4px}
.lcard .note{color:#4a5266;font-size:15px;margin:8px 0 18px;line-height:1.4}
.role-btn{display:flex;align-items:center;gap:12px;width:100%;margin:0 0 10px;padding:12px 14px;border:0;border-radius:0;color:#fff;font:700 17px "Avenir Next","Segoe UI",Roboto,Helvetica,Arial,sans-serif;cursor:pointer;text-align:left}
.role-btn small{display:block;font:500 13px/1.3 -apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;opacity:.92;margin-top:2px}
.role-btn:hover,.role-btn:focus-visible{filter:brightness(1.08);outline:3px solid #1d2433;outline-offset:2px}
.lcard .rule{height:1px;background:#e6e9f0;margin:16px 0 12px}
.lcard .wp{color:#9aa1b2;font:bold 12px Helvetica,Arial,sans-serif;letter-spacing:.3px}
.lcard ol{margin:8px 0 0;padding-left:20px;color:#4a5266;font-size:14px}
.lfoot{text-align:center;margin-top:20px;color:#6b7385;font:14px "Avenir Next","Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.lfoot .cp{color:#9aa1b2;font-size:12px;margin-top:4px}.lfoot a{color:#6b7385}
/* working pages */
.top{display:flex;align-items:center;flex-wrap:wrap;gap:8px 14px;padding:10px 18px;background:var(--a)}
.badge{background:#fff;color:#c2185b;font-weight:700;font-size:19px;padding:2px 12px;letter-spacing:.3px}
.top .app{color:var(--appc);font-size:14px}
.top .pill:first-of-type{margin-left:auto}
.pill{background:var(--pill);color:#fff;text-decoration:none;font-size:13px;font-weight:700;padding:6px 14px;border:0;cursor:pointer}
.pill:hover{background:var(--pillh)}
.strip{display:flex;height:4px}.strip i{flex:1}
.wrap{display:flex;min-height:calc(100vh - 96px)}
.side{width:250px;flex:none;background:#1a2f66;padding:8px 0 20px;display:flex;flex-direction:column}
.side .head{color:var(--tint);font-weight:700;font-size:12px;letter-spacing:.3px;padding:16px 18px 4px}
.side a{display:block;color:#e8eef7;text-decoration:none;font-size:15px;padding:6px 18px 6px 21px;border-left:5px solid transparent;margin:1px 8px 1px 0}
.side a:hover{background:var(--sideh)}
.side a.on{background:var(--msel);border-left-color:var(--tint);font-weight:700;color:#fff}
.side a.homelink{font-size:22px;line-height:1.25;padding-top:8px;padding-bottom:8px}
.content{flex:1;min-width:0;padding:22px 26px 60px}
.content main{max-width:1100px}
.content h1{color:#1d2433;font-size:25px;font-weight:700;margin:0}
.content h1:after{content:"";display:block;width:64px;height:4px;background:var(--sel);margin:8px 0 16px}
h2{font-size:18px;margin:22px 0 8px;color:#1d2433}
.card{border:1px solid #d5dbe7;border-radius:2px;padding:16px;margin:12px 0;background:#fff}
.card>h2:first-child{color:var(--a);font-size:16px;margin-top:0}
.tbl{width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;margin:6px 0}
table{width:100%;border-collapse:collapse;background:#fff}
th{background:var(--a);color:#fff;text-align:left;font-size:14px;padding:7px 8px;white-space:nowrap}
td{border-bottom:1px solid #e3e8f1;padding:6px 8px;font-size:15px;vertical-align:top}
tr:nth-child(even) td{background:#f2f6ff}
tr.sum td{font-weight:800;background:#e8eefb}
.r{text-align:right;white-space:nowrap}
.c{text-align:center}.nw{white-space:nowrap}
.muted{color:#5b6b84;font-size:14px}
label{display:block;font-weight:600;font-size:14px;margin:10px 0 4px}
input,select,textarea{font:inherit;font-size:16px;padding:9px 10px;border:1px solid #c6cddb;border-radius:2px;width:100%;background:#fff;color:#1d2433}
input:focus,select:focus,textarea:focus{outline:none;border-color:var(--sel);box-shadow:0 0 0 1px var(--sel)}
input[type=checkbox]{width:auto;transform:scale(1.3);margin:0 8px 0 2px}
input[readonly]{background:#f2f4f8}
.row{display:flex;flex-wrap:wrap;gap:0 12px}.row>div{flex:1;min-width:160px}
button,.btn{display:inline-block;font-size:16px;font-weight:600;padding:9px 16px;border-radius:3px;border:1px solid #c6cddb;background:#fff;color:#1d2433;cursor:pointer;text-decoration:none;margin:8px 8px 0 0}
button:hover,.btn:hover{background:var(--hov);border-color:var(--sel)}
button.primary,.btn.primary{background:var(--sel);color:#fff;border-color:var(--sel);font-weight:700}
button.primary:hover,.btn.primary:hover{background:var(--a);border-color:var(--a)}
button.danger{color:#b00020;border-color:#e3a3ad}
button.small,.btn.small{padding:5px 11px;font-size:14px;margin:0}
button:disabled{opacity:.45;cursor:not-allowed}
.msg{padding:12px 14px;margin:10px 0;font-weight:600}.ok{background:#e6f4ea;color:#0f6b45}
.bad{background:#f8d7da;color:#8a1328}.warn{background:#fff3cd;color:#7a5600}.info{background:#e6efff;color:#23406e}
.total{font-size:22px;font-weight:800;color:var(--a)}
.banner{position:relative;overflow:hidden;border-radius:14px;padding:22px 26px 20px;margin:0 0 18px;color:#fff;background:linear-gradient(90deg,#17418f,var(--a))}
.banner:before,.banner:after{content:"";position:absolute;border-radius:50%;background:rgba(255,255,255,.10)}
.banner:before{width:240px;height:240px;right:-70px;top:-110px}.banner:after{width:150px;height:150px;right:170px;bottom:-95px}
.banner h1{color:#fff;font-size:26px;margin:0;position:relative}.banner h1:after{display:none}
.banner .pos{color:var(--tint);font-weight:700;font-size:15px;margin-top:2px;position:relative}
.banner ul{margin:12px 0 0;padding-left:20px;color:#e3e9f5;font-size:14px;line-height:1.5;position:relative}
.banner .note{color:#e3e9f5;font-size:13px;margin-top:8px;opacity:.9;position:relative}
.acts{margin:-4px 0 14px}.acts .btn{margin:6px 8px 0 0}
.about{display:flex;background:#e6efff;margin:0 0 16px;overflow:hidden}
.about i{flex:none;width:4px;background:#8fa6d6}.about p{margin:0;padding:10px 14px;color:#33405c;font-size:14px;line-height:1.45}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin:12px 0}
.tile{background:#fff;border:1px solid #d5dbe7;border-top:4px solid var(--sel);padding:12px 14px}
.tile .k{font-size:13px;color:#5b6b84;font-weight:600}.tile .v{font:800 22px "Avenir Next","Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:#1d2433;margin-top:2px}
.tile .s{font-size:13px;color:#5b6b84}
.todo{list-style:none;padding:0;margin:8px 0}
.todo li{background:#fff;border:1px solid #d5dbe7;border-left:5px solid var(--sel);padding:10px 12px;margin:0 0 8px}
.todo li.done{border-left-color:#22a06b;color:#5b6b84}
.steps{margin:8px 0 0;padding-left:22px}.steps li{margin:4px 0}
.tab{display:inline-block;background:#dfe4ee;color:#6b7385;font-weight:700;font-size:14px;padding:9px 16px;margin:0 2px 0 0;border:1px solid #d5dbe7;border-bottom:0;cursor:pointer;border-radius:0}
.tab:hover{color:#1d2433}.tab.on{background:#fff;color:var(--a);box-shadow:inset 0 3px 0 var(--sel)}
.tabs{border-bottom:1px solid #d5dbe7;margin:4px 0 14px}
.tabs .tab{margin-top:0}
.line{display:grid;grid-template-columns:1fr 130px 40px;gap:8px;align-items:end;margin:0 0 6px}
.line label{margin-top:0}
.line button{margin:0;height:43px;padding:0;width:100%}
.chip{display:inline-block;font-size:12px;font-weight:700;padding:2px 8px;border-radius:10px;background:#e3ebf9;color:#17418f;white-space:nowrap}
.chip.g{background:#e6f4ea;color:#0f6b45}.chip.r{background:#f8d7da;color:#8a1328}.chip.y{background:#fff3cd;color:#7a5600}
.bars{margin:8px 0}.bar{display:grid;grid-template-columns:72px 1fr 110px;gap:8px;align-items:center;margin:4px 0;font-size:14px}
.bar .b{height:18px;background:var(--sel)}.bar .b.now{background:#f2c230}
.deno{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:4px 12px}
.deno div{display:grid;grid-template-columns:62px 1fr;align-items:center;gap:6px}
.deno label{margin:0;text-align:right}
.deno input{padding:7px 8px}
/* the RCD form, as ALTOS prints it on A4 (LTOM, Annex 18); scaled to fit a phone */
.sheet-wrap{width:100%;max-width:796px;overflow:hidden;margin:8px 0 4px;border:1px solid #cfd5e2}
.pinch{display:none}
.sheet{width:794px;background:#fff;color:#000;padding:30px 34px;font:12px/1.35 "Times New Roman",Times,serif;transform-origin:0 0;position:relative}
.sheet:after{content:"SAMPLE ONLY · NOT VALID";position:absolute;left:50%;top:45%;transform:translate(-50%,-50%) rotate(-28deg);font:800 64px "Avenir Next","Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:rgba(194,24,91,.10);white-space:nowrap;pointer-events:none}
.sheet p{margin:0 0 4px}
.sheet .rcdtitle{text-align:center;font-size:15px;font-weight:bold;margin:2px 0 6px}
.sheet .lgu{text-align:center;font-weight:bold;font-size:14px;margin:0;border-bottom:1px solid #000;display:inline-block;padding:0 30px}
.sheet .lgucap{text-align:center;font-size:10px;margin:0}.sheet .printed{text-align:center;font-size:10px;margin:2px 0 8px}
.sheet .hdr{width:100%;margin:8px 0;border-collapse:collapse;background:transparent}.sheet .hdr td{padding:2px 4px;border:none;font-size:12px;background:transparent!important}
.sheet .u{border-bottom:1px solid #000!important;font-weight:bold}
.sheet table.g{width:100%;border-collapse:collapse;margin:4px 0 8px;background:#fff}
.sheet table.g th,.sheet table.g td{border:1px solid #000;padding:3px 5px;vertical-align:top;font-size:12px;color:#000;background:#fff!important;white-space:normal;font-family:inherit}
.sheet table.g th{background:#f0f0f0!important;font-weight:bold;text-align:center}
.sheet .small th,.sheet .small td{font-size:10px!important}
.sheet .r{text-align:right}.sheet .c{text-align:center}.sheet .b{font-weight:bold}
.sheet .sec{font-weight:bold;margin-top:10px}.sheet .ind{padding-left:12px}
.sheet .two{width:100%;border-collapse:collapse;background:transparent}.sheet .two>tbody>tr>td{vertical-align:top;width:50%;padding:0 6px 0 0;border:none;background:transparent!important}
.sheet .dsum{background:transparent}.sheet .dsum td{border:none;padding:2px 4px;font-size:12px;background:transparent!important}.sheet .dsum .amt{text-align:right;border-bottom:1px solid #000;min-width:90px}
.sheet .sigline{width:100%;border-collapse:collapse;margin-top:26px;background:transparent}.sheet .sigline td{border:none;padding:1px 4px;text-align:center;font-size:12px;background:transparent!important}
.sheet .sigline .nm{border-bottom:1px solid #000;font-weight:bold;width:65%}.sheet .sigline .dt{border-bottom:1px solid #000}.sheet .sigline .cap{font-size:10px}
.sheet .certbox{width:100%;border-collapse:collapse;margin-top:12px;background:transparent}.sheet .certbox>tbody>tr>td{width:50%;vertical-align:top;border:1px solid #000;padding:6px 8px;font-size:12px;background:#fff!important}
/* RAAF and CRAAF: landscape forms (LTOM Annexes 16-17) */
.sheet-wrap.wide{max-width:1125px}.sheet.wide{width:1123px}
.sheet .ref{font-size:9px;color:#444;text-align:right;margin:0}.sheet .lth{font-size:15px;text-align:center;margin:2px 0 0;font-weight:bold;color:#000;font-family:inherit}
.sheet .ltlgu{text-align:center;margin:8px 0 0}.sheet .ltlgu span{display:inline-block;min-width:260px;border-bottom:1px solid #000;font-weight:bold;padding:0 10px}
.sheet .ltcap{text-align:center;font-size:10px;font-style:italic;font-weight:bold;margin:0 0 4px}
.sheet .fld{display:inline-block;min-width:170px;border-bottom:1px solid #000;padding:0 6px;font-weight:bold;text-align:center}
.sheet .ltsig{display:inline-block;text-align:center;width:250px;margin:34px 40px 0 0;vertical-align:top}.sheet .ltsig .ln{border-top:1px solid #000;padding-top:2px;font-size:11px}
/* sample receipt and check: clearly not valid */
.paper{position:relative;overflow:hidden;background:#fffdf5;border:1px solid #cfc6a8;max-width:520px;padding:18px 20px;margin:12px 0;font-size:14px}
.paper.check{background:#f2fbf6;border-color:#9fd2b6;max-width:640px}
.paper:after{content:"SAMPLE ONLY · NOT VALID";position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-24deg);font:800 34px "Avenir Next","Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:rgba(194,24,91,.16);white-space:nowrap;pointer-events:none}
.paper .ph{text-align:center;line-height:1.3}.paper .ph b{font-size:15px}
.paper .no{color:#c2185b;font-weight:800;font-size:18px}
.paper table td,.paper table th{background:transparent!important;color:#1d2433;border-bottom:1px solid #e2dcc6;font-size:14px}
.paper .void{margin-top:10px;font-size:12px;color:#8a1328;font-weight:700;text-align:center}
.paper .amt{font:700 20px "Avenir Next","Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.fadein{animation:fadein .22s ease-out}@keyframes fadein{from{opacity:.25;transform:translateY(6px)}to{opacity:1;transform:none}}
noscript p{max-width:560px;margin:40px auto;padding:0 16px}
@media(max-width:820px){
 .lg{display:block}.lg .panel{padding:26px 18px 22px}.lg .c1,.lg .c2,.lg .c3{display:none}
 .lg .tag{font-size:17px;margin-top:14px}.lg .ttl{margin-top:16px}.dev{margin-top:16px}
 .lg .side2{padding:20px 12px 36px}.lcard{padding:24px 18px 22px}
 .top{padding:8px 10px;gap:6px 8px}.badge{font-size:14px;padding:2px 8px}.top .app{display:none}.pill{font-size:12px;padding:5px 10px}
 .wrap{display:block}
 .side{width:auto;flex-direction:row;overflow-x:auto;padding:0;white-space:nowrap;-webkit-overflow-scrolling:touch}
 .side .head{display:none}
 .side a{margin:0;border-left:0;border-bottom:4px solid transparent;padding:12px 14px}
 .side a.on{border-bottom-color:var(--tint)}.side a.homelink{font-size:15px;padding-top:12px;padding-bottom:12px}
 .content{padding:16px 10px 50px}
 .banner{padding:16px 16px 14px}.banner h1{font-size:21px}
 table{font-size:14px}th,td{padding:7px 6px;font-size:14px}
 .row>div{min-width:130px}
 .cb th,.cb td{padding:6px 3px;font-size:12px}.cb th{white-space:normal}
 .pinch{display:block;margin:4px 0 0}
 .line{grid-template-columns:1fr 110px 40px}
 .bar{grid-template-columns:44px 1fr 92px;font-size:13px}
 .paper{padding:14px 12px}.paper:after{font-size:24px}
}
@media print{.demo-bar,.top,.strip,.side,.noprint{display:none}.content{padding:0}}
"""


def demo_page():
    """The whole demo page, written without the site layout so no ads can appear on it."""
    from pages import asset_url  # imported here: pages.py imports this module
    url = f"https://{SITE['domain']}{DEMO_URL}"
    title = f"{DEMO_TITLE}: Try the Treasury Software · {SITE['short_name']}"
    t_ = TINTS
    login_panel = (
        f'<div class="panel"><i class="c1"></i><i class="c2"></i><i class="c3"></i><div class="in">'
        f'<div class="brand">{brand_svg()}</div>'
        f'<div class="ttl"><span style="color:{t_["col"]}">Automated</span> <span style="color:{t_["lo"]}">Local</span> '
        f'<span style="color:{t_["do"]}">Treasury</span><br><span style="color:{t_["sys"]}">Operations System</span></div>'
        f'<div class="bar4"><i style="background:{t_["col"]}"></i><i style="background:{t_["lo"]}"></i>'
        f'<i style="background:{t_["do"]}"></i><i style="background:{t_["sys"]}"></i></div>'
        '<div class="tag">Collect &nbsp;&#183;&nbsp; Disburse &nbsp;&#183;&nbsp; Report</div>'
        '<div class="motto">A 360&#176; accountability for every peso<br>the taxpayers pay to the treasury.</div>'
        '<div class="dev"><div class="by">Developed by:</div><span class="nm">aumahinay</span></div>'
        '</div></div>'
    )
    doc = t.html(
        t.head(
            t.meta(charset="utf-8"),
            t.meta(name="viewport", content="width=device-width, initial-scale=1"),
            t.meta(name="theme-color", content="#f2c230"),
            t.title(title),
            # https://aumahinay.dev is the only address: test copies on *.pages.dev and plain http jump to it
            t.script(Raw(f'if (/\\.pages\\.dev$/.test(location.hostname) || (location.protocol === "http:" && location.hostname === "{SITE["domain"]}")) location.replace("https://{SITE["domain"]}" + location.pathname + location.search + location.hash);')),
            t.link(rel="canonical", href=url),
            t.meta(name="robots", content="noindex"),  # drawn by JavaScript: no text for Google (Butch, 2026-11-20)
            t.meta(name="description", content=DEMO_DESCRIPTION),
            t.meta(property="og:type", content="website"),
            t.meta(property="og:site_name", content=SITE["short_name"]),
            t.meta(property="og:title", content=title),
            t.meta(property="og:description", content=DEMO_DESCRIPTION),
            t.meta(property="og:url", content=url),
            t.meta(property="og:image", content=f"https://{SITE['domain']}" + asset_url("share.jpg")),
            t.meta(property="og:image:width", content="1200"),
            t.meta(property="og:image:height", content="630"),
            t.meta(name="twitter:card", content="summary_large_image"),
            t.link(rel="icon", href="/favicon.ico", sizes="any"),
            t.link(rel="icon", type="image/png", sizes="32x32", href=asset_url("favicon-32.png")),
            t.link(rel="apple-touch-icon", href=asset_url("apple-touch-icon.png")),
            t.style(Raw(CSS)),
        ),
        t.body(
            t.div(t.span(t.b("DEMO"), " Made-up sample data. Not connected to any treasury. Nothing you do is saved."),
                  t.a("Leave demo ✕", href="/projects/"), class_="demo-bar", role="note"),
            t.div(
                # the sign-in page, also what a visitor sees before the script runs
                Raw('<div class="lg">' + login_panel + '<div class="side2" id="pick"></div></div>'),
                id="altos-demo",
            ),
            t.noscript(t.p("This demo runs in your browser. Please turn on JavaScript to try it, or read about ALTOS on the ",
                           t.a("Projects page", href="/projects/"), ".")),
            t.script(Raw("window.ALTOS_BRAND = " + json.dumps(login_panel).replace("</", "<\\/") + ";")),
            t.script(src=asset_url("altos-demo.js")),
        ),
        lang="en",
    )
    return "<!doctype html>\n" + doc
