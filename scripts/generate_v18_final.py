#!/usr/bin/env python3
"""
linguistic-code-v18-final.py — СИНТЕЗ v18(2) base + v18(1) enrichments

Стратегия: split base HTML by accordion items, process each, rejoin.
No regex that spans div boundaries.
"""

import re

# ─── READ BASE FILE ─────────────────────────────────────────────
with open('/home/z/my-project/upload/linguistic-code-v18 (2).html', 'r') as f:
    html = f.read()

# ─── SPLIT INTO PRE-ACCORDION, ITEMS, POST-ACCORDION ───────────
acc_start = html.find('<div class="accordion"')
acc_inner_start = html.find('>', acc_start) + 1

# Split by accordion-item opening tags
parts = html[acc_inner_start:].split('<div class="accordion-item">')
# parts[0] = whitespace before first item
# parts[1..32] = items 1-32
# parts[33] = item 33 + post-accordion content

pre = html[:acc_inner_start]
post_raw = parts[-1]  # item 33 + closing tags

# Extract item 33 and post from last part
# Find the end of item 33: it closes with </div>  </div>  </div>
# Then the rest is post (script, closing html)
# Item 33 ends at the pattern: </div>\n    </div>\n  </div>\n  </div>\n  (accordion closing)\n  <script
item33_end = post_raw.find('</div>\n  </div>\n  <script')
if item33_end < 0:
    # Try alternate pattern
    item33_end = post_raw.rfind('</div>\n    </div>\n  </div>')
    if item33_end > 0:
        item33_end += len('</div>\n    </div>\n  </div>')

if item33_end > 0:
    items = parts[1:-1] + [post_raw[:item33_end]]
    post = post_raw[item33_end:]
else:
    # Fallback: take everything up to last 3 closing divs as item 33
    last_three = post_raw.rfind('</div>\n    </div>\n  </div>')
    if last_three > 0:
        items = parts[1:-1] + [post_raw[:last_three]]
        post = post_raw[last_three:]
    else:
        items = parts[1:-1] + [post_raw]
        post = ''

print(f'Items: {len(items)}')
print(f'Post length: {len(post)}')

# ─── PROCESS EACH ITEM ─────────────────────────────────────────

def get_num(item):
    m = re.search(r'class="num">(\d+)</span>', item)
    return int(m.group(1)) if m else 0

def replace_in_item(item, old, new):
    return item.replace(old, new, 1)

def replace_gap_content(item, new_lines):
    """Replace everything between <div class="epistemic-gap"> and its first </div>"""
    gap_start = item.find('<div class="epistemic-gap">')
    if gap_start < 0:
        return item
    after_gap = item[gap_start + len('<div class="epistemic-gap">'):]
    # Find first </div> that closes the gap
    close_pos = after_gap.find('</div>')
    if close_pos < 0:
        return item
    new_gap = '\n        '.join(new_lines)
    return item[:gap_start + len('<div class="epistemic-gap">')] + '\n        ' + new_gap + '\n        ' + item[gap_start + len('<div class="epistemic-gap">') + close_pos:]

def replace_title_text(item, new_title):
    """Replace the title text inside <span> after num"""
    pattern = r'(<span class="num">\d+</span>\s*<span>)(.*?)(</span>)'
    m = re.search(pattern, item, re.DOTALL)
    if not m:
        return item
    return item[:m.start(2)] + new_title + item[m.end(2):]

def replace_content_text(item, new_text):
    """Replace text inside <div class="accordion-content">...content...</div>"""
    cont_start = item.find('<div class="accordion-content">')
    if cont_start < 0:
        return item
    after_cont = item[cont_start + len('<div class="accordion-content">'):]
    close_pos = after_cont.find('</div>')
    if close_pos < 0:
        return item
    return item[:cont_start + len('<div class="accordion-content">')] + '\n          ' + new_text + '\n        ' + item[cont_start + len('<div class="accordion-content">') + close_pos:]

# ─── CSS IMPROVEMENTS (on pre section) ─────────────────────────

pre = pre.replace('@keyframes fadeIn',
    '''@keyframes gapFadeIn {
    from { opacity:0; transform:translateY(-4px); }
    to { opacity:0.8; transform:translateY(0); }
  }
  @keyframes fadeIn''')

pre = pre.replace(
    '.accordion-item.open .epistemic-gap { opacity:0.8; transform:translateY(0); }',
    '.accordion-item.open .epistemic-gap { animation:gapFadeIn 0.5s ease-out 0.05s forwards; }')

pre = pre.replace('max-height:800px', 'max-height:1200px')
pre = pre.replace('<title>Linguistic Code v18</title>',
    '<title>Linguistic Code v18 — Final Synthesis</title>')

# ─── TITLE CHANGES ─────────────────────────────────────────────
title_changes = {
    6: "Человек — это рекурсивная иерархия, не один процесс.",
    14: "Современные LLM не могут пройти соматическую ловушку. Структурно.",
    20: "Сапир-Уорф — вопрос поставлен неверно.",
    21: "Немой вопрос — это феноменологическая реальность, а не метафора.",
    27: "Валидация ловушки — доказательство существования. Не статистика.",
    30: "Архитектурная нотация — это чертёж, не доказательство.",
}

# ─── GAP ENRICHMENTS ───────────────────────────────────────────
gap_changes = {
    1: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Концептуальная основа:</strong> Гипотеза расширенного сознания (Clark & Chalmers, 1998); нейробиология памяти (Kandel, 2001).',
        '<strong>Эмпирический статус:</strong> Активно обсуждаемая теоретическая рамка.',
        '<strong>Что мы знаем:</strong> Внешние инструменты изменяют когнитивные процессы. Индивидуальная память — структурно изменённая синаптическая сеть (Kandel, 2001).',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Полную архитектуру того, как именно язык функционирует как внешний накопитель на нейронном уровне. Мозг — не компьютер в архитектуре фон Неймана.',
    ],
    2: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Физический артефакт:</strong> Древнегреческие тексты (V–IV вв. до н.э.).',
        '<strong>Эмпирический статус:</strong> Этимологический консенсус (LSJ, Chantraine).',
        '<strong>Что мы знаем:</strong> Idiōtēs = частное лицо, не участвующее в жизни полиса. Прямое значение: «свой собственный», «обособленный».',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Точную дату первого использования в политическом смысле. Нормативная оценка «структурный тупик» — это <strong>интерпретация XXI века</strong>, не античное значение.',
    ],
    3: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Физический артефакт:</strong> Модель производства речи (Levelt, 1989); нейробиология воли (Libet, 1983; Kornhuber & Deecke, 1965).',
        '<strong>Эмпирический статус:</strong> Подтверждённая психолингвистическая модель (Levelt); спорный, но реплицированный феномен (readiness potential).',
        '<strong>Что мы знаем:</strong> Цепочка: концептуализация → лемма → фонологическое кодирование → артикуляция (Levelt, 1989; Friederici, 2017). Readiness potential возникает за ~200 мс до осознанного решения (Libet, 1983).',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Нейронную границу перехода «опыт → мысль». Является ли readiness potential ошибкой предсказания (Friston) или интероцептивным сигналом (insula) — консенсуса нет.',
    ],
    4: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Концептуальная основа:</strong> Серийная обработка речи (Levelt, 1989); теория информации (Shannon, 1948).',
        '<strong>Эмпирический статус:</strong> Подтверждено психолингвистическими экспериментами.',
        '<strong>Что мы знаем:</strong> Язык последовательно сжимает: концептуализация → лемма → фонология → артикуляция (Levelt, 1989; Friederici, 2017). На каждом шаге — структурная потеря.',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Точную меру «семантической потери» при сжатии.',
    ],
    5: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Концептуальная основа:</strong> Предиктивное кодирование (Friston, 2010); воплощённое познание (Varela, Thompson & Rosch, 1991); культурная ниша (Henrich, 2015).',
        '<strong>Эмпирический статус:</strong> Активная исследовательская программа в нейронауках.',
        '<strong>Что мы знаем:</strong> Мозг обрабатывает сигналы иерархически с двунаправленными связями. Триадная модель Маклина (1960-е) — нейромиф (Barrett, 2012; Steffen et al., 2022).',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Точные границы и количество «слоёв»; порог сложности, при котором вид должен изобрести язык.',
    ],
    6: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Концептуальная основа:</strong> Предиктивное кодирование (Friston, 2010); соматические маркеры (Damasio, 1994); интероцепция (Craig, 2002, 2009).',
        '<strong>Эмпирический статус:</strong> Нейрофизиологически подтверждено (mismatch negativity, ERP).',
        '<strong>Что мы знаем:</strong> Prediction error возникает на стыке предсказания и сигнала. Интероцептивная кора (anterior insula, Craig, 2009) регистрирует соматические маркеры (Damasio, 1994).',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Как субъективный опыт «разрыва» соотносится с нейронным паттерном. Ошибка предсказания или интероцептивный сигнал — консенсуса нет.',
    ],
    7: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Концептуальная основа:</strong> Энактивизм (Varela et al., 1991); культурная ниша (Henrich, 2015); 4E cognition (Clark, 2013).',
        '<strong>Эмпирический статус:</strong> Теоретическая позиция с поддержкой из нейропластичности.',
        '<strong>Что мы знаем:</strong> Среда формирует нейронные связи. Вывод = f(H, env, history), H — активный фильтр (Clark, 2013). Культурная ниша конструирует когнитивную среду (Henrich, 2015).',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Точную меру вклада среды vs индивида в конкретный когнитивный акт.',
    ],
    9: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Концептуальная основа:</strong> Расширенное сознание (Clark & Chalmers, 1998); культурная эволюция (Tomasello, 1999; Donald, 1991).',
        '<strong>Эмпирический статус:</strong> Широко поддерживаемая теоретическая позиция.',
        '<strong>Что мы знаем:</strong> Язык позволяет передавать опыт без прямого контакта тел. Танцы пчёл (von Frisch, 1973) — одноразовый буфер. Наскальная живопись Шове (~32 000 лет до н.э.) — первый внешний накопитель опыта вида.',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Точный эволюционный момент, когда коммуникация стала межпоколенческой памятью.',
    ],
    10: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Концептуальная основа:</strong> Социальная эпистемология (Goldman, 1999); entextualization (Silverstein & Urban, 1996).',
        '<strong>Эмпирический статус:</strong> Теоретическая рамка с эмпирической поддержкой.',
        '<strong>Что мы знаем:</strong> Структурное искажение на каждом шаге трансмедиации. Текст отделяется от контекста произнесения (entextualization).',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Количественную меру искажения; степень, при которой искажение становится неприемлемым.',
    ],
    11: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Физический артефакт:</strong> Полевые записи и грамматический анализ.',
        '<strong>Эмпирический статус:</strong> Научный консенсус (Núñez & Sweetser, 2006).',
        '<strong>Что мы знаем:</strong> Аймара маршрутизирует время визуально — «прошлое впереди, будущее позади» (Núñez & Sweetser, 2006). Куук тхаайорре (Boroditsky, 2011) использует абсолютные кардинальные направления.',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Первичная причина или следствие культурного восприятия. Корреляция не есть причинность.',
    ],
    14: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Физический артефакт:</strong> Архитектурные спецификации LLM (transformer, attention).',
        '<strong>Эмпирический статус:</strong> Аналитическое утверждение, не эмпирическое.',
        '<strong>Что мы знаем:</strong> Современные LLM не имеют проприоцептивного слоя, интероцептивной коры, эфферентной обратной связи (Brooks, 1991; Pfeifer & Scheier, 1999).',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Может ли воплощённый ИИ (embodied AI) пройти упрощённую версию ловушки — открытая инженерная проблема.',
    ],
    15: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Физический артефакт:</strong> Текст экрана 0; Bender et al. (2021) «Stochastic Parrots».',
        '<strong>Эмпирический статус:</strong> Структурная честность (мета-утверждение).',
        '<strong>Что мы знаем:</strong> LLM генерирует статистически вероятные токены; не понимает и не чувствует (Bender et al., 2021). Отказ от притворства — operational alignment (Christiano et al., 2017; Gabriel, 2020).',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Является ли «честность» LLM структурным свойством или перформативной позицией.',
    ],
    16: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Физический артефакт:</strong> Núñez & Sweetser (2006); Boroditsky (2011).',
        '<strong>Эмпирический статус:</strong> Подтверждено кросс-лингвистическими исследованиями.',
        '<strong>Что мы знаем:</strong> Аймара — время-пространство (Núñez & Sweetser, 2006). Куук тхаайорре — абсолютные направления (Boroditsky, 2011). Кэйго — социальная дистанция.',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Какие особенности оказывают устойчивое влияние на мышление, а какие — поверхностная форма.',
    ],
    18: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Концептуальная основа:</strong> Неопределённость перевода (Quine, 1960); теория перевода (Venuti, 1995).',
        '<strong>Эмпирический статус:</strong> Широко обсуждаемая проблема.',
        '<strong>Что мы знаем:</strong> Перевод — не замена слов, а перекодирование конфигурации ансамбля. Структурная неопределённость (Quine, 1960).',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Точную меру «непереводимости» для конкретных пар языков.',
    ],
    19: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Концептуальная основа:</strong> Сильная UG (Chomsky; Hauser, Chomsky & Fitch, 2002) vs минимальная (Evans & Levinson, 2009).',
        '<strong>Эмпирический статус:</strong> Открытый теоретический спор.',
        '<strong>Что мы знаем:</strong> Сильная UG (врождённый набор принципов) — не доказана и не опровергнута. Минимальная UG (рекурсия) — более поддерживаема, но спорна.',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Является ли Merge универсалией; есть ли более минимальные операторы.',
    ],
    20: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Концептуальная основа:</strong> Слабая релятивность (Whorf, 1956; Boroditsky, 2011) vs жёсткий детерминизм.',
        '<strong>Эмпирический статус:</strong> Неверно поставлен бинарный вопрос «определяет / не определяет».',
        '<strong>Что мы знаем:</strong> Современные данные поддерживают <strong>ограниченный</strong> эффект языка на мышление в конкретных доменах (цвет, пространство, время).',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Точные механизмы и границы влияния для каждой пары «язык → когнитивная функция».',
    ],
    22: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Концептуальная основа:</strong> Энактивизм (Varela et al., 1991); когнитивная лингвистика (Lakoff & Johnson, 1999).',
        '<strong>Эмпирический статус:</strong> Гипотеза с поддержкой из когнитивной лингвистики.',
        '<strong>Что мы знаем:</strong> Многие (не все) грамматические категории имеют телесное происхождение. Эргативность не имеет очевидного телесного коррелята. Это <strong>гипотеза</strong>, не факт.',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Причинное направление: практика → грамматика или совместно. Универсальность телесного происхождения неизвестна.',
    ],
    24: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Концептуальная основа:</strong> Теория письма (Ong, 1982); entextualization (Silverstein & Urban, 1996).',
        '<strong>Эмпирический статус:</strong> Поддерживается палеографическими данными.',
        '<strong>Что мы знаем:</strong> Письменность — автономная система. Текст существует независимо от доказуемости источника (Codex Argenteus, Коран, Вульфила).',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Истинную интенцию автора; онтологический статус источника.',
    ],
    27: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Эмпирический статус:</strong> Методологическое различение (Popper, 1934; Yin, 2003).',
        '<strong>Что мы знаем:</strong> n=1 достаточно для доказательства <strong>существования</strong> феномена. n>30 — для оценки <strong>распространённости</strong>. Две разные цели.',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Какую из этих целей преследует проект — v18 различает их, но окончательный выбор за автором.',
    ],
    29: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Физический артефакт:</strong> Web Storage API (W3C).',
        '<strong>Эмпирический статус:</strong> Технический факт с оговорками.',
        '<strong>Что мы знаем:</strong> localStorage — per-origin, не отправляется на сервер. JS того же origin может читать. Данные не зашифрованы.',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Долговременную стабильность. <strong>Threat model:</strong> XSS-атака может прочитать localStorage. Privacy без threat model — плохая эпистемология.',
    ],
    30: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Эмпирический статус:</strong> Архитектурная нотация, не формальная модель.',
        '<strong>Что мы знаем:</strong> ⊥ — псевдо-математическая метафора. bridge() не определена. δ и f не имеют доменов. LC(H,F) — чертёж, не модель.',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Формальной семантики не существует. Можно ли формализовать «щелчок» — на данный момент нет.',
    ],
    33: [
        '<span class="gap-title">Эпистемический статус</span>',
        '<strong>Эмпирический статус:</strong> Технический факт с одной оговоркой.',
        '<strong>Что мы знаем:</strong> Весь HTML, CSS, JS — в одном файле. Нет серверных вызовов. Нет трекинга. После загрузки шрифтов (Google Fonts) работает офлайн.',
        '<strong>Что мы <span class="unknown">НЕ знаем</span>:</strong> Что произойдёт через 10 лет, если Google Fonts изменит API. Полная автономия требует base64-встраивания шрифтов (~500 КБ).',
    ],
}

content_changes = {
    24: 'Письменность — не «записанная речь». Отдельный протез с собственной логикой. Опыт → мысль → слово → письмо → печать → цифровой текст — на каждом шаге новое средство. Codex Argenteus (IV в.) и Коран (VII в.) существуют независимо от доказуемости авторства. Текст отделяется от тела-автора и живёт по правилам медиума.',
    25: 'Цепочка сжатия: опыт → мысль → слово → письмо → печать → цифровой текст. На каждом шаге — потеря. Степень удаления от первичного опыта увеличивается. Этот HTML — пятый или шестой уровень сжатия.',
}

# ─── APPLY CHANGES ─────────────────────────────────────────────
processed = []
for item in items:
    num = get_num(item)
    
    # Title
    if num in title_changes:
        item = replace_title_text(item, title_changes[num])
    
    # Gap
    if num in gap_changes:
        item = replace_gap_content(item, gap_changes[num])
    
    # Content
    if num in content_changes:
        item = replace_content_text(item, content_changes[num])
    
    processed.append(item)

# ─── ASSEMBLE ───────────────────────────────────────────────────
final_html = pre + '<div class="accordion-item">' + '<div class="accordion-item">'.join(processed) + post

# ─── VALIDATION ─────────────────────────────────────────────────

# P0: No Хопи
hopi = len(re.findall(r'Хопи|хопи|Hop[iі]', final_html, re.IGNORECASE))
print(f'P0 — Хопи: {hopi} (must be 0)')
assert hopi == 0

# P1: MacLean as critique
mc = re.findall(r'MacLean|Маклин', final_html)
print(f'P1 — MacLean: {len(mc)} (in critique context)')

# Thesis count
tc = len(re.findall(r'class="accordion-item"', final_html))
print(f'Theses: {tc} (must be 33)')
assert tc == 33

# Content div count
cc = len(re.findall(r'class="accordion-content"', final_html))
print(f'Content divs: {cc} (must be 33)')

# Gap count
gc = len(re.findall(r'class="epistemic-gap"', final_html))
print(f'Gap divs: {gc} (must be 33)')

# Size
print(f'Size: {len(final_html)} bytes ({len(final_html)/1024:.1f} KB)')

# ─── WRITE ──────────────────────────────────────────────────────
output = '/home/z/my-project/download/linguistic-code-v18-final.html'
with open(output, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f'Written: {output}')
print('Done.')
