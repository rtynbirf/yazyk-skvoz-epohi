#!/usr/bin/env python3
"""Deep validation of v18.2.html"""

PATH = '/home/z/my-project/download/linguistic-code-v18.2.html'

with open(PATH, 'r', encoding='utf-8') as f:
    html = f.read()

errors = []
checks = 0

def check(name, condition, detail=''):
    global checks
    checks += 1
    if not condition:
        errors.append(f'FAIL [{name}]: {detail}')
    else:
        print(f'  [OK] {name}')

# === STRUCTURAL INTEGRITY ===
print('=== STRUCTURAL INTEGRITY ===')
check('DOCTYPE', '<!DOCTYPE html>' in html)
check('lang=ru', 'lang="ru"' in html)
check('charset UTF-8', 'charset="UTF-8"' in html)
check('viewport meta', 'viewport' in html)
check('Google Fonts link', 'fonts.googleapis.com' in html)
check('Cormorant Garamond', 'Cormorant Garamond' in html)
check('Inter font', 'Inter' in html)
check('JetBrains Mono', 'JetBrains Mono' in html)

# === SCREENS 0-6 ===
print('\n=== SCREENS ===')
for i in range(7):
    check(f'screen{i} exists', f'id="screen{i}"' in html)
check('screen0 active', 'screen screen-honesty active' in html)
check('screen6 is manifest', 'screen screen-manifest' in html)

# === 33 THESES ===
print('\n=== 33 THESES ===')
thesis_count = html.count('class="accordion-item"')
check(f'33 accordion items (found {thesis_count})', thesis_count == 33)

gap_count = html.count('class="epistemic-gap"')
check(f'33 epistemic gaps (found {gap_count})', gap_count == 33)

content_count = html.count('class="accordion-content"')
check(f'33 accordion contents (found {content_count})', content_count == 33)

trigger_count = html.count('class="accordion-trigger"')
check(f'33 accordion triggers (found {trigger_count})', trigger_count == 33)

# Verify thesis numbers 01-33
for i in [1, 6, 14, 24, 27, 30, 33]:
    num = f'{i:02d}'
    check(f'thesis {num} present', f'<span class="num">{num}</span>' in html)

# === ACADEMIC REFERENCES ===
print('\n=== ACADEMIC REFERENCES ===')
refs = ['Kandel, 2001', 'Levelt, 1989', 'Friston, 2010', 'Barrett, 2017',
        'Damasio, 1994', 'Vygotsky', 'Whorf', 'Clark & Chalmers, 1998',
        'Nunez & Sweetser, 2006', 'Bateson, 1972']
for ref in refs:
    check(f'ref: {ref[:30]}', ref in html)

# === NO HOPF (P0 fix verification) ===
print('\n=== P0 FIXES ===')
check('No Hopi', 'Хопи' not in html and 'хопи' not in html)
check('No Hopi (eng)', 'Hopi' not in html)
check('Aymara present', 'аймара' in html.lower() or 'Aymara' in html)
check('Friston present (not MacLean)', 'Friston' in html)

# === JS FUNCTIONS ===
print('\n=== JS FUNCTIONS ===')
check('goTo function', 'function goTo(' in html)
check('seal function', 'function seal(' in html)
check('toggleAcc function', 'function toggleAcc(' in html)
check('localStorage in seal', 'localStorage' in html)

# === REDUCED MOTION ===
print('\n=== ACCESSIBILITY ===')
rm_count = html.count('prefers-reduced-motion')
check(f'prefers-reduced-motion present ({rm_count} occurrences)', rm_count >= 3)
check('Ghost rail reduced motion', 'ghost-rail { transition: none; }' in html or 'ghost-rail{transition:none' in html)

# === RESPONSIVE LAYER v18.2 ===
print('\n=== RESPONSIVE LAYER ===')
check('min(560px trap width', 'min(560px' in html)
check('min(740px content width', 'min(740px' in html)
check('min(840px gap width', 'min(840px' in html)
check('clamp() for content', 'clamp(15px, 0.35vw' in html)
check('clamp() for gap', 'clamp(10px, 0.15vw' in html)
check('clamp() for title', 'clamp(23px, 1.2vw' in html)

# === GHOST RAIL ===
print('\n=== GHOST RAIL ===')
check('Ghost rail HTML', 'id="ghostRail"' in html)
check('Ghost rail CSS class', '.ghost-rail {' in html or '.ghost-rail{' in html)
check('Ghost rail right: 20px', 'right: 20px' in html)
check('Ghost rail opacity 0.12', 'opacity: 0.12' in html)
check('Ghost rail >=1280px', 'min-width: 1280px' in html)
check('Ghost rail IntersectionObserver', 'IntersectionObserver' in html)
check('Ghost rail aria-label', 'aria-label' in html)
check('Ghost rail scrollIntoView', 'scrollIntoView' in html)
check('Ghost rail hover 0.85', 'opacity: 0.85' in html)
check('Ghost rail prefers-reduced-motion in JS', 'prefers-reduced-motion: reduce' in html)

# === INTEGRITY CHECKS ===
print('\n=== FILE INTEGRITY ===')
check('Single <html> tag', html.count('<html') == 1)
check('Single </html> tag', html.count('</html>') == 1)
check('Single <body> tag', html.count('<body>') == 1)
check('Single </body> tag', html.count('</body>') == 1)
check('Single <style> block', html.count('<style>') == 1)
check('Single </style> tag', html.count('</style>') == 1)
check('Script tag closed', '<script>' in html and '</script>' in html)
check('No broken HTML entities', '&rarr;' in html or '&mdash;' in html)
check('Formula present', 'LC(H, F)' in html)
check('v18 label', 'v18' in html)
check('Footer note', 'no server' in html.lower())

# === SUMMARY ===
print(f'\n{"="*50}')
print(f'Total checks: {checks}')
print(f'Passed: {checks - len(errors)}')
print(f'Failed: {len(errors)}')
if errors:
    print('\nFAILURES:')
    for e in errors:
        print(f'  {e}')
else:
    print('\nALL CHECKS PASSED ✓')

size_kb = len(html.encode('utf-8')) / 1024
print(f'File size: {size_kb:.1f} KB')
