import re

# Read the extracted SVG
with open('india_svg_extracted.txt', encoding='utf-8') as f:
    india_svg = f.read()

# Update styling on the SVG
india_svg = india_svg.replace(
    '<svg class="india-svg" viewBox="0 0 612 696" fill="none">',
    '<svg id="indiaSvg" class="india-svg" viewBox="0 0 612 696" fill="none" xmlns="http://www.w3.org/2000/svg">'
)

# Build complete new HTML
new_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IGP by Sparklehood | India\'s Premier EV Charging Station Installation Services</title>
  <meta name="description" content="Turnkey EV Charging Station Installation across India for Homes, Apartments, Offices, Malls, Hotels, Hospitals, and EV Fleets. Discom &amp; CEA Approved.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
  <style>
    /* =====================================================================
       DESIGN TOKENS
       ===================================================================== */
    :root {
      --bg-dark: #0B192C;
      --bg-darker: #080E1A;
      --bg-card-dark: #102238;
      --bg-light: #F8FAFC;
      --white: #FFFFFF;
      --blue: #0052FF;
      --blue-600: #0044D9;
      --blue-glow: rgba(0, 82, 255, 0.22);
      --green: #10B981;
      --green-bright: #00E599;
      --green-glow: rgba(16, 185, 129, 0.25);
      --text-dark: #0F172A;
      --text-light: #F8FAFC;
      --text-muted: #64748B;
      --text-muted-dark: #94A3B8;
      --border-light: rgba(226, 232, 240, 0.8);
      --border-dark: rgba(30, 41, 59, 0.9);
      --cyan: #00D4FF;
      --transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      --shadow-sm: 0 1px 4px rgba(15, 23, 42, 0.07);
      --shadow-md: 0 4px 20px rgba(15, 23, 42, 0.10);
      --shadow-lg: 0 16px 48px rgba(15, 23, 42, 0.14);
      --shadow-blue: 0 8px 24px rgba(0, 82, 255, 0.28);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --radius-xl: 20px;
    }

    *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

    html { scroll-behavior: smooth; overflow-x: hidden; }

    body {
      font-family: \'Plus Jakarta Sans\', system-ui, -apple-system, sans-serif;
      background: var(--white);
      color: var(--text-dark);
      line-height: 1.65;
      -webkit-font-smoothing: antialiased;
    }

    /* =====================================================================
       TYPOGRAPHY
       ===================================================================== */
    h1, h2, h3, h4, h5 {
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.15;
      color: var(--text-dark);
    }
    p { color: var(--text-muted); }
    a { text-decoration: none; }

    /* =====================================================================
       UTILITIES
       ===================================================================== */
    .container {
      width: 100%;
      max-width: 1264px;
      margin: 0 auto;
      padding: 0 24px;
    }

    section { padding: 96px 0; position: relative; }

    .badge-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 14px;
      border-radius: 999px;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      border: 1px solid;
    }
    .badge-blue {
      background: rgba(0,82,255,0.07);
      border-color: rgba(0,82,255,0.18);
      color: var(--blue);
    }
    .badge-cyan {
      background: rgba(0,212,255,0.08);
      border-color: rgba(0,212,255,0.25);
      color: var(--cyan);
    }
    .badge-green {
      background: rgba(16,185,129,0.1);
      border-color: rgba(16,185,129,0.3);
      color: var(--green);
    }

    .section-header {
      text-align: center;
      max-width: 640px;
      margin: 0 auto 56px;
    }
    .section-header h2 {
      font-size: clamp(1.75rem, 4vw, 2.6rem);
      margin: 10px 0 12px;
    }
    .section-header p { font-size: 1.05rem; }

    /* =====================================================================
       SCROLL PROGRESS
       ===================================================================== */
    .scroll-progress {
      position: fixed; top: 0; left: 0; height: 3px; width: 0%;
      background: linear-gradient(90deg, var(--blue), var(--cyan), var(--green));
      z-index: 9999;
      transition: width 0.1s ease-out;
    }

    /* =====================================================================
       NAVBAR
       ===================================================================== */
    .navbar {
      position: fixed; top: 0; left: 0; width: 100%; z-index: 1000;
      padding: 0;
      transition: var(--transition);
    }
    .navbar-inner {
      display: flex; align-items: center; justify-content: space-between;
      padding: 16px 32px;
      border-bottom: 1px solid transparent;
      transition: var(--transition);
    }
    .navbar.scrolled .navbar-inner {
      background: rgba(255,255,255,0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom-color: var(--border-light);
      box-shadow: 0 1px 16px rgba(15,23,42,0.06);
      padding: 12px 32px;
    }

    .brand-logo {
      display: flex; align-items: center; gap: 10px;
      text-decoration: none;
    }
    .logo-mark {
      width: 38px; height: 38px; border-radius: var(--radius-sm);
      background: var(--blue);
      display: flex; align-items: center; justify-content: center;
      flex-shrink: 0;
      box-shadow: 0 2px 10px var(--blue-glow);
    }
    .brand-name-wrap { display: flex; flex-direction: column; gap: 0; }
    .brand-name { font-size: 1.15rem; font-weight: 800; color: var(--text-dark); letter-spacing: -0.03em; line-height: 1.1; }
    .navbar.scrolled .brand-name { color: var(--text-dark); }
    .navbar:not(.scrolled) .brand-name { color: var(--white); }
    .brand-sub { font-size: 0.68rem; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.07em; line-height: 1; }
    .navbar:not(.scrolled) .brand-sub { color: rgba(255,255,255,0.6); }

    .nav-links {
      display: flex; align-items: center; gap: 2px;
      list-style: none;
    }
    .nav-link {
      padding: 8px 12px; border-radius: var(--radius-sm);
      font-size: 0.875rem; font-weight: 600;
      color: var(--text-muted);
      transition: var(--transition);
      cursor: pointer;
    }
    .navbar:not(.scrolled) .nav-link { color: rgba(255,255,255,0.75); }
    .nav-link:hover {
      color: var(--blue);
      background: rgba(0,82,255,0.06);
    }
    .navbar:not(.scrolled) .nav-link:hover {
      color: var(--white);
      background: rgba(255,255,255,0.1);
    }

    .btn-nav {
      display: inline-flex; align-items: center; gap: 8px;
      padding: 9px 18px;
      background: var(--blue);
      color: var(--white);
      border: none; border-radius: var(--radius-md);
      font-size: 0.875rem; font-weight: 700;
      cursor: pointer;
      transition: var(--transition);
      box-shadow: var(--shadow-blue);
    }
    .btn-nav:hover { background: var(--blue-600); transform: translateY(-1px); box-shadow: 0 10px 28px var(--blue-glow); }
    .btn-nav svg { width: 14px; height: 14px; }

    .hamburger {
      display: none; flex-direction: column; gap: 5px;
      background: none; border: none; cursor: pointer; padding: 4px; z-index: 1001;
    }
    .hamburger span {
      width: 22px; height: 2px; border-radius: 2px;
      background: var(--text-dark); transition: var(--transition);
    }
    .navbar:not(.scrolled) .hamburger span { background: var(--white); }

    /* Mobile Menu */
    .mobile-menu {
      position: fixed; top: 0; right: -100%; width: 85%; max-width: 380px;
      height: 100vh; background: var(--white);
      box-shadow: -8px 0 40px rgba(15,23,42,0.14);
      z-index: 998; padding: 90px 28px 36px;
      display: flex; flex-direction: column; justify-content: space-between;
      transition: var(--transition);
    }
    .mobile-menu.active { right: 0; }
    .mobile-nav-links { list-style: none; display: flex; flex-direction: column; gap: 4px; }
    .mobile-nav-link {
      display: block; padding: 12px 16px; border-radius: var(--radius-md);
      font-size: 1.05rem; font-weight: 700; color: var(--text-dark);
      transition: var(--transition);
    }
    .mobile-nav-link:hover { color: var(--blue); background: rgba(0,82,255,0.06); }

    /* =====================================================================
       HERO
       ===================================================================== */
    .hero {
      min-height: 100vh;
      background: var(--bg-dark);
      background-image:
        radial-gradient(ellipse 60% 50% at 100% 0%, rgba(0,82,255,0.15) 0%, transparent 60%),
        radial-gradient(ellipse 40% 40% at 0% 100%, rgba(0,82,255,0.08) 0%, transparent 60%);
      display: flex; align-items: center;
      padding-top: 80px;
      overflow: hidden;
      position: relative;
    }

    /* Dot grid overlay */
    .hero::before {
      content: \'\';
      position: absolute; inset: 0;
      background-image: radial-gradient(circle, rgba(255,255,255,0.06) 1px, transparent 1px);
      background-size: 28px 28px;
      pointer-events: none;
    }

    .hero-grid {
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 64px;
      align-items: center;
      position: relative; z-index: 2;
    }

    /* Hero Left */
    .hero-badge {
      display: inline-flex; align-items: center; gap: 8px;
      padding: 6px 14px;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.12);
      border-radius: 999px;
      color: var(--cyan);
      font-size: 0.72rem; font-weight: 700;
      text-transform: uppercase; letter-spacing: 0.09em;
      margin-bottom: 20px;
    }
    .hero-badge-dot {
      width: 7px; height: 7px; border-radius: 50%;
      background: var(--green-bright);
      box-shadow: 0 0 8px var(--green-bright);
      animation: blink 1.8s ease-in-out infinite;
    }
    @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.4} }

    .hero h1 {
      font-size: clamp(2.8rem, 5.5vw, 4rem);
      color: var(--white);
      font-weight: 800;
      line-height: 1.08;
      letter-spacing: -0.03em;
      margin-bottom: 20px;
    }
    .hero h1 .accent { color: var(--blue); }

    .hero-subtitle {
      font-size: 1.1rem;
      color: var(--text-muted-dark);
      max-width: 520px;
      line-height: 1.7;
      margin-bottom: 36px;
    }

    .hero-ctas { display: flex; align-items: center; gap: 14px; flex-wrap: wrap; margin-bottom: 48px; }

    .btn-primary {
      display: inline-flex; align-items: center; gap: 8px;
      padding: 14px 26px;
      background: var(--blue); color: var(--white);
      border: none; border-radius: var(--radius-md);
      font-size: 0.95rem; font-weight: 700;
      cursor: pointer; transition: var(--transition);
      box-shadow: var(--shadow-blue);
    }
    .btn-primary:hover { background: var(--blue-600); transform: translateY(-2px); box-shadow: 0 12px 32px var(--blue-glow); }

    .btn-secondary {
      display: inline-flex; align-items: center; gap: 8px;
      padding: 13px 26px;
      background: rgba(255,255,255,0.06); color: var(--white);
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: var(--radius-md);
      font-size: 0.95rem; font-weight: 700;
      cursor: pointer; transition: var(--transition);
    }
    .btn-secondary:hover { background: rgba(255,255,255,0.10); border-color: rgba(255,255,255,0.3); transform: translateY(-2px); }

    /* Hero Stats Strip */
    .hero-stats-strip {
      display: flex; align-items: center; gap: 0;
      border-top: 1px solid rgba(255,255,255,0.1);
      padding-top: 32px;
    }
    .hero-stat {
      flex: 1; padding-right: 24px;
    }
    .hero-stat:not(:last-child) {
      border-right: 1px solid rgba(255,255,255,0.1);
      margin-right: 24px;
    }
    .hero-stat-num {
      font-size: 2rem; font-weight: 800; color: var(--white);
      letter-spacing: -0.03em; line-height: 1;
      display: block;
    }
    .hero-stat-label { font-size: 0.82rem; color: var(--text-muted-dark); margin-top: 4px; font-weight: 500; }

    /* Hero Terminal */
    .hero-terminal {
      background: #0a1628;
      border: 1px solid rgba(30,41,59,0.9);
      border-radius: var(--radius-xl);
      padding: 0;
      box-shadow: 0 32px 80px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,255,255,0.04);
      overflow: hidden;
      position: relative;
    }

    .terminal-titlebar {
      display: flex; align-items: center; justify-content: space-between;
      padding: 14px 20px;
      background: rgba(255,255,255,0.03);
      border-bottom: 1px solid rgba(255,255,255,0.07);
    }
    .terminal-dots { display: flex; gap: 6px; }
    .terminal-dot {
      width: 10px; height: 10px; border-radius: 50%;
    }
    .t-red { background: #FF5F57; }
    .t-yellow { background: #FEBC2E; }
    .t-green { background: #28C840; }

    .terminal-node-id {
      font-size: 0.78rem; font-weight: 600; color: var(--text-muted-dark);
      font-family: \'Courier New\', monospace;
    }

    .live-pill {
      display: inline-flex; align-items: center; gap: 6px;
      padding: 4px 10px;
      background: rgba(16,185,129,0.12);
      border: 1px solid rgba(16,185,129,0.3);
      border-radius: 999px;
      font-size: 0.72rem; font-weight: 700;
      color: var(--green-bright);
    }
    .live-dot {
      width: 6px; height: 6px; border-radius: 50%;
      background: var(--green-bright);
      box-shadow: 0 0 6px var(--green-bright);
      animation: blink 1.5s ease-in-out infinite;
    }

    .terminal-body { padding: 24px 20px; }

    /* Circular Power Gauge */
    .gauge-wrap {
      display: flex; flex-direction: column; align-items: center;
      margin-bottom: 20px;
    }
    .gauge-svg-wrap { position: relative; width: 160px; height: 160px; margin: 0 auto 12px; }
    .gauge-label-center {
      position: absolute; inset: 0;
      display: flex; flex-direction: column; align-items: center; justify-content: center;
    }
    .gauge-kw { font-size: 2rem; font-weight: 800; color: var(--white); line-height: 1; }
    .gauge-unit { font-size: 0.72rem; color: var(--text-muted-dark); margin-top: 2px; letter-spacing: 0.04em; }
    .gauge-type-label { font-size: 0.8rem; color: var(--text-muted-dark); font-weight: 600; }

    @keyframes dashAnim {
      from { stroke-dashoffset: 502; }
      to { stroke-dashoffset: 75; }
    }
    .gauge-progress {
      animation: dashAnim 2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    /* Terminal 2x2 Data Grid */
    .terminal-grid {
      display: grid; grid-template-columns: 1fr 1fr; gap: 10px;
    }
    .terminal-cell {
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(255,255,255,0.07);
      border-radius: var(--radius-md);
      padding: 12px 14px;
    }
    .cell-label { font-size: 0.72rem; color: var(--text-muted-dark); font-weight: 500; letter-spacing: 0.04em; display: block; margin-bottom: 4px; }
    .cell-value { font-size: 1rem; font-weight: 800; color: var(--white); display: block; }
    .cell-value.blue { color: var(--cyan); }
    .cell-value.green { color: var(--green-bright); }

    /* =====================================================================
       TRUST MARQUEE
       ===================================================================== */
    .trust-section {
      padding: 48px 0;
      background: var(--white);
      border-top: 1px solid var(--border-light);
      border-bottom: 1px solid var(--border-light);
      overflow: hidden;
    }
    .trust-label {
      text-align: center;
      font-size: 0.75rem; font-weight: 700;
      text-transform: uppercase; letter-spacing: 0.12em;
      color: var(--text-muted); margin-bottom: 28px;
    }
    .logo-marquee {
      display: flex; overflow: hidden;
      mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
      -webkit-mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
    }
    .logo-track {
      display: flex; align-items: center; gap: 48px;
      animation: marquee 22s linear infinite;
      white-space: nowrap;
      flex-shrink: 0;
    }
    @keyframes marquee { 0%{transform:translateX(0)} 100%{transform:translateX(-50%)} }
    .client-chip {
      display: inline-flex; align-items: center; gap: 8px;
      padding: 9px 20px; border-radius: 999px;
      background: var(--bg-light);
      border: 1px solid var(--border-light);
      font-size: 0.88rem; font-weight: 700;
      color: var(--text-dark); opacity: 0.75;
      transition: var(--transition);
    }
    .client-chip:hover { opacity: 1; border-color: var(--blue); color: var(--blue); }

    /* =====================================================================
       SERVICES SECTION
       ===================================================================== */
    .services-section { background: var(--bg-light); }

    .services-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }

    .service-card {
      background: var(--white);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-lg);
      padding: 32px;
      display: flex; flex-direction: column;
      transition: var(--transition);
      position: relative; overflow: hidden;
    }
    .service-card:hover {
      border-color: rgba(0,82,255,0.4);
      box-shadow: var(--shadow-lg), 0 0 0 1px rgba(0,82,255,0.08);
      transform: translateY(-4px);
    }
    .service-card::before {
      content: \'\'; position: absolute; top: 0; left: 0; right: 0; height: 3px;
      background: linear-gradient(90deg, var(--blue), var(--cyan));
      transform: scaleX(0); transform-origin: left;
      transition: var(--transition);
    }
    .service-card:hover::before { transform: scaleX(1); }

    .service-icon-box {
      width: 48px; height: 48px; border-radius: var(--radius-md);
      background: rgba(0,82,255,0.07);
      display: flex; align-items: center; justify-content: center;
      color: var(--blue); margin-bottom: 20px;
      transition: var(--transition);
    }
    .service-card:hover .service-icon-box { background: var(--blue); color: var(--white); }

    .service-card h3 { font-size: 1.15rem; margin-bottom: 10px; }

    .service-card > p { font-size: 0.9rem; margin-bottom: 20px; flex-grow: 1; }

    .service-checklist { list-style: none; display: flex; flex-direction: column; gap: 8px; margin-bottom: 24px; }
    .service-checklist li {
      display: flex; align-items: center; gap: 8px;
      font-size: 0.85rem; font-weight: 600; color: var(--text-muted);
    }
    .check-mark {
      width: 18px; height: 18px; border-radius: 50%;
      background: rgba(16,185,129,0.1);
      display: flex; align-items: center; justify-content: center;
      flex-shrink: 0; color: var(--green);
    }

    .service-link {
      display: inline-flex; align-items: center; gap: 6px;
      font-size: 0.875rem; font-weight: 700;
      color: var(--blue); margin-top: auto;
      transition: var(--transition); cursor: pointer;
    }
    .service-link:hover { gap: 10px; }

    /* =====================================================================
       WHY CHOOSE US
       ===================================================================== */
    .why-section { background: var(--bg-dark); }

    .why-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
    }

    .why-card {
      background: var(--bg-card-dark);
      border: 1px solid var(--border-dark);
      border-radius: var(--radius-lg);
      padding: 28px;
      transition: var(--transition);
    }
    .why-card:hover {
      border-color: rgba(0,82,255,0.5);
      transform: translateY(-4px);
      box-shadow: 0 16px 40px rgba(0,0,0,0.4);
    }

    .why-icon-box {
      width: 44px; height: 44px; border-radius: var(--radius-md);
      background: rgba(0,82,255,0.15);
      display: flex; align-items: center; justify-content: center;
      color: var(--cyan); margin-bottom: 16px;
      transition: var(--transition);
    }
    .why-card:hover .why-icon-box { background: var(--blue); color: var(--white); }

    .why-card h3 { font-size: 1.05rem; color: var(--white); margin-bottom: 8px; }
    .why-card p { font-size: 0.88rem; color: var(--text-muted-dark); line-height: 1.65; }

    /* =====================================================================
       PROCESS TIMELINE
       ===================================================================== */
    .process-section { background: var(--white); }

    .timeline { position: relative; max-width: 860px; margin: 0 auto; }
    .timeline::before {
      content: \'\'; position: absolute;
      top: 0; bottom: 0; left: 50%; width: 1px;
      background: var(--border-light);
      transform: translateX(-50%);
    }

    .timeline-step {
      display: flex; justify-content: flex-end;
      padding-right: 56px; position: relative;
      margin-bottom: 40px; width: 50%;
    }
    .timeline-step:nth-child(even) {
      justify-content: flex-start;
      padding-right: 0; padding-left: 56px;
      margin-left: 50%;
    }

    .step-marker {
      position: absolute; top: 8px; right: -20px;
      width: 40px; height: 40px; border-radius: 50%;
      background: var(--blue);
      border: 3px solid var(--white);
      box-shadow: 0 0 0 3px var(--blue-glow), var(--shadow-sm);
      color: var(--white);
      font-weight: 800; font-size: 0.82rem;
      display: flex; align-items: center; justify-content: center;
      z-index: 2;
    }
    .timeline-step:nth-child(even) .step-marker { right: auto; left: -20px; }

    .step-card {
      background: var(--bg-light);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-lg); padding: 24px;
      width: 100%; transition: var(--transition);
    }
    .step-card:hover { border-color: rgba(0,82,255,0.3); box-shadow: var(--shadow-md); transform: translateY(-2px); }
    .step-num { font-size: 0.72rem; font-weight: 700; color: var(--blue); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 6px; }
    .step-card h3 { font-size: 1.05rem; margin-bottom: 6px; }
    .step-card p { font-size: 0.88rem; }

    /* =====================================================================
       PROJECT SHOWCASE
       ===================================================================== */
    .showcase-section { background: var(--bg-light); }

    .showcase-filters {
      display: flex; justify-content: center; gap: 10px;
      margin-bottom: 44px; flex-wrap: wrap;
    }
    .filter-btn {
      padding: 9px 20px; border-radius: 999px;
      border: 1px solid var(--border-light);
      background: var(--white); color: var(--text-muted);
      font-size: 0.875rem; font-weight: 700;
      cursor: pointer; transition: var(--transition);
    }
    .filter-btn:hover { border-color: var(--blue); color: var(--blue); }
    .filter-btn.active { background: var(--bg-dark); color: var(--white); border-color: var(--bg-dark); }

    .showcase-grid {
      display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px;
    }

    .project-card {
      background: var(--white);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-lg);
      overflow: hidden;
      transition: var(--transition);
    }
    .project-card:hover { border-color: rgba(0,82,255,0.3); box-shadow: var(--shadow-lg); transform: translateY(-4px); }

    .project-banner {
      position: relative; height: 180px;
      background: var(--bg-dark);
      display: flex; align-items: center; justify-content: center;
      overflow: hidden;
    }
    .project-banner::before {
      content: \'\'; position: absolute; inset: 0;
      background-image: radial-gradient(circle, rgba(255,255,255,0.06) 1px, transparent 1px);
      background-size: 20px 20px;
    }
    .project-banner-icon {
      position: relative; z-index: 1;
      width: 56px; height: 56px;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: var(--radius-lg);
      display: flex; align-items: center; justify-content: center;
      color: rgba(255,255,255,0.4);
    }
    .project-location-badge {
      position: absolute; top: 14px; left: 14px; z-index: 2;
      padding: 5px 12px;
      background: rgba(11,25,44,0.75);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 999px;
      font-size: 0.72rem; font-weight: 700; color: var(--white);
    }
    .project-type-tag {
      position: absolute; top: 14px; right: 14px; z-index: 2;
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 0.68rem; font-weight: 700;
    }
    .tag-commercial { background: rgba(0,82,255,0.15); color: var(--cyan); border: 1px solid rgba(0,82,255,0.3); }
    .tag-residential { background: rgba(16,185,129,0.15); color: var(--green-bright); border: 1px solid rgba(16,185,129,0.3); }
    .tag-fleet { background: rgba(251,146,60,0.15); color: #FB923C; border: 1px solid rgba(251,146,60,0.3); }

    .project-info { padding: 24px; }
    .project-info h3 { font-size: 1.05rem; margin-bottom: 10px; }
    .project-meta {
      display: flex; flex-wrap: wrap; gap: 12px;
      margin-bottom: 12px; padding-bottom: 12px;
      border-bottom: 1px solid var(--border-light);
    }
    .meta-tag {
      font-size: 0.78rem; font-weight: 600; color: var(--text-muted);
    }
    .project-info p { font-size: 0.875rem; }

    /* =====================================================================
       INDIA MAP
       ===================================================================== */
    .map-section { background: var(--bg-dark); }

    .map-layout {
      display: grid; grid-template-columns: 1fr 1fr; gap: 56px;
      align-items: center;
    }

    .city-selector-list { display: flex; flex-direction: column; gap: 12px; margin-top: 28px; }
    .city-item {
      display: flex; align-items: center; justify-content: space-between;
      padding: 14px 18px;
      background: rgba(255,255,255,0.03);
      border: 1px solid rgba(255,255,255,0.07);
      border-radius: var(--radius-md);
      cursor: pointer; transition: var(--transition);
    }
    .city-item:hover, .city-item.active {
      background: rgba(0,82,255,0.12);
      border-color: rgba(0,82,255,0.4);
    }
    .city-item-left { display: flex; align-items: center; gap: 12px; }
    .city-dot {
      width: 8px; height: 8px; border-radius: 50%;
      background: var(--blue); flex-shrink: 0;
    }
    .city-item.active .city-dot { background: var(--green-bright); box-shadow: 0 0 8px var(--green-bright); }
    .city-name { font-size: 0.95rem; font-weight: 700; color: var(--white); }
    .city-stat { font-size: 0.82rem; font-weight: 700; color: var(--cyan); }

    .map-container {
      position: relative; width: 100%;
      background: rgba(255,255,255,0.02);
      border: 1px solid rgba(255,255,255,0.07);
      border-radius: var(--radius-xl);
      padding: 20px;
      display: flex; align-items: center; justify-content: center;
      min-height: 460px;
    }

    .india-svg {
      width: 100%; height: 100%; max-height: 420px;
      filter: drop-shadow(0 0 16px rgba(0,82,255,0.15));
    }

    .map-hotspot { cursor: pointer; }
    .map-hotspot circle { transition: var(--transition); }
    .map-hotspot:hover circle:last-of-type { r: 8; }

    .hotspot-pulse {
      animation: hotspot-ping 2.2s cubic-bezier(0, 0, 0.2, 1) infinite;
    }
    @keyframes hotspot-ping { 75%,100%{ transform: scale(2.5); opacity: 0; } }

    /* =====================================================================
       ROI CALCULATOR
       ===================================================================== */
    .calc-section { background: var(--white); }

    .calc-wrapper {
      display: grid; grid-template-columns: 1fr 1fr; gap: 0;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-xl);
      overflow: hidden;
      box-shadow: var(--shadow-lg);
    }

    .calc-controls {
      background: var(--white);
      padding: 40px 36px;
      border-right: 1px solid var(--border-light);
    }

    .form-group { margin-bottom: 28px; }
    .form-label {
      display: flex; justify-content: space-between; align-items: center;
      font-size: 0.88rem; font-weight: 700; color: var(--text-dark);
      margin-bottom: 10px;
    }
    .form-label-val {
      font-size: 0.82rem; font-weight: 700; color: var(--blue);
      padding: 3px 10px; border-radius: 999px;
      background: rgba(0,82,255,0.07);
    }
    .form-select {
      width: 100%; padding: 12px 16px;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      background: var(--bg-light);
      font-family: inherit; font-size: 0.9rem; color: var(--text-dark);
      outline: none; transition: var(--transition); cursor: pointer;
    }
    .form-select:focus { border-color: var(--blue); background: var(--white); box-shadow: 0 0 0 3px var(--blue-glow); }

    .range-slider {
      width: 100%; height: 6px; border-radius: 3px;
      background: var(--border-light);
      accent-color: var(--blue);
      outline: none; cursor: pointer;
    }

    /* Calc Results */
    .calc-results {
      background: var(--bg-dark);
      padding: 40px 36px;
      display: flex; flex-direction: column; justify-content: space-between;
    }
    .calc-results-title { font-size: 1.15rem; font-weight: 800; color: var(--white); margin-bottom: 28px; }
    .result-rows { display: flex; flex-direction: column; gap: 0; flex: 1; }
    .result-row {
      display: flex; justify-content: space-between; align-items: center;
      padding: 16px 0;
      border-bottom: 1px solid rgba(255,255,255,0.07);
    }
    .result-row:first-child { border-top: 1px solid rgba(255,255,255,0.07); }
    .result-lbl { font-size: 0.875rem; color: var(--text-muted-dark); font-weight: 500; }
    .result-val { font-size: 1.25rem; font-weight: 800; color: var(--cyan); }
    .result-val.green { color: var(--green-bright); }

    .btn-quote {
      display: flex; align-items: center; justify-content: center; gap: 8px;
      width: 100%; padding: 14px;
      background: var(--blue); color: var(--white);
      border: none; border-radius: var(--radius-md);
      font-size: 0.95rem; font-weight: 700;
      cursor: pointer; margin-top: 28px;
      transition: var(--transition);
    }
    .btn-quote:hover { background: var(--blue-600); transform: translateY(-2px); box-shadow: var(--shadow-blue); }

    /* =====================================================================
       TESTIMONIALS
       ===================================================================== */
    .testimonials-section { background: var(--bg-light); }

    .testimonials-grid {
      display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px;
    }

    .testimonial-card {
      background: var(--white);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-lg);
      padding: 28px;
      display: flex; flex-direction: column;
      transition: var(--transition);
    }
    .testimonial-card:hover { border-color: rgba(0,82,255,0.25); box-shadow: var(--shadow-md); transform: translateY(-3px); }

    .stars { display: flex; gap: 3px; margin-bottom: 16px; }
    .star { color: #F59E0B; font-size: 1rem; }

    .testimonial-quote {
      font-size: 0.925rem; color: var(--text-dark); line-height: 1.7;
      flex-grow: 1; margin-bottom: 24px;
    }

    .author-wrap {
      display: flex; align-items: center; gap: 12px;
      padding-top: 20px; border-top: 1px solid var(--border-light);
    }
    .author-avatar {
      width: 44px; height: 44px; border-radius: 50%;
      background: var(--bg-dark);
      display: flex; align-items: center; justify-content: center;
      font-size: 0.85rem; font-weight: 800; color: var(--white);
      flex-shrink: 0;
    }
    .author-name { font-size: 0.88rem; font-weight: 700; color: var(--text-dark); margin-bottom: 2px; }
    .author-title { font-size: 0.78rem; color: var(--text-muted); }

    /* =====================================================================
       FAQ
       ===================================================================== */
    .faq-section { background: var(--white); }

    .faq-container {
      max-width: 760px; margin: 0 auto;
      display: flex; flex-direction: column; gap: 12px;
    }

    .faq-item {
      background: var(--white);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-lg);
      overflow: hidden; transition: var(--transition);
    }
    .faq-item.active { border-color: rgba(0,82,255,0.3); box-shadow: var(--shadow-sm); }

    .faq-question {
      padding: 20px 24px;
      display: flex; justify-content: space-between; align-items: center;
      cursor: pointer;
      font-size: 1rem; font-weight: 700; color: var(--text-dark);
    }
    .faq-toggle {
      width: 28px; height: 28px; border-radius: 50%;
      background: var(--bg-light);
      display: flex; align-items: center; justify-content: center;
      flex-shrink: 0; transition: var(--transition); color: var(--text-muted);
    }
    .faq-item.active .faq-toggle { background: var(--blue); color: var(--white); transform: rotate(180deg); }

    .faq-answer {
      max-height: 0; overflow: hidden; padding: 0 24px;
      color: var(--text-muted); font-size: 0.925rem; line-height: 1.7;
      transition: max-height 0.35s ease, padding 0.35s ease;
    }
    .faq-item.active .faq-answer { max-height: 280px; padding-bottom: 20px; }

    /* =====================================================================
       CONTACT
       ===================================================================== */
    .contact-section { background: var(--bg-light); }

    .contact-grid {
      display: grid; grid-template-columns: 1fr 1.1fr; gap: 40px; align-items: start;
    }

    .contact-info-card {
      background: var(--bg-dark);
      border-radius: var(--radius-xl); padding: 40px;
      color: var(--white);
    }
    .contact-info-card h3 { color: var(--white); font-size: 1.5rem; margin-bottom: 8px; }
    .contact-info-card > p { color: var(--text-muted-dark); margin-bottom: 32px; }

    .info-list { display: flex; flex-direction: column; gap: 20px; }
    .info-item { display: flex; align-items: flex-start; gap: 14px; }
    .info-icon-box {
      width: 44px; height: 44px; border-radius: var(--radius-md);
      background: rgba(255,255,255,0.07);
      display: flex; align-items: center; justify-content: center;
      color: var(--cyan); flex-shrink: 0;
    }
    .info-item-label { font-size: 0.78rem; color: var(--text-muted-dark); font-weight: 500; }
    .info-item-value { font-size: 0.925rem; font-weight: 700; color: var(--white); margin-top: 2px; }

    .contact-form-card {
      background: var(--white);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-xl); padding: 40px;
      box-shadow: var(--shadow-md);
    }
    .contact-form-card h3 { font-size: 1.35rem; margin-bottom: 6px; }
    .contact-form-card > p { margin-bottom: 28px; font-size: 0.9rem; }

    .contact-form-group { margin-bottom: 20px; }
    .contact-label {
      display: block; font-size: 0.82rem; font-weight: 700; color: var(--text-dark); margin-bottom: 7px;
    }
    .contact-input, .contact-select, .contact-textarea {
      width: 100%; padding: 11px 14px;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      background: var(--bg-light);
      font-family: inherit; font-size: 0.9rem; color: var(--text-dark);
      outline: none; transition: var(--transition);
    }
    .contact-input:focus, .contact-select:focus, .contact-textarea:focus {
      border-color: var(--blue); background: var(--white);
      box-shadow: 0 0 0 3px var(--blue-glow);
    }
    .contact-textarea { resize: vertical; min-height: 110px; }

    /* =====================================================================
       FOOTER
       ===================================================================== */
    .footer {
      background: var(--bg-darker);
      border-top: 1px solid var(--border-dark);
      padding: 72px 0 28px;
    }

    .footer-grid {
      display: grid; grid-template-columns: 1.6fr repeat(3, 1fr); gap: 40px;
      margin-bottom: 56px;
    }

    .footer-col h4 {
      font-size: 0.88rem; color: var(--white);
      margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.08em;
    }
    .footer-desc { font-size: 0.88rem; color: var(--text-muted-dark); line-height: 1.7; margin-top: 12px; margin-bottom: 20px; }

    .footer-links { list-style: none; display: flex; flex-direction: column; gap: 10px; }
    .footer-links a {
      font-size: 0.88rem; color: var(--text-muted-dark);
      transition: var(--transition);
    }
    .footer-links a:hover { color: var(--white); padding-left: 4px; }

    .footer-bottom {
      padding-top: 24px; border-top: 1px solid var(--border-dark);
      display: flex; justify-content: space-between; align-items: center;
      color: var(--text-muted-dark); font-size: 0.82rem;
    }
    .footer-legal { display: flex; gap: 20px; }
    .footer-legal a { color: var(--text-muted-dark); transition: var(--transition); }
    .footer-legal a:hover { color: var(--white); }

    /* =====================================================================
       BACK TO TOP & MODAL & TOAST
       ===================================================================== */
    .back-to-top {
      position: fixed; bottom: 24px; right: 24px;
      width: 48px; height: 48px; border-radius: 50%;
      background: var(--bg-dark); color: var(--white);
      border: 1px solid rgba(255,255,255,0.15);
      display: flex; align-items: center; justify-content: center;
      cursor: pointer; z-index: 900;
      opacity: 0; visibility: hidden; transform: translateY(16px);
      transition: var(--transition);
      box-shadow: var(--shadow-md);
    }
    .back-to-top.visible { opacity: 1; visibility: visible; transform: translateY(0); }
    .back-to-top:hover { background: var(--blue); }

    .modal-overlay {
      position: fixed; inset: 0;
      background: rgba(8,14,26,0.75); backdrop-filter: blur(8px);
      z-index: 2000; display: flex; align-items: center; justify-content: center;
      opacity: 0; visibility: hidden; transition: var(--transition);
      padding: 20px;
    }
    .modal-overlay.active { opacity: 1; visibility: visible; }

    .modal-card {
      background: var(--white); border-radius: var(--radius-xl);
      max-width: 500px; width: 100%; padding: 40px; position: relative;
      transform: scale(0.94) translateY(16px); transition: var(--transition);
      box-shadow: var(--shadow-lg);
    }
    .modal-overlay.active .modal-card { transform: scale(1) translateY(0); }
    .modal-close {
      position: absolute; top: 16px; right: 16px;
      width: 32px; height: 32px; border-radius: 50%;
      background: var(--bg-light); border: none;
      display: flex; align-items: center; justify-content: center;
      cursor: pointer; font-size: 1rem; color: var(--text-muted);
      transition: var(--transition);
    }
    .modal-close:hover { background: var(--border-light); color: var(--text-dark); }
    .modal-card h3 { font-size: 1.35rem; margin-bottom: 8px; }
    .modal-card > p { font-size: 0.9rem; margin-bottom: 24px; }

    .modal-form-group { margin-bottom: 16px; }
    .modal-label { display: block; font-size: 0.82rem; font-weight: 700; color: var(--text-dark); margin-bottom: 6px; }
    .modal-input {
      width: 100%; padding: 11px 14px;
      border: 1px solid var(--border-light); border-radius: var(--radius-md);
      background: var(--bg-light); font-family: inherit; font-size: 0.9rem;
      outline: none; transition: var(--transition);
    }
    .modal-input:focus { border-color: var(--blue); background: var(--white); box-shadow: 0 0 0 3px var(--blue-glow); }

    .toast {
      position: fixed; bottom: 24px; left: 24px;
      background: var(--bg-dark); color: var(--white);
      padding: 14px 20px; border-radius: var(--radius-lg);
      border: 1px solid var(--cyan);
      display: flex; align-items: center; gap: 10px;
      z-index: 3000;
      transform: translateY(24px); opacity: 0;
      transition: var(--transition);
      max-width: 380px; box-shadow: var(--shadow-lg);
    }
    .toast.show { transform: translateY(0); opacity: 1; }
    .toast-icon { color: var(--cyan); flex-shrink: 0; }
    .toast-msg { font-size: 0.875rem; font-weight: 600; }

    /* =====================================================================
       RESPONSIVE
       ===================================================================== */
    @media (max-width: 1024px) {
      .hero-grid, .map-layout, .calc-wrapper, .contact-grid { grid-template-columns: 1fr; gap: 40px; }
      .calc-wrapper { border-radius: var(--radius-xl); }
      .calc-controls { border-right: none; border-bottom: 1px solid var(--border-light); }
      .hero { min-height: auto; padding: 120px 0 80px; }
      .hero-terminal { max-width: 500px; margin: 0 auto; }
      .footer-grid { grid-template-columns: 1fr 1fr; }
      .services-grid, .why-grid, .showcase-grid, .testimonials-grid { grid-template-columns: repeat(2, 1fr); }
    }

    @media (max-width: 768px) {
      .nav-links, .btn-nav { display: none; }
      .hamburger { display: flex; }
      section { padding: 72px 0; }
      .services-grid, .why-grid, .showcase-grid, .testimonials-grid { grid-template-columns: 1fr; }
      .hero h1 { font-size: 2.2rem; }
      .hero-stats-strip { flex-direction: column; gap: 20px; }
      .hero-stat:not(:last-child) { border-right: none; border-bottom: 1px solid rgba(255,255,255,0.1); padding-right: 0; padding-bottom: 20px; margin-right: 0; margin-bottom: 0; }
      .timeline::before { left: 20px; }
      .timeline-step { width: 100%; padding-right: 0; padding-left: 52px; }
      .timeline-step:nth-child(even) { margin-left: 0; padding-left: 52px; }
      .step-marker { right: auto !important; left: 0 !important; }
      .footer-grid { grid-template-columns: 1fr; }
      .footer-bottom { flex-direction: column; gap: 12px; text-align: center; }
      .footer-legal { flex-wrap: wrap; justify-content: center; }
      .contact-grid { grid-template-columns: 1fr; }
      .terminal-grid { grid-template-columns: 1fr; }
      .gauge-svg-wrap { width: 140px; height: 140px; }
    }
  </style>
</head>
<body>

  <!-- Scroll Progress -->
  <div class="scroll-progress" id="scrollProgress"></div>

  <!-- NAVBAR -->
  <nav class="navbar" id="navbar">
    <div class="navbar-inner">
      <a href="#" class="brand-logo">
        <div class="logo-mark">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
          </svg>
        </div>
        <div class="brand-name-wrap">
          <span class="brand-name">IGP BY SPARKLEHOOD</span>
          <span class="brand-sub">EV Infrastructure Partner</span>
        </div>
      </a>

      <ul class="nav-links">
        <li><a href="#home" class="nav-link">Home</a></li>
        <li><a href="#services" class="nav-link">Services</a></li>
        <li><a href="#why-us" class="nav-link">Why Choose Us</a></li>
        <li><a href="#process" class="nav-link">Process</a></li>
        <li><a href="#showcase" class="nav-link">Projects</a></li>
        <li><a href="#map" class="nav-link">Pan India</a></li>
        <li><a href="#calculator" class="nav-link">Calculator</a></li>
        <li><a href="#faq" class="nav-link">FAQ</a></li>
      </ul>

      <div style="display:flex;align-items:center;gap:12px;">
        <button class="btn-nav" onclick="openModal()">
          Book Free Consultation
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </button>
        <button class="hamburger" id="hamburgerBtn" aria-label="Toggle Menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </nav>

  <!-- MOBILE MENU -->
  <div class="mobile-menu" id="mobileMenu">
    <ul class="mobile-nav-links">
      <li><a href="#home" class="mobile-nav-link">Home</a></li>
      <li><a href="#services" class="mobile-nav-link">Services</a></li>
      <li><a href="#why-us" class="mobile-nav-link">Why Choose Us</a></li>
      <li><a href="#process" class="mobile-nav-link">Process</a></li>
      <li><a href="#showcase" class="mobile-nav-link">Projects</a></li>
      <li><a href="#map" class="mobile-nav-link">Pan India Network</a></li>
      <li><a href="#calculator" class="mobile-nav-link">ROI Calculator</a></li>
      <li><a href="#faq" class="mobile-nav-link">FAQ</a></li>
      <li><a href="#contact" class="mobile-nav-link">Contact Us</a></li>
    </ul>
    <button class="btn-primary" style="width:100%;justify-content:center;" onclick="openModal()">Book Free Consultation</button>
  </div>

  <!-- HERO SECTION -->
  <section class="hero" id="home">
    <div class="container">
      <div class="hero-grid">
        <!-- Left: Content -->
        <div class="hero-content">
          <div class="hero-badge">
            <span class="hero-badge-dot"></span>
            India\'s #1 Turnkey EV Infrastructure Partner
          </div>
          <h1>Powering India\'s EV<br><span class="accent">Future.</span></h1>
          <p class="hero-subtitle">
            Seamless end-to-end EV charging station installation for residential societies, commercial complexes, retail hubs, hotels, and enterprise EV fleets across all 28 states.
          </p>
          <div class="hero-ctas">
            <button class="btn-primary" onclick="openModal()">
              Book Site Survey
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </button>
            <a href="#contact" class="btn-secondary">Talk to Expert</a>
          </div>
          <div class="hero-stats-strip">
            <div class="hero-stat">
              <span class="hero-stat-num counter" data-target="1500">0</span>+
              <p class="hero-stat-label">Stations Commissioned</p>
            </div>
            <div class="hero-stat">
              <span class="hero-stat-num counter" data-target="28">0</span>
              <p class="hero-stat-label">States &amp; UT Footprint</p>
            </div>
            <div class="hero-stat">
              <span class="hero-stat-num counter" data-target="99">0</span>%
              <p class="hero-stat-label">Customer Satisfaction</p>
            </div>
          </div>
        </div>

        <!-- Right: Live Telemetry Terminal -->
        <div class="hero-terminal">
          <div class="terminal-titlebar">
            <div style="display:flex;align-items:center;gap:14px;">
              <div class="terminal-dots">
                <div class="terminal-dot t-red"></div>
                <div class="terminal-dot t-yellow"></div>
                <div class="terminal-dot t-green"></div>
              </div>
              <span class="terminal-node-id">Node ID: IN-DLH-8821</span>
            </div>
            <div class="live-pill">
              <span class="live-dot"></span>
              LIVE ENERGIZED
            </div>
          </div>

          <div class="terminal-body">
            <!-- Power Gauge -->
            <div class="gauge-wrap">
              <div class="gauge-svg-wrap">
                <svg width="160" height="160" viewBox="0 0 160 160" fill="none">
                  <!-- Track -->
                  <circle cx="80" cy="80" r="68" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="10"/>
                  <!-- Blue glow ring -->
                  <circle cx="80" cy="80" r="68" fill="none" stroke="rgba(0,82,255,0.15)" stroke-width="10"/>
                  <!-- Progress arc -->
                  <circle
                    cx="80" cy="80" r="68"
                    fill="none"
                    stroke="url(#gaugeGrad)"
                    stroke-width="10"
                    stroke-linecap="round"
                    stroke-dasharray="427"
                    stroke-dashoffset="64"
                    transform="rotate(-90 80 80)"
                    class="gauge-progress"
                  />
                  <defs>
                    <linearGradient id="gaugeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" stop-color="#0052FF"/>
                      <stop offset="100%" stop-color="#00D4FF"/>
                    </linearGradient>
                  </defs>
                </svg>
                <div class="gauge-label-center">
                  <span class="gauge-kw">240</span>
                  <span class="gauge-unit">kW OUTPUT</span>
                </div>
              </div>
              <span class="gauge-type-label">Ultra-Fast DC Charging</span>
            </div>

            <!-- 2x2 Data Grid -->
            <div class="terminal-grid">
              <div class="terminal-cell">
                <span class="cell-label">Grid Power</span>
                <span class="cell-value">415V / 3-Phase</span>
              </div>
              <div class="terminal-cell">
                <span class="cell-label">OCPP Protocol</span>
                <span class="cell-value blue">v1.6J Compliant</span>
              </div>
              <div class="terminal-cell">
                <span class="cell-label">Safety Certification</span>
                <span class="cell-value green">&#x2713; Discom Certified</span>
              </div>
              <div class="terminal-cell">
                <span class="cell-label">Uptime SLA</span>
                <span class="cell-value">99.9% Live</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- TRUST MARQUEE -->
  <section class="trust-section">
    <div class="container">
      <p class="trust-label">Trusted by Leading Enterprises, Builders &amp; RWAs Across India</p>
      <div class="logo-marquee">
        <div class="logo-track">
          <div class="client-chip">DLF Cybercity</div>
          <div class="client-chip">Oberoi Realty</div>
          <div class="client-chip">Marriott Hotels</div>
          <div class="client-chip">Apollo Hospitals</div>
          <div class="client-chip">BluSmart Fleets</div>
          <div class="client-chip">Prestige Group</div>
          <div class="client-chip">Embassy TechVillage</div>
          <div class="client-chip">Tata Power Partners</div>
          <div class="client-chip">Amazon Logistics</div>
          <div class="client-chip">DLF Cybercity</div>
          <div class="client-chip">Oberoi Realty</div>
          <div class="client-chip">Marriott Hotels</div>
          <div class="client-chip">Apollo Hospitals</div>
          <div class="client-chip">BluSmart Fleets</div>
          <div class="client-chip">Prestige Group</div>
          <div class="client-chip">Embassy TechVillage</div>
          <div class="client-chip">Tata Power Partners</div>
          <div class="client-chip">Amazon Logistics</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SERVICES -->
  <section class="services-section" id="services">
    <div class="container">
      <div class="section-header">
        <span class="badge-pill badge-blue">Comprehensive Solutions</span>
        <h2>Turnkey EV Infrastructure Services</h2>
        <p>From site feasibility audits to high-power grid transformer upgrades and 24x7 IoT management.</p>
      </div>
      <div class="services-grid">
        <!-- Service 1 -->
        <div class="service-card">
          <div class="service-icon-box">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
          </div>
          <h3>Residential Installation</h3>
          <p>Smart AC wallbox chargers for single-family homes, luxury villas, and private parking slots with smart app metering.</p>
          <ul class="service-checklist">
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> Single/Three phase load enhancement</li>
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> Auto-off &amp; surge protection</li>
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> Smartphone app integration</li>
          </ul>
          <a class="service-link" onclick="openModal(\'Residential\')">Inquire Installation <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
        </div>
        <!-- Service 2 -->
        <div class="service-card">
          <div class="service-icon-box">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"/><line x1="9" y1="6" x2="9" y2="6.01"/><line x1="15" y1="6" x2="15" y2="6.01"/><line x1="9" y1="10" x2="9" y2="10.01"/><line x1="15" y1="10" x2="15" y2="10.01"/><line x1="9" y1="14" x2="9" y2="14.01"/><line x1="15" y1="14" x2="15" y2="14.01"/><line x1="9" y1="18" x2="15" y2="18"/></svg>
          </div>
          <h3>Commercial Charging</h3>
          <p>Monetized EV charging stations for shopping malls, office parks, commercial complexes, and hospitality chains.</p>
          <ul class="service-checklist">
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> RFID &amp; UPI Payment Gateways</li>
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> Revenue sharing models</li>
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> Dual-gun fast charging hubs</li>
          </ul>
          <a class="service-link" onclick="openModal(\'Commercial\')">Explore Business Hubs <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
        </div>
        <!-- Service 3 -->
        <div class="service-card">
          <div class="service-icon-box">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <h3>Apartment &amp; Community</h3>
          <p>RWA-compliant shared charging hubs for high-rise gated societies with individual resident billing accounts.</p>
          <ul class="service-checklist">
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> Zero load-penalty smart distribution</li>
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> Automatic society billing sync</li>
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> NOC assistance from Discom</li>
          </ul>
          <a class="service-link" onclick="openModal(\'Apartment\')">Get RWA Proposal <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
        </div>
        <!-- Service 4 -->
        <div class="service-card">
          <div class="service-icon-box">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
          </div>
          <h3>Fleet Charging Hubs</h3>
          <p>High-throughput DC fast-charging logistics depots for electric taxis, delivery vans, and heavy e-buses.</p>
          <ul class="service-checklist">
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> 60kW to 360kW Ultra-DC Guns</li>
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> 99.9% uptime SLA guarantee</li>
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> Fleet telematics integration</li>
          </ul>
          <a class="service-link" onclick="openModal(\'Fleet\')">Setup Fleet Depot <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
        </div>
        <!-- Service 5 -->
        <div class="service-card">
          <div class="service-icon-box">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
          </div>
          <h3>Highway Fast Corridors</h3>
          <p>Ultra-fast highway charging plazas with transformer yards, food-court amenities, and solar canopies.</p>
          <ul class="service-checklist">
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> Dynamic load balancing</li>
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> All EV brand compatibility</li>
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> Weatherproof IP65 hardware</li>
          </ul>
          <a class="service-link" onclick="openModal(\'Highway\')">View Highway Models <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
        </div>
        <!-- Service 6 -->
        <div class="service-card">
          <div class="service-icon-box">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <h3>Solar &amp; Grid Integration</h3>
          <p>100% green EV charging powered by rooftop solar panels, battery storage (BESS), and smart grid power.</p>
          <ul class="service-checklist">
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> Zero carbon emission charging</li>
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> Battery energy storage sync</li>
            <li><span class="check-mark"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span> Grid net-metering setup</li>
          </ul>
          <a class="service-link" onclick="openModal(\'Solar\')">Explore Solar-EV <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
        </div>
      </div>
    </div>
  </section>

  <!-- WHY CHOOSE US -->
  <section class="why-section" id="why-us">
    <div class="container">
      <div class="section-header">
        <span class="badge-pill badge-cyan">Unmatched Excellence</span>
        <h2 style="color:var(--white);">Why Industry Leaders Choose IGP</h2>
        <p style="color:var(--text-muted-dark);">Precision engineering, statutory compliance, and bulletproof infrastructure reliability.</p>
      </div>
      <div class="why-grid">
        <div class="why-card">
          <div class="why-icon-box">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
          </div>
          <h3>Certified Engineers</h3>
          <p>CEA &amp; Discom-licensed electrical engineers trained in high-voltage transformer management and safety protocols.</p>
        </div>
        <div class="why-card">
          <div class="why-icon-box">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
          </div>
          <h3>Pan India Footprint</h3>
          <p>Active deployment presence across 28 states with local service centers for rapid response and maintenance support.</p>
        </div>
        <div class="why-card">
          <div class="why-icon-box">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          </div>
          <h3>Rapid 72-Hour Turnaround</h3>
          <p>From initial site inspection and electrical load approval to complete hardware setup and live testing in 3 days.</p>
        </div>
        <div class="why-card">
          <div class="why-icon-box">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <h3>5-Year Comprehensive Warranty</h3>
          <p>Full hardware protection against voltage fluctuations, weather wear, component fatigue, and lightning surges.</p>
        </div>
        <div class="why-card">
          <div class="why-icon-box">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
          </div>
          <h3>24x7 IoT Command Center</h3>
          <p>Remote health diagnostic monitoring, auto-fault correction, and automated uptime reporting across all chargers.</p>
        </div>
        <div class="why-card">
          <div class="why-icon-box">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
          </div>
          <h3>100% Statutory Compliance</h3>
          <p>End-to-end management of State Electricity Board permissions, NOC approvals, and grid safety audits.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- PROCESS TIMELINE -->
  <section class="process-section" id="process">
    <div class="container">
      <div class="section-header">
        <span class="badge-pill badge-blue">Seamless Execution</span>
        <h2>Our 6-Step Turnkey Process</h2>
        <p>A standardized engineering pipeline engineered for zero downtime and maximum grid safety.</p>
      </div>
      <div class="timeline">
        <div class="timeline-step">
          <div class="step-marker">1</div>
          <div class="step-card">
            <div class="step-num">Step 01</div>
            <h3>Free Technical Consultation</h3>
            <p>Our EV infrastructure expert reviews your location, vehicle load requirements, and power availability.</p>
          </div>
        </div>
        <div class="timeline-step">
          <div class="step-marker">2</div>
          <div class="step-card">
            <div class="step-num">Step 02</div>
            <h3>Precision Site Audit &amp; Survey</h3>
            <p>Electrical engineers visit the property to audit transformer capacity, cable route distance, and safety earthing.</p>
          </div>
        </div>
        <div class="timeline-step">
          <div class="step-marker">3</div>
          <div class="step-card">
            <div class="step-num">Step 03</div>
            <h3>Engineering &amp; Discom Approval</h3>
            <p>We draft CAD single-line diagrams (SLD) and secure necessary load extension permissions from local electricity boards.</p>
          </div>
        </div>
        <div class="timeline-step">
          <div class="step-marker">4</div>
          <div class="step-card">
            <div class="step-num">Step 04</div>
            <h3>Precision Hardware Installation</h3>
            <p>Heavy-duty armored cabling, IS-compliant RCCB protection panels, and IP65 EV chargers mounted cleanly.</p>
          </div>
        </div>
        <div class="timeline-step">
          <div class="step-marker">5</div>
          <div class="step-card">
            <div class="step-num">Step 05</div>
            <h3>Safety Testing &amp; Commissioning</h3>
            <p>Full-load thermal imaging, insulation resistance check, and live vehicle charging protocol verification.</p>
          </div>
        </div>
        <div class="timeline-step">
          <div class="step-marker">6</div>
          <div class="step-card">
            <div class="step-num">Step 06</div>
            <h3>24x7 Operations &amp; Managed Care</h3>
            <p>Integration with CMS cloud dashboard, automated billing setup, and SLA-backed maintenance coverage.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- PROJECT SHOWCASE -->
  <section class="showcase-section" id="showcase">
    <div class="container">
      <div class="section-header">
        <span class="badge-pill badge-blue">Proven Impact</span>
        <h2>Flagship Project Showcase</h2>
        <p>Explore recent turnkey installations across India\'s leading commercial hubs and residential societies.</p>
      </div>
      <div class="showcase-filters">
        <button class="filter-btn active" onclick="filterShowcase(\'all\', this)">All Projects</button>
        <button class="filter-btn" onclick="filterShowcase(\'commercial\', this)">Commercial</button>
        <button class="filter-btn" onclick="filterShowcase(\'residential\', this)">Residential RWAs</button>
        <button class="filter-btn" onclick="filterShowcase(\'fleet\', this)">Fleet Depots</button>
      </div>
      <div class="showcase-grid">
        <!-- Project 1 -->
        <div class="project-card" data-category="commercial">
          <div class="project-banner">
            <span class="project-location-badge">Gurugram, Haryana</span>
            <span class="project-type-tag tag-commercial">Commercial</span>
            <div class="project-banner-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="9" y1="6" x2="9" y2="6.01"/><line x1="15" y1="6" x2="15" y2="6.01"/></svg>
            </div>
          </div>
          <div class="project-info">
            <h3>DLF Cybercity Fast Hub</h3>
            <div class="project-meta">
              <span class="meta-tag">&#9200; 48 Hrs Setup</span>
              <span class="meta-tag">&#9889; 120kW DC + 22kW AC</span>
            </div>
            <p>12-Gun ultra-fast charging hub deployed for corporate executives and visiting EV drivers with automated app billing.</p>
          </div>
        </div>
        <!-- Project 2 -->
        <div class="project-card" data-category="residential">
          <div class="project-banner">
            <span class="project-location-badge">Bengaluru, Karnataka</span>
            <span class="project-type-tag tag-residential">Residential</span>
            <div class="project-banner-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
            </div>
          </div>
          <div class="project-info">
            <h3>Prestige Golfshire Residency</h3>
            <div class="project-meta">
              <span class="meta-tag">&#9200; 72 Hrs Setup</span>
              <span class="meta-tag">&#9889; 32 x 7.4kW Smart Guns</span>
            </div>
            <p>Shared community EV charging grid for 400+ luxury apartment residents with zero main transformer overloading.</p>
          </div>
        </div>
        <!-- Project 3 -->
        <div class="project-card" data-category="fleet">
          <div class="project-banner">
            <span class="project-location-badge">Mumbai, Maharashtra</span>
            <span class="project-type-tag tag-fleet">Fleet Depot</span>
            <div class="project-banner-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
            </div>
          </div>
          <div class="project-info">
            <h3>BluSmart Cab Depot</h3>
            <div class="project-meta">
              <span class="meta-tag">&#9200; 5 Days Turnkey</span>
              <span class="meta-tag">&#9889; 240kW Ultra Fast DC</span>
            </div>
            <p>High-throughput fleet turnaround station servicing 250+ commercial electric cabs daily with 99.9% uptime SLA.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- PAN INDIA MAP -->
  <section class="map-section" id="map">
    <div class="container">
      <div class="map-layout">
        <div>
          <span class="badge-pill badge-cyan">Nationwide Presence</span>
          <h2 style="color:var(--white);margin:12px 0 14px;">Pan-India Installation &amp; Service Network</h2>
          <p style="color:var(--text-muted-dark);margin-bottom:8px;">
            With operational hubs across 28 states and 8 union territories, IGP guarantees rapid technician deployment and seamless supply chain support anywhere in India.
          </p>
          <div class="city-selector-list">
            <div class="city-item active" onclick="selectCity(\'Delhi NCR\', \'450+ Installations\', \'24x7 Regional Command Center\')">
              <div class="city-item-left">
                <div class="city-dot"></div>
                <span class="city-name">Delhi NCR</span>
              </div>
              <span class="city-stat">450+ Stations</span>
            </div>
            <div class="city-item" onclick="selectCity(\'Mumbai\', \'380+ Installations\', \'Western Fleet Operations Hub\')">
              <div class="city-item-left">
                <div class="city-dot"></div>
                <span class="city-name">Mumbai</span>
              </div>
              <span class="city-stat">380+ Stations</span>
            </div>
            <div class="city-item" onclick="selectCity(\'Bengaluru\', \'410+ Installations\', \'Tech Park Grid Hub\')">
              <div class="city-item-left">
                <div class="city-dot"></div>
                <span class="city-name">Bengaluru</span>
              </div>
              <span class="city-stat">410+ Stations</span>
            </div>
            <div class="city-item" onclick="selectCity(\'Hyderabad\', \'260+ Installations\', \'High-Power DC Plaza\')">
              <div class="city-item-left">
                <div class="city-dot"></div>
                <span class="city-name">Hyderabad</span>
              </div>
              <span class="city-stat">260+ Stations</span>
            </div>
          </div>
        </div>

        <!-- SVG Map -->
        <div class="map-container">
          ''' + india_svg + '''
        </div>
      </div>
    </div>
  </section>

  <!-- ROI CALCULATOR -->
  <section class="calc-section" id="calculator">
    <div class="container">
      <div class="section-header">
        <span class="badge-pill badge-blue">Smart Estimation</span>
        <h2>EV Charger Setup &amp; ROI Calculator</h2>
        <p>Estimate equipment capex, electrical load requirements, and monthly financial savings in real-time.</p>
      </div>
      <div class="calc-wrapper">
        <!-- Controls -->
        <div class="calc-controls">
          <div class="form-group">
            <label class="form-label">Property Category</label>
            <select class="form-select" id="propertyType" onchange="calculateROI()">
              <option value="commercial">Commercial Mall / Office Park</option>
              <option value="residential">Residential Society (RWA)</option>
              <option value="fleet">Fleet Depot / Logistics Hub</option>
              <option value="hotel">Hotel / Resort</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">
              Number of Charging Guns
              <span class="form-label-val" id="gunCountVal">4 Guns</span>
            </label>
            <input type="range" class="range-slider" id="gunCount" min="1" max="20" value="4" oninput="calculateROI()">
          </div>
          <div class="form-group">
            <label class="form-label">Charger Capacity Type</label>
            <select class="form-select" id="chargerType" onchange="calculateROI()">
              <option value="3.3">3.3 kW AC Slow</option>
              <option value="7">7.4 kW AC Smart</option>
              <option value="22">22 kW AC Fast</option>
              <option value="60">60 kW Dual DC Fast Charger</option>
              <option value="120">120 kW Ultra Fast DC</option>
              <option value="240">240 kW Super Fast DC</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">
              Average Daily Utilization
              <span class="form-label-val" id="hoursVal">6 Hours / Day</span>
            </label>
            <input type="range" class="range-slider" id="dailyHours" min="1" max="24" value="6" oninput="calculateROI()">
          </div>
        </div>

        <!-- Results -->
        <div class="calc-results">
          <div>
            <p class="calc-results-title">Financial &amp; Grid Summary</p>
            <div class="result-rows">
              <div class="result-row">
                <span class="result-lbl">Est. Installation Capex</span>
                <span class="result-val" id="resCapex">&#8377; 8.80 Lakhs</span>
              </div>
              <div class="result-row">
                <span class="result-lbl">Power Load Required</span>
                <span class="result-val" id="resLoad">264 kVA</span>
              </div>
              <div class="result-row">
                <span class="result-lbl">Monthly Net Revenue / Savings</span>
                <span class="result-val green" id="resRevenue">&#8377; 1.51 Lakhs</span>
              </div>
              <div class="result-row">
                <span class="result-lbl">Est. Payback Period</span>
                <span class="result-val" id="resROI">5.8 Months</span>
              </div>
            </div>
          </div>
          <button class="btn-quote" onclick="openModal()">
            Get Detailed Official Quote
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- TESTIMONIALS -->
  <section class="testimonials-section" id="testimonials">
    <div class="container">
      <div class="section-header">
        <span class="badge-pill badge-green">Verified Customer Stories</span>
        <h2>What Our Partners Say</h2>
        <p>Read real experiences from property managers, builders, and fleet operators.</p>
      </div>
      <div class="testimonials-grid">
        <div class="testimonial-card">
          <div class="stars">
            <span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span>
          </div>
          <p class="testimonial-quote">"IGP executed our 16-charger commercial installation at DLF Cybercity in record time. Their Discom load permission process was completely stress-free."</p>
          <div class="author-wrap">
            <div class="author-avatar">RK</div>
            <div>
              <div class="author-name">Rajesh Kapoor</div>
              <div class="author-title">VP Facilities, Commercial Real Estate</div>
            </div>
          </div>
        </div>
        <div class="testimonial-card">
          <div class="stars">
            <span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span>
          </div>
          <p class="testimonial-quote">"Our gated society RWA was worried about transformer load balancing. IGP installed smart chargers with individual resident billing accounts. Exceptional work!"</p>
          <div class="author-wrap">
            <div class="author-avatar">AM</div>
            <div>
              <div class="author-name">Ananya Mehta</div>
              <div class="author-title">RWA President, Prestige Residency</div>
            </div>
          </div>
        </div>
        <div class="testimonial-card">
          <div class="stars">
            <span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span>
          </div>
          <p class="testimonial-quote">"Operating 100+ electric cabs requires 99.9% charger uptime. IGP\'s 24x7 IoT command center resolves minor faults remotely before we even notice."</p>
          <div class="author-wrap">
            <div class="author-avatar">VS</div>
            <div>
              <div class="author-name">Vikram Sharma</div>
              <div class="author-title">Director Fleet Operations, UrbanMobility</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="faq-section" id="faq">
    <div class="container">
      <div class="section-header">
        <span class="badge-pill badge-blue">Common Questions</span>
        <h2>Frequently Asked Questions</h2>
        <p>Everything you need to know about EV charging station installation in India.</p>
      </div>
      <div class="faq-container">
        <div class="faq-item active">
          <div class="faq-question" onclick="toggleFaq(this)">
            What is the average cost of EV charging station installation?
            <span class="faq-toggle"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
          </div>
          <div class="faq-answer">
            Costs vary based on charger type and site complexity. A 7.4 kW AC Smart Charger starts at ₹45,000–₹75,000 per gun. A 60 kW DC Fast Charger ranges ₹2–4 Lakhs. A 120 kW Ultra Fast DC can cost ₹4–7 Lakhs. IGP provides all-inclusive turnkey quotes covering hardware, civil work, electrical upgrades, and Discom approvals.
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-question" onclick="toggleFaq(this)">
            Does IGP handle Discom load extension and NOC approvals?
            <span class="faq-toggle"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
          </div>
          <div class="faq-answer">
            Yes. IGP provides complete end-to-end Discom load extension management including SLD preparation, NOC filing, inspection scheduling, and meter upgrade coordination. Our in-house compliance team has managed 500+ Discom approvals across 28 states.
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-question" onclick="toggleFaq(this)">
            How long does a typical EV charging hub installation take?
            <span class="faq-toggle"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
          </div>
          <div class="faq-answer">
            Small residential setups (1–4 guns) can be completed in 24–48 hours from site visit. Commercial hubs with Discom approval requirements take 7–14 working days. Large fleet depots with transformer upgrades may require 3–6 weeks including grid synchronization.
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-question" onclick="toggleFaq(this)">
            Can IGP handle transformer and high-voltage grid upgrades?
            <span class="faq-toggle"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
          </div>
          <div class="faq-answer">
            Absolutely. IGP has a dedicated High Voltage division for transformer augmentation (100 kVA to 1 MVA), HT metering upgrades, and dedicated EV feeder connections. Our CEA-licensed HV engineers manage the complete grid enhancement scope.
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-question" onclick="toggleFaq(this)">
            What warranty and AMC support does IGP provide?
            <span class="faq-toggle"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
          </div>
          <div class="faq-answer">
            IGP provides a 5-year comprehensive hardware warranty against component failure, voltage surge damage, and weather wear. Our 24x7 IoT monitoring auto-detects faults. Annual Maintenance Contracts (AMC) include preventive servicing, remote diagnostics, and guaranteed 4-hour on-site response.
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-question" onclick="toggleFaq(this)">
            Which EV brands and connector standards does IGP support?
            <span class="faq-toggle"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></span>
          </div>
          <div class="faq-answer">
            IGP installs chargers compatible with all major standards: Type 2 AC (for Tata, MG, Hyundai, BMW, Audi), CCS2 DC (for Tata, Mahindra, BYD), CHAdeMO (for Nissan Leaf, Mitsubishi), and GB/T for Chinese OEMs. All DC chargers support OCPP 1.6J / 2.0 for smart grid management.
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CONTACT -->
  <section class="contact-section" id="contact">
    <div class="container">
      <div class="section-header">
        <span class="badge-pill badge-blue">Get In Touch</span>
        <h2>Request Your Free Site Survey</h2>
        <p>Our certified EV electrical engineer will call you within 15 minutes to confirm inspection timing.</p>
      </div>
      <div class="contact-grid">
        <div class="contact-info-card">
          <h3>Contact IGP Directly</h3>
          <p>Speak with our infrastructure specialists for site-specific technical advisory.</p>
          <div class="info-list">
            <div class="info-item">
              <div class="info-icon-box">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 14a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 3.26h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 10a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
              </div>
              <div>
                <div class="info-item-label">Call / WhatsApp</div>
                <div class="info-item-value">+91 99999 88888</div>
              </div>
            </div>
            <div class="info-item">
              <div class="info-icon-box">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
              </div>
              <div>
                <div class="info-item-label">Email Us</div>
                <div class="info-item-value">info@igpsparklehood.com</div>
              </div>
            </div>
            <div class="info-item">
              <div class="info-icon-box">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
              </div>
              <div>
                <div class="info-item-label">Headquarters</div>
                <div class="info-item-value">New Delhi, India (Pan India Operations)</div>
              </div>
            </div>
            <div class="info-item">
              <div class="info-icon-box">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
              </div>
              <div>
                <div class="info-item-label">Response Time</div>
                <div class="info-item-value">15-Minute Call Back Guarantee</div>
              </div>
            </div>
          </div>
        </div>
        <div class="contact-form-card">
          <h3>Book Free Site Survey</h3>
          <p>Fill this form and our engineer will contact you within 15 minutes.</p>
          <form onsubmit="handleContactSubmit(event)">
            <div class="contact-form-group">
              <label class="contact-label">Full Name</label>
              <input type="text" class="contact-input" placeholder="e.g. Vikram Sharma" required>
            </div>
            <div class="contact-form-group">
              <label class="contact-label">Phone Number</label>
              <input type="tel" class="contact-input" placeholder="+91 98765 43210" required>
            </div>
            <div class="contact-form-group">
              <label class="contact-label">Property Type</label>
              <select class="contact-select">
                <option>Residential Home / Villa</option>
                <option>Gated Apartment Society (RWA)</option>
                <option>Commercial Office / Mall</option>
                <option>Fleet / Logistics Depot</option>
                <option>Hotel / Resort / Hospital</option>
              </select>
            </div>
            <div class="contact-form-group">
              <label class="contact-label">Preferred Survey Date</label>
              <input type="date" class="contact-input" required>
            </div>
            <div class="contact-form-group">
              <label class="contact-label">Additional Details</label>
              <textarea class="contact-textarea" placeholder="Tell us about your EV charging requirements, number of vehicles, site location..."></textarea>
            </div>
            <button type="submit" class="btn-primary" style="width:100%;justify-content:center;margin-top:8px;">
              Confirm Booking &rarr;
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <a href="#" class="brand-logo" style="margin-bottom:0;">
            <div class="logo-mark">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
            </div>
            <div class="brand-name-wrap">
              <span class="brand-name" style="color:var(--white);">IGP BY SPARKLEHOOD</span>
              <span class="brand-sub">EV Infrastructure Partner</span>
            </div>
          </a>
          <p class="footer-desc">
            India\'s premier turnkey EV charging station installation company. Discom approved, CEA certified, and powered by 24x7 smart IoT management.
          </p>
        </div>
        <div class="footer-col">
          <h4>Quick Links</h4>
          <ul class="footer-links">
            <li><a href="#home">Home</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#why-us">Why Choose Us</a></li>
            <li><a href="#process">Process Pipeline</a></li>
            <li><a href="#showcase">Project Portfolio</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Solutions</h4>
          <ul class="footer-links">
            <li><a href="#services">Residential EV Charging</a></li>
            <li><a href="#services">Apartment &amp; RWA Grids</a></li>
            <li><a href="#services">Commercial Mall Plazas</a></li>
            <li><a href="#services">High-Power Fleet Depots</a></li>
            <li><a href="#services">Solar &amp; Battery Sync</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Government &amp; Safety</h4>
          <ul class="footer-links">
            <li><a href="#">Ministry of Power Norms</a></li>
            <li><a href="#">CEA Safety Guidelines</a></li>
            <li><a href="#">Discom Load Approvals</a></li>
            <li><a href="#">State EV Subsidies</a></li>
            <li><a href="#">ISO 9001:2015 Certified</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; 2026 IGP by Sparklehood. All rights reserved. Built with precision for India\'s EV Transition.</span>
        <div class="footer-legal">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Service</a>
          <a href="#">Site Map</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- BACK TO TOP -->
  <button class="back-to-top" id="backToTopBtn" onclick="scrollToTop()" aria-label="Back to Top">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="18 15 12 9 6 15"/></svg>
  </button>

  <!-- MODAL -->
  <div class="modal-overlay" id="surveyModal">
    <div class="modal-card">
      <button class="modal-close" onclick="closeModal()">&times;</button>
      <h3 id="modalTitle">Book Free Site Survey</h3>
      <p>Our certified EV electrical engineer will call you in 15 minutes to confirm site inspection timing.</p>
      <form onsubmit="handleModalSubmit(event)">
        <div class="modal-form-group">
          <label class="modal-label">Full Name</label>
          <input type="text" class="modal-input" placeholder="e.g. Vikram Sharma" required>
        </div>
        <div class="modal-form-group">
          <label class="modal-label">Phone Number</label>
          <input type="tel" class="modal-input" placeholder="+91 98765 43210" required>
        </div>
        <div class="modal-form-group">
          <label class="modal-label">Preferred Survey Date</label>
          <input type="date" class="modal-input" required>
        </div>
        <button type="submit" class="btn-primary" style="width:100%;justify-content:center;margin-top:8px;">Confirm Booking</button>
      </form>
    </div>
  </div>

  <!-- TOAST -->
  <div class="toast" id="toast">
    <svg class="toast-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
    <span class="toast-msg" id="toastMsg">Request Submitted Successfully!</span>
  </div>

  <script>
    // Navbar scroll
    const navbar = document.getElementById(\'navbar\');
    const scrollProgress = document.getElementById(\'scrollProgress\');
    const backToTopBtn = document.getElementById(\'backToTopBtn\');

    window.addEventListener(\'scroll\', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      scrollProgress.style.width = ((scrollTop / docHeight) * 100) + \'%\';
      navbar.classList.toggle(\'scrolled\', scrollTop > 60);
      backToTopBtn.classList.toggle(\'visible\', scrollTop > 400);
    });

    // Mobile menu
    const hamburgerBtn = document.getElementById(\'hamburgerBtn\');
    const mobileMenu = document.getElementById(\'mobileMenu\');
    hamburgerBtn.addEventListener(\'click\', () => mobileMenu.classList.toggle(\'active\'));
    document.querySelectorAll(\'.mobile-nav-link\').forEach(link => {
      link.addEventListener(\'click\', () => mobileMenu.classList.remove(\'active\'));
    });

    // Scroll to top
    function scrollToTop() { window.scrollTo({ top: 0, behavior: \'smooth\' }); }

    // Modal
    function openModal(serviceName) {
      const modal = document.getElementById(\'surveyModal\');
      const modalTitle = document.getElementById(\'modalTitle\');
      modalTitle.textContent = serviceName ? `Inquire: ${serviceName} Installation` : \'Book Free Site Survey\';
      modal.classList.add(\'active\');
    }
    function closeModal() { document.getElementById(\'surveyModal\').classList.remove(\'active\'); }
    document.getElementById(\'surveyModal\').addEventListener(\'click\', (e) => {
      if (e.target === e.currentTarget) closeModal();
    });

    // Toast
    function showToast(msg) {
      const toast = document.getElementById(\'toast\');
      document.getElementById(\'toastMsg\').textContent = msg;
      toast.classList.add(\'show\');
      setTimeout(() => toast.classList.remove(\'show\'), 4000);
    }

    // Form handlers
    function handleContactSubmit(e) {
      e.preventDefault();
      showToast(\'Thank you! Your Site Survey request has been registered. Our engineer will call you in 15 mins.\');
      e.target.reset();
    }
    function handleModalSubmit(e) {
      e.preventDefault();
      closeModal();
      showToast(\'Booking Confirmed! You will receive an SMS with technician details.\');
      e.target.reset();
    }

    // FAQ toggle
    function toggleFaq(element) {
      const faqItem = element.parentElement;
      const isActive = faqItem.classList.contains(\'active\');
      document.querySelectorAll(\'.faq-item\').forEach(item => item.classList.remove(\'active\'));
      if (!isActive) faqItem.classList.add(\'active\');
    }

    // Showcase filter
    function filterShowcase(category, btn) {
      document.querySelectorAll(\'.filter-btn\').forEach(b => b.classList.remove(\'active\'));
      btn.classList.add(\'active\');
      document.querySelectorAll(\'.project-card\').forEach(card => {
        card.style.display = (category === \'all\' || card.dataset.category === category) ? \'block\' : \'none\';
      });
    }

    // City selection
    function selectCity(name, stats, info) {
      document.querySelectorAll(\'.city-item\').forEach(item => item.classList.remove(\'active\'));
      event.currentTarget.classList.add(\'active\');
      showToast(`${name} — ${stats} | ${info}`);
    }

    // ROI Calculator
    function calculateROI() {
      const guns = parseInt(document.getElementById(\'gunCount\').value);
      const capacity = parseFloat(document.getElementById(\'chargerType\').value);
      const hours = parseInt(document.getElementById(\'dailyHours\').value);

      document.getElementById(\'gunCountVal\').textContent = `${guns} Gun${guns > 1 ? \'s\' : \'\'}`;
      document.getElementById(\'hoursVal\').textContent = `${hours} Hour${hours > 1 ? \'s\' : \'\'} / Day`;

      // Capex per gun based on capacity
      let costPerGun;
      if (capacity <= 3.3) costPerGun = 0.45;
      else if (capacity <= 7) costPerGun = 0.7;
      else if (capacity <= 22) costPerGun = 1.1;
      else if (capacity <= 60) costPerGun = 2.2;
      else if (capacity <= 120) costPerGun = 4.5;
      else costPerGun = 8.5;

      const totalCapex = (guns * costPerGun).toFixed(2);
      const totalLoad = Math.round(guns * capacity * 1.1);

      // Monthly revenue/savings in Lakhs
      const monthlyKwh = guns * capacity * hours * 30;
      const marginPerKwh = 3.5;
      const monthlyRevenue = ((monthlyKwh * marginPerKwh) / 100000).toFixed(2);
      const roiMonths = monthlyRevenue > 0 ? (parseFloat(totalCapex) / parseFloat(monthlyRevenue)).toFixed(1) : \'N/A\';

      document.getElementById(\'resCapex\').textContent = `\\u20B9 ${totalCapex} Lakhs`;
      document.getElementById(\'resLoad\').textContent = `${totalLoad} kVA`;
      document.getElementById(\'resRevenue\').textContent = `\\u20B9 ${monthlyRevenue} Lakhs`;
      document.getElementById(\'resROI\').textContent = `${roiMonths} Months`;
    }

    // Counter animation
    const counters = document.querySelectorAll(\'.counter\');
    let animated = false;
    const heroSection = document.getElementById(\'home\');

    window.addEventListener(\'scroll\', () => {
      if (!animated && window.scrollY + window.innerHeight > heroSection.offsetTop + 200) {
        counters.forEach(counter => {
          const target = +counter.getAttribute(\'data-target\');
          const duration = 2000;
          const step = target / (duration / 16);
          let current = 0;
          const update = () => {
            current += step;
            if (current < target) {
              counter.textContent = Math.ceil(current);
              requestAnimationFrame(update);
            } else {
              counter.textContent = target;
            }
          };
          update();
        });
        animated = true;
      }
    });

    // Initialize calculator
    calculateROI();

    // Trigger counter immediately if hero visible
    setTimeout(() => {
      const scrollEvent = new Event(\'scroll\');
      window.dispatchEvent(scrollEvent);
    }, 500);
  </script>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"Done! New index.html written: {len(new_html):,} chars")
