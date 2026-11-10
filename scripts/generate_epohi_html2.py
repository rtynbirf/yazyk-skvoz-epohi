#!/usr/bin/env python3
"""
Generate Epohti_jazyka.html — 7 epochs, each with its OWN typographic era.
Antiquity gets Cinzel, Middle Ages gets blackletter, etc.
Linguistic Code dark aesthetic, left nav rail, mobile responsive.
"""

epochs = [
    {
        "id": "antiquity",
        "num": "I",
        "title": "Античность",
        "subtitle": "Логос и природа имени",
        "period": "VIII в. до н.э. — V в. н.э.",
        "font_class": "era-antiquity",
        "paragraphs": [
            "Древние эллины полагали, что речь человека не есть нечто произвольное: она либо тянется от самой природы вещей, либо устанавливается людьми через соглашение. В диалоге Платона «Кратил» герменевты спорят: даны ли имена от природы, так что каждая вещь носит верное имя по своему естеству, или же люди наложили имена по своему усмотрению, как налагают клеймо на сосуд? Гераклит ещё раньше утверждал, что логос — общий для всех — уподобляется вечному огню, мерно вспыхивающему и мерно угасающему. Логос для досократиков — не слово в нашем смысле, но первоосновное начало, которому подчинено всё сущее.",
            "Аристотель в трактате «Об истолковании» положил, что звуки голоса суть знаки аффектов души, а письмена — знаки звуков голоса. Но аффекты души — те же у всех, а звуки — различны в зависимости от народа. Таким образом, античная мысль установила тройное соответствие: вещь — страсть души — голос — буква. Стоики развили это учение: они различали \u03bb\u03b5\u03ba\u03c4\u03cc\u03bd, то есть сказуемое содержание, от самого звука. Голос пропадает, лектон остаётся — так стоики впервые разделили то, что произносится, от того, что мыслится.",
            "Риторика и диалектика составляли два главных искусства слова. Риторика учила убеждать в суде и в народном собрании, диалектика — вести спор посредством вопросов и ответов. И то, и другое опирались на \u03c4\u03cc\u03c0\u03bf\u03b9, общие места, из которых черпаются доводы. Слово было не инструментом передачи мыслей, но действием, способным менять душу слушателя. Софисты первыми поняли, что слово может быть сильнее меча, и за это Платон не простил им до конца своих дней.",
        ],
        "quote": "Слова суть подражания вещам — или по природе, или по установлению.",
        "names": "Гераклит \u00b7 Платон \u00b7 Аристотель \u00b7 стоики",
    },
    {
        "id": "middle-ages",
        "num": "II",
        "title": "Средние века",
        "subtitle": "Знак, отпечаток и воля Творца",
        "period": "V — XV вв.",
        "font_class": "era-medieval",
        "paragraphs": [
            "Когда христианское откровение стало главной опорой мысли, вопрос о языке переместился из сферы природы в сферу воли. Блаженный Августин в трактате «О учителе» положил, что слова суть знаки, указывающие на вещи, но сами по себе они лишь побуждают душу обратиться к вещам, которые она уже знает. Никто не учит через слова, если душа не имеет внутри себя того, к чему слова лишь прикасаются. Это замечание сделало средневековую мысль глубоко интроспективной: язык стал рассматриваться как движение души, ищущей вещь в самой себе.",
            "Схоласты построили грандиозное учение о знаке. Знак, по их определению, есть нечто, что сверх своей собственной формы явно понуждает душу к познанию чего-то иного. Фома Аквинский разделил знаки на естественные, которые суть следы вещей (как дым от огня), и намеренные, которые человек ставит ради указания. Модисты — философы грамматики — развили учение о способах означивания, modi significandi, которые присущи каждому слову и делают его способным означать. Они верили, что грамматические категории отражают реальные свойства вещей, так что структура латинской речи отражает устройство бытия.",
            "Особое место занимал спор об универсалиях: существуют ли общие имена в вещах, лишь в уме, или отдельно от того и другого? Реалисты утверждали, что род и вид имеют подлинное бытие; номиналисты, от Росцелина до Оккама, настаивали, что лишь единичные вещи реальны, а общие имена — лишь flatus vocis, дыхание голоса. Этот спор определил всю средневековую философию языка: имя стало полем битвы между онтологией и логикой, между верой в реальность общих понятий и радикальным эмпиризмом.",
        ],
        "quote": "Слова суть знаки, побуждающие душу к познанию того, что она уже хранит.",
        "names": "Августин \u00b7 Фома Аквинский \u00b7 модисты \u00b7 Оккам",
    },
    {
        "id": "early-modern",
        "num": "III",
        "title": "Раннее Новое время",
        "subtitle": "От голоса к разуму",
        "period": "XV — XVII вв.",
        "font_class": "era-early-modern",
        "paragraphs": [
            "Когда рукопечатные книги стали распространяться по Европе, латынь утратила монополию на учёную речь. Лоренцо Валла в XV веке доказал, что изящная латынь Цицерона не есть язык церкви, и что каждый народ имеет право говорить и мыслить на своём наречии. Этьен Доле перевёл Платона на французский и заявил, что философия не нуждается в латыни, если мысль ясна. Так началось великое расслоение: язык стал одновременно объектом гордости национальной и инструментом познания всеобщего.",
            "Фрэнсис Бэкон в «Новом Органоне» провозгласил, что слова, как правило, искажают мысль: они навязывают разуму ложные сходства и мешают созерцанию природы. Язык, по Бэкону, — идолы площади, общие заблуждения, коренящиеся в словах. Декарт в «Размышлениях» пошёл дальше: он усомнился в том, что слова вообще способны выражать мысль адекватно, и потому искал всеобщую науку, построенную на ясных идеях, а не на словах. Лейбниц, напротив, верил, что можно построить characteristica universalis — искусственный язык, в котором каждый знак будет однозначно соответствовать простой идее, и тогда всякий спор разрешится путём исчисления.",
            "Джон Локк в «Опыте о человеческом разумении» положил, что слова суть чувственно воспринимаемые знаки идей, а идеи — то, что душа обнаруживает внутри себя при размышлении. Слова не обозначают вещи непосредственно, но лишь постольку, поскольку они суть знаки идей в голове говорящего. Общность языка покоится не на сходстве имён с вещами, но на том, что люди произвольно соединяют определённые звуки с определёнными идеями. Локк первым чётко разделил значение слова (идея) и вещь, к которой оно отсылает, и этим навсегда изменил вопрос о языке.",
        ],
        "quote": "Слова суть чувственно воспринимаемые знаки внутренних идей.",
        "names": "Валла \u00b7 Бэкон \u00b7 Декарт \u00b7 Локк \u00b7 Лейбниц",
    },
    {
        "id": "enlightenment",
        "num": "IV",
        "title": "Просвещение",
        "subtitle": "Чувство, разум и происхождение речи",
        "period": "XVIII в.",
        "font_class": "era-enlightenment",
        "paragraphs": [
            "Век разума обратился к вопросу, которого древние почти не касались: как зародилась речь? Этьен Бонно де Кондильяк в «Опыте о происхождении человеческих знаний» предположил, что язык родился из естественных жестов и криков. Два детей, растущие в одиночестве, начнут с мимики и возгласов, затем перейдут к произвольным знакам, а оттуда — к языку. Кондильяк утверждал, что язык не был изобретён раз и навсегда, но развивался постепенно, подобно тому как ребёнок учится говорить. Анализ и m\u00e9thode — вот инструменты, благодаря которым язык совершенствовался от грубых криков к сложным конструкциям.",
            "Жан-Жак Руссо в «Рассуждении о происхождении и основаниях неравенства» и в «Опыте о происхождении языков» утверждал нечто иное: первые языки были не аналитическими, но певучими, наполненными страстью и образами. Прежде чем человек стал доказывать, он пел; прежде чем рассуждать, он чувствовал. По Руссо, потребность породила первые жесты, а страсть — первые слова. Иоганн Готфрид Гердер в трактате «О происхождении языка» пошёл ещё дальше: он отверг как божественное откровение, так и чисто рассудочное изобретение. Язык, по Гердеру, — медленно выработанное средство познания, тесно связанное с чувственным опытом и с сознательной деятельностью человека.",
            "Просвещение создало общую грамматику — учение о всеобщих принципах, лежащих в основе каждого языка. Грамматисты Порт-Рояля утверждали, что всякое proposition, то есть суждение, состоит из субъекта, атрибута и связки, и что эта структура отражает саму структуру мысли. Они полагали, что грамматические категории суть не произвольные условности, но необходимые формы, в которых разум артикулирует свои идеи. Эта вера в универсальную логику речи определила всю последующую лингвистику вплоть до XX века.",
        ],
        "quote": "Страстям мы обязаны первыми словами, а потребностям — первыми жестами.",
        "names": "Кондильяк \u00b7 Руссо \u00b7 Гердер \u00b7 грамматисты Порт-Рояля",
    },
    {
        "id": "nineteenth",
        "num": "V",
        "title": "XIX век",
        "subtitle": "Родство языков и дух народа",
        "period": "XIX в.",
        "font_class": "era-nineteenth",
        "paragraphs": [
            "Когда Франц Бопп в 1816 году опубликовал «Сравнительное спряжение», он доказал, что санскрит, латинский, греческий, германские и кельтские языки восходят к общему предку. Это открытие изменило всё: язык перестал быть лишь орудием мысли и стал историческим памятником, живым свидетелем перемещений народов. Якоб Гримм сформулировал свой знаменитый закон о чередовании согласных, и сравнительное языкознание превратилось в строгую дисциплину, способную восстанавливать формы, которые никогда не были записаны.",
            "Вильгельм фон Гумбольдт в сочинении «О различии строения человеческих языков» высказал мысль, что язык не есть продукт, но деятельность. Каждый язык есть органическое целое, обладающее внутренней формой — особым способом, которым народ членит мир и придаёт ему словесную плоть. Дух народа и его язык нераздельны: язык есть орган внутреннего, а не внешнего бытия народа. Гумбольдт утверждал, что изучать язык — значит не описывать его правила, но постигать мировоззрение народа, им владеющего.",
            "В России Александр Афанасьевич Потебня развивал идеи Гумбольдта: он утверждал, что слово есть не знак вещи, а средство создания образа. Слово делится на внешнюю форму, звучание, и внутреннюю, его значение, причём внутренняя форма есть образ, посредством которого народ понимает сущность вещи. Эта мысль стала основой русской лингвистической традиции и одновременно питала литературную критику и поэтику. Язык в XIX веке впервые предстал не как инструмент, но как существо, живущее по собственным законам, растущее и ветвящееся подобно дереву.",
        ],
        "quote": "Язык не есть продукт деятельности, но сама деятельность духа.",
        "names": "Бопп \u00b7 Гримм \u00b7 Гумбольдт \u00b7 Потебня",
    },
    {
        "id": "twentieth",
        "num": "VI",
        "title": "XX век",
        "subtitle": "Знак, система и порождающее устройство",
        "period": "XX в.",
        "font_class": "era-twentieth",
        "paragraphs": [
            "Фердинанд де Соссюр в «Женевских лекциях» совершил переворот, равного которому лингвистика не знала со времён Аристотеля. Он разделил язык на две неравные части: язык как систему знаков и речь как индивидуальный акт. Язык существует в коллективе и не зависит от воли говорящего; речь есть осуществление этой системы в конкретном высказывании. Знак, по Соссюру, состоит из означающего и означаемого, и связь между ними произвольна. Это значит: нет никакого естественного родства между звуком и смыслом — оно установлено обществом.",
            "Соссюр также разделил изучение языка на синхронию и диахронию: первая рассматривает систему в данный момент, вторая — её изменения во времени. Он утверждал, что синхрония должна предшествовать диахронии, так как говорящий не сознаёт исторических изменений. Значение каждого знака определяется не его собственной природой, но его положением в системе, его отношением к другим знакам. Лингвистика стала наукой о системах: языки — как кристаллы, каждый с собственной структурой, каждый — целое по своим правилам.",
            "Во второй половине века Ноам Хомский превратил лингвистику в раздел когнитивной науки. Он предложил различать компетенцию, знание языка, и употребление, то есть практическое владение. Компетенция описывается порождающей грамматикой — конечным набором правил, способным производить бесконечное множество предложений. Глубинная структура предложения, его подлинная форма, трансформируется в поверхностную посредством правил перестановки, удаления и вставки. Хомский доказал, что ребёнок способен усвоить язык лишь потому, что врождённые структуры мозга уже содержат универсальную грамматику.",
        ],
        "quote": "Язык — это система знаков, выражающих идеи.",
        "names": "Соссюр \u00b7 Хомский",
    },
    {
        "id": "twentyfirst",
        "num": "VII",
        "title": "Конец XX — XXI век",
        "subtitle": "Тело, мозг и предсказание",
        "period": "конец XX — начало XXI в.",
        "font_class": "era-twentyfirst",
        "paragraphs": [
            "Когнитивная революция 1970\u20131980-х годов вернула языку его тело. Джордж Лакофф в книге «Женщины, огонь и опасные вещи» доказал, что человеческие категории строятся не по формальной логике, но на основе телесного опыта, метафор и прототипов. Мы не мыслим абстрактными символами — мы мыслим телом. Понятия — аргумент, время, состояние понимаются через метафоры: спора как войны, времени как движения, состояния как контейнера. Эти метафоры не украшение речи, а основа мышления, коренящаяся в том, как наше тело взаимодействует с миром.",
            "Одновременно нейробиология показала, что язык не локализован в одной зоне мозга, но распределён по обширным сетям. Антонио Дамасио выдвинул гипотезу соматического маркера: каждое решение, каждое высказывание сопровождается телесным ощущением, которое направляет выбор слов и конструкций. Лиза Фельдман Барретт показала, что эмоции не есть врождённые реакции, но предсказания мозга, основанные на интероцепции — непрерывном считывании состояния тела. Язык, следовательно, есть не кодирование мыслей в звуки, а непрерывное действие тела, стремящегося минимизировать разницу между ожиданием и ощущением.",
            "Карл Фристон сформулировал принцип свободной энергии: мозг постоянно строит модель мира и обновляет её, чтобы предсказывать входящие сигналы. Язык в этой картине — не средство передачи информации, а один из каналов, через который мозг снижает неопределённость. Говорящий не кодирует готовую мысль в слова — он совершает телесное действие, направленное на изменение состояний другого тела. Слушающий не декодирует слова — он использует их как сигналы для обновления собственной предиктивной модели. Язык вернулся к тому, с чего начинал у Гераклита: он есть действие, событие, развёртывающееся между телами, а не вещь, которую можно передать из головы в голову.",
        ],
        "quote": "Язык есть не код, но действие тела, направленное на другой мир.",
        "names": "Лакофф \u00b7 Дамасио \u00b7 Барретт \u00b7 Фристон",
    },
]

nav_html = ""
for e in epochs:
    eid = e['id']
    nav_html += '    <a href="#' + eid + '" class="nav-link" data-target="' + eid + '">\n'
    nav_html += '      <span class="nav-num">' + e['num'] + '</span>\n'
    nav_html += '      <span class="nav-label">' + e['title'] + '</span>\n'
    nav_html += '    </a>\n'

sections_html = ""
for e in epochs:
    fc = e['font_class']
    paras = ""
    for p in e['paragraphs']:
        paras += '      <p>' + p + '</p>\n'
    quote_str = '    <blockquote>' + e['quote'] + '</blockquote>\n'
    sections_html += '  <section id="' + e['id'] + '" class="epoch-section ' + fc + '">\n'
    sections_html += '    <div class="epoch-header">\n'
    sections_html += '      <span class="epoch-num">' + e['num'] + '</span>\n'
    sections_html += '      <h2 class="epoch-title">' + e['title'] + '</h2>\n'
    sections_html += '      <p class="epoch-subtitle">' + e['subtitle'] + '</p>\n'
    sections_html += '      <span class="epoch-period">' + e['period'] + '</span>\n'
    sections_html += '    </div>\n'
    sections_html += '    <div class="epoch-body">\n'
    sections_html += paras
    sections_html += quote_str
    sections_html += '      <p class="epoch-names">' + e['names'] + '</p>\n'
    sections_html += '    </div>\n'
    sections_html += '  </section>\n\n'

html_out = '''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Язык сквозь эпохи</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=UnifrakturMaguntia&family=EB+Garamond:ital,wght@0,400;0,600;1,400&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lora:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500&family=JetBrains+Mono:wght@300;400&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

  :root {
    --bg: #0E1011; --surface: #16181B; --surface-2: #1C1F23;
    --text: #D4D0C8; --text-dim: #7A7770; --text-faint: #4A4843;
    --gold: #C6A85B; --gold-dim: #8B7A44;
    --gold-faint: rgba(198,168,91,0.08);
  }

  html { scroll-behavior: smooth; }
  body {
    background: var(--bg); color: var(--text);
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-weight: 400; line-height: 1.7; overflow-x: hidden;
  }

  /* ============================================
     EPOCH-SPECIFIC TYPOGRAPHY
     ============================================ */

  /* I. ANTIQUITY — Roman inscriptions, all-caps dignity */
  .era-antiquity .epoch-title {
    font-family: 'Cinzel', serif;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
    font-size: clamp(20px, 2.8vw, 28px);
  }
  .era-antiquity .epoch-subtitle {
    font-family: 'Cinzel', serif;
    font-weight: 400;
    font-style: normal;
    letter-spacing: 1px;
  }
  .era-antiquity .epoch-num {
    font-family: 'Cinzel', serif;
    letter-spacing: 6px;
    font-size: 10px;
  }
  .era-antiquity .epoch-body p {
    font-family: 'EB Garamond', 'Times New Roman', serif;
    font-size: clamp(17px, 1.8vw, 19px);
    line-height: 1.9;
  }
  .era-antiquity blockquote {
    font-family: 'Cinzel', serif;
    font-style: normal;
    letter-spacing: 1px;
    font-size: clamp(14px, 1.5vw, 16px);
    text-transform: uppercase;
  }
  .era-antiquity .epoch-period {
    font-family: 'Cinzel', serif;
    letter-spacing: 2px;
    text-transform: uppercase;
  }

  /* II. MIDDLE AGES — Gothic blackletter / manuscript */
  .era-medieval .epoch-title {
    font-family: 'UnifrakturMaguntia', blackletter, serif;
    font-weight: 400;
    font-size: clamp(26px, 3.5vw, 38px);
    letter-spacing: 1px;
  }
  .era-medieval .epoch-subtitle {
    font-family: 'EB Garamond', serif;
    font-style: italic;
    font-size: 16px;
  }
  .era-medieval .epoch-num {
    font-family: 'EB Garamond', serif;
    font-variant: small-caps;
    letter-spacing: 4px;
    font-size: 13px;
  }
  .era-medieval .epoch-body p {
    font-family: 'EB Garamond', 'Palatino Linotype', serif;
    font-size: clamp(17px, 1.8vw, 19px);
    line-height: 1.95;
    text-align: justify;
    hyphens: auto;
  }
  .era-medieval blockquote {
    font-family: 'EB Garamond', serif;
    font-style: italic;
    font-size: clamp(15px, 1.6vw, 17px);
  }
  .era-medieval .epoch-period {
    font-family: 'EB Garamond', serif;
    font-variant: small-caps;
  }

  /* III. EARLY MODERN — Humanist, Aldine press, Garamond */
  .era-early-modern .epoch-title {
    font-family: 'EB Garamond', serif;
    font-weight: 600;
    font-size: clamp(24px, 3.2vw, 34px);
    font-style: italic;
  }
  .era-early-modern .epoch-subtitle {
    font-family: 'EB Garamond', serif;
    font-style: italic;
    font-size: 17px;
    color: var(--text-dim);
  }
  .era-early-modern .epoch-num {
    font-family: 'EB Garamond', serif;
    font-size: 13px;
    font-variant: small-caps;
    letter-spacing: 3px;
  }
  .era-early-modern .epoch-body p {
    font-family: 'EB Garamond', 'Times New Roman', serif;
    font-size: clamp(17px, 1.8vw, 19px);
    line-height: 1.9;
  }
  .era-early-modern blockquote {
    font-family: 'EB Garamond', serif;
    font-style: italic;
    font-size: clamp(15px, 1.6vw, 17px);
  }
  .era-early-modern .epoch-period {
    font-family: 'EB Garamond', serif;
    font-variant: small-caps;
  }

  /* IV. ENLIGHTENMENT — Didone / Bodoni, high contrast */
  .era-enlightenment .epoch-title {
    font-family: 'Playfair Display', 'Didot', serif;
    font-weight: 700;
    font-size: clamp(24px, 3.2vw, 34px);
    letter-spacing: 1px;
  }
  .era-enlightenment .epoch-subtitle {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-weight: 400;
    font-size: 17px;
  }
  .era-enlightenment .epoch-num {
    font-family: 'Playfair Display', serif;
    font-size: 11px;
    letter-spacing: 4px;
    font-weight: 400;
  }
  .era-enlightenment .epoch-body p {
    font-family: 'Playfair Display', 'Georgia', serif;
    font-size: clamp(16px, 1.7vw, 18px);
    line-height: 1.85;
    font-weight: 400;
  }
  .era-enlightenment blockquote {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-weight: 400;
    font-size: clamp(15px, 1.6vw, 17px);
  }
  .era-enlightenment .epoch-period {
    font-family: 'Playfair Display', serif;
    font-size: 11px;
    letter-spacing: 2px;
  }

  /* V. 19TH CENTURY — Transitional, readable, industrial press */
  .era-nineteenth .epoch-title {
    font-family: 'Lora', serif;
    font-weight: 600;
    font-size: clamp(22px, 3vw, 30px);
  }
  .era-nineteenth .epoch-subtitle {
    font-family: 'Lora', serif;
    font-style: italic;
    font-size: 16px;
  }
  .era-nineteenth .epoch-num {
    font-family: 'Lora', serif;
    font-size: 11px;
    letter-spacing: 3px;
    font-weight: 400;
  }
  .era-nineteenth .epoch-body p {
    font-family: 'Lora', 'Georgia', serif;
    font-size: clamp(16px, 1.7vw, 18px);
    line-height: 1.85;
  }
  .era-nineteenth blockquote {
    font-family: 'Lora', serif;
    font-style: italic;
    font-size: clamp(15px, 1.5vw, 17px);
  }
  .era-nineteenth .epoch-period {
    font-family: 'Lora', serif;
    font-size: 11px;
    letter-spacing: 1px;
  }

  /* VI. 20TH CENTURY — Swiss grotesk, sans-serif, grid */
  .era-twentieth .epoch-title {
    font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
    font-weight: 500;
    font-size: clamp(22px, 3vw, 30px);
    letter-spacing: -0.5px;
  }
  .era-twentieth .epoch-subtitle {
    font-family: 'Inter', sans-serif;
    font-style: normal;
    font-size: 15px;
    font-weight: 300;
    letter-spacing: 0.5px;
  }
  .era-twentieth .epoch-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    font-weight: 400;
  }
  .era-twentieth .epoch-body p {
    font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
    font-size: clamp(15px, 1.5vw, 17px);
    line-height: 1.8;
    font-weight: 300;
  }
  .era-twentieth blockquote {
    font-family: 'Inter', sans-serif;
    font-style: normal;
    font-weight: 400;
    font-size: clamp(14px, 1.4vw, 16px);
    letter-spacing: 0.3px;
  }
  .era-twentieth .epoch-period {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
  }

  /* VII. 21ST CENTURY — Monospace, code, technical */
  .era-twentyfirst .epoch-title {
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    font-weight: 400;
    font-size: clamp(18px, 2.5vw, 24px);
    letter-spacing: 1px;
  }
  .era-twentyfirst .epoch-subtitle {
    font-family: 'Inter', sans-serif;
    font-style: normal;
    font-size: 14px;
    font-weight: 300;
    color: var(--text-dim);
  }
  .era-twentyfirst .epoch-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 4px;
  }
  .era-twentyfirst .epoch-body p {
    font-family: 'Inter', 'Helvetica Neue', sans-serif;
    font-size: clamp(15px, 1.5vw, 17px);
    line-height: 1.8;
    font-weight: 300;
  }
  .era-twentyfirst blockquote {
    font-family: 'JetBrains Mono', monospace;
    font-style: normal;
    font-size: clamp(13px, 1.3vw, 15px);
    letter-spacing: 0.5px;
    opacity: 0.8;
  }
  .era-twentyfirst .epoch-period {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
  }
  .era-twentyfirst .epoch-names {
    font-family: 'JetBrains Mono', monospace;
  }

  /* ============================================
     SHARED LAYOUT
     ============================================ */

  .page { display: flex; min-height: 100vh; }

  /* NAV RAIL */
  .nav-rail {
    position: fixed; left: 0; top: 0; bottom: 0; width: 200px;
    background: var(--surface);
    border-right: 1px solid var(--gold-faint);
    display: flex; flex-direction: column;
    padding: 40px 0; z-index: 100;
    transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }
  .nav-rail-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 15px; font-weight: 600;
    color: var(--gold); letter-spacing: 0.5px;
    padding: 0 24px 32px;
    border-bottom: 1px solid var(--gold-faint);
    margin-bottom: 24px;
  }
  .nav-link {
    display: flex; align-items: baseline; gap: 10px;
    padding: 10px 24px; text-decoration: none;
    color: var(--text-dim); transition: all 0.25s ease;
    border-left: 2px solid transparent;
  }
  .nav-link:hover { color: var(--text); background: var(--gold-faint); }
  .nav-link.active {
    color: var(--gold); border-left-color: var(--gold);
    background: var(--gold-faint);
  }
  .nav-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px; font-weight: 400;
    min-width: 18px; opacity: 0.5;
  }
  .nav-link.active .nav-num { opacity: 1; color: var(--gold); }
  .nav-label {
    font-family: 'Inter', sans-serif;
    font-size: 12px; letter-spacing: 0.3px;
  }

  /* MOBILE BAR */
  .mobile-bar {
    display: none; position: fixed; top: 0; left: 0; right: 0;
    height: 52px; background: var(--surface);
    border-bottom: 1px solid var(--gold-faint);
    z-index: 200; align-items: center;
    padding: 0 16px; gap: 12px;
  }
  .mobile-bar-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 14px; font-weight: 600; color: var(--gold);
  }
  .mobile-bar-open {
    background: none; border: none; color: var(--text-dim);
    font-size: 20px; cursor: pointer; padding: 4px 8px; margin-left: auto;
  }
  .mobile-overlay {
    display: none; position: fixed; inset: 0;
    background: rgba(0,0,0,0.6); z-index: 150;
    opacity: 0; transition: opacity 0.3s ease;
  }
  .mobile-overlay.open { opacity: 1; }

  /* CONTENT */
  .content {
    margin-left: 200px; flex: 1;
    max-width: 720px; padding: 80px 48px 120px;
  }

  /* PAGE TITLE */
  .page-title-block {
    margin-bottom: 72px; padding-bottom: 48px;
    border-bottom: 1px solid var(--gold-faint);
  }
  .page-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(28px, 4vw, 42px);
    font-weight: 600; color: var(--text);
    line-height: 1.3; margin-bottom: 16px;
  }
  .page-subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 14px; color: var(--text-dim); letter-spacing: 0.5px;
  }
  .page-english {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px; letter-spacing: 3px;
    color: var(--text-faint); text-transform: uppercase; margin-top: 20px;
  }

  /* EPOCH SECTIONS (shared structure) */
  .epoch-section {
    margin-bottom: 80px;
    opacity: 0; transform: translateY(20px);
    transition: opacity 0.6s ease, transform 0.6s ease;
  }
  .epoch-section.visible { opacity: 1; transform: translateY(0); }

  .epoch-header {
    margin-bottom: 32px; padding-bottom: 24px;
    border-bottom: 1px solid rgba(198,168,91,0.1);
  }
  .epoch-num {
    display: block; margin-bottom: 8px;
    color: var(--gold-dim);
  }
  .epoch-title {
    color: var(--text); line-height: 1.3; margin-bottom: 6px;
  }
  .epoch-subtitle { color: var(--text-dim); margin-bottom: 12px; }
  .epoch-period { color: var(--text-faint); }

  .epoch-body p {
    color: var(--text); margin-bottom: 20px; text-align: justify;
  }
  .epoch-body blockquote {
    margin: 32px 0; padding: 20px 0 20px 24px;
    border-left: 2px solid var(--gold-dim);
    color: var(--text-dim); line-height: 1.7;
  }
  .epoch-names {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px; letter-spacing: 1px;
    color: var(--text-faint); margin-top: 32px;
    padding-top: 20px; border-top: 1px solid rgba(198,168,91,0.06);
  }

  /* RESPONSIVE */
  @media (max-width: 860px) {
    .nav-rail { transform: translateX(-100%); width: 240px; }
    .nav-rail.open { transform: translateX(0); }
    .mobile-bar { display: flex; }
    .mobile-overlay.open { display: block; }
    .content { margin-left: 0; padding: 72px 24px 100px; max-width: 100%; }
    .page-title-block { margin-bottom: 48px; padding-bottom: 32px; }
    .epoch-section { margin-bottom: 56px; }
  }

  /* SCROLLBAR */
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: var(--bg); }
  ::-webkit-scrollbar-thumb { background: var(--surface-2); border-radius: 3px; }
  ::-webkit-scrollbar-thumb:hover { background: var(--text-faint); }

  /* REDUCED MOTION */
  @media (prefers-reduced-motion: reduce) {
    .epoch-section { opacity: 1; transform: none; transition: none; }
    html { scroll-behavior: auto; }
    .nav-rail, .mobile-overlay { transition: none; }
  }
</style>
</head>
<body>

<div class="mobile-bar">
  <span class="mobile-bar-title">Эпохи</span>
  <button class="mobile-bar-open" id="menuBtn" aria-label="Навигация">&#9776;</button>
</div>
<div class="mobile-overlay" id="overlay"></div>

<div class="page">
  <nav class="nav-rail" id="navRail" aria-label="Навигация по эпохам">
    <div class="nav-rail-title">Эпохи</div>
''' + nav_html + '''  </nav>

  <main class="content">
    <div class="page-title-block">
      <h1 class="page-title">Язык сквозь эпохи</h1>
      <p class="page-subtitle">Семь эпох языковой мысли — каждая своим шрифтом</p>
      <p class="page-english">Language Through the Ages</p>
    </div>

''' + sections_html + '''  </main>
</div>

<script>
  const menuBtn = document.getElementById('menuBtn');
  const navRail = document.getElementById('navRail');
  const overlay = document.getElementById('overlay');
  function openMenu() { navRail.classList.add('open'); overlay.classList.add('open'); }
  function closeMenu() { navRail.classList.remove('open'); overlay.classList.remove('open'); }
  menuBtn.addEventListener('click', () => {
    navRail.classList.contains('open') ? closeMenu() : openMenu();
  });
  overlay.addEventListener('click', closeMenu);
  document.querySelectorAll('.nav-link').forEach(l => l.addEventListener('click', closeMenu));

  const secs = document.querySelectorAll('.epoch-section');
  const links = document.querySelectorAll('.nav-link');
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        const id = e.target.id;
        links.forEach(l => l.classList.remove('active'));
        const a = document.querySelector('.nav-link[data-target="' + id + '"]');
        if (a) a.classList.add('active');
      }
    });
  }, { rootMargin: '-20% 0px -60% 0px' });
  secs.forEach(s => obs.observe(s));

  const fadeObs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('visible'); fadeObs.unobserve(e.target); }
    });
  }, { threshold: 0.1 });
  secs.forEach(s => fadeObs.observe(s));
</script>
</body>
</html>'''

output_path = "/home/z/my-project/download/Epohti_jazyka.html"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_out)
print(f"Saved: {output_path}")
print(f"Size: {len(html_out)} chars")
