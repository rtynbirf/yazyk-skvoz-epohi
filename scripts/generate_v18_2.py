#!/usr/bin/env python3
"""
generate_v18_2.py — v18.2: Adaptive Focus + Ghost Rail

Из v18-final: адаптивная ширина, clamp()-типографика, Ghost Rail.

Синтез 7 мнений ("Языковые модели.txt"):
  - Слой 1: Читательская ширина 740px (Dyson & Haselgrove, 2001)
  - Слой 2: clamp() вместо ступенек (fluid typography)
  - Слой 3: Ghost Rail ≥1280px (карта, не навигация)
"""

import re
from v18_2_css import V18_2_CSS

INPUT = '/home/z/my-project/download/linguistic-code-v18-final.html'
OUTPUT = '/home/z/my-project/download/linguistic-code-v18.2.html'

with open(INPUT, 'r', encoding='utf-8') as f:
    html = f.read()

# ═══════════════════════════════════════════════════════════════
# 1. ADD IDs to each accordion-item
# ═══════════════════════════════════════════════════════════════
counter = [0]
def add_id(m):
    counter[0] += 1
    return f'<div class="accordion-item" id="thesis-{counter[0]:02d}">'
html = re.sub(r'<div class="accordion-item">', add_id, html)
assert html.count('id="thesis-') == 33
print('✓ 33 thesis IDs added')

# ═══════════════════════════════════════════════════════════════
# 2. GENERATE GHOST RAIL HTML
# ═══════════════════════════════════════════════════════════════
rail_links = '\n'.join(
    f'        <a class="ghost-rail-link" href="#thesis-{i:02d}" data-thesis="{i:02d}">{i:02d}</a>'
    for i in range(1, 34)
)
ghost_rail = f'''\n  <nav class="ghost-rail" id="ghostRail" aria-hidden="true">\n    {rail_links}\n  </nav>\n'''
html = html.replace('<body>', '<body>' + ghost_rail, 1)
print('✓ Ghost Rail HTML injected')

# ═══════════════════════════════════════════════════════════════
# 3. REPLACE CSS (anchor-based: between <style> and </style>)
# ═══════════════════════════════════════════════════════════════
style_start = html.find('<style>') + len('<style>')
style_end = html.find('</style>')
html = html[:style_start] + '\n  ' + V18_2_CSS + '\n' + html[style_end:]
print('✓ CSS replaced with v18.2 responsive')

# ═══════════════════════════════════════════════════════════════
# 4. ADD GHOST RAIL JAVASCRIPT
# ═══════════════════════════════════════════════════════════════
ghost_js = '''
// ─── Ghost Rail: IntersectionObserver (desktop only) ───
(function() {
  var rail = document.getElementById('ghostRail');
  if (!rail) return;
  var links = rail.querySelectorAll('.ghost-rail-link');
  var items = document.querySelectorAll('.accordion-item[id]');
  if (links.length === 0 || items.length === 0) return;
  for (var i = 0; i < links.length; i++) {
    links[i].addEventListener('click', function(e) {
      e.preventDefault();
      var id = this.getAttribute('href').substring(1);
      var target = document.getElementById(id);
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
  }
  if ('IntersectionObserver' in window) {
    var obs = new IntersectionObserver(function(entries) {
      for (var i = 0; i < entries.length; i++) {
        if (entries[i].isIntersecting) {
          var num = entries[i].target.id.replace('thesis-', '');
          for (var j = 0; j < links.length; j++) {
            links[j].classList.toggle('active', links[j].getAttribute('data-thesis') === num);
          }
        }
      }
    }, { rootMargin: '-20% 0px -60% 0px' });
    for (var k = 0; k < items.length; k++) obs.observe(items[k]);
  }
})();
'''
html = html.replace('</script>', ghost_js + '</script>', 1)
print('✓ Ghost Rail JS injected')

# ═══════════════════════════════════════════════════════════════
# 5. UPDATE TITLE
# ═══════════════════════════════════════════════════════════════
html = html.replace(
    '<title>Linguistic Code v18 — Final Synthesis</title>',
    '<title>Linguistic Code v18.2</title>'
)

# ═══════════════════════════════════════════════════════════════
# 6. VALIDATION
# ═══════════════════════════════════════════════════════════════
assert 'Linguistic Code v18.2' in html; print('✓ Title: v18.2')
assert html.count('class="accordion-item"') == 33; print('✓ 33 theses')
assert html.count('id="thesis-') == 33; print('✓ 33 thesis IDs')
assert len(re.findall(r'class="ghost-rail-link"', html)) == 33; print('✓ Ghost Rail (33 links)')
assert 'IntersectionObserver' in html; print('✓ Ghost Rail JS')

count_clamp = lambda: html.count('clamp(')
print(f'✓ clamp() used {count_clamp()} times')
assert count_clamp() >= 10

assert '--trap-max' in html; assert '--read-max' in html; assert '--col-max' in html
print('✓ CSS variables: trap-max, read-max, col-max')

assert 'var(--read-max)' in html; assert 'var(--col-max)' in html
print('✓ Width cascade: 520→680→840 (content capped at 740)')

hopi = len(re.findall(r'Хопи|хопи|Hop[iі]', html, re.IGNORECASE))
assert hopi == 0; print('✓ No Хопи')

assert 'prefers-reduced-motion' in html; print('✓ Reduced motion')

refs = ['Kandel','Levelt','Friederici','Friston','Damasio','Craig','Henrich','Quine','Popper']
for r in refs: assert r in html, f'Missing: {r}'
print(f'✓ References OK ({len(refs)} spot-checked)')

assert '.ghost-rail { display:none; }' in html; print('✓ Ghost Rail hidden on mobile')
assert 'min-width:1280px' in html; print('✓ Ghost Rail breakpoint: ≥1280px')

# Check somatic trap cap
assert re.search(r'\.card \{ max-width:560px; \}', html); print('✓ Somatic trap capped at 560px')

# Check reading column cap
assert 'max-width:var(--col-max)' in html; print('✓ Reading column capped at 740px')

print(f'\nSize: {len(html)} bytes ({len(html)/1024:.1f} KB)')

# ═══════════════════════════════════════════════════════════════
# 7. WRITE
# ═══════════════════════════════════════════════════════════════
with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Written: {OUTPUT}')
print('Done.')
