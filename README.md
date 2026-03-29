<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pulsar Star Classification — Technical README</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&display=swap" rel="stylesheet">
<style>
:root {
  --ink:        #0f1117;
  --ink-2:      #2d3142;
  --ink-3:      #5c6178;
  --ink-4:      #9098b0;
  --rule:       #e4e7ef;
  --surface:    #f7f8fc;
  --page:       #ffffff;
  --accent:     #1a56db;
  --accent-dim: #e8effe;
  --accent-mid: #6b8fe8;
  --green:      #0e7c4a;
  --green-bg:   #e9f6ee;
  --amber:      #92500f;
  --amber-bg:   #fef3e2;
  --red:        #b91c1c;
  --red-bg:     #fef2f2;
  --mono:       'DM Mono', monospace;
  --serif:      'DM Serif Display', Georgia, serif;
  --sans:       'DM Sans', system-ui, sans-serif;
  --sidebar-w:  240px;
  --max-w:      780px;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{background:var(--page);color:var(--ink);font-family:var(--sans);font-size:15px;line-height:1.75;-webkit-font-smoothing:antialiased;}

/* LAYOUT */
.shell{display:flex;min-height:100vh;}

/* SIDEBAR */
.sidebar{position:sticky;top:0;height:100vh;width:var(--sidebar-w);min-width:var(--sidebar-w);overflow-y:auto;border-right:1px solid var(--rule);background:var(--surface);display:flex;flex-direction:column;}
.sidebar-logo{padding:1.5rem 1.5rem 1.25rem;border-bottom:1px solid var(--rule);}
.sidebar-project{display:flex;align-items:center;gap:0.6rem;}
.sidebar-icon{width:28px;height:28px;background:var(--ink);border-radius:6px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.sidebar-icon svg{width:16px;height:16px;fill:white;}
.sidebar-name{font-size:0.8rem;font-weight:600;color:var(--ink);line-height:1.3;}
.sidebar-sub{font-size:0.68rem;color:var(--ink-4);margin-top:0.1rem;}
.sidebar-nav{padding:1.25rem 0 2rem;flex:1;}
.nav-group{margin-bottom:0.25rem;}
.nav-group-label{font-family:var(--mono);font-size:0.6rem;font-weight:500;letter-spacing:0.12em;text-transform:uppercase;color:var(--ink-4);padding:0.6rem 1.5rem 0.35rem;display:block;}
.nav-link{display:flex;align-items:center;gap:0.5rem;padding:0.35rem 1.5rem;font-size:0.82rem;color:var(--ink-3);text-decoration:none;font-weight:400;border-left:2px solid transparent;transition:color .15s,background .15s,border-color .15s;}
.nav-link:hover{color:var(--accent);background:var(--accent-dim);}
.nav-link.active{color:var(--accent);border-left-color:var(--accent);background:var(--accent-dim);font-weight:500;}
.nav-link .nav-num{font-family:var(--mono);font-size:0.65rem;color:var(--ink-4);min-width:1.2rem;}
.sidebar-meta{padding:1rem 1.5rem;border-top:1px solid var(--rule);}
.meta-tag{display:inline-block;font-family:var(--mono);font-size:0.63rem;background:var(--accent-dim);color:var(--accent);padding:0.2rem 0.5rem;border-radius:3px;margin:0.15rem 0.1rem;}

/* MAIN */
.main{flex:1;min-width:0;}
.topbar{position:sticky;top:0;z-index:10;background:rgba(255,255,255,0.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--rule);padding:0.75rem 3rem;display:flex;align-items:center;justify-content:space-between;}
.topbar-path{font-family:var(--mono);font-size:0.72rem;color:var(--ink-4);display:flex;align-items:center;gap:0.4rem;}
.topbar-path span{color:var(--ink-3);}
.topbar-path .sep{color:var(--rule);}
.topbar-badges{display:flex;gap:0.5rem;align-items:center;}
.tb-badge{font-family:var(--mono);font-size:0.62rem;padding:0.18rem 0.55rem;border-radius:3px;font-weight:500;background:var(--green-bg);color:var(--green);border:1px solid rgba(14,124,74,.15);}
.tb-badge.b2{background:var(--accent-dim);color:var(--accent);border-color:rgba(26,86,219,.15);}
.tb-badge.b3{background:var(--amber-bg);color:var(--amber);border-color:rgba(146,80,15,.15);}

/* ARTICLE */
.article{max-width:var(--max-w);margin:0 auto;padding:3.5rem 3rem 6rem;}

/* PAGE HEADER */
.page-header{padding-bottom:2.5rem;margin-bottom:3rem;border-bottom:1px solid var(--rule);}
.page-eyebrow{display:flex;align-items:center;gap:0.5rem;margin-bottom:1rem;}
.eyebrow-tag{font-family:var(--mono);font-size:0.65rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--ink-4);}
.eyebrow-dot{color:var(--rule);}
.page-title{font-family:var(--serif);font-size:2.6rem;font-weight:400;line-height:1.15;letter-spacing:-0.02em;color:var(--ink);margin-bottom:1rem;}
.page-title em{font-style:italic;color:var(--accent);}
.page-description{font-size:1.05rem;color:var(--ink-3);max-width:600px;line-height:1.7;font-weight:300;}
.page-meta-row{display:flex;gap:2rem;margin-top:1.75rem;flex-wrap:wrap;}
.meta-item{display:flex;flex-direction:column;gap:0.2rem;}
.meta-key{font-family:var(--mono);font-size:0.62rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--ink-4);}
.meta-val{font-size:0.82rem;font-weight:500;color:var(--ink-2);}

/* SECTIONS */
.doc-section{margin-bottom:3.5rem;scroll-margin-top:5rem;}
.section-heading{display:flex;align-items:baseline;gap:0.75rem;margin-bottom:1.25rem;padding-bottom:0.75rem;border-bottom:1px solid var(--rule);}
.section-num{font-family:var(--mono);font-size:0.68rem;color:var(--ink-4);letter-spacing:0.05em;flex-shrink:0;}
h2{font-family:var(--serif);font-size:1.6rem;font-weight:400;color:var(--ink);letter-spacing:-0.01em;}
h3{font-size:0.78rem;font-weight:600;color:var(--ink);letter-spacing:0.05em;text-transform:uppercase;font-family:var(--mono);margin:2rem 0 0.75rem;}
p{color:var(--ink-3);margin-bottom:0.9rem;font-size:0.93rem;}
p strong{color:var(--ink);font-weight:600;}
p code{font-family:var(--mono);font-size:0.83em;background:var(--surface);border:1px solid var(--rule);padding:0.1em 0.35em;border-radius:3px;color:var(--accent);}

/* CALLOUT */
.callout{display:flex;gap:0.875rem;padding:1rem 1.25rem;border-radius:6px;margin:1.25rem 0;border:1px solid;}
.callout.note{background:var(--accent-dim);border-color:rgba(26,86,219,.2);}
.callout.warn{background:var(--amber-bg);border-color:rgba(146,80,15,.2);}
.callout.danger{background:var(--red-bg);border-color:rgba(185,28,28,.2);}
.callout.success{background:var(--green-bg);border-color:rgba(14,124,74,.2);}
.callout-icon{font-size:1rem;flex-shrink:0;line-height:1.75;}
.callout-body{font-size:0.86rem;color:var(--ink-2);line-height:1.65;}
.callout-body strong{color:var(--ink);}

/* FORMULA */
.formula-block{background:var(--surface);border:1px solid var(--rule);border-left:3px solid var(--accent);border-radius:0 6px 6px 0;padding:1.25rem 1.75rem;margin:1.25rem 0;font-family:var(--mono);}
.formula-label{font-size:0.62rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--ink-4);margin-bottom:0.5rem;}
.formula-eq{font-size:1rem;color:var(--ink);margin-bottom:0.4rem;}
.formula-note{font-size:0.76rem;color:var(--ink-3);}

/* CODE */
.code-wrap{margin:1.5rem 0;border:1px solid var(--rule);border-radius:6px;overflow:hidden;}
.code-header{display:flex;align-items:center;justify-content:space-between;padding:0.6rem 1rem;background:#1e2030;border-bottom:1px solid rgba(255,255,255,.07);}
.code-filename{font-family:var(--mono);font-size:0.68rem;color:rgba(255,255,255,.5);display:flex;align-items:center;gap:0.4rem;}
.code-lang{font-family:var(--mono);font-size:0.6rem;color:rgba(255,255,255,.3);letter-spacing:0.08em;text-transform:uppercase;}
pre{background:#1e2030;padding:1.5rem;overflow-x:auto;font-family:var(--mono);font-size:0.8rem;line-height:1.9;color:#cdd6f4;margin:0;}
.kw{color:#cba6f7;}.fn{color:#89dceb;}.st{color:#a6e3a1;}.cm{color:#585b70;font-style:italic;}.nu{color:#fab387;}.cl{color:#89b4fa;}

/* TABLE */
.doc-table{width:100%;border-collapse:collapse;font-size:0.84rem;margin:1.25rem 0;}
.doc-table th{font-family:var(--mono);font-size:0.63rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--ink-4);font-weight:500;padding:0.6rem 1rem;text-align:left;border-bottom:2px solid var(--rule);background:var(--surface);}
.doc-table td{padding:0.7rem 1rem;border-bottom:1px solid var(--rule);color:var(--ink-3);vertical-align:top;}
.doc-table td:first-child{font-family:var(--mono);font-size:0.78rem;color:var(--accent);font-weight:500;white-space:nowrap;}
.doc-table tr:last-child td{border-bottom:none;}
.doc-table tr:hover td{background:var(--surface);}

/* METRIC CARDS */
.metric-row{display:grid;grid-template-columns:1fr 1fr;gap:0.875rem;margin:1.25rem 0;}
.metric-card{border:1px solid var(--rule);border-radius:6px;padding:1.125rem 1.25rem;background:var(--page);transition:box-shadow .2s;}
.metric-card:hover{box-shadow:0 2px 12px rgba(0,0,0,.07);}
.mc-name{font-family:var(--mono);font-size:0.63rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--ink-4);margin-bottom:0.35rem;}
.mc-formula{font-family:var(--mono);font-size:0.85rem;color:var(--accent);font-weight:500;margin-bottom:0.5rem;}
.mc-desc{font-size:0.8rem;color:var(--ink-3);line-height:1.55;margin:0;}

/* PIPELINE */
.pipeline{margin:1.5rem 0;}
.pipeline-step{display:flex;gap:1rem;padding:0.875rem 0;border-bottom:1px solid var(--rule);align-items:flex-start;}
.pipeline-step:last-child{border-bottom:none;}
.ps-num{font-family:var(--mono);font-size:0.65rem;color:var(--ink-4);min-width:1.75rem;padding-top:0.15rem;}
.ps-title{font-size:0.88rem;font-weight:600;color:var(--ink);margin-bottom:0.2rem;}
.ps-desc{font-size:0.8rem;color:var(--ink-3);margin:0;line-height:1.55;}
.ps-tag{margin-left:auto;font-family:var(--mono);font-size:0.6rem;padding:0.15rem 0.45rem;border-radius:3px;flex-shrink:0;align-self:flex-start;margin-top:0.1rem;}
.ps-tag.critical{background:var(--red-bg);color:var(--red);}
.ps-tag.important{background:var(--amber-bg);color:var(--amber);}
.ps-tag.core{background:var(--accent-dim);color:var(--accent);}

/* COMPARE */
.compare-grid{display:grid;grid-template-columns:1fr 1fr;gap:0;border:1px solid var(--rule);border-radius:6px;overflow:hidden;margin:1.25rem 0;}
.cg-header{padding:0.75rem 1.25rem;font-family:var(--mono);font-size:0.65rem;letter-spacing:0.1em;text-transform:uppercase;font-weight:500;border-bottom:1px solid var(--rule);}
.cg-header.before{background:var(--red-bg);color:var(--red);}
.cg-header.after{background:var(--green-bg);color:var(--green);border-left:1px solid var(--rule);}
.cg-body{padding:1rem 1.25rem;font-size:0.82rem;color:var(--ink-3);line-height:1.65;background:var(--page);}
.cg-body.after-body{border-left:1px solid var(--rule);}
.cg-body strong{color:var(--ink);}

/* CHARTS */
.chart-wrap{margin:1.75rem 0;border:1px solid var(--rule);border-radius:6px;overflow:hidden;background:var(--page);}
.chart-header{padding:0.75rem 1.25rem;border-bottom:1px solid var(--rule);background:var(--surface);display:flex;align-items:center;justify-content:space-between;}
.chart-title{font-family:var(--mono);font-size:0.65rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--ink-3);font-weight:500;}
.chart-note{font-family:var(--mono);font-size:0.62rem;color:var(--ink-4);}
.chart-body{padding:1.5rem;text-align:center;}
.chart-caption{font-size:0.76rem;color:var(--ink-4);text-align:center;padding:0 1.25rem 1rem;line-height:1.5;}

/* CONFUSION MATRIX */
.cm-grid{display:grid;grid-template-columns:auto 1fr 1fr;grid-template-rows:auto 1fr 1fr;gap:6px;margin:1.5rem 0;max-width:480px;}
.cm-col-label{font-family:var(--mono);font-size:0.65rem;letter-spacing:0.08em;text-transform:uppercase;color:var(--ink-4);text-align:center;padding:0.4rem 0;}
.cm-row-label{font-family:var(--mono);font-size:0.65rem;letter-spacing:0.08em;text-transform:uppercase;color:var(--ink-4);display:flex;align-items:center;justify-content:flex-end;padding-right:0.75rem;writing-mode:vertical-rl;text-orientation:mixed;transform:rotate(180deg);}
.cm-cell{border-radius:6px;padding:1.25rem;text-align:center;}
.cm-cell .cell-label{font-family:var(--mono);font-size:1.5rem;font-weight:500;display:block;margin-bottom:0.25rem;}
.cm-cell .cell-name{font-family:var(--mono);font-size:0.68rem;letter-spacing:0.05em;display:block;margin-bottom:0.35rem;}
.cm-cell .cell-desc{font-size:0.74rem;line-height:1.45;}
.cell-tn{background:var(--green-bg);}.cell-tn .cell-label{color:var(--green);}.cell-tn .cell-name{color:var(--green);opacity:.7;}.cell-tn .cell-desc{color:#2d6a4f;}
.cell-fp{background:var(--amber-bg);}.cell-fp .cell-label{color:var(--amber);}.cell-fp .cell-name{color:var(--amber);opacity:.7;}.cell-fp .cell-desc{color:#7c4a0a;}
.cell-fn{background:var(--red-bg);border:2px solid rgba(185,28,28,.3);}.cell-fn .cell-label{color:var(--red);}.cell-fn .cell-name{color:var(--red);opacity:.8;}.cell-fn .cell-desc{color:#991b1b;}
.cell-tp{background:var(--accent-dim);border:2px solid rgba(26,86,219,.25);}.cell-tp .cell-label{color:var(--accent);}.cell-tp .cell-name{color:var(--accent);opacity:.8;}.cell-tp .cell-desc{color:#1e40af;}

/* FOOTER */
.doc-footer{border-top:1px solid var(--rule);padding:2rem 3rem;max-width:var(--max-w);margin:0 auto;display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:1.5rem;}
.footer-col h4{font-family:var(--mono);font-size:0.62rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--ink-4);margin-bottom:0.5rem;font-weight:500;}
.footer-col p{font-size:0.78rem;color:var(--ink-4);margin:0.15rem 0;}

/* REVEAL */
.reveal{opacity:0;transform:translateY(12px);transition:opacity .4s ease,transform .4s ease;}
.reveal.visible{opacity:1;transform:translateY(0);}

@media(max-width:900px){
  .sidebar{display:none;}
  .topbar{padding:.75rem 1.5rem;}
  .article{padding:2rem 1.5rem 4rem;}
  .metric-row{grid-template-columns:1fr;}
  .compare-grid{grid-template-columns:1fr;}
  .cg-header.after,.cg-body.after-body{border-left:none;border-top:1px solid var(--rule);}
}
</style>
</head>
<body>
<div class="shell">

<!-- SIDEBAR -->
<aside class="sidebar">
  <div class="sidebar-logo">
    <div class="sidebar-project">
      <div class="sidebar-icon">
        <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/></svg>
      </div>
      <div>
        <div class="sidebar-name">Pulsar Classification</div>
        <div class="sidebar-sub">HTRU2 · Logistic Regression</div>
      </div>
    </div>
  </div>
  <nav class="sidebar-nav">
    <div class="nav-group">
      <span class="nav-group-label">Overview</span>
      <a href="#s-intro" class="nav-link active"><span class="nav-num">01</span>Introduction</a>
      <a href="#s-problem" class="nav-link"><span class="nav-num">02</span>The Problem</a>
    </div>
    <div class="nav-group">
      <span class="nav-group-label">Mathematics</span>
      <a href="#s-model" class="nav-link"><span class="nav-num">03</span>The Model</a>
      <a href="#s-metrics" class="nav-link"><span class="nav-num">04</span>Evaluation Metrics</a>
      <a href="#s-threshold" class="nav-link"><span class="nav-num">05</span>Threshold Tuning</a>
    </div>
    <div class="nav-group">
      <span class="nav-group-label">Implementation</span>
      <a href="#s-pipeline" class="nav-link"><span class="nav-num">06</span>Data Pipeline</a>
      <a href="#s-code" class="nav-link"><span class="nav-num">07</span>Full Code</a>
      <a href="#s-results" class="nav-link"><span class="nav-num">08</span>Expected Results</a>
      <a href="#s-reference" class="nav-link"><span class="nav-num">09</span>Quick Reference</a>
    </div>
  </nav>
  <div class="sidebar-meta">
    <div class="meta-tag">Python 3.9+</div>
    <div class="meta-tag">scikit-learn</div>
    <div class="meta-tag">pandas</div>
    <div class="meta-tag">matplotlib</div>
  </div>
</aside>

<!-- MAIN -->
<div class="main">
  <div class="topbar">
    <div class="topbar-path">
      <span>ml-projects</span><span class="sep">/</span>
      <span>pulsar-classification</span><span class="sep">/</span>
      <span style="color:var(--ink)">README</span>
    </div>
    <div class="topbar-badges">
      <span class="tb-badge">Logistic Regression</span>
      <span class="tb-badge b2">Class Imbalance</span>
      <span class="tb-badge b3">Threshold Tuning</span>
    </div>
  </div>

  <div class="article">

    <!-- PAGE HEADER -->
    <div class="page-header">
      <div class="page-eyebrow">
        <span class="eyebrow-tag">Machine Learning</span>
        <span class="eyebrow-dot">·</span>
        <span class="eyebrow-tag">Astrophysics</span>
        <span class="eyebrow-dot">·</span>
        <span class="eyebrow-tag">Binary Classification</span>
      </div>
      <h1 class="page-title">Pulsar Star Identification<br><em>from Radio Signal Data</em></h1>
      <p class="page-description">A complete technical guide — from the astrophysics of pulsars to the mathematics of logistic regression, class imbalance, and the threshold-tuning techniques that make the model actually useful.</p>
      <div class="page-meta-row">
        <div class="meta-item"><span class="meta-key">Dataset</span><span class="meta-val">HTRU2 (UCI / Kaggle)</span></div>
        <div class="meta-item"><span class="meta-key">Samples</span><span class="meta-val">17,898 candidates</span></div>
        <div class="meta-item"><span class="meta-key">Features</span><span class="meta-val">8 continuous variables</span></div>
        <div class="meta-item"><span class="meta-key">Class ratio</span><span class="meta-val">90.8% noise / 9.2% pulsar</span></div>
        <div class="meta-item"><span class="meta-key">Algorithm</span><span class="meta-val">Logistic Regression</span></div>
      </div>
    </div>

    <!-- 01 INTRO -->
    <section class="doc-section reveal" id="s-intro">
      <div class="section-heading"><span class="section-num">01</span><h2>What is a Pulsar?</h2></div>
      <p>When a massive star exhausts its fuel and collapses in a supernova explosion, its core can compress into an object roughly the size of a city but with a mass greater than our Sun — a <strong>neutron star</strong>. When a neutron star rotates and emits a focused beam of radio waves, sweeping through space like a lighthouse, it is classified as a <strong>pulsar</strong>.</p>
      <p>Each time the beam crosses Earth, radio telescopes detect a precise, repeating pulse. This regularity makes pulsars extraordinarily useful: they test general relativity, probe the interstellar medium, and are candidates for deep-space navigation systems. But detecting them requires sifting through enormous volumes of data — the vast majority of which is background noise or radio frequency interference.</p>

      <div class="chart-wrap reveal">
        <div class="chart-header"><span class="chart-title">Pulsar Geometry — How a Signal Reaches Earth</span></div>
        <div class="chart-body">
          <svg viewBox="0 0 700 230" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:680px;">
            <defs>
              <radialGradient id="cg1" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="#1a56db" stop-opacity=".9"/>
                <stop offset="55%" stop-color="#3b82f6" stop-opacity=".4"/>
                <stop offset="100%" stop-color="#1a56db" stop-opacity="0"/>
              </radialGradient>
            </defs>
            <g fill="#9098b0" opacity=".4">
              <circle cx="40" cy="30" r="1"/><circle cx="120" cy="18" r="1.2"/><circle cx="260" cy="35" r=".9"/>
              <circle cx="490" cy="22" r="1"/><circle cx="640" cy="45" r="1.1"/><circle cx="680" cy="12" r=".8"/>
              <circle cx="70" cy="195" r="1"/><circle cx="635" cy="185" r=".9"/>
            </g>
            <polygon points="340,115 65,75 65,155" fill="#1a56db" opacity=".06"/>
            <polygon points="340,115 615,75 615,155" fill="#1a56db" opacity=".06"/>
            <line x1="340" y1="115" x2="35" y2="115" stroke="#1a56db" stroke-width="1.5" stroke-dasharray="5 4" opacity=".4"/>
            <line x1="340" y1="115" x2="665" y2="115" stroke="#1a56db" stroke-width="1.5" stroke-dasharray="5 4" opacity=".4"/>
            <ellipse cx="340" cy="115" rx="52" ry="14" fill="none" stroke="#9098b0" stroke-width="1" opacity=".25"/>
            <circle cx="340" cy="115" r="32" fill="url(#cg1)"/>
            <circle cx="340" cy="115" r="17" fill="#1a56db" opacity=".85"/>
            <circle cx="340" cy="115" r="8" fill="#ffffff"/>
            <rect x="628" y="103" width="18" height="22" rx="2" fill="none" stroke="#5c6178" stroke-width="1.5"/>
            <line x1="637" y1="103" x2="637" y2="96" stroke="#5c6178" stroke-width="1.5"/>
            <rect x="632" y="91" width="10" height="6" rx="1" fill="none" stroke="#5c6178" stroke-width="1.5"/>
            <text x="637" y="142" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">Earth</text>
            <g transform="translate(595,64)" stroke="#1a56db" stroke-width="1.5" fill="none" opacity=".8">
              <polyline points="0,10 6,10 8,2 11,18 14,2 17,18 20,10 30,10"/>
            </g>
            <text x="610" y="60" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="8">DETECTED PULSE</text>
            <text x="340" y="182" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="9" letter-spacing="2">NEUTRON STAR · ROTATING · TWIN RADIO BEAMS</text>
          </svg>
        </div>
        <p class="chart-caption">A pulsar's radio beams sweep through space. When one intersects Earth, radio telescopes record a pulse. The regularity of these pulses — some more precise than atomic clocks — is what makes pulsars scientifically invaluable.</p>
      </div>

      <h3>The HTRU2 Dataset</h3>
      <p>This project uses the <strong>High Time Resolution Universe Survey (HTRU2)</strong> dataset. Each row represents one candidate signal. The 8 features capture statistical properties of the signal's integrated pulse profile and its dispersion-measure (DM) curve — two core measurements used by astrophysicists to characterise radio signals.</p>

      <table class="doc-table">
        <thead><tr><th>Feature</th><th>Source</th><th>Description</th></tr></thead>
        <tbody>
          <tr><td>mean_ip</td><td>Integrated Profile</td><td>Mean signal intensity over time</td></tr>
          <tr><td>std_ip</td><td>Integrated Profile</td><td>Standard deviation — spread of intensities</td></tr>
          <tr><td>kurt_ip</td><td>Integrated Profile</td><td>Kurtosis — sharpness of the signal peak (pulsars have very sharp peaks)</td></tr>
          <tr><td>skew_ip</td><td>Integrated Profile</td><td>Skewness — asymmetry of the signal shape</td></tr>
          <tr><td>mean_dm</td><td>DM-SNR Curve</td><td>Mean of the signal-to-noise ratio vs. dispersion measure curve</td></tr>
          <tr><td>std_dm</td><td>DM-SNR Curve</td><td>Standard deviation of the DM curve</td></tr>
          <tr><td>kurt_dm</td><td>DM-SNR Curve</td><td>Kurtosis of the DM curve</td></tr>
          <tr><td>skew_dm</td><td>DM-SNR Curve</td><td>Skewness of the DM curve</td></tr>
        </tbody>
      </table>
    </section>

    <!-- 02 PROBLEM -->
    <section class="doc-section reveal" id="s-problem">
      <div class="section-heading"><span class="section-num">02</span><h2>The Class Imbalance Problem</h2></div>
      <p>Of the 17,898 candidates in HTRU2, only <strong>1,639 are real pulsars (9.2%)</strong>. The remaining <strong>16,259 are noise (90.8%)</strong>. This imbalance reflects reality — real astronomical phenomena are genuinely rare against a background of noise.</p>

      <div class="chart-wrap reveal">
        <div class="chart-header"><span class="chart-title">Class Distribution — HTRU2 Dataset</span><span class="chart-note">n = 17,898 total candidates</span></div>
        <div class="chart-body">
          <svg viewBox="0 0 640 160" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:640px;">
            <rect x="60" y="20" width="462" height="36" rx="3" fill="#fca5a5" opacity=".7"/>
            <rect x="60" y="20" width="462" height="36" rx="3" fill="none" stroke="#ef4444" stroke-width="1" opacity=".5"/>
            <text x="52" y="42" text-anchor="end" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">Noise</text>
            <text x="530" y="42" fill="#5c6178" font-family="DM Mono,monospace" font-size="9">16,259 &nbsp;·&nbsp; 90.8%</text>
            <rect x="60" y="76" width="47" height="36" rx="3" fill="#93c5fd" opacity=".7"/>
            <rect x="60" y="76" width="47" height="36" rx="3" fill="none" stroke="#1a56db" stroke-width="1" opacity=".5"/>
            <text x="52" y="98" text-anchor="end" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">Pulsar</text>
            <text x="115" y="98" fill="#5c6178" font-family="DM Mono,monospace" font-size="9">1,639 &nbsp;·&nbsp; 9.2%</text>
            <line x1="60" y1="130" x2="525" y2="130" stroke="#e4e7ef" stroke-width="1"/>
            <text x="60" y="145" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="8">0</text>
            <text x="176" y="145" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="8">4,000</text>
            <text x="292" y="145" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="8">8,000</text>
            <text x="408" y="145" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="8">12,000</text>
            <text x="524" y="145" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="8">16,000</text>
          </svg>
        </div>
      </div>

      <h3>Why Accuracy Fails</h3>
      <p>A model that predicts <strong>"noise"</strong> for every single input — with no learning — scores <strong>90.8% accuracy</strong>. That sounds high. It is completely useless for finding pulsars.</p>
      <div class="callout warn">
        <span class="callout-icon">⚠</span>
        <div class="callout-body"><strong>The Accuracy Trap:</strong> In imbalanced datasets, overall accuracy is dominated by the majority class. A model that ignores the minority class entirely still scores high. We need metrics that explicitly reward correct identification of pulsars.</div>
      </div>

      <h3>The Confusion Matrix</h3>
      <p>Every prediction falls into one of four categories. These form the foundation of every metric used in this project.</p>
      <div style="margin:1.5rem 0;overflow-x:auto;">
        <div style="min-width:400px;">
          <p style="font-family:var(--mono);font-size:0.65rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--ink-4);text-align:center;margin-bottom:0.4rem;">— Predicted Class —</p>
          <div class="cm-grid">
            <div></div>
            <div class="cm-col-label">Predicted: Noise</div>
            <div class="cm-col-label">Predicted: Pulsar</div>
            <div class="cm-row-label">Actual: Noise</div>
            <div class="cm-cell cell-tn"><span class="cell-label">TN</span><span class="cell-name">True Negative</span><span class="cell-desc">Noise correctly labelled as noise. ✓</span></div>
            <div class="cm-cell cell-fp"><span class="cell-label">FP</span><span class="cell-name">False Positive</span><span class="cell-desc">Noise incorrectly called a pulsar. Wastes follow-up resources.</span></div>
            <div class="cm-row-label">Actual: Pulsar</div>
            <div class="cm-cell cell-fn"><span class="cell-label">FN</span><span class="cell-name">False Negative</span><span class="cell-desc">Real pulsar missed entirely. The most costly error in this domain.</span></div>
            <div class="cm-cell cell-tp"><span class="cell-label">TP</span><span class="cell-name">True Positive</span><span class="cell-desc">Pulsar correctly identified. The primary objective. ✓</span></div>
          </div>
        </div>
      </div>
      <div class="callout danger">
        <span class="callout-icon">✗</span>
        <div class="callout-body"><strong>False Negatives are the critical failure mode.</strong> Missing a real pulsar means a scientifically significant signal is discarded. A well-tuned model must minimise FN — this is directly captured by the Recall metric.</div>
      </div>
    </section>

    <!-- 03 MODEL -->
    <section class="doc-section reveal" id="s-model">
      <div class="section-heading"><span class="section-num">03</span><h2>The Model — Logistic Regression</h2></div>
      <p>Logistic Regression learns a set of <strong>weights</strong> — one per feature — that, when applied to a signal's 8 measurements, produce a probability that the signal is a pulsar. Despite its name, it is a classifier, not a regressor.</p>

      <h3>The Sigmoid Function</h3>
      <p>The model computes a linear combination of the input features and squashes the result into [0, 1] using the <strong>sigmoid function</strong>, producing a valid probability score.</p>

      <div class="formula-block">
        <div class="formula-label">Step 1 — Linear Combination</div>
        <div class="formula-eq">z = w₁x₁ + w₂x₂ + … + w₈x₈ + b</div>
        <div class="formula-note">x₁…x₈ are the 8 input features. w₁…w₈ are the learned weights. b is the bias term.</div>
      </div>
      <div class="formula-block">
        <div class="formula-label">Step 2 — Sigmoid Activation</div>
        <div class="formula-eq">P(pulsar | x) = σ(z) = 1 / (1 + e⁻ᶻ)</div>
        <div class="formula-note">Output is always ∈ (0, 1). Above 0.5 → predict Pulsar. Below 0.5 → predict Noise (by default).</div>
      </div>

      <div class="chart-wrap reveal">
        <div class="chart-header"><span class="chart-title">Sigmoid Function σ(z)</span><span class="chart-note">Maps any real number to (0, 1)</span></div>
        <div class="chart-body">
          <svg viewBox="0 0 640 210" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:640px;">
            <line x1="80" y1="25" x2="80" y2="178" stroke="#e4e7ef" stroke-width="1"/>
            <line x1="80" y1="178" x2="580" y2="178" stroke="#e4e7ef" stroke-width="1"/>
            <line x1="80" y1="101" x2="580" y2="101" stroke="#e4e7ef" stroke-width="1" stroke-dasharray="4 3"/>
            <line x1="330" y1="25" x2="330" y2="178" stroke="#e4e7ef" stroke-width="1" stroke-dasharray="4 3"/>
            <line x1="80" y1="25" x2="580" y2="25" stroke="#e4e7ef" stroke-width="1" stroke-dasharray="4 3"/>
            <path d="M85,175 C110,173 145,169 180,160 C215,151 245,139 268,128 C290,118 308,110 320,105 C325,103 328,102 330,101 C332,100 338,99 350,96 C368,92 390,85 415,76 C440,67 468,56 498,44 C518,38 542,32 570,28"
                  fill="none" stroke="#1a56db" stroke-width="2.5" stroke-linecap="round"/>
            <path d="M330,101 C332,100 338,99 350,96 C368,92 390,85 415,76 C440,67 468,56 498,44 C518,38 542,32 570,28 L570,178 L330,178 Z"
                  fill="#1a56db" opacity=".04"/>
            <circle cx="330" cy="101" r="5" fill="#1a56db" stroke="white" stroke-width="2"/>
            <text x="342" y="90" fill="#1a56db" font-family="DM Mono,monospace" font-size="9">Default threshold = 0.5</text>
            <text x="72" y="29" text-anchor="end" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">1.0</text>
            <text x="72" y="105" text-anchor="end" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">0.5</text>
            <text x="72" y="181" text-anchor="end" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">0.0</text>
            <text x="80" y="196" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">−6</text>
            <text x="330" y="196" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">0</text>
            <text x="580" y="196" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">+6</text>
            <text x="195" y="168" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">→ Predict: Noise</text>
            <text x="468" y="168" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">Predict: Pulsar ←</text>
          </svg>
        </div>
        <p class="chart-caption">No matter the input, σ(z) is always bounded between 0 and 1. The model outputs "73% chance this is a pulsar" — not just a binary label.</p>
      </div>

      <div class="callout note">
        <span class="callout-icon">ℹ</span>
        <div class="callout-body"><strong>Why scale features?</strong> Logistic Regression uses gradient-based optimisation. If one feature ranges 0–1,000 and another 0–1, gradients for each weight have wildly different magnitudes, destabilising training. <code>StandardScaler</code> normalises all features to mean = 0, std = 1 before fitting.</div>
      </div>
    </section>

    <!-- 04 METRICS -->
    <section class="doc-section reveal" id="s-metrics">
      <div class="section-heading"><span class="section-num">04</span><h2>Evaluation Metrics</h2></div>
      <p>Four metrics are central to evaluating a classifier on imbalanced data. Each answers a different question about model behaviour, and together they give a complete performance picture.</p>

      <div class="metric-row">
        <div class="metric-card">
          <div class="mc-name">Precision</div>
          <div class="mc-formula">TP / (TP + FP)</div>
          <p class="mc-desc">Of all signals labelled "pulsar," what fraction were genuine? High precision means few false alarms.</p>
        </div>
        <div class="metric-card">
          <div class="mc-name">Recall  ·  Sensitivity</div>
          <div class="mc-formula">TP / (TP + FN)</div>
          <p class="mc-desc">Of all real pulsars, what fraction did we catch? High recall means few missed pulsars. This is the primary objective in this domain.</p>
        </div>
        <div class="metric-card">
          <div class="mc-name">F1-Score</div>
          <div class="mc-formula">2 × (P × R) / (P + R)</div>
          <p class="mc-desc">The harmonic mean of Precision and Recall. Penalises extreme values of either metric. Use this to find the optimal threshold.</p>
        </div>
        <div class="metric-card">
          <div class="mc-name">ROC-AUC</div>
          <div class="mc-formula">Area Under ROC Curve</div>
          <p class="mc-desc">Overall ability to discriminate between classes across all thresholds. AUC = 1.0 is perfect. AUC = 0.5 equals random guessing.</p>
        </div>
      </div>

      <h3>The Precision–Recall Trade-off</h3>
      <div class="chart-wrap reveal">
        <div class="chart-header"><span class="chart-title">Precision &amp; Recall vs. Classification Threshold</span></div>
        <div class="chart-body">
          <svg viewBox="0 0 640 210" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:640px;">
            <line x1="80" y1="25" x2="80" y2="178" stroke="#e4e7ef" stroke-width="1"/>
            <line x1="80" y1="178" x2="580" y2="178" stroke="#e4e7ef" stroke-width="1"/>
            <line x1="80" y1="101" x2="580" y2="101" stroke="#e4e7ef" stroke-width="1" stroke-dasharray="3 3"/>
            <line x1="80" y1="25" x2="580" y2="25" stroke="#e4e7ef" stroke-width="1" stroke-dasharray="3 3"/>
            <path d="M85,30 C120,36 160,50 200,66 C240,82 278,104 315,125 C345,142 375,156 415,166 C450,174 488,178 555,178"
                  fill="none" stroke="#1a56db" stroke-width="2.5" stroke-linecap="round"/>
            <path d="M85,178 C115,172 155,160 195,144 C235,128 272,107 310,89 C342,74 374,58 416,48 C450,40 488,33 555,28"
                  fill="none" stroke="#ef4444" stroke-width="2.5" stroke-linecap="round"/>
            <line x1="308" y1="25" x2="308" y2="178" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="5 3" opacity=".9"/>
            <circle cx="308" cy="107" r="6" fill="#f59e0b" stroke="white" stroke-width="2"/>
            <text x="148" y="58" fill="#1a56db" font-family="DM Mono,monospace" font-size="10">Recall</text>
            <text x="460" y="45" fill="#ef4444" font-family="DM Mono,monospace" font-size="10">Precision</text>
            <text x="320" y="85" fill="#f59e0b" font-family="DM Mono,monospace" font-size="9">Best F1</text>
            <text x="72" y="29" text-anchor="end" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">1.0</text>
            <text x="72" y="105" text-anchor="end" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">0.5</text>
            <text x="72" y="181" text-anchor="end" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">0.0</text>
            <text x="80" y="196" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">0.0</text>
            <text x="330" y="196" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">0.5</text>
            <text x="580" y="196" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">1.0</text>
            <text x="330" y="208" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">Threshold →</text>
          </svg>
        </div>
        <p class="chart-caption">The optimal threshold (amber) is where F1-Score peaks — balancing Precision and Recall rather than maximising either in isolation.</p>
      </div>

      <h3>The ROC Curve</h3>
      <div class="chart-wrap reveal">
        <div class="chart-header"><span class="chart-title">ROC Curve — Illustrative Performance</span><span class="chart-note">Expected AUC ≈ 0.97–0.98</span></div>
        <div class="chart-body">
          <svg viewBox="0 0 400 310" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:360px;">
            <defs>
              <linearGradient id="aucF" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#1a56db" stop-opacity=".1"/>
                <stop offset="100%" stop-color="#1a56db" stop-opacity=".02"/>
              </linearGradient>
            </defs>
            <rect x="55" y="28" width="300" height="250" fill="#f7f8fc" rx="2"/>
            <line x1="55" y1="153" x2="355" y2="153" stroke="#e4e7ef" stroke-width="1"/>
            <line x1="205" y1="28" x2="205" y2="278" stroke="#e4e7ef" stroke-width="1"/>
            <line x1="55" y1="278" x2="355" y2="28" stroke="#9098b0" stroke-width="1.5" stroke-dasharray="6 4" opacity=".6"/>
            <text x="240" y="175" fill="#9098b0" font-family="DM Mono,monospace" font-size="8" transform="rotate(-40,240,175)">Random AUC=0.5</text>
            <path d="M55,278 C75,238 90,175 112,136 C138,92 168,66 205,50 C245,36 285,31 355,28 L355,278 Z" fill="url(#aucF)"/>
            <path d="M55,278 C75,238 90,175 112,136 C138,92 168,66 205,50 C245,36 285,31 355,28" fill="none" stroke="#1a56db" stroke-width="2.5" stroke-linecap="round"/>
            <text x="272" y="198" fill="#1a56db" font-family="DM Mono,monospace" font-size="14" font-weight="500">≈ 0.98</text>
            <text x="272" y="213" fill="#9098b0" font-family="DM Mono,monospace" font-size="9">AUC Score</text>
            <circle cx="55" cy="28" r="4" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="65" y="26" fill="#9098b0" font-family="DM Mono,monospace" font-size="8">Perfect (0,1)</text>
            <line x1="55" y1="278" x2="355" y2="278" stroke="#5c6178" stroke-width="1"/>
            <line x1="55" y1="28" x2="55" y2="278" stroke="#5c6178" stroke-width="1"/>
            <text x="55" y="296" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="8">0</text>
            <text x="205" y="296" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="8">0.5</text>
            <text x="355" y="296" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="8">1.0</text>
            <text x="205" y="310" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="8">False Positive Rate →</text>
            <text x="43" y="153" text-anchor="end" fill="#9098b0" font-family="DM Mono,monospace" font-size="8">0.5</text>
            <text x="43" y="31" text-anchor="end" fill="#9098b0" font-family="DM Mono,monospace" font-size="8">1.0</text>
            <text x="20" y="153" text-anchor="middle" fill="#9098b0" font-family="DM Mono,monospace" font-size="8" transform="rotate(-90,20,153)">TPR →</text>
          </svg>
        </div>
        <p class="chart-caption">The curve hugs the top-left corner — far above the random baseline. AUC ≈ 0.98 indicates the model has strong intrinsic discriminative ability, even before threshold tuning.</p>
      </div>
    </section>

    <!-- 05 THRESHOLD -->
    <section class="doc-section reveal" id="s-threshold">
      <div class="section-heading"><span class="section-num">05</span><h2>Threshold Tuning</h2></div>
      <p>By default, <code>.predict()</code> labels any sample with predicted probability ≥ 0.5 as "pulsar." This threshold is arbitrary. On imbalanced data, the optimal threshold is almost never 0.5.</p>

      <div class="formula-block">
        <div class="formula-label">Threshold Application</div>
        <div class="formula-eq">ŷᵢ = 1 &nbsp; if &nbsp; P(pulsar | xᵢ) ≥ τ &nbsp; else &nbsp; 0</div>
        <div class="formula-note">τ (tau) is the threshold we tune. The optimal τ is found by computing F1-Score at each τ ∈ [0.1, 0.9] in increments of 0.01.</div>
      </div>

      <h3>Effect of class_weight='balanced'</h3>
      <div class="compare-grid">
        <div class="cg-header before">Without class_weight='balanced'</div>
        <div class="cg-header after">With class_weight='balanced'</div>
        <div class="cg-body">Model treats all errors equally. Learns to be conservative — only predicts "pulsar" when very confident. <strong>High precision, low recall.</strong></div>
        <div class="cg-body after-body">Penalises missed pulsars ~10× more, proportional to class frequencies. Learns to be more sensitive. <strong>Higher recall, fewer missed pulsars.</strong></div>
      </div>
    </section>

    <!-- 06 PIPELINE -->
    <section class="doc-section reveal" id="s-pipeline">
      <div class="section-heading"><span class="section-num">06</span><h2>Data Pipeline</h2></div>
      <div class="pipeline">
        <div class="pipeline-step"><span class="ps-num">01</span><div><div class="ps-title">Load &amp; Exploratory Analysis</div><p class="ps-desc">Read HTRU_2.csv, check dtypes and missing values, quantify imbalance with <code>value_counts()</code>, visualise feature distributions by class.</p></div><span class="ps-tag important">EDA</span></div>
        <div class="pipeline-step"><span class="ps-num">02</span><div><div class="ps-title">Stratified Train / Test Split</div><p class="ps-desc">Split 80/20 with <code>stratify=y</code> to preserve the 90.8/9.2 class ratio in both sets, preventing biased evaluation.</p></div><span class="ps-tag critical">Critical</span></div>
        <div class="pipeline-step"><span class="ps-num">03</span><div><div class="ps-title">Feature Scaling — StandardScaler</div><p class="ps-desc">Fit the scaler on training data only, then transform both sets. Fitting on test data constitutes data leakage.</p></div><span class="ps-tag critical">Critical</span></div>
        <div class="pipeline-step"><span class="ps-num">04</span><div><div class="ps-title">Baseline Logistic Regression</div><p class="ps-desc">Train a default model with no class weighting. Record precision, recall, and F1 for the pulsar class. This is the performance floor.</p></div><span class="ps-tag important">Baseline</span></div>
        <div class="pipeline-step"><span class="ps-num">05</span><div><div class="ps-title">Re-train with class_weight='balanced'</div><p class="ps-desc">Retrain with balanced class weights. Compare recall against the baseline. Expect a meaningful improvement.</p></div><span class="ps-tag core">Imbalance</span></div>
        <div class="pipeline-step"><span class="ps-num">06</span><div><div class="ps-title">Threshold Optimisation</div><p class="ps-desc">Extract probabilities via <code>predict_proba()</code>. Sweep thresholds 0.1–0.9 in 0.01 steps. Select the threshold that maximises F1-Score.</p></div><span class="ps-tag core">Core Task</span></div>
        <div class="pipeline-step"><span class="ps-num">07</span><div><div class="ps-title">Plot ROC &amp; Precision-Recall Curves</div><p class="ps-desc">Visualise performance across all thresholds. Compute AUC. Generate the final classification report with the optimal threshold applied.</p></div></div>
      </div>
    </section>

    <!-- 07 CODE -->
    <section class="doc-section reveal" id="s-code">
      <div class="section-heading"><span class="section-num">07</span><h2>Full Implementation</h2></div>
      <div class="code-wrap">
        <div class="code-header">
          <span class="code-filename">📄 pulsar_classification.py</span>
          <span class="code-lang">Python 3.9+</span>
        </div>
        <pre><span class="cm"># ── 1. IMPORTS ──────────────────────────────────────────────────</span>
<span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">import</span> numpy <span class="kw">as</span> np
<span class="kw">import</span> matplotlib.pyplot <span class="kw">as</span> plt
<span class="kw">from</span> sklearn.model_selection  <span class="kw">import</span> train_test_split
<span class="kw">from</span> sklearn.preprocessing   <span class="kw">import</span> StandardScaler
<span class="kw">from</span> sklearn.linear_model    <span class="kw">import</span> LogisticRegression
<span class="kw">from</span> sklearn.metrics         <span class="kw">import</span> (
    classification_report, roc_auc_score,
    roc_curve, f1_score
)

<span class="cm"># ── 2. LOAD & INSPECT ───────────────────────────────────────────</span>
cols = [<span class="st">'mean_ip'</span>, <span class="st">'std_ip'</span>, <span class="st">'kurt_ip'</span>, <span class="st">'skew_ip'</span>,
        <span class="st">'mean_dm'</span>, <span class="st">'std_dm'</span>, <span class="st">'kurt_dm'</span>, <span class="st">'skew_dm'</span>, <span class="st">'target'</span>]
df = pd.<span class="fn">read_csv</span>(<span class="st">'HTRU_2.csv'</span>, header=<span class="nu">None</span>, names=cols)

print(df[<span class="st">'target'</span>].<span class="fn">value_counts</span>())
<span class="cm"># 0    16259   (noise)
# 1     1639   (pulsar)</span>

X = df.drop(<span class="st">'target'</span>, axis=<span class="nu">1</span>)
y = df[<span class="st">'target'</span>]

<span class="cm"># ── 3. STRATIFIED SPLIT ─────────────────────────────────────────</span>
X_train, X_test, y_train, y_test = <span class="fn">train_test_split</span>(
    X, y, test_size=<span class="nu">0.2</span>, random_state=<span class="nu">42</span>, stratify=y
)

<span class="cm"># ── 4. FEATURE SCALING (fit on train only) ──────────────────────</span>
scaler  = <span class="cl">StandardScaler</span>()
X_train = scaler.<span class="fn">fit_transform</span>(X_train)
X_test  = scaler.<span class="fn">transform</span>(X_test)

<span class="cm"># ── 5. BASELINE MODEL ───────────────────────────────────────────</span>
baseline = <span class="cl">LogisticRegression</span>(max_iter=<span class="nu">1000</span>, random_state=<span class="nu">42</span>)
baseline.<span class="fn">fit</span>(X_train, y_train)
print(<span class="st">"── Baseline ──"</span>)
print(<span class="fn">classification_report</span>(y_test, baseline.<span class="fn">predict</span>(X_test),
      target_names=[<span class="st">'Noise'</span>, <span class="st">'Pulsar'</span>]))

<span class="cm"># ── 6. BALANCED CLASS WEIGHTS ───────────────────────────────────</span>
model = <span class="cl">LogisticRegression</span>(
    class_weight=<span class="st">'balanced'</span>, max_iter=<span class="nu">1000</span>, random_state=<span class="nu">42</span>
)
model.<span class="fn">fit</span>(X_train, y_train)

<span class="cm"># ── 7. THRESHOLD TUNING ─────────────────────────────────────────</span>
y_proba        = model.<span class="fn">predict_proba</span>(X_test)[:, <span class="nu">1</span>]
best_threshold = <span class="nu">0.5</span>
best_f1        = <span class="nu">0.0</span>
log            = []

<span class="kw">for</span> t <span class="kw">in</span> np.<span class="fn">arange</span>(<span class="nu">0.1</span>, <span class="nu">0.91</span>, <span class="nu">0.01</span>):
    f1 = <span class="fn">f1_score</span>(y_test, (y_proba >= t).<span class="fn">astype</span>(int), zero_division=<span class="nu">0</span>)
    log.<span class="fn">append</span>((t, f1))
    <span class="kw">if</span> f1 > best_f1:
        best_f1, best_threshold = f1, t

print(<span class="st">f"Optimal threshold : {best_threshold:.2f}"</span>)
print(<span class="st">f"Best F1-Score     : {best_f1:.4f}"</span>)

y_final = (y_proba >= best_threshold).<span class="fn">astype</span>(int)
print(<span class="st">"── Tuned Model ──"</span>)
print(<span class="fn">classification_report</span>(y_test, y_final,
      target_names=[<span class="st">'Noise'</span>, <span class="st">'Pulsar'</span>]))

<span class="cm"># ── 8. ROC CURVE ────────────────────────────────────────────────</span>
fpr, tpr, _ = <span class="fn">roc_curve</span>(y_test, y_proba)
auc_score   = <span class="fn">roc_auc_score</span>(y_test, y_proba)

fig, axes = plt.<span class="fn">subplots</span>(<span class="nu">1</span>, <span class="nu">2</span>, figsize=(<span class="nu">12</span>, <span class="nu">5</span>))

axes[<span class="nu">0</span>].<span class="fn">plot</span>(fpr, tpr, lw=<span class="nu">2</span>, label=<span class="st">f'AUC = {auc_score:.3f}'</span>)
axes[<span class="nu">0</span>].<span class="fn">plot</span>([<span class="nu">0</span>,<span class="nu">1</span>], [<span class="nu">0</span>,<span class="nu">1</span>], <span class="st">'--'</span>, color=<span class="st">'grey'</span>)
axes[<span class="nu">0</span>].<span class="fn">set</span>(xlabel=<span class="st">'False Positive Rate'</span>, ylabel=<span class="st">'True Positive Rate'</span>,
         title=<span class="st">'ROC Curve'</span>)
axes[<span class="nu">0</span>].<span class="fn">legend</span>()

thresholds, f1s = <span class="fn">zip</span>(*log)
axes[<span class="nu">1</span>].<span class="fn">plot</span>(thresholds, f1s, lw=<span class="nu">2</span>)
axes[<span class="nu">1</span>].<span class="fn">axvline</span>(best_threshold, color=<span class="st">'red'</span>, ls=<span class="st">'--'</span>,
             label=<span class="st">f'Best τ = {best_threshold:.2f}'</span>)
axes[<span class="nu">1</span>].<span class="fn">set</span>(xlabel=<span class="st">'Threshold'</span>, ylabel=<span class="st">'F1-Score'</span>,
         title=<span class="st">'F1-Score vs Threshold'</span>)
axes[<span class="nu">1</span>].<span class="fn">legend</span>()

plt.<span class="fn">tight_layout</span>()
plt.<span class="fn">savefig</span>(<span class="st">'results.png'</span>, dpi=<span class="nu">150</span>)
plt.<span class="fn">show</span>()</pre>
      </div>
    </section>

    <!-- 08 RESULTS -->
    <section class="doc-section reveal" id="s-results">
      <div class="section-heading"><span class="section-num">08</span><h2>Expected Results</h2></div>
      <table class="doc-table">
        <thead><tr><th>Model Configuration</th><th>Precision (Pulsar)</th><th>Recall (Pulsar)</th><th>F1 (Pulsar)</th><th>ROC-AUC</th></tr></thead>
        <tbody>
          <tr><td>Baseline (default threshold)</td><td>~0.86</td><td>~0.68</td><td>~0.76</td><td>~0.97</td></tr>
          <tr><td>class_weight='balanced'</td><td>~0.79</td><td>~0.88</td><td>~0.83</td><td>~0.98</td></tr>
          <tr><td>Balanced + Optimal threshold</td><td>~0.83</td><td>~0.91</td><td>~0.87</td><td>~0.98</td></tr>
        </tbody>
      </table>
      <div class="callout success">
        <span class="callout-icon">✓</span>
        <div class="callout-body"><strong>Key observation:</strong> The baseline AUC is already strong (~0.97), indicating good intrinsic class separation. Threshold tuning converts that latent ability into operational improvement — specifically higher Recall, meaning fewer missed pulsars in practice.</div>
      </div>
      <div class="callout note">
        <span class="callout-icon">ℹ</span>
        <div class="callout-body"><strong>Going further:</strong> Explore SMOTE for synthetic minority oversampling, cross-validated threshold selection to avoid overfitting on the test set, and tree-based alternatives (Random Forest, Gradient Boosting) as a comparison baseline.</div>
      </div>
    </section>

    <!-- 09 REFERENCE -->
    <section class="doc-section reveal" id="s-reference">
      <div class="section-heading"><span class="section-num">09</span><h2>Quick Reference</h2></div>
      <table class="doc-table">
        <thead><tr><th>Term</th><th>Definition</th></tr></thead>
        <tbody>
          <tr><td>Class imbalance</td><td>One class far outnumbers another, making standard accuracy misleading as a performance metric.</td></tr>
          <tr><td>Stratified split</td><td>Ensures both train and test sets preserve the original class ratio. Prevents evaluation bias.</td></tr>
          <tr><td>StandardScaler</td><td>Normalises features to mean=0, std=1. Must be fit on training data only to prevent data leakage.</td></tr>
          <tr><td>Data leakage</td><td>When test-set information accidentally influences model training, inflating reported metrics.</td></tr>
          <tr><td>class_weight='balanced'</td><td>Adjusts the loss function so minority class errors are penalised proportionally more during training.</td></tr>
          <tr><td>predict_proba()</td><td>Returns raw probability scores instead of hard class labels, enabling threshold optimisation.</td></tr>
          <tr><td>Precision</td><td>TP / (TP + FP). Of everything called "pulsar," what fraction truly was?</td></tr>
          <tr><td>Recall</td><td>TP / (TP + FN). Of all real pulsars, what fraction did we catch?</td></tr>
          <tr><td>F1-Score</td><td>Harmonic mean of Precision and Recall. Use as the objective when selecting an optimal threshold.</td></tr>
          <tr><td>ROC-AUC</td><td>Discrimination ability across all thresholds. Ranges from 0.5 (random) to 1.0 (perfect).</td></tr>
          <tr><td>Threshold τ</td><td>The probability cutoff above which a sample is labelled "pulsar." Default 0.5; optimise for your use case.</td></tr>
        </tbody>
      </table>
    </section>

  </div><!-- /article -->

  <footer class="doc-footer">
    <div class="footer-col"><h4>Project</h4><p>Pulsar Star Classification</p><p>HTRU2 · Binary Classification</p></div>
    <div class="footer-col"><h4>Algorithm</h4><p>Logistic Regression</p><p>scikit-learn · Python 3.9+</p></div>
    <div class="footer-col"><h4>Source</h4><p>R. J. Lyon et al.</p><p>UCI Machine Learning Repository</p></div>
  </footer>

</div><!-- /main -->
</div><!-- /shell -->

<script>
const sections = document.querySelectorAll('.doc-section');
const navLinks = document.querySelectorAll('.nav-link');
const io1 = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      navLinks.forEach(l => l.classList.remove('active'));
      const a = document.querySelector(`.nav-link[href="#${e.target.id}"]`);
      if (a) a.classList.add('active');
    }
  });
}, { rootMargin: '-20% 0px -70% 0px' });
sections.forEach(s => io1.observe(s));

const io2 = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('visible'); io2.unobserve(e.target); }
  });
}, { threshold: 0.08 });
document.querySelectorAll('.reveal').forEach(el => io2.observe(el));
</script>
</body>
</html>