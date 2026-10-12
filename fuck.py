# ============================================================================
#   █████╗  ██████╗ ███████╗
#  ██╔══██╗██╔════╝ ██╔════╝
#  ███████║██║  ███╗███████╗
#  ██╔══██║██║   ██║╚════██║
#  ██║  ██║╚██████╔╝███████║
#  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
#
#  AGS BIO CHANGER — Premium Bio Updater
#  Owner    : AGS
#  Contact  : @ags_owner_atif
#  Community: AGS-COMMUNITY
#  All Rights Reserved © AGS
# ============================================================================

import os
import requests
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# ============================================================================
#  CONFIG — সব environment variable থেকে (কোনো secret কোডে নেই)
#  Vercel → Settings → Environment Variables:
#     AGS_API_URL   = https://your-api.example.com/bio
#     AGS_API_KEY   = (optional)
#     AGS_REGION    = BD
# ============================================================================
AGS_API_URL   = os.environ.get("AGS_API_URL", "").strip()
AGS_API_KEY   = os.environ.get("AGS_API_KEY", "").strip()
AGS_REGION    = os.environ.get("AGS_REGION", "BD").strip()

# ============================================================================
#  HTML — AGS BIO CHANGER
# ============================================================================
HTML_TEMPLATE = r"""
<!DOCTYPE html>
<!--
  ============================================================================
   AGS BIO CHANGER — Premium Bio Updater
   Owner    : AGS
   Contact  : @ags_owner_atif
   Community: AGS-COMMUNITY
   All Rights Reserved © AGS
  ============================================================================
-->
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<meta name="author" content="AGS">
<title>AGS BIO CHANGER — Premium Edition</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600;700&family=Orbitron:wght@600;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
/* ==========================================================================
   AGS BIO CHANGER — Metallic Blue · Premium · Animated
   All Rights Reserved © AGS
   ========================================================================== */
:root{
  --bg-0:#01040c; --bg-1:#04091a; --bg-2:#071329;
  --cyan:#5ce1ff; --cyan-2:#39c8ff;
  --blue:#2f7dff; --blue-2:#1a52e0;
  --violet:#7c6bff;
  --ink:#eaf4ff; --muted:#7d90ac;
  --line:rgba(92,225,255,.14);
  --line-2:rgba(92,225,255,.32);
  --glass:rgba(10,20,42,.55);
  --glass-2:rgba(11,22,46,.72);
  --success:#4dffb8; --danger:#ff5c7c; --warn:#ffbe4d;
  --radius-lg:26px; --radius-md:18px; --radius-sm:13px;
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{
  font-family:'Inter',system-ui,sans-serif;
  color:var(--ink);
  background:
    radial-gradient(1200px 700px at 12% -8%, rgba(92,225,255,.18), transparent 55%),
    radial-gradient(1000px 600px at 100% 12%, rgba(124,107,255,.16), transparent 55%),
    radial-gradient(900px 700px at 50% 110%, rgba(47,125,255,.18), transparent 55%),
    linear-gradient(180deg, var(--bg-1), var(--bg-0) 60%, #00020a);
  min-height:100vh; overflow-x:hidden;
  -webkit-font-smoothing:antialiased;
}

/* Metallic sheen overlay */
body::before{
  content:"";position:fixed;inset:0;z-index:0;pointer-events:none;
  background:
    linear-gradient(115deg, transparent 30%, rgba(92,225,255,.045) 45%, transparent 55%, rgba(124,107,255,.04) 70%, transparent 82%);
  background-size:220% 220%;
  animation:sheen 16s linear infinite;
  mix-blend-mode:screen;
}
@keyframes sheen{0%{background-position:0% 0%}100%{background-position:200% 200%}}

/* Aurora */
.aurora{position:fixed;inset:-20% -10%;z-index:0;pointer-events:none;filter:blur(100px);opacity:.5}
.aurora span{position:absolute;border-radius:50%;mix-blend-mode:screen;animation:drift 24s ease-in-out infinite}
.aurora span:nth-child(1){width:520px;height:520px;left:5%;top:10%;background:radial-gradient(circle, rgba(92,225,255,.6), transparent 60%)}
.aurora span:nth-child(2){width:460px;height:460px;right:8%;top:20%;background:radial-gradient(circle, rgba(124,107,255,.55), transparent 60%);animation-delay:-6s}
.aurora span:nth-child(3){width:600px;height:600px;left:30%;bottom:5%;background:radial-gradient(circle, rgba(47,125,255,.55), transparent 60%);animation-delay:-12s}
@keyframes drift{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(40px,-30px) scale(1.08)}66%{transform:translate(-30px,35px) scale(.94)}}

/* Grid */
.grid-overlay{
  position:fixed;inset:0;z-index:0;pointer-events:none;opacity:.32;
  background-image:linear-gradient(rgba(92,225,255,.06) 1px, transparent 1px),linear-gradient(90deg, rgba(92,225,255,.06) 1px, transparent 1px);
  background-size:44px 44px;
  mask-image:radial-gradient(circle at 50% 40%, black 30%, transparent 78%);
  -webkit-mask-image:radial-gradient(circle at 50% 40%, black 30%, transparent 78%);
}

/* Particles */
.particles{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.particles i{
  position:absolute;bottom:-20px;width:4px;height:4px;border-radius:50%;
  background:linear-gradient(180deg,var(--cyan),var(--blue));
  box-shadow:0 0 12px rgba(92,225,255,.75);
  animation:floatUp linear infinite;
}
@keyframes floatUp{0%{transform:translateY(0);opacity:0}10%{opacity:.9}100%{transform:translateY(-110vh) translateX(30px);opacity:0}}

/* Layout */
.wrap{position:relative;z-index:2;max-width:880px;margin:0 auto;padding:28px 16px 60px}

/* Topbar */
.topbar{
  display:flex;align-items:center;justify-content:space-between;gap:14px;
  padding:14px 18px;border-radius:var(--radius-md);
  background:var(--glass);border:1px solid var(--line);
  backdrop-filter:blur(22px) saturate(160%);
  -webkit-backdrop-filter:blur(22px) saturate(160%);
  box-shadow:0 12px 44px rgba(0,0,0,.5), inset 0 1px 0 rgba(255,255,255,.06);
  margin-bottom:22px;
}
.brand{display:flex;align-items:center;gap:12px}
.logo{
  width:46px;height:46px;border-radius:14px;display:grid;place-items:center;
  background:linear-gradient(135deg,var(--cyan) 0%, var(--blue) 55%, var(--violet) 100%);
  color:#02060f;font-size:20px;font-weight:900;
  box-shadow:0 0 26px rgba(92,225,255,.55), inset 0 0 14px rgba(255,255,255,.4);
  position:relative;overflow:hidden;
  animation:pulseGlow 3s ease-in-out infinite;
}
.logo::after{
  content:"";position:absolute;inset:0;
  background:linear-gradient(120deg, transparent 30%, rgba(255,255,255,.5) 50%, transparent 70%);
  transform:translateX(-120%);
  animation:logoSheen 3.4s ease-in-out infinite;
}
@keyframes logoSheen{0%,60%{transform:translateX(-120%)}80%{transform:translateX(120%)}100%{transform:translateX(120%)}}
@keyframes pulseGlow{0%,100%{box-shadow:0 0 26px rgba(92,225,255,.55), inset 0 0 14px rgba(255,255,255,.4)}50%{box-shadow:0 0 40px rgba(92,225,255,.9), inset 0 0 18px rgba(255,255,255,.65)}}
.brand-text{line-height:1.15}
.brand-text b{font-size:15px;font-weight:800;letter-spacing:.4px}
.brand-text small{display:block;color:var(--muted);font-size:10px;font-weight:600;letter-spacing:1.6px;text-transform:uppercase;margin-top:4px}
.status-chip{
  display:inline-flex;align-items:center;gap:7px;
  font-size:11px;font-weight:700;letter-spacing:.6px;
  padding:7px 12px;border-radius:999px;
  color:var(--success);background:rgba(77,255,184,.08);
  border:1px solid rgba(77,255,184,.22);
}
.status-chip .dot{width:6px;height:6px;border-radius:50%;background:var(--success);box-shadow:0 0 8px var(--success);animation:blink 1.6s ease-in-out infinite}
@keyframes blink{50%{opacity:.35}}

/* Hero */
.hero{text-align:center;padding:20px 12px 26px;position:relative}

/* ASCII Banner */
.ascii-banner{
  display:inline-block;font-family:'Orbitron',monospace;
  font-weight:900;letter-spacing:4px;
  font-size:clamp(1.6rem, 5.5vw, 2.8rem);
  line-height:1.05;
  margin:0 auto 8px;
  background:linear-gradient(100deg, #ffffff 0%, var(--cyan) 25%, var(--blue) 55%, var(--violet) 80%, var(--cyan) 100%);
  background-size:280% 100%;
  -webkit-background-clip:text;background-clip:text;
  color:transparent;
  text-transform:uppercase;
  filter:drop-shadow(0 0 22px rgba(92,225,255,.4));
  animation:shine 6s linear infinite;
}
.ascii-banner .sub{
  display:block;font-size:.5em;letter-spacing:12px;
  color:transparent;font-weight:800;
  margin-top:6px;
}
.ascii-glow{
  position:relative;display:inline-block;
}
.ascii-glow::before{
  content:"";position:absolute;inset:-14px -30px;
  background:radial-gradient(ellipse, rgba(92,225,255,.35), transparent 70%);
  filter:blur(28px);z-index:-1;animation:heroPulse 4s ease-in-out infinite;
}
@keyframes heroPulse{0%,100%{opacity:.6}50%{opacity:1}}
@keyframes shine{0%{background-position:0% 50%}100%{background-position:200% 50%}}

.hero p{margin-top:14px;color:#9eb2cc;font-size:13px;font-weight:500;letter-spacing:.3px}
.hero .pills{display:flex;justify-content:center;gap:8px;flex-wrap:wrap;margin-top:16px}
.hero .pills span{
  font-size:10.5px;font-weight:700;letter-spacing:1.1px;
  padding:7px 13px;border-radius:999px;color:#cfe9ff;
  background:rgba(92,225,255,.07);border:1px solid var(--line);
  backdrop-filter:blur(8px);transition:.25s;
}
.hero .pills span:hover{border-color:var(--cyan);color:var(--cyan);box-shadow:0 0 22px rgba(92,225,255,.28);transform:translateY(-1px)}

/* Telegram channel banner */
.tg-banner{
  display:flex;align-items:center;justify-content:center;gap:12px;
  margin:18px auto 0;padding:12px 18px;
  max-width:480px;
  border-radius:999px;
  background:linear-gradient(90deg, rgba(92,225,255,.1), rgba(47,125,255,.12), rgba(124,107,255,.1));
  border:1px solid var(--line-2);
  text-decoration:none;color:var(--ink);
  font-size:12.5px;font-weight:700;letter-spacing:.4px;
  transition:.25s;position:relative;overflow:hidden;
  box-shadow:0 0 26px rgba(92,225,255,.15);
}
.tg-banner:hover{transform:translateY(-2px);border-color:var(--cyan);box-shadow:0 0 40px rgba(92,225,255,.4)}
.tg-banner::before{
  content:"";position:absolute;inset:0;
  background:linear-gradient(120deg, transparent 30%, rgba(255,255,255,.18) 50%, transparent 70%);
  transform:translateX(-120%);animation:tgSheen 4.5s ease-in-out infinite;
}
@keyframes tgSheen{0%,65%{transform:translateX(-120%)}85%{transform:translateX(120%)}100%{transform:translateX(120%)}}
.tg-banner i{color:var(--cyan);font-size:15px}
.tg-banner .tg-tag{color:var(--cyan);font-weight:800}

/* Card */
.card{
  position:relative;margin-top:16px;padding:22px;
  border-radius:var(--radius-lg);
  background:linear-gradient(150deg,var(--glass-2),rgba(6,12,26,.62));
  border:1px solid var(--line);
  backdrop-filter:blur(24px) saturate(160%);
  -webkit-backdrop-filter:blur(24px) saturate(160%);
  box-shadow:0 20px 60px rgba(0,0,0,.5),inset 0 1px 0 rgba(255,255,255,.05),0 0 0 1px rgba(92,225,255,.03);
  overflow:hidden;animation:cardIn .5s ease both;
}
@keyframes cardIn{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
.card::before{content:"";position:absolute;inset:0;pointer-events:none;border-radius:inherit;background:linear-gradient(120deg,rgba(92,225,255,.07),transparent 42%,rgba(124,107,255,.05));opacity:.75}
.card-head{position:relative;display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:16px}
.card-head h3{font-size:15px;font-weight:800;letter-spacing:.2px;display:flex;align-items:center;gap:9px}
.card-head h3 i{color:var(--cyan);filter:drop-shadow(0 0 6px rgba(92,225,255,.6))}
.card-kicker{font-size:10px;font-weight:700;letter-spacing:1.4px;text-transform:uppercase;color:var(--muted)}

/* Tabs */
.tabs{
  display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:18px;
  padding:6px;border-radius:var(--radius-md);
  background:rgba(5,12,26,.6);border:1px solid var(--line);
  position:relative;
}
.tab{
  position:relative;padding:12px 8px;border-radius:var(--radius-sm);
  border:0;background:transparent;color:var(--muted);
  font-family:inherit;font-size:12px;font-weight:700;letter-spacing:.4px;
  cursor:pointer;transition:.25s;display:flex;flex-direction:column;align-items:center;gap:5px;
  overflow:hidden;
}
.tab i{font-size:15px}
.tab:hover{color:#cfe4ff}
.tab.active{
  color:#02060f;
  background:linear-gradient(135deg,var(--cyan),var(--blue) 60%, var(--violet));
  box-shadow:0 8px 24px rgba(92,225,255,.4), inset 0 1px 0 rgba(255,255,255,.45);
  transform:translateY(-1px);
}
.tab:active{transform:scale(.97)}

/* Fields */
.field{margin-top:12px;animation:fade .35s ease both}
.field:first-child{margin-top:0}
@keyframes fade{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
.field label{display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:700;letter-spacing:1.3px;text-transform:uppercase;color:#9db4d3;margin:0 0 7px 4px}
.field label i{color:var(--cyan);font-size:11px}
.input-wrap{position:relative}
.input-wrap > i.lead{
  position:absolute;left:14px;top:50%;transform:translateY(-50%);
  color:#56718f;font-size:13px;pointer-events:none;transition:.25s;
}
.input-wrap input,.input-wrap textarea{
  width:100%;color:var(--ink);background:rgba(2,6,15,.72);
  border:1px solid var(--line-2);border-radius:var(--radius-sm);
  padding:14px 14px 14px 40px;
  font-family:inherit;font-size:13.5px;font-weight:500;
  outline:none;transition:.25s;box-shadow:inset 0 1px 0 rgba(255,255,255,.02);
}
.input-wrap textarea{padding-top:16px;min-height:96px;resize:vertical;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.55}
.input-wrap input::placeholder,.input-wrap textarea::placeholder{color:#4d6484}
.input-wrap input:focus,.input-wrap textarea:focus{
  border-color:var(--cyan);background:rgba(2,9,20,.88);
  box-shadow:0 0 0 4px rgba(92,225,255,.1),0 0 26px rgba(92,225,255,.22);
}
.input-wrap input:focus + i.lead,.input-wrap textarea:focus + i.lead{color:var(--cyan)}
.input-wrap .eye{
  position:absolute;right:10px;top:50%;transform:translateY(-50%);
  width:34px;height:34px;border-radius:10px;
  background:rgba(92,225,255,.07);border:1px solid var(--line);
  color:#8ba9c9;display:grid;place-items:center;cursor:pointer;transition:.2s;font-size:12px;
}
.input-wrap .eye:hover{color:var(--cyan);border-color:var(--cyan);background:rgba(92,225,255,.15);box-shadow:0 0 16px rgba(92,225,255,.35)}

/* Select */
.select-wrap{position:relative}
.select-wrap i.lead{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:#56718f;font-size:13px;pointer-events:none;z-index:1}
.select-wrap select{
  width:100%;color:var(--ink);background:rgba(2,6,15,.72);
  border:1px solid var(--line-2);border-radius:var(--radius-sm);
  padding:14px 40px 14px 40px;
  font-family:inherit;font-size:13.5px;font-weight:600;
  outline:none;transition:.25s;cursor:pointer;
  appearance:none;-webkit-appearance:none;
  background-image:
    linear-gradient(45deg, transparent 50%, #7d90ac 50%),
    linear-gradient(135deg, #7d90ac 50%, transparent 50%);
  background-position:calc(100% - 20px) 50%, calc(100% - 14px) 50%;
  background-size:6px 6px, 6px 6px;
  background-repeat:no-repeat;
}
.select-wrap select:focus{border-color:var(--cyan);box-shadow:0 0 0 4px rgba(92,225,255,.1),0 0 26px rgba(92,225,255,.22)}
.select-wrap select option{background:#08152e;color:var(--ink)}

/* Counter + hint */
.hint{display:flex;justify-content:space-between;align-items:center;margin-top:8px;color:#6c86a6;font-size:11px;font-weight:500}
.hint .count{font-family:'JetBrains Mono',monospace;font-weight:700;color:#9bb6d6}
.hint .count.warn{color:var(--warn)}
.hint .count.over{color:var(--danger)}

/* Row */
.row{display:grid;grid-template-columns:1fr 1fr;gap:12px}
@media(max-width:560px){.row{grid-template-columns:1fr}}

/* Buttons — metallic glow on click */
.btn{
  position:relative;width:100%;margin-top:16px;padding:15px 20px;
  border:0;border-radius:var(--radius-sm);cursor:pointer;
  font-family:inherit;font-size:13.5px;font-weight:800;letter-spacing:.6px;
  color:#02060f;
  background:linear-gradient(100deg,var(--cyan),var(--blue) 55%,var(--violet));
  background-size:220% 100%;
  box-shadow:0 10px 32px rgba(92,225,255,.35), inset 0 1px 0 rgba(255,255,255,.45), 0 0 0 1px rgba(255,255,255,.08);
  transition:transform .18s, box-shadow .28s, background-position .6s, filter .2s;
  overflow:hidden;display:flex;align-items:center;justify-content:center;gap:9px;
}
.btn::after{
  content:"";position:absolute;top:50%;left:50%;
  width:0;height:0;border-radius:50%;
  background:rgba(255,255,255,.6);
  transform:translate(-50%,-50%);
  transition:width .6s ease, height .6s ease, opacity .6s ease;
  opacity:0;pointer-events:none;
}
.btn:hover{transform:translateY(-2px);box-shadow:0 16px 46px rgba(92,225,255,.5), inset 0 1px 0 rgba(255,255,255,.55);background-position:100% 50%}
.btn:active{transform:translateY(0) scale(.98);filter:brightness(1.06)}
.btn:active::after{width:360px;height:360px;opacity:1;transition:0s}
.btn:disabled{opacity:.55;cursor:not-allowed;transform:none}
.btn:disabled:hover{transform:none;background-position:0 50%}

.btn-ghost{
  margin-top:10px;width:100%;padding:12px;
  border:1px solid var(--line-2);border-radius:var(--radius-sm);
  background:rgba(92,225,255,.05);color:#bcd9ff;
  font-family:inherit;font-size:12px;font-weight:700;letter-spacing:.4px;
  cursor:pointer;transition:.25s;
  display:flex;align-items:center;justify-content:center;gap:8px;
  position:relative;overflow:hidden;
}
.btn-ghost::after{
  content:"";position:absolute;top:50%;left:50%;
  width:0;height:0;border-radius:50%;
  background:rgba(92,225,255,.35);
  transform:translate(-50%,-50%);
  transition:width .55s ease, height .55s ease, opacity .55s ease;
  opacity:0;pointer-events:none;
}
.btn-ghost:hover{border-color:var(--cyan);color:var(--cyan);background:rgba(92,225,255,.1);box-shadow:0 0 26px rgba(92,225,255,.25)}
.btn-ghost:active{transform:scale(.98)}
.btn-ghost:active::after{width:300px;height:300px;opacity:1;transition:0s}

/* Live preview */
.preview{
  min-height:76px;padding:16px;border-radius:var(--radius-sm);
  border:1px dashed var(--line-2);
  background:linear-gradient(135deg,rgba(92,225,255,.05),rgba(124,107,255,.05));
  color:#eef7ff;font-size:14.5px;line-height:1.55;word-break:break-word;
  font-family:'JetBrains Mono',monospace;
}
.preview.empty{color:#5a7090;font-style:italic}

/* Result overlay */
.result{
  position:fixed;inset:0;z-index:2000;display:none;
  align-items:center;justify-content:center;padding:20px;
  background:rgba(1,3,8,.8);backdrop-filter:blur(20px);
  animation:fade .3s ease;
}
.result.show{display:flex}
.result-box{
  max-width:460px;width:100%;padding:30px 24px;border-radius:24px;text-align:center;
  background:linear-gradient(150deg,rgba(19,27,44,.96),rgba(7,12,21,.97));
  border:1px solid var(--line-2);
  box-shadow:0 30px 100px rgba(0,0,0,.65), 0 0 60px rgba(92,225,255,.18);
  animation:pop .35s cubic-bezier(.2,1.4,.4,1) both;
}
@keyframes pop{from{transform:scale(.9);opacity:0}to{transform:scale(1);opacity:1}}
.result-icon{font-size:62px;margin-bottom:10px;display:block}
.result.ok .result-icon{color:var(--success);animation:ring 1.2s ease infinite}
.result.err .result-icon{color:var(--danger)}
@keyframes ring{0%{transform:scale(1)}50%{transform:scale(1.08)}100%{transform:scale(1)}}
.result-title{font-size:22px;font-weight:900;margin-bottom:10px;letter-spacing:-.4px}
.result-body{color:#b8c8dd;font-size:13px;line-height:1.7;word-break:break-word}
.result-body strong{color:#fff}
.result .credit{margin-top:14px;font-size:10px;color:#5a6b82;letter-spacing:.6px}
.result .credit a{color:var(--cyan);text-decoration:none;font-weight:700}
.result .close{
  margin-top:16px;padding:10px 22px;border-radius:999px;
  border:1px solid var(--line-2);background:transparent;color:#a8c4e2;
  font-family:inherit;font-size:11px;font-weight:700;letter-spacing:.5px;cursor:pointer;transition:.2s;
}
.result .close:hover{border-color:var(--cyan);color:var(--cyan);box-shadow:0 0 18px rgba(92,225,255,.35)}

/* Credit footer */
.credit{
  text-align:center;padding:26px 10px 8px;color:#5a6b82;font-size:11px;letter-spacing:.5px;
  border-top:1px solid rgba(255,255,255,.06);margin-top:28px;line-height:1.9;
}
.credit a{color:var(--cyan);text-decoration:none;font-weight:700}
.credit a:hover{color:#8ca2ff;text-shadow:0 0 12px rgba(92,225,255,.7)}
.credit .brandline{
  display:inline-block;font-family:'Orbitron',monospace;font-weight:900;
  letter-spacing:3px;font-size:13px;
  background:linear-gradient(90deg, var(--cyan), var(--blue), var(--violet));
  -webkit-background-clip:text;background-clip:text;color:transparent;
  margin-bottom:6px;
}
.credit .badges{display:flex;justify-content:center;gap:14px;flex-wrap:wrap;margin-top:10px;font-size:10px;color:#4f5b6f}

/* Loading dots */
.dots::after{content:"";animation:dots 1.4s steps(4,end) infinite}
@keyframes dots{0%{content:""}25%{content:"."}50%{content:".."}75%{content:"..."}}

/* Responsive */
@media(max-width:600px){
  .wrap{padding:18px 12px 44px}
  .topbar{border-radius:16px;padding:12px 14px}
  .card{padding:18px;border-radius:22px}
  .hero{padding:14px 6px 20px}
  .tabs{gap:6px}
  .tab{font-size:10.5px;padding:10px 4px}
  .tab i{font-size:13px}
  .ascii-banner{letter-spacing:2.5px}
}
</style>
</head>
<body>

<!-- AGS BIO CHANGER — All Rights Reserved © AGS -->

<div class="aurora"><span></span><span></span><span></span></div>
<div class="grid-overlay"></div>
<div class="particles" id="particles"></div>

<div class="wrap">

  <div class="topbar">
    <div class="brand">
      <div class="logo"><i class="fas fa-bolt"></i></div>
      <div class="brand-text">
        <b>AGS BIO CHANGER</b>
        <small>Premium Edition · @ags_owner_atif</small>
      </div>
    </div>
    <div class="status-chip"><span class="dot"></span> ONLINE</div>
  </div>

  <div class="hero">
    <div class="ascii-glow">
      <div class="ascii-banner">
        AGS BIO CHANGER
        <span class="sub">PREMIUM</span>
      </div>
    </div>
    <p>Fast · Secure · Premium Bio Editing Tool</p>
    <div class="pills">
      <span><i class="fas fa-crown"></i> AGS</span>
      <span><i class="fas fa-shield-alt"></i> AGS-COMMUNITY</span>
      <span><i class="fas fa-user"></i> @ags_owner_atif</span>
    </div>

    <a class="tg-banner" href="https://t.me/ags_owner_atif" target="_blank" rel="noopener">
      <i class="fab fa-telegram"></i>
      <span>Join AGS Community → <span class="tg-tag">@ags_owner_atif</span></span>
    </a>
  </div>

  <div class="card">
    <div class="card-head">
      <h3><i class="fas fa-key"></i> Authentication</h3>
      <span class="card-kicker">3 Methods</span>
    </div>

    <div class="tabs">
      <button class="tab active" data-tab="uid"><i class="fas fa-user-lock"></i> UID + PASS</button>
      <button class="tab" data-tab="access"><i class="fas fa-id-badge"></i> ACCESS</button>
      <button class="tab" data-tab="jwt"><i class="fas fa-key"></i> JWT</button>
    </div>

    <div class="field">
      <label><i class="fas fa-globe"></i> Region / Server</label>
      <div class="select-wrap">
        <i class="fas fa-earth-asia lead"></i>
        <select id="region">
          <option value="BD" selected>🇧🇩 BD — Bangladesh</option>
          <option value="IND">🇮🇳 IND — India</option>
          <option value="SG">🇸🇬 SG — Singapore</option>
          <option value="BR">🇧🇷 BR — Brazil</option>
          <option value="US">🇺🇸 US — USA</option>
          <option value="EU">🇪🇺 EU — Europe</option>
          <option value="ID">🇮🇩 ID — Indonesia</option>
          <option value="PK">🇵🇰 PK — Pakistan</option>
          <option value="MY">🇲🇾 MY — Malaysia</option>
          <option value="TH">🇹🇭 TH — Thailand</option>
        </select>
      </div>
    </div>

    <div class="tab-panel" id="panel-uid">
      <div class="field">
        <label><i class="fas fa-user"></i> UID</label>
        <div class="input-wrap">
          <i class="fas fa-hashtag lead"></i>
          <input id="uid-input" type="text" placeholder="Enter your UID (e.g. 123456789)" autocomplete="off" inputmode="numeric">
        </div>
      </div>
      <div class="field">
        <label><i class="fas fa-lock"></i> Password</label>
        <div class="input-wrap">
          <i class="fas fa-asterisk lead"></i>
          <input id="pass-input" type="password" placeholder="Enter your password" autocomplete="new-password">
          <button class="eye" type="button" onclick="togglePwd('pass-input',this)"><i class="fas fa-eye"></i></button>
        </div>
      </div>
    </div>

    <div class="tab-panel" id="panel-access" style="display:none">
      <div class="field">
        <label><i class="fas fa-id-badge"></i> Access Token</label>
        <div class="input-wrap">
          <i class="fas fa-key lead"></i>
          <input id="access-input" type="text" placeholder="Paste your access token" autocomplete="off">
        </div>
      </div>
    </div>

    <div class="tab-panel" id="panel-jwt" style="display:none">
      <div class="field">
        <label><i class="fas fa-key"></i> JWT Token</label>
        <div class="input-wrap">
          <i class="fas fa-shield-halved lead"></i>
          <input id="jwt-input" type="text" placeholder="Paste your JWT token (eyJ...)" autocomplete="off">
        </div>
      </div>
    </div>

    <div class="field">
      <label><i class="fas fa-pen-fancy"></i> New Bio</label>
      <div class="input-wrap">
        <textarea id="bio-input" maxlength="300" placeholder="Type your new bio here... [b]bold[/b] [i]italic[/i] [FF0000]red[/FF0000]"></textarea>
      </div>
      <div class="hint">
        <span>Supports [b], [i], [u], [s], [c] and HEX colors</span>
        <span class="count" id="bio-count">0 / 300</span>
      </div>
    </div>

    <div class="field">
      <label><i class="fas fa-eye"></i> Live Preview</label>
      <div class="preview empty" id="preview">Your bio preview will appear here…</div>
    </div>

    <button class="btn" id="submit-btn" onclick="submitForm()">
      <i class="fas fa-rocket"></i> UPDATE BIO
    </button>
    <button class="btn-ghost" onclick="clearAll()">
      <i class="fas fa-eraser"></i> CLEAR ALL
    </button>
  </div>

  <div class="credit">
    <div class="brandline">AGS · COMMUNITY</div><br>
    Owner <a href="https://t.me/ags_owner_atif" target="_blank">@ags_owner_atif</a> · NAME: AGS
    <div class="badges">
      <span><i class="fas fa-code"></i> AGS BIO CHANGER</span>
      <span><i class="fas fa-crown"></i> All Rights Reserved © AGS</span>
    </div>
  </div>
</div>

<div class="result" id="result-overlay">
  <div class="result-box" id="result-box">
    <i class="fas fa-check-circle result-icon" id="result-icon"></i>
    <div class="result-title" id="result-title">Success</div>
    <div class="result-body" id="result-body"></div>
    <div class="credit">AGS BIO CHANGER · <a href="https://t.me/ags_owner_atif" target="_blank">@ags_owner_atif</a></div>
    <button class="close" onclick="closeResult()">CLOSE</button>
  </div>
</div>

<script>
/* AGS BIO CHANGER — All Rights Reserved © AGS */
console.log("%c AGS BIO CHANGER ","background:linear-gradient(90deg,#5ce1ff,#2f7dff,#7c6bff);color:#02060f;font-weight:900;padding:6px 14px;border-radius:6px;font-size:13px;letter-spacing:2px;");
console.log("%c @ags_owner_atif ","background:#7c6bff;color:#fff;font-weight:700;padding:4px 10px;border-radius:6px;font-size:11px;");

// Particles
(function(){
  const p = document.getElementById('particles');
  for(let i=0;i<24;i++){
    const d=document.createElement('i');
    d.style.left=Math.random()*100+"%";
    d.style.animationDuration=(8+Math.random()*10)+"s";
    d.style.animationDelay=(-Math.random()*12)+"s";
    d.style.opacity=(.3+Math.random()*.6).toFixed(2);
    p.appendChild(d);
  }
})();

// Tabs
let currentTab = "uid";
document.querySelectorAll('.tab').forEach(btn=>{
  btn.addEventListener('click',()=>{
    const t = btn.dataset.tab;
    currentTab = t;
    document.querySelectorAll('.tab').forEach(b=>b.classList.toggle('active', b===btn));
    document.querySelectorAll('.tab-panel').forEach(p=>p.style.display='none');
    document.getElementById('panel-'+t).style.display='block';
  });
});

// Password eye
function togglePwd(id, btn){
  const el = document.getElementById(id);
  const isPwd = el.type === 'password';
  el.type = isPwd ? 'text' : 'password';
  btn.innerHTML = isPwd ? '<i class="fas fa-eye-slash"></i>' : '<i class="fas fa-eye"></i>';
}

// Bio counter + preview
const bioEl = document.getElementById('bio-input');
const countEl = document.getElementById('bio-count');
const previewEl = document.getElementById('preview');
const MAX = 300;

function updateCount(){
  const n = bioEl.value.length;
  countEl.textContent = n + " / " + MAX;
  countEl.classList.toggle('warn', n > MAX*0.8 && n <= MAX);
  countEl.classList.toggle('over', n > MAX);
}
function escapeHtml(s){
  return s.replace(/[&<>"']/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
}
function renderPreview(){
  const raw = bioEl.value;
  if(!raw.trim()){ previewEl.textContent = "Your bio preview will appear here…"; previewEl.classList.add('empty'); return; }
  previewEl.classList.remove('empty');
  let out = escapeHtml(raw);
  out = out.replace(/\[b\](.*?)\[\/b\]/gis, '<b>$1</b>');
  out = out.replace(/\[i\](.*?)\[\/i\]/gis, '<i>$1</i>');
  out = out.replace(/\[u\](.*?)\[\/u\]/gis, '<u>$1</u>');
  out = out.replace(/\[s\](.*?)\[\/s\]/gis, '<s>$1</s>');
  out = out.replace(/\[c\](.*?)\[\/c\]/gis, '<span style="font-style:italic">$1</span>');
  out = out.replace(/\[([0-9A-Fa-f]{6})\](.*?)\[\/\1\]/g, '<span style="color:#$1">$2</span>');
  out = out.replace(/\n/g, '<br>');
  previewEl.innerHTML = out;
}
bioEl.addEventListener('input', ()=>{ updateCount(); renderPreview(); });
updateCount(); renderPreview();

// Submit
function getPayload(){
  const region = document.getElementById('region').value;
  const bio = bioEl.value.trim();
  if(!bio) return {error:"Bio is required"};
  if(currentTab === 'uid'){
    const uid = document.getElementById('uid-input').value.trim();
    const pass = document.getElementById('pass-input').value;
    if(!uid) return {error:"UID is required"};
    if(!pass) return {error:"Password is required"};
    return {method:'uid', uid, password:pass, bio, region};
  }
  if(currentTab === 'access'){
    const access = document.getElementById('access-input').value.trim();
    if(!access) return {error:"Access token is required"};
    return {method:'access', token:access, bio, region};
  }
  if(currentTab === 'jwt'){
    const jwt = document.getElementById('jwt-input').value.trim();
    if(!jwt) return {error:"JWT token is required"};
    return {method:'jwt', token:jwt, bio, region};
  }
  return {error:"Unknown method"};
}

async function submitForm(){
  const payload = getPayload();
  if(payload.error){ showResult(false, "Missing Field", payload.error); return; }

  const btn = document.getElementById('submit-btn');
  const original = btn.innerHTML;
  btn.disabled = true;
  btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> PROCESSING<span class="dots"></span>';

  try{
    const res = await fetch('/api/update', {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify(payload)
    });
    const data = await res.json();

    if(data.status === 'success'){
      showResult(true, "Success", `
        <div><strong>UID:</strong> ${data.uid || payload.uid || 'N/A'}</div>
        <div><strong>Name:</strong> ${data.name || 'N/A'}</div>
        <div><strong>Region:</strong> ${data.region_used || payload.region || 'N/A'}</div>
        <div><strong>Method:</strong> ${data.login_method || payload.method || 'N/A'}</div>
        <div style="margin-top:10px;color:#4dffb8;">✅ ${data.message || 'Bio updated successfully'}</div>
      `);
      clearAll();
    } else {
      showResult(false, "Failed", data.message || data.error || 'Unknown error');
    }
  } catch(e){
    showResult(false, "Network Error", escapeHtml(String(e.message || e)));
  } finally {
    btn.disabled = false;
    btn.innerHTML = original;
  }
}

function clearAll(){
  document.getElementById('uid-input').value = '';
  document.getElementById('pass-input').value = '';
  document.getElementById('access-input').value = '';
  document.getElementById('jwt-input').value = '';
  bioEl.value = '';
  updateCount(); renderPreview();
}

function showResult(ok, title, bodyHtml){
  const ov = document.getElementById('result-overlay');
  const box = document.getElementById('result-box');
  const icon = document.getElementById('result-icon');
  document.getElementById('result-title').textContent = title;
  document.getElementById('result-body').innerHTML = bodyHtml;
  box.className = 'result-box ' + (ok ? 'ok' : 'err');
  icon.className = (ok ? 'fas fa-check-circle' : 'fas fa-times-circle') + ' result-icon';
  ov.classList.add('show');
}
function closeResult(){ document.getElementById('result-overlay').classList.remove('show'); }
document.getElementById('result-overlay').addEventListener('click', e=>{ if(e.target.id==='result-overlay') closeResult(); });
</script>
</body>
</html>
"""


# ============================================================================
#  ROUTES
# ============================================================================
@app.route('/', methods=['GET'])
def index():
    q = request.args
    if any(k in q for k in ('uid','pass','password','bio','jwt','access','token','method')):
        return api_handler(
            method=(q.get('method') or ('uid' if q.get('uid') else 'jwt' if q.get('jwt') else 'access' if q.get('access') else 'jwt')),
            token=(q.get('token') or q.get('uid') or q.get('jwt') or q.get('access') or '').strip(),
            password=(q.get('password') or q.get('pass') or '').strip(),
            bio=(q.get('bio') or '').strip(),
            region=(q.get('region') or q.get('server') or AGS_REGION).strip()
        )
    return render_template_string(HTML_TEMPLATE)


@app.route('/api/update', methods=['POST'])
def update_bio():
    data = request.get_json(silent=True) or request.form.to_dict()
    if not data:
        return jsonify({"status":"error","message":"Missing data","owner":"AGS"}), 400

    method = (data.get('method') or '').lower()
    if method == 'uid':
        token = (data.get('uid') or data.get('token') or '').strip()
        password = (data.get('password') or data.get('pass') or '').strip()
    else:
        token = (data.get('token') or data.get('access') or data.get('jwt') or '').strip()
        password = ''
        if not method:
            method = 'jwt'

    return api_handler(
        method=method, token=token, password=password,
        bio=(data.get('bio') or '').strip(),
        region=(data.get('region') or data.get('server') or AGS_REGION).strip()
    )


@app.route('/bio', methods=['GET'])
def bio_api():
    q = request.args
    return api_handler(
        method=(q.get('method') or 'jwt').lower(),
        token=(q.get('token') or q.get('uid') or q.get('jwt') or q.get('access') or '').strip(),
        password=(q.get('password') or q.get('pass') or '').strip(),
        bio=(q.get('bio') or '').strip(),
        region=(q.get('region') or q.get('server') or AGS_REGION).strip()
    )


# ============================================================================
#  CORE HANDLER
# ============================================================================
OWNER = "AGS"

def api_handler(method, token, password, bio, region):
    if not bio:
        return jsonify({"status":"error","message":"Bio is required","owner":OWNER}), 400
    if not token:
        return jsonify({"status":"error","message":"Token/UID is required","owner":OWNER}), 400
    if not AGS_API_URL:
        return jsonify({"status":"error","message":"Server not configured","owner":OWNER}), 500

    if method == 'uid':
        if not password:
            return jsonify({"status":"error","message":"Password required for UID method","owner":OWNER}), 400
        params = {"bio": bio, "uid": token, "pass": password, "region": region}
    elif method == 'access':
        params = {"bio": bio, "access": token, "region": region}
    elif method == 'jwt':
        params = {"bio": bio, "jwt": token, "region": region}
    elif method == 'eat':
        params = {"bio": bio, "eat": token, "region": region}
    else:
        return jsonify({"status":"error","message":f"Unsupported method: {method}","owner":OWNER}), 400

    headers = {}
    if AGS_API_KEY:
        headers['Authorization'] = f"Bearer {AGS_API_KEY}"

    try:
        r = requests.get(AGS_API_URL, params=params, headers=headers, timeout=30)
        r.raise_for_status()
        api_data = r.json()

        ok = bool(api_data.get('success'))
        result = {
            "status": "success" if ok else "error",
            "message": api_data.get('status') or ('Bio updated' if ok else 'Update failed'),
            "uid": api_data.get('uid'),
            "name": api_data.get('name'),
            "region_used": api_data.get('region_used') or region,
            "login_method": api_data.get('login_method') or method,
            "server_response": api_data.get('server_response'),
            "generated_jwt": api_data.get('generated_jwt'),
            "http_code": api_data.get('http_code'),
            "owner": "AGS",
            "community": "AGS-COMMUNITY",
            "contact": "@ags_owner_atif",
        }
        return jsonify(result)

    except requests.exceptions.Timeout:
        return jsonify({"status":"error","message":"API timeout — try again","owner":OWNER}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"status":"error","message":f"API request failed: {e}","owner":OWNER}), 502
    except Exception as e:
        return jsonify({"status":"error","message":f"Server error: {e}","owner":OWNER}), 500


# ============================================================================
if __name__ == '__main__':
    print("="*60)
    print("  AGS BIO CHANGER — Premium Edition")
    print("  Owner    : AGS")
    print("  Contact  : @ags_owner_atif")
    print("  Community: AGS-COMMUNITY")
    print("  Web      : http://localhost:5000/")
    print("  API      : http://localhost:5000/bio?uid=...&pass=...&bio=...")
    print("="*60)
    app.run(debug=False, host='0.0.0.0', port=5000)