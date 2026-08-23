# -*- coding: utf-8 -*-
"""v18.2 CSS — extracted as a Python module to avoid brace-escaping issues."""

V18_2_CSS = '''  /* ─── v18.2 Adaptive Focus + Ghost Rail ─────────────────── */
  *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
  :root {
    --bg:#0E1011;--surface:#16181B;--surface-2:#1C1F23;
    --text:#D4D0C8;--text-dim:#7A7770;--text-faint:#4A4843;
    --gold:#C6A85B;--gold-dim:#8B7A44;--gold-faint:rgba(198,168,91,0.08);
    --serif:'Cormorant Garamond',Georgia,serif;
    --sans:'Inter',system-ui,sans-serif;
    --mono:'JetBrains Mono',monospace;
    --gap-bg:#0A0B0C;--gap-border:#2A2823;--gap-label:#5A5853;
    --trap-max:520px;    /* somatic trap width: mobile */
    --read-max:840px;    /* manifest container: desktop */
    --col-max:740px;     /* reading column: serif optimum */
    --rail-w:36px;       /* ghost rail width */
  }
  html,body { height:100%; background:var(--bg); color:var(--text); font-family:var(--sans); font-weight:300; overflow:hidden; }
  .container { display:flex; align-items:center; justify-content:center; height:100%; padding:24px; }
  .card { width:100%; max-width:var(--trap-max); min-height:0; }

  /* ─── Intro screens (0-5): somatic trap, always narrow ─── */
  .screen-honesty { text-align:center; animation:fadeIn 1.4s ease-out; }
  .honesty-mark { font-family:var(--mono); font-size:9px; letter-spacing:4px; color:var(--text-faint); text-transform:uppercase; margin-bottom:56px; line-height:1.8; }
  .honesty-title { font-family:var(--serif); font-size:clamp(23px, 1.2vw + 18px, 36px); line-height:1.5; font-weight:400; color:var(--text); margin-bottom:20px; }
  .honesty-body { font-family:var(--serif); font-size:clamp(16px, 0.4vw + 14px, 20px); line-height:1.8; font-weight:400; color:var(--text-dim); font-style:italic; max-width:420px; margin:0 auto 48px; }
  .honesty-body strong { color:var(--gold-dim); font-style:normal; font-weight:600; }
  .honesty-note { font-family:var(--mono); font-size:clamp(10px, 0.15vw + 9.5px, 11px); letter-spacing:0.3px; color:var(--text-faint); line-height:1.9; max-width:400px; margin:0 auto 48px; }
  .honesty-disclaimer { font-family:var(--mono); font-size:clamp(9px, 0.1vw + 8.5px, 10px); letter-spacing:0.3px; color:var(--gold-dim); line-height:1.8; max-width:400px; margin:0 auto 40px; opacity:0.7; }
  .btn-somatic { display:inline-block; padding:14px 40px; border:1px solid var(--gold-dim); border-radius:2px; background:transparent; color:var(--gold); font-family:var(--mono); font-size:12px; letter-spacing:2px; text-transform:uppercase; cursor:pointer; transition:border-color 0.4s,color 0.4s,transform 0.15s; }
  .btn-somatic:hover { border-color:var(--gold); transform:translateY(-1px); }
  .btn-somatic:active { transform:translateY(0); }
  .btn-bridge { padding:10px 28px; border-radius:2px; font-family:var(--mono); font-size:11px; letter-spacing:1px; text-transform:uppercase; cursor:pointer; transition:all 0.3s; }
  .btn-bridge.primary { background:transparent; border:1px solid var(--gold-dim); color:var(--gold); }
  .btn-bridge.primary:hover { border-color:var(--gold); }
  .btn-bridge.ghost { background:transparent; border:1px solid transparent; color:var(--text-dim); opacity:0.5; }
  .btn-bridge.ghost:hover { opacity:0.8; }
  .btn-next { padding:10px 32px; border:1px solid var(--text-faint); border-radius:2px; background:transparent; color:var(--text-dim); font-family:var(--mono); font-size:10px; letter-spacing:1.5px; text-transform:uppercase; cursor:pointer; transition:all 0.3s; }
  .btn-next:hover { border-color:var(--text-dim); color:var(--text); }
  .step-1 { text-align:center; animation:fadeIn 1.2s ease-out; }
  .step-label { font-family:var(--mono); font-size:11px; letter-spacing:3px; color:var(--gold-dim); text-transform:uppercase; margin-bottom:48px; }
  .step-1 .instruction { font-family:var(--serif); font-size:clamp(22px, 1.1vw + 18px, 32px); line-height:1.5; font-weight:400; color:var(--text); margin-bottom:12px; }
  .step-1 .sub-instruction { font-family:var(--serif); font-size:clamp(17px, 0.5vw + 15px, 24px); line-height:1.5; font-weight:400; color:var(--text-dim); font-style:italic; margin-bottom:56px; }
  .step-1 .sub-instruction em { color:var(--gold-dim); font-style:normal; border-bottom:1px solid var(--gold-faint); padding-bottom:1px; }
  .step-2 { display:flex; align-items:center; justify-content:center; height:100vh; }
  .pulse-dot { width:6px; height:6px; border-radius:50%; background:var(--gold); animation:pulse 2.4s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:0.15;transform:scale(1);} 50%{opacity:0.8;transform:scale(1.8);} }
  .step-3 { text-align:center; animation:fadeIn 0.8s ease-out; }
  .origin-tag { font-family:var(--mono); font-size:10px; letter-spacing:3px; color:var(--text-dim); text-transform:uppercase; margin-bottom:40px; }
  .origin-tag .degree { color:var(--text-faint); font-size:9px; }
  .step-3 .statement { font-family:var(--serif); font-size:clamp(23px, 1.2vw + 18px, 34px); line-height:1.6; font-weight:400; color:var(--text); }
  .step-3 .statement em { color:var(--gold); font-style:normal; border-bottom:1px solid var(--gold-dim); }
  .step-4 { text-align:center; animation:fadeIn 1.5s ease-out; }
  .step-4 .observation { font-family:var(--serif); font-size:clamp(17px, 0.4vw + 15px, 21px); line-height:1.7; font-weight:400; color:var(--text-dim); font-style:italic; max-width:440px; margin:0 auto 44px; }
  .bridge-prompt { font-family:var(--mono); font-size:11px; letter-spacing:0.5px; color:var(--text-dim); margin-bottom:20px; line-height:1.6; opacity:0.7; }
  .bridge-field { width:100%; max-width:440px; margin:0 auto; }
  .bridge-field textarea { width:100%; min-height:80px; max-height:200px; padding:16px; background:var(--surface); border:1px solid var(--gold-faint); border-radius:2px; color:var(--text); font-family:var(--serif); font-size:clamp(15px, 0.2vw + 14px, 17px); font-style:italic; line-height:1.7; resize:vertical; outline:none; transition:border-color 0.3s; }
  .bridge-field textarea::placeholder { color:var(--text-dim); opacity:0.4; font-style:italic; }
  .bridge-field textarea:focus { border-color:var(--gold-dim); }
  .bridge-actions { display:flex; gap:12px; justify-content:center; margin-top:24px; }
  .step-5 { text-align:center; animation:fadeIn 2s ease-out; }
  .step-5 .sealed-text { font-family:var(--serif); font-size:clamp(22px, 0.6vw + 18px, 28px); line-height:1.6; color:var(--gold); margin-bottom:36px; }
  .step-5 .sealed-sub { font-family:var(--mono); font-size:10px; letter-spacing:0.5px; color:var(--text-dim); opacity:0.4; line-height:1.7; max-width:380px; margin:0 auto 32px; }
  .step-5 .user-text-echo { font-family:var(--serif); font-size:16px; font-style:italic; color:var(--text); opacity:0.6; line-height:1.7; max-width:440px; margin:0 auto 36px; padding:16px; border-left:2px solid var(--gold-dim); text-align:left; }

  /* ─── Manifest (screen 6) ──────────────────────────────── */
  .screen-manifest { text-align:left; animation:fadeIn 1.2s ease-out; overflow-y:auto; max-height:100vh; padding:32px 24px 100px; -webkit-overflow-scrolling:touch; }
  .manifest-header { text-align:center; margin-bottom:40px; position:sticky; top:0; padding:24px 0 16px; background:var(--bg); z-index:2; }
  .manifest-header .mh-label { font-family:var(--mono); font-size:9px; letter-spacing:4px; color:var(--gold-dim); text-transform:uppercase; margin-bottom:14px; }
  .manifest-header .mh-title { font-family:var(--serif); font-size:clamp(19px, 0.8vw + 16px, 28px); line-height:1.4; color:var(--text); font-weight:400; }
  .manifest-header .mh-sub { font-family:var(--mono); font-size:10px; letter-spacing:0.5px; color:var(--text-faint); margin-top:10px; }
  .accordion { max-width:var(--trap-max); margin:0 auto; transition:max-width 0.3s ease; }
  .accordion-item { border-bottom:1px solid var(--surface-2); }
  .accordion-trigger { width:100%; display:flex; align-items:baseline; gap:12px; padding:15px 0; background:none; border:none; color:var(--text); cursor:pointer; text-align:left; font-family:var(--sans); font-size:clamp(14px, 0.2vw + 13px, 16px); font-weight:400; line-height:1.5; transition:color 0.2s; }
  .accordion-trigger:hover { color:var(--gold); }
  .accordion-trigger .num { font-family:var(--mono); font-size:clamp(10px, 0.08vw + 9.5px, 11px); color:var(--gold-dim); min-width:24px; flex-shrink:0; }
  .accordion-trigger .arrow { font-family:var(--mono); font-size:10px; color:var(--text-faint); margin-left:auto; flex-shrink:0; transition:transform 0.3s; }
  .accordion-item.open .accordion-trigger .arrow { transform:rotate(90deg); color:var(--gold-dim); }
  .accordion-body { max-height:0; overflow:hidden; transition:max-height 0.4s ease; }
  .accordion-item.open .accordion-body { max-height:1200px; }
  .epistemic-gap {
    background:var(--gap-bg); border-left:2px solid var(--gap-border);
    padding:14px 18px; margin:0 0 16px 36px; font-family:var(--mono);
    font-size:clamp(10.5px, 0.15vw + 10px, 12px); line-height:1.75; color:var(--text-dim); text-align:left;
    opacity:0; transform:translateY(4px);
    transition:opacity 0.35s ease, transform 0.35s ease;
  }
  .accordion-item.open .epistemic-gap { animation:gapFadeIn 0.5s ease-out 0.05s forwards; }
  .epistemic-gap .gap-title {
    font-size:8.5px; letter-spacing:2.5px; color:var(--gap-label);
    text-transform:uppercase; margin-bottom:10px; display:block;
  }
  .epistemic-gap strong { color:var(--text); font-weight:400; }
  .epistemic-gap .unknown { color:var(--gold-dim); font-style:italic; }
  .accordion-content { padding:0 0 18px 36px; font-family:var(--serif); font-size:clamp(16px, 0.35vw + 14.5px, 18px); line-height:1.75; color:var(--text-dim); font-style:italic; }
  .manifest-footer { text-align:center; margin-top:48px; padding-top:28px; border-top:1px solid var(--surface-2); max-width:var(--trap-max); margin-left:auto; margin-right:auto; transition:max-width 0.3s ease; }
  .manifest-footer .mf-text { font-family:var(--serif); font-size:clamp(17px, 0.25vw + 15.5px, 19px); color:var(--text-dim); font-style:italic; line-height:1.6; margin-bottom:20px; }
  .manifest-footer .mf-formula { font-family:var(--mono); font-size:clamp(10px, 0.1vw + 9.5px, 11px); letter-spacing:0.5px; color:var(--text-faint); line-height:1.9; max-width:580px; margin:0 auto 24px; }
  .manifest-footer .mf-note { font-family:var(--mono); font-size:9px; letter-spacing:0.3px; color:var(--text-faint); opacity:0.6; line-height:1.8; max-width:480px; margin:0 auto; }
  .footer-id { position:fixed; bottom:20px; right:24px; font-family:var(--mono); font-size:9px; letter-spacing:1px; color:var(--text-faint); opacity:0.5; z-index:3; }
  .screen { display:none; }
  .screen.active { display:flex; flex-direction:column; }
  @keyframes gapFadeIn {
    from { opacity:0; transform:translateY(-4px); }
    to { opacity:0.8; transform:translateY(0); }
  }
  @keyframes fadeIn { from{opacity:0;transform:translateY(10px);} to{opacity:1;transform:translateY(0);} }

  /* ─── Ghost Rail (≥1280px, manifest only) ─────────────── */
  .ghost-rail { display:none; }
  @media(min-width:1280px) {
    .ghost-rail {
      display:flex; flex-direction:column; align-items:center; gap:2px;
      position:fixed; left:20px; top:50%; transform:translateY(-50%);
      z-index:5;
    }
    .ghost-rail-link {
      font-family:var(--mono); font-size:9px; color:var(--text-faint);
      opacity:0.15; text-decoration:none; padding:3px 0;
      transition:opacity 0.3s, color 0.3s; line-height:1;
    }
    .ghost-rail-link:hover { opacity:0.7; color:var(--text); }
    .ghost-rail-link.active { opacity:0.8; color:var(--gold-dim); }
  }

  /* ─── Responsive: expand manifest on wider screens ────── */
  @media(min-width:768px) {
    .container { padding:32px; }
    .screen-manifest { padding:40px 32px 120px; }
    .accordion { max-width:680px; }
    .manifest-footer { max-width:680px; }
    .epistemic-gap { margin-left:40px; padding:16px 20px; }
    .accordion-content { padding-left:40px; padding-bottom:20px; }
  }
  @media(min-width:1024px) {
    .container { padding:40px; }
    .screen-manifest { padding:48px 40px 140px; }
    .accordion { max-width:var(--read-max); }
    .manifest-footer { max-width:var(--read-max); }
    .epistemic-gap { margin-left:44px; padding:18px 22px; margin-bottom:20px; }
    .accordion-content { padding-left:44px; padding-bottom:24px; max-width:var(--col-max); }
    .accordion-trigger { padding:18px 0; gap:14px; }
    .accordion-trigger .num { min-width:28px; }
    .manifest-header { margin-bottom:48px; }
  }
  @media(min-width:1440px) {
    .container { padding:48px; }
    .screen-manifest { padding:56px 48px 160px; }
    .epistemic-gap { margin-left:48px; padding:20px 24px; }
    .accordion-content { padding-left:48px; padding-bottom:28px; }
    .accordion-trigger { padding:20px 0; gap:16px; }
    .accordion-trigger .num { min-width:32px; }
    .manifest-footer { margin-top:56px; padding-top:32px; }
  }

  /* ─── Somatic trap: stays narrow on all screens ──────── */
  @media(min-width:768px) {
    .card { max-width:560px; }
  }
  @media(min-width:1024px) {
    .card { max-width:560px; }
    .bridge-field { max-width:480px; }
    .step-4 .observation { max-width:480px; }
    .step-5 .user-text-echo { max-width:460px; }
    .honesty-body { max-width:460px; }
    .honesty-note { max-width:440px; }
    .honesty-disclaimer { max-width:440px; }
  }

  /* ─── Small screen fallback ────────────────────────────── */
  @media(max-width:480px) {
    .accordion-content{font-size:15px;padding-left:24px;}
    .epistemic-gap{margin-left:24px;}
    .manifest-header .mh-title{font-size:19px;}
  }

  /* ─── Reduced motion (unchanged) ──────────────────────── */
  @media(prefers-reduced-motion:reduce) {
    .pulse-dot{animation:none;opacity:0.5;}
    .screen-honesty,.step-1,.step-3,.step-4,.step-5,.screen-manifest{animation:none;}
    .accordion-body{transition:none;}
    .epistemic-gap{transition:none;opacity:0.8;transform:none;}
    .btn-somatic,.btn-bridge,.btn-next,.accordion-trigger{transition:none;}
  }'''
