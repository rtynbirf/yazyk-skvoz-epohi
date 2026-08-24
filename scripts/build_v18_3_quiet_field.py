#!/usr/bin/env python3
"""
Build linguistic-code-v18.3.html from v18-final.html
"The Quiet Field" — polymathic synthesis v2

Three layers:
  1. Stable Measure — scale the field, not the content (trap 560, field 900, text 720, gap 800)
  2. Fluid Typography — clamp() everywhere
  3. Quiet Compass — thesis counter (07/33) + ephemeral map on click

Based on v18-final.html (clean base, no previous patches)
"""

import re

SRC = '/home/z/my-project/download/linguistic-code-v18-final.html'
DST = '/home/z/my-project/download/linguistic-code-v18.3.html'

RESPONSIVE_CSS = r'''
  /* ================================================================
     ADAPTIVE LAYER v18.3 — "The Quiet Field"
     Principle: scale the field, not the content.
     Silence is not waste. Silence is the design.
     ================================================================ */

  /* --- LAYER 1: STABLE MEASURE ---
     Trap stays narrow forever (somatic event).
     Manifest: the FIELD expands, the TEXT stays stable.
     On 1920px: 720px text inside 900px field = ~600px of silence.
     This is the Talmudic manuscript principle:
     text in the center, contemplation in the margins. */

  /* Trap (screens 0-5): somatic compression, all screens */
  .screen-honesty .card,
  .step-1 .card,
  .step-4 .card,
  .step-5 .card {
    max-width: min(560px, calc(100vw - 48px));
  }

  /* Manifest (screen 6): the field expands, text stays at reading measure */
  .screen-manifest .accordion {
    max-width: min(900px, calc(100vw - 48px));
    margin: 0 auto;
  }
  .screen-manifest .accordion-content {
    max-width: 720px;
  }
  .screen-manifest .epistemic-gap {
    max-width: 800px;
  }
  .screen-manifest .manifest-footer {
    max-width: 720px;
  }
  .screen-manifest .manifest-header {
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
  }

  /* --- LAYER 2: FLUID TYPOGRAPHY ---
     Screens are continuous, not discrete.
     No stepped 16→17→18→19 jumps. */

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

  /* --- LAYER 3: QUIET COMPASS ---
     Not a Ghost Rail. Not a Submarine Index. Not a sidebar.
     A single number in the corner: "07 / 33"
     Click → ephemeral map appears → click thesis → map disappears.
     Navigation exists only when the body calls it. */

  .quiet-compass {
    display: none;
    position: fixed;
    right: 24px;
    bottom: 24px;
    font-family: var(--mono);
    font-size: 9px;
    letter-spacing: 0.5px;
    color: var(--text-faint);
    opacity: 0.3;
    z-index: 50;
    cursor: pointer;
    padding: 6px 10px;
    border-radius: 2px;
    transition: opacity 0.25s ease;
    -webkit-user-select: none;
    user-select: none;
  }
  .quiet-compass:hover {
    opacity: 0.7;
  }

  /* Ephemeral map: invisible by default, summoned by click */
  .ephemeral-map {
    display: none;
    position: fixed;
    right: 24px;
    bottom: 48px;
    z-index: 60;
    background: var(--surface);
    border: 1px solid var(--surface-2);
    border-radius: 4px;
    padding: 12px 14px;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s ease;
  }
  .ephemeral-map.visible {
    opacity: 1;
    pointer-events: auto;
  }
  .ephemeral-map-grid {
    display: grid;
    grid-template-columns: repeat(6, 28px);
    gap: 2px;
  }
  .emap-cell {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--text-faint);
    text-align: center;
    padding: 4px 0;
    cursor: pointer;
    border-radius: 2px;
    transition: color 0.15s, background 0.15s;
  }
  .emap-cell:hover {
    color: var(--gold);
    background: var(--gold-faint);
  }
  .emap-cell.active {
    color: var(--gold);
    background: rgba(198,168,91,0.12);
  }

  /* Only on desktop */
  @media (min-width: 1024px) {
    .quiet-compass {
      display: block;
    }
    .ephemeral-map {
      display: block;
    }
  }

  /* Reduced motion */
  @media (prefers-reduced-motion: reduce) {
    .quiet-compass { transition: none; }
    .ephemeral-map { transition: none; }
    .emap-cell { transition: none; }
  }
'''

QUIET_COMPASS_HTML = '''<div class="quiet-compass" id="quietCompass" role="button" aria-label="Навигация по тезисам" tabindex="0"></div>
<div class="ephemeral-map" id="ephemeralMap"><div class="ephemeral-map-grid" id="emapGrid"></div></div>'''

QUIET_COMPASS_JS = r'''
// Quiet Compass: thesis counter + ephemeral map
(function(){
  var compass=document.getElementById('quietCompass');
  var emap=document.getElementById('ephemeralMap');
  var grid=document.getElementById('emapGrid');
  if(!compass||!emap||!grid)return;

  // Generate 33 cells in 6-column grid
  for(var i=1;i<=33;i++){
    var cell=document.createElement('div');
    cell.className='emap-cell';
    cell.textContent=(i<10?'0':'')+i;
    cell.dataset.idx=i;
    cell.addEventListener('click',function(e){
      e.stopPropagation();
      var idx=this.dataset.idx;
      var items=document.querySelectorAll('.accordion-item');
      var target=items[idx-1];
      if(target){
        var rmq=window.matchMedia('(prefers-reduced-motion: reduce)');
        target.scrollIntoView({behavior:rmq.matches?'auto':'smooth',block:'center'});
        var trig=target.querySelector('.accordion-trigger');
        if(trig&&!target.classList.contains('open'))trig.click();
      }
      hideMap();
    });
    grid.appendChild(cell);
  }

  // Toggle map on compass click
  var mapOpen=false;
  function showMap(){mapOpen=true;emap.classList.add('visible');}
  function hideMap(){mapOpen=false;emap.classList.remove('visible');}
  compass.addEventListener('click',function(e){
    e.stopPropagation();
    if(mapOpen)hideMap();else showMap();
  });
  // Also on Enter/Space for keyboard accessibility
  compass.addEventListener('keydown',function(e){
    if(e.key==='Enter'||e.key===' '){
      e.preventDefault();
      if(mapOpen)hideMap();else showMap();
    }
  });
  // Close map on click outside
  document.addEventListener('click',function(e){
    if(mapOpen&&!emap.contains(e.target)&&!compass.contains(e.target)){
      hideMap();
    }
  });
  // Close map on Escape
  document.addEventListener('keydown',function(e){
    if(e.key==='Escape'&&mapOpen)hideMap();
  });

  // IntersectionObserver: update compass text + highlight map cell
  var items=document.querySelectorAll('.accordion-item');
  var cells=grid.querySelectorAll('.emap-cell');
  var reducedMotion=window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var obs=new IntersectionObserver(function(entries){
    for(var i=0;i<entries.length;i++){
      if(entries[i].isIntersecting){
        var idx=Array.prototype.indexOf.call(items,entries[i].target)+1;
        var label=(idx<10?'0':'')+idx+' / 33';
        compass.textContent=label;
        for(var j=0;j<cells.length;j++){
          if(j===idx-1)cells[j].classList.add('active');
          else cells[j].classList.remove('active');
        }
        break;
      }
    }
  },{threshold:0.4,rootMargin:'-10% 0px -60% 0px'});

  for(var k=0;k<items.length;k++)obs.observe(items[k]);
  // Initial label
  compass.textContent='01 / 33';
})();
'''

def add_thesis_ids(html):
    """Add id='thesis-NN' to each accordion-item for semantic navigation."""
    count = 0
    def replacer(m):
        nonlocal count
        count += 1
        num = f'{count:02d}'
        return f'<div class="accordion-item" id="thesis-{num}"'
    result = re.sub(r'<div class="accordion-item">', replacer, html)
    assert count == 33, f'Expected 33 replacements, got {count}'
    return result

def main():
    with open(SRC, 'r', encoding='utf-8') as f:
        html = f.read()

    # Validate source
    assert html.count('class="accordion-item"') == 33
    assert html.count('class="epistemic-gap"') == 33
    assert 'function goTo(' in html
    assert 'function seal(' in html
    assert 'function toggleAcc(' in html
    assert 'prefers-reduced-motion' in html
    print('[OK] Source validation')

    # 1. Add thesis IDs
    html = add_thesis_ids(html)
    assert html.count('id="thesis-') == 33
    print('[OK] 33 thesis IDs added')

    # 2. Insert responsive CSS before </style>
    html = html.replace('</style>', RESPONSIVE_CSS + '\n  </style>', 1)
    print('[OK] Responsive CSS injected')

    # 3. Insert Quiet Compass HTML before </body>
    html = html.replace('</body>', QUIET_COMPASS_HTML + '\n</body>', 1)
    print('[OK] Quiet Compass HTML injected')

    # 4. Insert JS before </script>
    html = html.replace('</script>', QUIET_COMPASS_JS + '\n</script>', 1)
    print('[OK] Quiet Compass JS injected')

    # Post-patch validation
    assert html.count('class="accordion-item"') == 33
    assert html.count('class="epistemic-gap"') == 33
    assert html.count('id="thesis-') == 33
    assert 'function goTo(' in html
    assert 'function seal(' in html
    assert 'function toggleAcc(' in html
    assert 'prefers-reduced-motion' in html
    assert 'quiet-compass' in html
    assert 'ephemeral-map' in html
    assert 'IntersectionObserver' in html
    assert 'min(560px' in html
    assert 'min(900px' in html
    assert '720px' in html
    assert '800px' in html
    assert 'clamp(' in html
    assert 'scrollIntoView' in html
    assert 'prefers-reduced-motion: reduce' in html
    print('[OK] Post-patch validation (19 checks)')

    with open(DST, 'w', encoding='utf-8') as f:
        f.write(html)

    size_kb = len(html.encode('utf-8')) / 1024
    print(f'[DONE] {DST} — {size_kb:.1f} KB')

if __name__ == '__main__':
    main()
