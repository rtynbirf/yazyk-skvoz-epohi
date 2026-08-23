#!/usr/bin/env python3
"""
patch_v18_2_responsive.py — Добавляет адаптивный дизайн к v18-final.

Стратегия: простая адаптация (вариант A). Одноколоночный layout сохраняется.
Ширина и типографика масштабируются через @media-запросы.

Брейкпоинты:
  768px  — планшет
  1024px — десктоп
  1440px — большой десктоп

Дизайн-решения:
  - Вступительные экраны (0-5) масштабируются умеренно (до 640px)
    чтобы сохранить интимность соматической ловушки
  - Манифест (экран 6) масштабируется полнее (до 960px)
    потому что это чтение/исследование
  - Все дочерние max-width (honesty-body, bridge-field, mf-formula и т.д.)
    привязаны к ширине контейнера через процентные соотношения
"""

import re

INPUT = '/home/z/my-project/download/linguistic-code-v18-final.html'
OUTPUT = '/home/z/my-project/download/linguistic-code-v18.2.html'

with open(INPUT, 'r', encoding='utf-8') as f:
    html = f.read()

# ─── RESPONSIVE CSS BLOCK ──────────────────────────────────────
responsive_css = '''
  /* ─── Адаптивный дизайн v18.2 ─────────────────────────────── */

  /* Планшет (≥768px) */
  @media(min-width:768px) {
    .container { padding:32px 32px; }
    .card { max-width:640px; }
    .honesty-title { font-size:32px; margin-bottom:24px; }
    .honesty-body { font-size:19px; max-width:520px; }
    .honesty-note { max-width:480px; font-size:10.5px; }
    .honesty-disclaimer { max-width:480px; }
    .step-1 .instruction { font-size:30px; }
    .step-1 .sub-instruction { font-size:22px; }
    .step-3 .statement { font-size:32px; }
    .step-4 .observation { font-size:20px; max-width:480px; }
    .bridge-field { max-width:480px; }
    .bridge-field textarea { min-height:90px; font-size:17px; }
    .step-5 .sealed-text { font-size:26px; }
    .step-5 .sealed-sub { max-width:400px; }
    .step-5 .user-text-echo { max-width:440px; font-size:17px; }
    .btn-somatic { padding:16px 48px; font-size:13px; }
    .manifest-header .mh-title { font-size:26px; }
    .manifest-header .mh-sub { font-size:11px; }
    .screen-manifest { padding:40px 32px 120px; }
    .accordion { max-width:680px; }
    .accordion-trigger { padding:18px 0; font-size:15px; gap:14px; }
    .accordion-trigger .num { font-size:11px; min-width:28px; }
    .epistemic-gap { padding:16px 20px; margin-left:42px; font-size:11px; line-height:1.8; }
    .accordion-content { padding-left:42px; font-size:17px; line-height:1.8; }
    .manifest-footer { max-width:680px; }
    .manifest-footer .mf-text { font-size:18px; }
    .manifest-footer .mf-formula { max-width:560px; font-size:10.5px; }
    .manifest-footer .mf-note { max-width:480px; }
  }

  /* Десктоп (≥1024px) */
  @media(min-width:1024px) {
    .container { padding:40px 40px; }
    .card { max-width:640px; }
    .honesty-mark { font-size:10px; margin-bottom:64px; }
    .honesty-title { font-size:36px; margin-bottom:28px; }
    .honesty-body { font-size:20px; max-width:560px; }
    .honesty-note { max-width:520px; }
    .honesty-disclaimer { max-width:520px; font-size:10px; }
    .step-label { font-size:12px; margin-bottom:56px; }
    .step-1 .instruction { font-size:34px; }
    .step-1 .sub-instruction { font-size:24px; }
    .origin-tag { font-size:11px; margin-bottom:48px; }
    .step-3 .statement { font-size:36px; line-height:1.55; }
    .step-4 .observation { font-size:21px; max-width:520px; margin-bottom:48px; }
    .bridge-prompt { font-size:12px; }
    .bridge-field { max-width:520px; }
    .bridge-field textarea { min-height:100px; font-size:18px; padding:18px; }
    .bridge-actions { margin-top:28px; }
    .step-5 .sealed-text { font-size:28px; margin-bottom:40px; }
    .step-5 .sealed-sub { max-width:440px; font-size:11px; }
    .step-5 .user-text-echo { max-width:480px; font-size:18px; }
    .btn-somatic { padding:18px 56px; font-size:13px; letter-spacing:2.5px; }
    .btn-bridge { padding:12px 32px; font-size:12px; }
    .btn-next { padding:12px 36px; font-size:11px; }
    .manifest-header { margin-bottom:48px; padding:28px 0 20px; }
    .manifest-header .mh-label { font-size:10px; margin-bottom:16px; }
    .manifest-header .mh-title { font-size:30px; }
    .manifest-header .mh-sub { font-size:11px; margin-top:12px; }
    .screen-manifest { padding:48px 40px 140px; }
    .accordion { max-width:860px; }
    .accordion-item { border-bottom-width:1px; }
    .accordion-trigger { padding:20px 0; font-size:16px; gap:16px; line-height:1.55; }
    .accordion-trigger .num { font-size:11px; min-width:32px; }
    .accordion-trigger .arrow { font-size:11px; }
    .epistemic-gap {
      padding:18px 24px; margin-left:48px; margin-bottom:20px;
      font-size:11.5px; line-height:1.85;
    }
    .epistemic-gap .gap-title { font-size:9px; letter-spacing:3px; margin-bottom:12px; }
    .accordion-content {
      padding-left:48px; padding-bottom:24px;
      font-size:18px; line-height:1.85;
    }
    .manifest-footer { max-width:860px; margin-top:56px; padding-top:32px; }
    .manifest-footer .mf-text { font-size:19px; margin-bottom:24px; }
    .manifest-footer .mf-formula { max-width:680px; font-size:11px; line-height:2; }
    .manifest-footer .mf-note { max-width:520px; font-size:9.5px; }
  }

  /* Большой десктоп (≥1440px) */
  @media(min-width:1440px) {
    .container { padding:48px 48px; }
    .card { max-width:680px; }
    .honesty-title { font-size:38px; }
    .honesty-body { font-size:21px; max-width:600px; }
    .step-1 .instruction { font-size:36px; }
    .step-1 .sub-instruction { font-size:26px; }
    .step-3 .statement { font-size:38px; }
    .step-4 .observation { font-size:22px; max-width:560px; }
    .bridge-field { max-width:560px; }
    .step-5 .sealed-text { font-size:30px; }
    .step-5 .user-text-echo { max-width:520px; font-size:19px; }
    .manifest-header .mh-title { font-size:32px; }
    .screen-manifest { padding:56px 48px 160px; }
    .accordion { max-width:960px; }
    .accordion-trigger { padding:22px 0; font-size:17px; gap:18px; }
    .accordion-trigger .num { font-size:12px; min-width:36px; }
    .epistemic-gap {
      padding:20px 28px; margin-left:54px;
      font-size:12px; line-height:1.9;
    }
    .epistemic-gap .gap-title { font-size:9.5px; }
    .accordion-content {
      padding-left:54px; padding-bottom:28px;
      font-size:19px; line-height:1.9;
    }
    .manifest-footer { max-width:960px; }
    .manifest-footer .mf-text { font-size:20px; }
    .manifest-footer .mf-formula { max-width:760px; font-size:11px; }
    .manifest-footer .mf-note { max-width:560px; }
  }
'''

# Insert before the closing </style> tag, after the existing @media(max-width:480px) block
# Also update the title
html = html.replace(
    '<title>Linguistic Code v18 — Final Synthesis</title>',
    '<title>Linguistic Code v18.2</title>'
)

# Insert responsive CSS right before </style>
html = html.replace(
    '</style>',
    responsive_css + '</style>'
)

# ─── VALIDATION ─────────────────────────────────────────────────

# Check title
assert 'Linguistic Code v18.2' in html, 'Title not updated'
print('✓ Title: v18.2')

# Check all 3 breakpoints present
for bp in ['min-width:768px', 'min-width:1024px', 'min-width:1440px']:
    assert bp in html, f'Missing breakpoint: {bp}'
print('✓ All 3 breakpoints present')

# Check original 480px breakpoint preserved
assert 'max-width:480px' in html, 'Original small-screen breakpoint lost'
print('✓ Original small-screen breakpoint preserved')

# Check original prefers-reduced-motion preserved
assert 'prefers-reduced-motion' in html, 'Reduced motion query lost'
print('✓ Reduced motion preserved')

# Thesis count
assert html.count('class="accordion-item"') == 33, f'Expected 33 items, got {html.count("accordion-item")}'
print('✓ 33 theses intact')

# Gap count
assert html.count('class="epistemic-gap"') == 33
print('✓ 33 epistemic gaps intact')

# No Хопи
hopi = len(re.findall(r'Хопи|хопи|Hop[iі]', html, re.IGNORECASE))
assert hopi == 0, f'Хопи found {hopi} times!'
print('✓ No Хопи')

# Responsive .accordion max-width values
for w in ['680px', '860px', '960px']:
    assert w in html, f'Missing accordion width: {w}'
print('✓ Accordion widths: 520→680→860→960')

# Content font-size scaling
for fs in ['font-size:17px', 'font-size:18px', 'font-size:19px']:
    assert fs in html, f'Missing font size: {fs}'
print('✓ Typography scales: 16→17→18→19')

# Size
print(f'Size: {len(html)} bytes ({len(html)/1024:.1f} KB)')

# ─── WRITE ──────────────────────────────────────────────────────
with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Written: {OUTPUT}')
print('Done.')
