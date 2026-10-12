# ============================================================================
#  AGS BIO CHANGER — Premium Golden Edition
#  Owner    : AGS
#  Contact  : @ags_owner_atif
#  Community: AGS-COMMUNITY
#  All Rights Reserved © AGS
# ============================================================================

import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# ============================================================================
#  CONFIG — Environment variable থেকে
#  Vercel / Render / Railway → Settings → Environment Variables:
#     AGS_API_URL  = https://drogon-bio-api.vercel.app/bio
#     AGS_API_KEY  = (optional)
#     AGS_REGION   = BD
# ============================================================================
AGS_API_URL = os.environ.get("AGS_API_URL", "").strip()
AGS_API_KEY = os.environ.get("AGS_API_KEY", "").strip()
AGS_REGION  = os.environ.get("AGS_REGION", "BD").strip()

# ============================================================================
#  HIGH-PERFORMANCE SESSION
# ============================================================================
session = requests.Session()
retry = Retry(total=3, backoff_factor=0.4,
              status_forcelist=[500, 502, 503, 504],
              allowed_methods=["GET", "POST"])
adapter = HTTPAdapter(pool_connections=50, pool_maxsize=100, max_retries=retry, pool_block=False)
session.mount("http://", adapter)
session.mount("https://", adapter)

# ============================================================================
#  HTML — Premium Golden UI
# ============================================================================
HTML_TEMPLATE = r"""<!DOCTYPE html>
<!--
  ============================================================================
   AGS BIO CHANGER — Premium Golden Edition
   Owner: AGS · @ags_owner_atif · AGS-COMMUNITY
   All Rights Reserved © AGS
  ============================================================================
-->
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>AGS BIO CHANGER — Premium Golden Edition</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=Orbitron:wght@600;800;900&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
:root{
  --bg-0:#05040a; --bg-1:#0a0814;
  --gold-1:#fff9d9; --gold-2:#ffe9a8; --gold-3:#ffc93c; --gold-4:#d4a017; --gold-5:#8a5a0a;
  --ink:#fdf6e3; --muted:#9c8e6f;
  --line:rgba(255,201,60,.22); --line-2:rgba(255,201,60,.5);
  --glass:rgba(20,16,10,.6); --glass-2:rgba(22,18,10,.78);
  --success:#4dffb8; --danger:#ff5c7c; --warn:#ffbe4d;
  --radius-lg:26px; --radius-md:18px; --radius-sm:13px;
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{
  font-family:'Inter',system-ui,sans-serif;font-weight:600;color:var(--ink);
  background:
    radial-gradient(1200px 700px at 12% -8%, rgba(255,201,60,.14), transparent 55%),
    radial-gradient(1000px 600px at 100% 12%, rgba(138,90,10,.28), transparent 55%),
    radial-gradient(900px 700px at 50% 110%, rgba(255,201,60,.12), transparent 55%),
    linear-gradient(180deg, var(--bg-1), var(--bg-0) 60%, #000);
  min-height:100vh;overflow-x:hidden;-webkit-font-smoothing:antialiased;
}
body::before{content:"";position:fixed;inset:0;z-index:0;pointer-events:none;
  background:linear-gradient(115deg, transparent 30%, rgba(255,233,168,.09) 45%, transparent 55%, rgba(255,201,60,.08) 70%, transparent 82%);
  background-size:220% 220%;animation:sheen 12s linear infinite;mix-blend-mode:screen}
@keyframes sheen{0%{background-position:0% 0%}100%{background-position:200% 200%}}
.aurora{position:fixed;inset:-20% -10%;z-index:0;pointer-events:none;filter:blur(110px);opacity:.55}
.aurora span{position:absolute;border-radius:50%;mix-blend-mode:screen;animation:drift 22s ease-in-out infinite}
.aurora span:nth-child(1){width:520px;height:520px;left:5%;top:10%;background:radial-gradient(circle, rgba(255,201,60,.7), transparent 60%)}
.aurora span:nth-child(2){width:460px;height:460px;right:8%;top:20%;background:radial-gradient(circle, rgba(255,233,168,.6), transparent 60%);animation-delay:-6s}
.aurora span:nth-child(3){width:600px;height:600px;left:30%;bottom:5%;background:radial-gradient(circle, rgba(138,90,10,.7), transparent 60%);animation-delay:-12s}
@keyframes drift{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(40px,-30px) scale(1.08)}66%{transform:translate(-30px,35px) scale(.94)}}
.grid-overlay{position:fixed;inset:0;z-index:0;pointer-events:none;opacity:.28;
  background-image:linear-gradient(rgba(255,201,60,.06) 1px, transparent 1px),linear-gradient(90deg, rgba(255,201,60,.06) 1px, transparent 1px);
  background-size:44px 44px;
  mask-image:radial-gradient(circle at 50% 40%, black 30%, transparent 78%);
  -webkit-mask-image:radial-gradient(circle at 50% 40%, black 30%, transparent 78%)}
.particles{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.particles i{position:absolute;bottom:-20px;width:5px;height:5px;border-radius:50%;
  background:radial-gradient(circle, #fff5c8, var(--gold-3));box-shadow:0 0 14px rgba(255,201,60,.95);
  animation:floatUp linear infinite}
@keyframes floatUp{0%{transform:translateY(0) scale(.8);opacity:0}10%{opacity:1}100%{transform:translateY(-110vh) translateX(30px) scale(1.2);opacity:0}}
.wrap{position:relative;z-index:2;max-width:880px;margin:0 auto;padding:28px 16px 60px}
.topbar{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:16px 20px;
  border-radius:var(--radius-md);
  background:linear-gradient(135deg, rgba(30,22,8,.72), rgba(12,9,4,.85));
  border:1px solid var(--line);backdrop-filter:blur(22px) saturate(160%);-webkit-backdrop-filter:blur(22px) saturate(160%);
  box-shadow:0 14px 48px rgba(0,0,0,.6),0 0 0 1px rgba(255,233,168,.06),inset 0 1px 0 rgba(255,233,168,.14);
  margin-bottom:22px}
.brand{display:flex;align-items:center;gap:14px}
.logo{width:50px;height:50px;border-radius:15px;display:grid;place-items:center;
  background:linear-gradient(135deg, #fff5c8 0%, var(--gold-3) 40%, var(--gold-4) 70%, var(--gold-5) 100%);
  color:#1a0f00;font-size:22px;font-weight:900;
  box-shadow:0 0 30px rgba(255,201,60,.7),0 0 60px rgba(255,201,60,.35),inset 0 2px 6px rgba(255,255,255,.7),inset 0 -3px 8px rgba(138,90,10,.5);
  position:relative;overflow:hidden;animation:logoPulse 3s ease-in-out infinite}
.logo::after{content:"";position:absolute;inset:0;background:linear-gradient(120deg, transparent 25%, rgba(255,255,255,.85) 50%, transparent 75%);
  transform:translateX(-150%);animation:logoSheen 3.6s ease-in-out infinite}
@keyframes logoSheen{0%,55%{transform:translateX(-150%)}80%{transform:translateX(150%)}100%{transform:translateX(150%)}}
@keyframes logoPulse{0%,100%{box-shadow:0 0 30px rgba(255,201,60,.7),0 0 60px rgba(255,201,60,.35),inset 0 2px 6px rgba(255,255,255,.7),inset 0 -3px 8px rgba(138,90,10,.5)}50%{box-shadow:0 0 45px rgba(255,201,60,1),0 0 90px rgba(255,201,60,.55),inset 0 2px 8px rgba(255,255,255,.9),inset 0 -3px 10px rgba(138,90,10,.7)}}
.brand-text{line-height:1.15}
.brand-text b{font-family:'Orbitron',sans-serif;font-size:16px;font-weight:900;letter-spacing:2px;
  background:linear-gradient(100deg,#fff5c8 0%, var(--gold-3) 50%, #fff5c8 100%);
  background-size:200% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;
  animation:shine 4s linear infinite;text-transform:uppercase}
.brand-text small{display:block;color:var(--muted);font-size:10px;font-weight:700;letter-spacing:1.8px;text-transform:uppercase;margin-top:4px}
.status-chip{display:inline-flex;align-items:center;gap:8px;font-size:11px;font-weight:800;letter-spacing:.8px;
  padding:8px 14px;border-radius:999px;color:#a8ffda;background:rgba(77,255,184,.08);
  border:1px solid rgba(77,255,184,.35);box-shadow:0 0 20px rgba(77,255,184,.2),inset 0 1px 0 rgba(255,255,255,.1);text-transform:uppercase}
.status-chip .dot{width:7px;height:7px;border-radius:50%;background:var(--success);box-shadow:0 0 10px var(--success);animation:blink 1.6s ease-in-out infinite}
@keyframes blink{50%{opacity:.35}}
.hero{text-align:center;padding:26px 12px 30px;position:relative}
.ascii-glow{position:relative;display:inline-block}
.ascii-glow::before{content:"";position:absolute;inset:-24px -40px;background:radial-gradient(ellipse, rgba(255,201,60,.5), transparent 70%);filter:blur(36px);z-index:-1;animation:heroPulse 3.4s ease-in-out infinite}
@keyframes heroPulse{0%,100%{opacity:.55;transform:scale(.98)}50%{opacity:1;transform:scale(1.02)}}
.ascii-banner{display:inline-block;font-family:'Orbitron',sans-serif;font-weight:900;letter-spacing:6px;
  font-size:clamp(1.7rem, 6vw, 3rem);line-height:1.05;margin:0 auto 8px;
  background:linear-gradient(100deg,#fff9d9 0%,var(--gold-2) 18%,var(--gold-3) 38%,#fff5c8 52%,var(--gold-4) 72%,#fff9d9 100%);
  background-size:280% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;
  text-transform:uppercase;filter:drop-shadow(0 0 20px rgba(255,201,60,.6)) drop-shadow(0 0 40px rgba(255,201,60,.3));
  animation:shine 5s linear infinite}
.ascii-banner .sub{display:block;font-size:.42em;letter-spacing:18px;font-weight:800;margin-top:10px;color:transparent;
  background:linear-gradient(90deg,#ffe9a8,#ffc93c,#ffe9a8);background-size:200% 100%;
  -webkit-background-clip:text;background-clip:text;animation:shine 4s linear infinite}
@keyframes shine{0%{background-position:0% 50%}100%{background-position:200% 50%}}
.hero p{margin-top:16px;color:#d8c79a;font-size:13.5px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;text-shadow:0 0 20px rgba(255,201,60,.35)}
.hero .pills{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin-top:20px}
.hero .pills span{font-size:11px;font-weight:800;letter-spacing:1.4px;padding:9px 16px;border-radius:999px;
  color:#fff5c8;background:linear-gradient(135deg, rgba(255,201,60,.14), rgba(138,90,10,.18));
  border:1px solid var(--line-2);backdrop-filter:blur(10px);
  box-shadow:0 0 20px rgba(255,201,60,.22),inset 0 1px 0 rgba(255,233,168,.35);
  transition:.3s;text-transform:uppercase;position:relative;overflow:hidden}
.hero .pills span::before{content:"";position:absolute;inset:0;background:linear-gradient(120deg, transparent 30%, rgba(255,255,255,.4) 50%, transparent 70%);
  transform:translateX(-120%);animation:pillSheen 4s ease-in-out infinite}
@keyframes pillSheen{0%,60%{transform:translateX(-120%)}80%{transform:translateX(120%)}100%{transform:translateX(120%)}}
.hero .pills span:hover{transform:translateY(-3px) scale(1.03);color:#fff9d9;border-color:var(--gold-2);box-shadow:0 0 35px rgba(255,201,60,.55),inset 0 1px 0 rgba(255,255,255,.6)}
.tg-banner{display:flex;align-items:center;justify-content:center;gap:12px;margin:24px auto 0;padding:14px 22px;max-width:500px;
  border-radius:999px;background:linear-gradient(100deg,rgba(255,201,60,.12) 0%,rgba(255,233,168,.2) 50%,rgba(255,201,60,.12) 100%);
  background-size:220% 100%;border:1px solid var(--gold-3);text-decoration:none;color:#fff9d9;
  font-size:13px;font-weight:800;letter-spacing:1px;transition:.3s;position:relative;overflow:hidden;
  box-shadow:0 0 30px rgba(255,201,60,.35),0 0 60px rgba(255,201,60,.18),inset 0 1px 0 rgba(255,255,255,.5),inset 0 -2px 8px rgba(138,90,10,.3);
  animation:tgPulse 3.5s ease-in-out infinite;text-transform:uppercase}
@keyframes tgPulse{0%,100%{box-shadow:0 0 30px rgba(255,201,60,.35),0 0 60px rgba(255,201,60,.18),inset 0 1px 0 rgba(255,255,255,.5),inset 0 -2px 8px rgba(138,90,10,.3)}50%{box-shadow:0 0 45px rgba(255,201,60,.6),0 0 90px rgba(255,201,60,.3),inset 0 1px 0 rgba(255,255,255,.7),inset 0 -2px 10px rgba(138,90,10,.5)}}
.tg-banner::before{content:"";position:absolute;inset:0;background:linear-gradient(120deg, transparent 30%, rgba(255,255,255,.5) 50%, transparent 70%);
  transform:translateX(-150%);animation:tgSheen 4.5s ease-in-out infinite}
@keyframes tgSheen{0%,60%{transform:translateX(-150%)}85%{transform:translateX(150%)}100%{transform:translateX(150%)}}
.tg-banner:hover{transform:translateY(-3px) scale(1.02);background-position:100% 50%;border-color:var(--gold-2);color:#fff}
.tg-banner i{color:var(--gold-3);font-size:18px;filter:drop-shadow(0 0 8px rgba(255,201,60,.9))}
.tg-banner .tg-tag{color:#fff5c8;font-weight:900;text-shadow:0 0 12px rgba(255,201,60,.8)}
.card{position:relative;margin-top:16px;padding:22px;border-radius:var(--radius-lg);
  background:linear-gradient(150deg, var(--glass-2), rgba(12,9,4,.7));border:1px solid var(--line);
  backdrop-filter:blur(24px) saturate(160%);-webkit-backdrop-filter:blur(24px) saturate(160%);
  box-shadow:0 20px 60px rgba(0,0,0,.6),inset 0 1px 0 rgba(255,233,168,.08),0 0 0 1px rgba(255,201,60,.04);
  overflow:hidden;animation:cardIn .5s ease both}
@keyframes cardIn{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
.card::before{content:"";position:absolute;inset:0;pointer-events:none;border-radius:inherit;background:linear-gradient(120deg,rgba(255,201,60,.06),transparent 42%,rgba(255,233,168,.05));opacity:.7}
.card-head{position:relative;display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:16px}
.card-head h3{font-size:15px;font-weight:800;letter-spacing:.2px;display:flex;align-items:center;gap:9px}
.card-head h3 i{color:var(--gold-3);filter:drop-shadow(0 0 6px rgba(255,201,60,.7))}
.card-kicker{font-size:10px;font-weight:700;letter-spacing:1.4px;text-transform:uppercase;color:var(--muted)}
.section-label{display:flex;align-items:center;gap:8px;font-size:10.5px;font-weight:800;
  letter-spacing:1.6px;text-transform:uppercase;color:#c9a752;margin-bottom:10px}
.section-label i{color:var(--gold-3);font-size:12px}
.tabs{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:18px 0;padding:6px;border-radius:var(--radius-md);
  background:rgba(12,9,4,.7);border:1px solid var(--line)}
.tab{position:relative;padding:12px 8px;border-radius:var(--radius-sm);border:0;background:transparent;
  color:var(--muted);font-family:inherit;font-size:12px;font-weight:800;letter-spacing:.5px;
  cursor:pointer;transition:.25s;display:flex;flex-direction:column;align-items:center;gap:5px;overflow:hidden}
.tab i{font-size:15px}
.tab:hover{color:#ffe9a8}
.tab.active{color:#1a0f00;background:linear-gradient(135deg, #fff5c8 0%, var(--gold-3) 50%, var(--gold-4) 100%);
  box-shadow:0 8px 26px rgba(255,201,60,.5),inset 0 1px 0 rgba(255,255,255,.6);transform:translateY(-1px)}
.tab:active{transform:scale(.97)}
.field{margin-top:12px;animation:fade .35s ease both}
.field:first-child{margin-top:0}
@keyframes fade{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
.field label{display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:800;
  letter-spacing:1.4px;text-transform:uppercase;color:#c9a752;margin:0 0 7px 4px}
.field label i{color:var(--gold-3);font-size:11px}
.input-wrap{position:relative}
.input-wrap > i.lead{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:#7a6530;font-size:13px;pointer-events:none;transition:.25s}
.input-wrap input,.input-wrap textarea{width:100%;color:var(--ink);background:rgba(6,4,2,.75);
  border:1px solid var(--line-2);border-radius:var(--radius-sm);padding:14px 14px 14px 40px;
  font-family:inherit;font-size:13.5px;font-weight:600;outline:none;transition:.25s;box-shadow:inset 0 1px 0 rgba(255,233,168,.05)}
.input-wrap textarea{padding-top:16px;min-height:96px;resize:vertical;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.55}
.input-wrap input::placeholder,.input-wrap textarea::placeholder{color:#6a5a3a}
.input-wrap input:focus,.input-wrap textarea:focus{border-color:var(--gold-3);background:rgba(15,10,3,.9);
  box-shadow:0 0 0 4px rgba(255,201,60,.12),0 0 28px rgba(255,201,60,.3)}
.input-wrap input:focus + i.lead,.input-wrap textarea:focus + i.lead{color:var(--gold-3)}
.input-wrap .eye{position:absolute;right:10px;top:50%;transform:translateY(-50%);width:34px;height:34px;border-radius:10px;
  background:rgba(255,201,60,.08);border:1px solid var(--line);color:#c9a752;display:grid;place-items:center;cursor:pointer;transition:.2s;font-size:12px}
.input-wrap .eye:hover{color:var(--gold-2);border-color:var(--gold-3);background:rgba(255,201,60,.16);box-shadow:0 0 18px rgba(255,201,60,.4)}
.select-wrap{position:relative}
.select-wrap i.lead{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:#7a6530;font-size:13px;pointer-events:none;z-index:1}
.select-wrap select{width:100%;color:var(--ink);background:rgba(6,4,2,.75);border:1px solid var(--line-2);
  border-radius:var(--radius-sm);padding:14px 40px 14px 40px;font-family:inherit;font-size:13.5px;font-weight:700;
  outline:none;transition:.25s;cursor:pointer;appearance:none;-webkit-appearance:none;
  background-image:linear-gradient(45deg, transparent 50%, #c9a752 50%),linear-gradient(135deg, #c9a752 50%, transparent 50%);
  background-position:calc(100% - 20px) 50%, calc(100% - 14px) 50%;background-size:6px 6px, 6px 6px;background-repeat:no-repeat}
.select-wrap select:focus{border-color:var(--gold-3);box-shadow:0 0 0 4px rgba(255,201,60,.12),0 0 28px rgba(255,201,60,.3)}
.select-wrap select option{background:#100b04;color:var(--ink)}
.hint{display:flex;justify-content:space-between;align-items:center;margin-top:8px;color:#8a7650;font-size:11px;font-weight:600}
.hint .count{font-family:'JetBrains Mono',monospace;font-weight:700;color:#d4b970}
.hint .count.warn{color:var(--warn)}
.hint .count.over{color:var(--danger)}
.btn{position:relative;width:100%;margin-top:18px;padding:16px 20px;border:0;border-radius:var(--radius-sm);
  cursor:pointer;font-family:inherit;font-size:14px;font-weight:900;letter-spacing:1px;color:#1a0f00;text-transform:uppercase;
  background:linear-gradient(100deg, #fff5c8 0%, var(--gold-2) 30%, var(--gold-3) 55%, var(--gold-4) 80%, #fff5c8 100%);
  background-size:220% 100%;
  box-shadow:0 12px 36px rgba(255,201,60,.45),0 0 0 1px rgba(255,233,168,.5),inset 0 2px 4px rgba(255,255,255,.7),inset 0 -3px 8px rgba(138,90,10,.4);
  transition:transform .18s, box-shadow .28s, background-position .6s, filter .2s;
  overflow:hidden;display:flex;align-items:center;justify-content:center;gap:10px;
  animation:btnGlow 3s ease-in-out infinite}
@keyframes btnGlow{0%,100%{box-shadow:0 12px 36px rgba(255,201,60,.45),0 0 0 1px rgba(255,233,168,.5),inset 0 2px 4px rgba(255,255,255,.7),inset 0 -3px 8px rgba(138,90,10,.4)}50%{box-shadow:0 12px 46px rgba(255,201,60,.7),0 0 20px rgba(255,201,60,.4),0 0 0 1px rgba(255,233,168,.7),inset 0 2px 6px rgba(255,255,255,.85),inset 0 -3px 10px rgba(138,90,10,.5)}}
.btn::after{content:"";position:absolute;top:50%;left:50%;width:0;height:0;border-radius:50%;background:rgba(255,255,255,.8);
  transform:translate(-50%,-50%);transition:width .6s ease, height .6s ease, opacity .6s ease;opacity:0;pointer-events:none}
.btn:hover{transform:translateY(-3px) scale(1.01);background-position:100% 50%;filter:brightness(1.06)}
.btn:active{transform:translateY(-1px) scale(.98)}
.btn:active::after{width:400px;height:400px;opacity:1;transition:0s}
.btn:disabled{opacity:.6;cursor:not-allowed;transform:none}
.btn:disabled:hover{transform:none;background-position:0 50%}
.btn-ghost{margin-top:10px;width:100%;padding:13px;border:1px solid var(--line-2);border-radius:var(--radius-sm);
  background:rgba(255,201,60,.05);color:#e8d59a;font-family:inherit;font-size:12px;font-weight:800;letter-spacing:.6px;
  cursor:pointer;transition:.25s;display:flex;align-items:center;justify-content:center;gap:8px;position:relative;overflow:hidden;text-transform:uppercase}
.btn-ghost::after{content:"";position:absolute;top:50%;left:50%;width:0;height:0;border-radius:50%;
  background:rgba(255,201,60,.4);transform:translate(-50%,-50%);transition:width .55s ease, height .55s ease, opacity .55s ease;opacity:0;pointer-events:none}
.btn-ghost:hover{border-color:var(--gold-3);color:var(--gold-2);background:rgba(255,201,60,.1);box-shadow:0 0 26px rgba(255,201,60,.3)}
.btn-ghost:active{transform:scale(.98)}
.btn-ghost:active::after{width:320px;height:320px;opacity:1;transition:0s}
.preview{min-height:76px;padding:16px;border-radius:var(--radius-sm);border:1px dashed var(--line-2);
  background:linear-gradient(135deg,rgba(255,201,60,.05),rgba(255,233,168,.05));
  color:#fff5c8;font-size:14.5px;line-height:1.55;word-break:break-word;font-family:'JetBrains Mono',monospace}
.preview.empty{color:#7a6530;font-style:italic}
.result{position:fixed;inset:0;z-index:2000;display:none;align-items:center;justify-content:center;padding:20px;
  background:rgba(2,1,0,.82);backdrop-filter:blur(20px);animation:fade .3s ease}
.result.show{display:flex}
.result-box{max-width:460px;width:100%;padding:32px 26px;border-radius:26px;text-align:center;
  background:linear-gradient(150deg,rgba(30,22,8,.97),rgba(12,9,4,.98));
  border:1px solid var(--line-2);box-shadow:0 30px 100px rgba(0,0,0,.75),0 0 80px rgba(255,201,60,.25);
  animation:pop .35s cubic-bezier(.2,1.4,.4,1) both}
@keyframes pop{from{transform:scale(.9);opacity:0}to{transform:scale(1);opacity:1}}
.result-icon{font-size:64px;margin-bottom:12px;display:block}
.result.ok .result-icon{color:var(--success);animation:ring 1.2s ease infinite}
.result.err .result-icon{color:var(--danger)}
@keyframes ring{0%{transform:scale(1)}50%{transform:scale(1.1)}100%{transform:scale(1)}}
.result-title{font-family:'Orbitron',sans-serif;font-size:22px;font-weight:900;margin-bottom:12px;letter-spacing:2px;
  background:linear-gradient(90deg,#fff5c8,var(--gold-3),#fff5c8);background-size:200% 100%;
  -webkit-background-clip:text;background-clip:text;color:transparent;animation:shine 3s linear infinite;text-transform:uppercase}
.result-body{color:#e0cc95;font-size:13px;line-height:1.7;word-break:break-word;font-weight:600}
.result-body strong{color:#fff5c8}
.result .credit{margin-top:16px;font-size:10px;color:#7a6530;letter-spacing:.6px}
.result .credit a{color:var(--gold-3);text-decoration:none;font-weight:800}
.result .close{margin-top:18px;padding:11px 24px;border-radius:999px;border:1px solid var(--line-2);background:transparent;
  color:#e8d59a;font-family:inherit;font-size:11px;font-weight:800;letter-spacing:1px;cursor:pointer;transition:.2s;text-transform:uppercase}
.result .close:hover{border-color:var(--gold-3);color:var(--gold-2);box-shadow:0 0 22px rgba(255,201,60,.4)}
.credit{text-align:center;padding:28px 10px 8px;color:#7a6530;font-size:11px;letter-spacing:.5px;
  border-top:1px solid rgba(255,201,60,.1);margin-top:32px;line-height:2;font-weight:600}
.credit a{color:var(--gold-3);text-decoration:none;font-weight:800}
.credit a:hover{color:var(--gold-2);text-shadow:0 0 14px rgba(255,201,60,.8)}
.credit .brandline{display:inline-block;font-family:'Orbitron',sans-serif;font-weight:900;letter-spacing:4px;font-size:14px;
  background:linear-gradient(90deg, #fff5c8, var(--gold-3), #fff5c8);background-size:200% 100%;
  -webkit-background-clip:text;background-clip:text;color:transparent;
  animation:shine 4s linear infinite;margin-bottom:8px;text-transform:uppercase}
.credit .badges{display:flex;justify-content:center;gap:16px;flex-wrap:wrap;margin-top:12px;font-size:10px;color:#6a5a3a}
.credit .badges span{display:inline-flex;align-items:center;gap:5px}
.dots::after{content:"";animation:dots 1.4s steps(4,end) infinite}
@keyframes dots{0%{content:""}25%{content:"."}50%{content:".."}75%{content:"..."}}
@media(max-width:600px){
  .wrap{padding:18px 12px 44px}
  .topbar{border-radius:16px;padding:14px 16px}
  .card{padding:18px;border-radius:22px}
  .hero{padding:18px 6px 22px}
  .tabs{gap:6px}
  .tab{font-size:10.5px;padding:10px 4px}
  .tab i{font-size:13px}
  .ascii-banner{letter-spacing:3px}
  .ascii-banner .sub{letter-spacing:10px}
  .hero p{font-size:11px;letter-spacing:1px}
  .tg-banner{font-size:11.5px;padding:12px 16px}
}
</style>
</head>
<body>

<div class="aurora"><span></span><span></span><span></span></div>
<div class="grid-overlay"></div>
<div class="particles" id="particles"></div>

<div class="wrap">
  <div class="topbar">
    <div class="brand">
      <div class="logo">⚡</div>
      <div class="brand-text">
        <b>AGS BIO CHANGER</b>
        <small>Premium Golden · @ags_owner_atif</small>
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
    <p>✦ Fast · Secure · Premium Bio Editing Tool ✦</p>
    <div class="pills">
      <span>👑 AGS</span>
      <span>🛡️ AGS-COMMUNITY</span>
      <span>💎 @ags_owner_atif</span>
    </div>
    <a class="tg-banner" href="https://t.me/ags_owner_atif" target="_blank" rel="noopener">
      <i class="fab fa-telegram"></i>
      <span>Join AGS Community → <span class="tg-tag">@ags_owner_atif</span></span>
    </a>
  </div>

  <div class="card">
    <div class="card-head">
      <h3><i class="fas fa-crown"></i> Bio Editor</h3>
      <span class="card-kicker">Premium Access</span>
    </div>

    <div class="section-label"><i class="fas fa-globe"></i> Region / Server</div>
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

    <div class="tabs">
      <button class="tab active" data-tab="uid"><i class="fas fa-user-lock"></i> UID + PASS</button>
      <button class="tab" data-tab="access"><i class="fas fa-id-badge"></i> ACCESS</button>
      <button class="tab" data-tab="jwt"><i class="fas fa-key"></i> JWT</button>
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
        <textarea id="bio-input" maxlength="300" placeholder="Type your new bio here... [b]bold[/b] [i]italic[/i] [FFC93C]gold[/FFC93C]"></textarea>
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
      <i class="fas fa-crown"></i> UPDATE BIO
    </button>
    <button class="btn-ghost" onclick="clearAll()">
      <i class="fas fa-eraser"></i> Clear All
    </button>
  </div>

  <div class="credit">
    <div class="brandline">AGS · COMMUNITY</div><br>
    Owner <a href="https://t.me/ags_owner_atif" target="_blank">@ags_owner_atif</a> · NAME: AGS
    <div class="badges">
      <span><i class="fas fa-crown"></i> AGS BIO CHANGER</span>
      <span><i class="fas fa-shield-halved"></i> All Rights Reserved © AGS</span>
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
console.log("%c AGS BIO CHANGER ","background:linear-gradient(90deg,#fff5c8,#ffc93c,#d4a017);color:#1a0f00;font-weight:900;padding:6px 14px;border-radius:6px;font-size:13px;letter-spacing:2px;");
(function(){const p=document.getElementById('particles');for(let i=0;i<26;i++){const d=document.createElement('i');d.style.left=Math.random()*100+"%";d.style.animationDuration=(8+Math.random()*10)+"s";d.style.animationDelay=(-Math.random()*12)+"s";d.style.opacity=(.3+Math.random()*.6).toFixed(2);p.appendChild(d);}})();
let currentTab="uid";
document.querySelectorAll('.tab').forEach(btn=>{btn.addEventListener('click',()=>{const t=btn.dataset.tab;currentTab=t;document.querySelectorAll('.tab').forEach(b=>b.classList.toggle('active',b===btn));document.querySelectorAll('.tab-panel').forEach(p=>p.style.display='none');document.getElementById('panel-'+t).style.display='block';});});
function togglePwd(id,btn){const el=document.getElementById(id);const isPwd=el.type==='password';el.type=isPwd?'text':'password';btn.innerHTML=isPwd?'<i class="fas fa-eye-slash"></i>':'<i class="fas fa-eye"></i>';}
const bioEl=document.getElementById('bio-input'),countEl=document.getElementById('bio-count'),previewEl=document.getElementById('preview'),MAX=300;
function updateCount(){const n=bioEl.value.length;countEl.textContent=n+" / "+MAX;countEl.classList.toggle('warn',n>MAX*0.8&&n<=MAX);countEl.classList.toggle('over',n>MAX);}
function escapeHtml(s){return s.replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));}
function renderPreview(){const raw=bioEl.value;if(!raw.trim()){previewEl.textContent="Your bio preview will appear here…";previewEl.classList.add('empty');return;}previewEl.classList.remove('empty');let out=escapeHtml(raw);out=out.replace(/\[b\](.*?)\[\/b\]/gis,'<b>$1</b>');out=out.replace(/\[i\](.*?)\[\/i\]/gis,'<i>$1</i>');out=out.replace(/\[u\](.*?)\[\/u\]/gis,'<u>$1</u>');out=out.replace(/\[s\](.*?)\[\/s\]/gis,'<s>$1</s>');out=out.replace(/\[c\](.*?)\[\/c\]/gis,'<span style="font-style:italic">$1</span>');out=out.replace(/\[([0-9A-Fa-f]{6})\](.*?)\[\/\1\]/g,'<span style="color:#$1">$2</span>');out=out.replace(/\n/g,'<br>');previewEl.innerHTML=out;}
bioEl.addEventListener('input',()=>{updateCount();renderPreview();});updateCount();renderPreview();
function getPayload(){const region=document.getElementById('region').value;const bio=bioEl.value.trim();if(!bio)return{error:"Bio is required"};if(currentTab==='uid'){const uid=document.getElementById('uid-input').value.trim();const pass=document.getElementById('pass-input').value;if(!uid)return{error:"UID is required"};if(!pass)return{error:"Password is required"};return{method:'uid',uid,password:pass,bio,region};}if(currentTab==='access'){const access=document.getElementById('access-input').value.trim();if(!access)return{error:"Access token is required"};return{method:'access',token:access,bio,region};}if(currentTab==='jwt'){const jwt=document.getElementById('jwt-input').value.trim();if(!jwt)return{error:"JWT token is required"};return{method:'jwt',token:jwt,bio,region};}return{error:"Unknown method"};}
async function submitForm(){const payload=getPayload();if(payload.error){showResult(false,"Missing Field",payload.error);return;}const btn=document.getElementById('submit-btn');const original=btn.innerHTML;btn.disabled=true;btn.innerHTML='<i class="fas fa-spinner fa-spin"></i> PROCESSING<span class="dots"></span>';try{const res=await fetch('/api/update',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});const data=await res.json();if(data.status==='success'){showResult(true,"Success",`<div><strong>UID:</strong> ${data.uid||payload.uid||'N/A'}</div><div><strong>Name:</strong> ${data.name||'N/A'}</div><div><strong>Region:</strong> ${data.region_used||payload.region||'N/A'}</div><div><strong>Method:</strong> ${data.login_method||payload.method||'N/A'}</div><div style="margin-top:12px;color:#4dffb8;">✅ ${data.message||'Bio updated successfully'}</div>`);clearAll();}else{showResult(false,"Failed",data.message||data.error||'Unknown error');}}catch(e){showResult(false,"Network Error",escapeHtml(String(e.message||e)));}finally{btn.disabled=false;btn.innerHTML=original;}}
function clearAll(){document.getElementById('uid-input').value='';document.getElementById('pass-input').value='';document.getElementById('access-input').value='';document.getElementById('jwt-input').value='';bioEl.value='';updateCount();renderPreview();}
function showResult(ok,title,bodyHtml){const ov=document.getElementById('result-overlay');const box=document.getElementById('result-box');const icon=document.getElementById('result-icon');document.getElementById('result-title').textContent=title;document.getElementById('result-body').innerHTML=bodyHtml;box.className='result-box '+(ok?'ok':'err');icon.className=(ok?'fas fa-check-circle':'fas fa-times-circle')+' result-icon';ov.classList.add('show');}
function closeResult(){document.getElementById('result-overlay').classList.remove('show');}
document.getElementById('result-overlay').addEventListener('click',e=>{if(e.target.id==='result-overlay')closeResult();});
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
        if not method: method = 'jwt'
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
        return jsonify({"status":"error","message":"Server not configured (AGS_API_URL missing)","owner":OWNER}), 500

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

    headers = {"User-Agent": "AGS-BIO-CHANGER/1.0"}
    if AGS_API_KEY:
        headers['Authorization'] = f"Bearer {AGS_API_KEY}"

    try:
        r = session.get(AGS_API_URL, params=params, headers=headers, timeout=(5, 25))
        r.raise_for_status()
        api_data = r.json()
        ok = bool(api_data.get('success'))
        return jsonify({
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
        })
    except requests.exceptions.Timeout:
        return jsonify({"status":"error","message":"API timeout — try again","owner":OWNER}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"status":"error","message":f"API request failed: {e}","owner":OWNER}), 502
    except Exception as e:
        return jsonify({"status":"error","message":f"Server error: {e}","owner":OWNER}), 500


# ============================================================================
if __name__ == '__main__':
    print("="*60)
    print("  AGS BIO CHANGER — Premium Golden Edition")
    print("  Web  : http://localhost:5000/")
    print("  API  : http://localhost:5000/bio?uid=..&pass=..&bio=..")
    print("="*60)
    app.run(debug=False, host='0.0.0.0', port=8000, threaded=True)