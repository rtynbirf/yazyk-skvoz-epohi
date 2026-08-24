#!/usr/bin/env python3
"""
Build linguistic-code-v18.2.html from v18-final.html
"The Quiet Reader" — polymathic golden middle synthesis

Three layers:
  1. Differentiated widths: trap 560px, manifest 740px/840px via min()
  2. Fluid typography via clamp()
  3. Ghost Rail (right side, >=1280px, opacity 0.12)
"""

import re

SRC = '/home/z/my-project/download/linguistic-code-v18-final.html'
DST = '/home/z/my-project/download/linguistic-code-v18.2.html'

RESPONSIVE_CSS = r'''
  /* ================================================================
     ADAPTIVE LAYER v18.2 — "The Quiet Reader"
     Polymathic synthesis from 9 perspectives
     Three layers: Widths / Typography / Ghost Rail
     ================================================================ */

  /* --- LAYER 1: Differentiated Widths (min() for true fluidity) --- */

  /* Trap (screens 0-5): narrow forever — somatic event
     +40px from 520px gives air on desktop without losing intimacy */
  .screen-honesty .card,
  .step-1 .card,
  .step-4 .card,
  .step-5 .card {
    max-width: min(560px, calc(100vw - 48px));
  }

  /* Manifest (screen 6): reader-optimal width
     740px for serif italic ~70 chars/line (Dyson & Haselgrove, 2001)
     840px for mono epistemic-gap (mono tolerates wider) */
  .screen-manifest .accordion {
    max-width: min(840px, calc(100vw - 48px));
    margin: 0 auto;
  }
  .screen-manifest .accordion-content {
    max-width: min(740px, calc(100vw - 48px));
  }
  .screen-manifest .epistemic-gap {
    max-width: min(840px, calc(100vw - 48px));
  }
  .screen-manifest .manifest-footer {
    max-width: min(740px, calc(100vw - 48px));
  }
  .screen-manifest .manifest-header {
    max-width: min(840px, calc(100vw - 48px));
    margin-left: auto;
    margin-right: auto;
  }

  /* --- LAYER 2: Fluid Typography via clamp() --- */

  .screen-manifest .accordion-content {
    font-size: clamp(15px, 0.35vw + 14.5px, 18px);
    line-height: clamp(1.7, 0.02vw + 1.68, 1.8);
  }
  .screen-manifest .epistemic-gap {
    font-size: clamp(10px, 0.15vw + 10px, 12px);
    line-height: clamp(1.7, 0.02vw + 1.68, 1.8);
  }
  .screen-manifest .manifest-header .mh-title {
    font-size: clamp(19px, 0.5vw + 18px, 22px);
  }
  .honesty-title {
    font-size: clamp(23px, 1.2vw + 18px, 32px);
  }
  .honesty-body {
    font-size: clamp(16px, 0.5vw + 15px, 18px);
    max-width: min(420px, calc(100vw - 96px));
  }
  .honesty-note {
    max-width: min(400px, calc(100vw - 96px));
  }
  .honesty-disclaimer {
    max-width: min(400px, calc(100vw - 96px));
  }
  .step-1 .instruction {
    font-size: clamp(22px, 1vw + 18px, 26px);
  }
  .step-1 .sub-instruction {
    font-size: clamp(17px, 0.6vw + 15.5px, 20px);
  }
  .step-3 .statement {
    font-size: clamp(23px, 1.2vw + 18px, 32px);
  }
  .step-4 .observation {
    font-size: clamp(17px, 0.5vw + 16px, 19px);
    max-width: min(400px, calc(100vw - 96px));
  }
  .bridge-field textarea {
    font-size: clamp(15px, 0.3vw + 14.5px, 16px);
  }

  /* --- LAYER 3: Ghost Rail (right side, >=1280px) ---
     Placed RIGHT (not left) because:
     - Russian is LTR: left margin = reading anchor point
     - Right margin = peripheral rest between lines
     - Navigation in periphery = discovery, not interference
     - Continues .footer-id tradition (already right: 24px) */

  .ghost-rail {
    display: none;
    position: fixed;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    z-index: 50;
    font-family: var(--mono);
    flex-direction: column;
    gap: 3px;
    opacity: 0.12;
    transition: opacity 0.3s ease;
    -webkit-user-select: none;
    user-select: none;
  }
  .ghost-rail:hover {
    opacity: 0.85;
  }
  .ghost-rail-item {
    font-size: 9.5px;
    line-height: 1.6;
    color: var(--text-faint);
    cursor: pointer;
    padding: 1px 8px;
    border-right: 2px solid transparent;
    transition: color 0.2s ease, border-color 0.2s ease;
    text-align: right;
  }
  .ghost-rail-item:hover {
    color: var(--text-dim);
  }
  .ghost-rail-item.active {
    color: var(--gold-dim);
    border-right-color: var(--gold-dim);
  }
  @media (min-width: 1280px) {
    .ghost-rail {
      display: flex;
    }
  }
  /* Ghost Rail respects reduced motion */
  @media (prefers-reduced-motion: reduce) {
    .ghost-rail { transition: none; }
    .ghost-rail-item { transition: none; }
  }
'''

GHOST_RAIL_HTML = '''<nav class="ghost-rail" id="ghostRail" aria-label="Навигация по тезисам"></nav>'''

GHOST_RAIL_JS = r'''
// Ghost Rail: generate thesis numbers + IntersectionObserver
(function(){
  var rail=document.getElementById('ghostRail');
  if(!rail)return;
  for(var i=1;i<=33;i++){
    var d=document.createElement('div');
    d.className='ghost-rail-item';
    d.textContent=(i<10?'0':'')+i;
    d.dataset.idx=i;
    d.setAttribute('role','button');
    d.setAttribute('aria-label','\u0422\u0435\u0437\u0438\u0441 '+i);
    d.addEventListener('click',function(){
      var idx=this.dataset.idx;
      var items=document.querySelectorAll('.accordion-item');
      var target=items[idx-1];
      if(target){
        var rmq=window.matchMedia('(prefers-reduced-motion: reduce)');
        target.scrollIntoView({behavior:rmq.matches?'auto':'smooth',block:'center'});
        var trig=target.querySelector('.accordion-trigger');
        if(trig&&!target.classList.contains('open'))trig.click();
      }
    });
    rail.appendChild(d);
  }
  var items=document.querySelectorAll('.accordion-item');
  var railItems=rail.querySelectorAll('.ghost-rail-item');
  var obs=new IntersectionObserver(function(entries){
    for(var i=0;i<entries.length;i++){
      if(entries[i].isIntersecting){
        var idx=Array.prototype.indexOf.call(items,entries[i].target);
        for(var j=0;j<railItems.length;j++){
          if(j===idx)railItems[j].classList.add('active');
          else railItems[j].classList.remove('active');
        }
      }
    }
  },{threshold:0.4,rootMargin:'-10% 0px -60% 0px'});
  for(var k=0;k<items.length;k++)obs.observe(items[k]);
})();
'''

def main():
    with open(SRC, 'r', encoding='utf-8') as f:
        html = f.read()

    # Validate source integrity
    assert html.count('class="accordion-item"') == 33, f"Expected 33 accordion items, found {html.count('class=\"accordion-item\"')}"
    assert html.count('class="epistemic-gap"') == 33, f"Expected 33 epistemic gaps, found {html.count('class=\"epistemic-gap\"')}"
    assert 'function goTo(' in html, 'goTo function missing'
    assert 'function seal(' in html, 'seal function missing'
    assert 'function toggleAcc(' in html, 'toggleAcc function missing'
    assert 'prefers-reduced-motion' in html, 'prefers-reduced-motion missing'
    print('[OK] Source validation: 33 theses, 33 gaps, JS functions, reduced-motion')

    # 1. Insert responsive CSS before </style>
    assert '</style>' in html, '</style> not found'
    html = html.replace('</style>', RESPONSIVE_CSS + '\n  </style>', 1)
    print('[OK] Responsive CSS injected before </style>')

    # 2. Insert Ghost Rail HTML before </body>
    assert '</body>' in html, '</body> not found'
    html = html.replace('</body>', GHOST_RAIL_HTML + '\n</body>', 1)
    print('[OK] Ghost Rail HTML injected before </body>')

    # 3. Insert Ghost Rail JS before </script>
    assert '</script>' in html, '</script> not found'
    html = html.replace('</script>', GHOST_RAIL_JS + '\n</script>', 1)
    print('[OK] Ghost Rail JS injected before </script>')

    # Post-patch validation
    assert html.count('class="accordion-item"') == 33
    assert html.count('class="epistemic-gap"') == 33
    assert 'function goTo(' in html
    assert 'function seal(' in html
    assert 'function toggleAcc(' in html
    assert 'prefers-reduced-motion' in html
    assert 'ghost-rail' in html
    assert 'ghostRail' in html
    assert 'IntersectionObserver' in html
    assert 'min(560px' in html
    assert 'min(740px' in html
    assert 'min(840px' in html
    assert 'clamp(' in html
    assert 'opacity: 0.12' in html
    assert 'right: 20px' in html
    assert 'min-width: 1280px' in html
    print('[OK] Post-patch validation passed (14 checks)')

    with open(DST, 'w', encoding='utf-8') as f:
        f.write(html)

    size_kb = len(html.encode('utf-8')) / 1024
    print(f'[DONE] {DST} — {size_kb:.1f} KB')

if __name__ == '__main__':
    main()
