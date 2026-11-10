const {
  Document, Packer, Paragraph, TextRun, Header, Footer,
  AlignmentType, HeadingLevel, PageNumber, PageOrientation,
  BorderStyle, ShadingType, Table, TableRow, TableCell,
  TableLayoutType, WidthType, TabStopType, TabStopPosition,
  TableOfContents, NumberFormat, SectionType, Break
} = require("docx");
const fs = require("fs");

// ============================================================
// UTILITIES FROM design-system.md
// ============================================================

function splitTitleLines(title, charsPerLine) {
  if (title.length <= charsPerLine) return [title];
  const breakAfter = new Set([
    ...",.!?", " ", "-", ":", ";"
  ]);
  const breakBefore = new Set([]);
  const lines = [];
  let remaining = title;
  while (remaining.length > 0) {
    if (remaining.length <= charsPerLine) {
      lines.push(remaining);
      break;
    }
    let breakIdx = -1;
    const searchEnd = Math.min(remaining.length - 1, Math.floor(charsPerLine * 1.3));
    for (let i = Math.floor(charsPerLine * 0.6); i <= searchEnd; i++) {
      if (breakAfter.has(remaining[i]) && i + 1 < remaining.length) {
        breakIdx = i + 1;
      }
    }
    if (breakIdx === -1) breakIdx = charsPerLine;
    lines.push(remaining.slice(0, breakIdx).trimEnd());
    remaining = remaining.slice(breakIdx).trimStart();
  }
  if (lines.length > 1) {
    const last = lines[lines.length - 1];
    if (last.length <= 2) {
      lines[lines.length - 2] += " " + last;
      lines.pop();
    }
  }
  return lines;
}

function calcTitleLayout(title, maxWidthTwips, preferredPt = 40, minPt = 24) {
  const charWidth = (pt) => pt * 20;
  const charsPerLine = (pt) => Math.floor(maxWidthTwips / charWidth(pt));
  let titlePt = preferredPt;
  let lines;
  while (titlePt >= minPt) {
    const cpl = charsPerLine(titlePt);
    if (cpl < 2) { titlePt -= 2; continue; }
    lines = splitTitleLines(title, cpl);
    if (lines.length <= 3) break;
    titlePt -= 2;
  }
  if (!lines || lines.length > 3) {
    const cpl = charsPerLine(minPt);
    lines = splitTitleLines(title, cpl);
    titlePt = minPt;
  }
  return { titlePt, titleLines: lines };
}

function calcCoverSpacing(params) {
  const {
    titleLineCount = 1, titlePt = 36, hasSubtitle = false,
    hasEnglishLabel = false, metaLineCount = 0,
    fixedHeight = 800, pageHeight = 16838,
    marginTop = 0, marginBottom = 0,
  } = params;
  const SAFETY = 1200;
  const usableHeight = pageHeight - marginTop - marginBottom - SAFETY;
  const titleHeight = titleLineCount * (titlePt * 23 + 200);
  const subtitleHeight = hasSubtitle ? (12 * 23 + 600) : 0;
  const englishLabelHeight = hasEnglishLabel ? (9 * 23 + 600) : 0;
  const metaHeight = metaLineCount * (10 * 23 + 100);
  const implicitParaHeight = 3 * 300;
  const contentHeight = titleHeight + subtitleHeight + englishLabelHeight +
    metaHeight + fixedHeight + implicitParaHeight;
  const remainingSpace = usableHeight - contentHeight;
  const safeRemaining = Math.max(remainingSpace, 400);
  const FOOTER_MIN = 800;
  const rawTop = Math.floor(safeRemaining * 0.45);
  const rawBottom = Math.floor(safeRemaining * 0.45);
  const bottomSpacing = Math.max(rawBottom, FOOTER_MIN);
  const topSpacing = Math.max(rawTop - Math.max(0, FOOTER_MIN - rawBottom), 400);
  return { topSpacing, bottomSpacing };
}

// ============================================================
// PALETTE: Terracotta (Warm + Medium + Calm) for humanities essay
// ============================================================
const palette = {
  primary: "#241E1A",
  body: "#36302C",
  secondary: "#6E6560",
  accent: "#B08050",
  surface: "#FDFBF9",
};
const c = (hex) => hex.replace("#", "");

const allNoBorders = {
  top: { style: BorderStyle.NONE, size: 0 },
  bottom: { style: BorderStyle.NONE, size: 0 },
  left: { style: BorderStyle.NONE, size: 0 },
  right: { style: BorderStyle.NONE, size: 0 },
  insideHorizontal: { style: BorderStyle.NONE, size: 0 },
  insideVertical: { style: BorderStyle.NONE, size: 0 },
};

// ============================================================
// COVER: R1 Pure Paragraph (Left-Aligned)
// ============================================================
function buildCoverR1(config) {
  const P = config.palette;
  const padL = 1200, padR = 800;
  const availableWidth = 11906 - padL - padR - 300;
  const { titlePt, titleLines } = calcTitleLayout(config.title, availableWidth, 40, 24);
  const titleSize = titlePt * 2;
  const spacing = calcCoverSpacing({
    titleLineCount: titleLines.length, titlePt,
    hasSubtitle: !!config.subtitle, hasEnglishLabel: !!config.englishLabel,
    metaLineCount: (config.metaLines || []).length,
    fixedHeight: 400,
  });
  const accentLeft = { style: BorderStyle.SINGLE, size: 8, color: c(P.accent), space: 12 };
  const children = [];
  children.push(new Paragraph({ spacing: { before: spacing.topSpacing } }));
  if (config.englishLabel) {
    children.push(new Paragraph({
      indent: { left: padL, right: padR }, spacing: { after: 500 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: c(P.accent), space: 8 } },
      children: [new TextRun({ text: config.englishLabel, size: 18, color: c(P.accent),
        font: { ascii: "Calibri" }, characterSpacing: 40 })],
    }));
  }
  for (let i = 0; i < titleLines.length; i++) {
    children.push(new Paragraph({
      indent: { left: padL },
      spacing: { after: i < titleLines.length - 1 ? 100 : 300, line: Math.ceil(titlePt * 23), lineRule: "atLeast" },
      children: [new TextRun({ text: titleLines[i], size: titleSize, bold: true,
        color: P.titleColor, font: { eastAsia: "SimHei", ascii: "Arial" } })],
    }));
  }
  if (config.subtitle) {
    children.push(new Paragraph({
      indent: { left: padL }, spacing: { after: 800 },
      children: [new TextRun({ text: config.subtitle, size: 24, color: c(P.subtitleColor),
        font: { eastAsia: "Microsoft YaHei", ascii: "Arial" } })],
    }));
  }
  for (const line of (config.metaLines || [])) {
    children.push(new Paragraph({
      indent: { left: padL + 200 }, spacing: { after: 80 },
      border: { left: accentLeft },
      children: [new TextRun({ text: line, size: 24, color: c(P.metaColor),
        font: { eastAsia: "Microsoft YaHei", ascii: "Arial" } })],
    }));
  }
  children.push(new Paragraph({ spacing: { before: spacing.bottomSpacing } }));
  if (config.footerLeft || config.footerRight) {
    children.push(new Paragraph({
      indent: { left: padL, right: padR },
      border: { top: { style: BorderStyle.SINGLE, size: 2, color: c(P.accent), space: 8 } },
      spacing: { before: 200 },
      children: [
        new TextRun({ text: config.footerLeft || "", size: 18, color: c(P.footerColor),
          font: { ascii: "Calibri" } }),
        ...(config.footerRight ? [new TextRun({ text: "", break: 1 }),
          new TextRun({ text: config.footerRight, size: 18, color: c(P.footerColor),
            font: { ascii: "Calibri" } })] : []),
      ],
    }));
  }
  return [new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    layout: TableLayoutType.FIXED,
    borders: allNoBorders,
    rows: [new TableRow({
      height: { value: 16838, rule: "exact" },
      children: [new TableCell({
        shading: { type: ShadingType.CLEAR, fill: c(P.bg) },
        borders: allNoBorders, verticalAlign: "top",
        children,
      })],
    })],
  })];
}

// ============================================================
// BODY HELPERS
// ============================================================
function heading(text, level = HeadingLevel.HEADING_1) {
  return new Paragraph({
    heading: level,
    spacing: { before: level === HeadingLevel.HEADING_1 ? 480 : 300, after: 160 },
    children: [new TextRun({ text, bold: true, color: "000000",
      font: { eastAsia: "SimHei", ascii: "Times New Roman" },
      size: level === HeadingLevel.HEADING_1 ? 32 : 28 })],
  });
}

function body(text) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    indent: { firstLine: 480 },
    spacing: { line: 312, after: 80 },
    children: [new TextRun({ text, size: 24, color: "000000",
    font: { eastAsia: "SimSun", ascii: "Times New Roman" } })],
  });
}

function italicBody(text) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    indent: { firstLine: 480 },
    spacing: { line: 312, after: 80 },
    children: [new TextRun({ text, size: 24, color: "000000", italics: true,
    font: { eastAsia: "SimSun", ascii: "Times New Roman" } })],
  });
}

function quoteBlock(text) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    indent: { left: 720, right: 720 },
    spacing: { line: 312, before: 160, after: 200 },
    border: { left: { style: BorderStyle.SINGLE, size: 6, color: c(palette.accent), space: 12 } },
    children: [new TextRun({ text, size: 22, color: palette.secondary, italics: true,
      font: { eastAsia: "SimSun", ascii: "Times New Roman" } })],
  });
}

// ============================================================
// EPOCH CONTENT — 7 эпох, каждая своими словами
// ============================================================

const epochs = [
  {
    title: "Эпоха I. Античность: логос и природа имени",
    period: "VIII в. до н.э. — V в. н.э.",
    paragraphs: [
      "Древние эллины полагали, что речь человека не есть нечто произвольное: она либо тянется от самой природы вещей, либо устанавливается людьми через соглашение. В диалоге Платона Кратил герменевты спорят: даны ли имена от природы, так что каждая вещь носит верное имя по своему естеству, или же люди наложили имена по своему усмотрению, как налагают клеймо на сосуд? Гераклит ещё раньше утверждал, что логос — общий для всех — уподобляется вечному огню, мерно вспыхивающему и мерно угасающему. Логос для досократиков — не слово в нашем смысле, но первоосновное начало, которому подчинено всё сущее.",
      "Аристотель в трактате Об истолковании положил, что звуки голоса суть знаки аффектов души, а письмена — знаки звуков голоса. Но аффекты души — те же у всех, а звуки — различны в зависимости от народа. Таким образом, античная мысль установила тройное соответствие: вещь — страсть души — голос — буква. Стоики развили это учение: они различали лектон, то есть сказуемое содержание, от самого звука. Голос пропадает, лектон остаётся — так стоики впервые разделили то, что произносится, от того, что мыслится.",
      "Риторика и диалектика составляли два главных искусства слова. Риторика учила убеждать в суде и в народном собрании, диалектика — вести спор посредством вопросов и ответов. И то, и другое опирались на топос, общие места, из которых черпаются доводы. Слово было не инструментом передачи мыслей, но действием, способным менять душу слушателя. Софисты первыми поняли, что слово может быть сильнее меча, и за это Платон не простил им до конца своих дней.",
    ],
    quote: "Слова суть подражания вещам — или по природе, или по установлению.",
  },
  {
    title: "Эпоха II. Средние века: знак, отпечаток и воля Творца",
    period: "V — XV вв.",
    paragraphs: [
      "Когда христианское откровение стало главной опорой мысли, вопрос о языке переместился из сферы природы в сферу воли. Блаженный Августин в трактате О учителе положил, что слова суть знаки, указывающие на вещи, но сами по себе они лишь побуждают душу обратиться к вещам, которые она уже знает. Никто не учит через слова, если душа не имеет внутри себя того, к чему слова лишь прикасаются. Это замечание сделало средневековую мысль глубоко интроспективной: язык стал рассматриваться как движение души, ищущей вещь в самой себе.",
      "Схоласты построили грандиозное учение о знаке. Знак, по их определению, есть нечто, что сверх своей собственной формы явно понуждает душу к познанию чего-то иного. Фома Аквинский разделил знаки на естественные, которые суть следы вещей (как дым от огня), и намеренные, которые человек ставит ради указания. Модисты — философы грамматики — развили учение о способах означивания, модусах сигнификации, которые присущи каждому слову и делают его способным означать. Они верили, что грамматические категории отражают реальные свойства вещей, так что структура латинской речи отражает устройство бытия.",
      "Особое место занимал спор об универсалиях: существуют ли общие имена в вещах, лишь в уме, или отдельно от того и другого? Реалисты утверждали, что род и вид имеют подлинное бытие; номиналисты, от Росцелина до Оккама, настаивали, что лишь единичные вещи реальны, а общие имена — лишь flatus vocis, дыхание голоса. Этот спор определил всю средневековую философию языка: имя стало полем битвы между онтологией и логикой, между верой в реальность общих понятий и радикальным эмпиризмом.",
    ],
    quote: "Слова суть знаки, побуждающие душу к познанию того, что она уже хранит.",
  },
  {
    title: "Эпоха III. Раннее Новое время: от голоса к разуму",
    period: "XV — XVII вв.",
    paragraphs: [
      "Когда рукопечатные книги стали распространяться по Европе, латынь утратила монополию на учёную речь. Лоренцо Валла в XV веке доказал, что изящная латынь Цицерона не есть язык церкви, и что каждый народ имеет право говорить и мыслить на своём наречии. Этьен Доле перевёл Платона на французский и заявил, что философия не нуждается в латыни, если мысль ясна. Так началось великое расслоение: язык стал одновременно объектом гордости национальной и инструментом познания всеобщего.",
      "Фрэнсис Бэкон в Новом Органоне провозгласил, что слова, как правило, искажают мысль: они навязывают разуму ложные сходства и мешают созерцанию природы. Язык, по Бэкону, — идолы площади, общие заблуждения, коренящиеся в словах. Декарт в Размышлениях пошёл дальше: он усомнился в том, что слова вообще способны выражать мысль адекватно, и потому искал всеобщую науку, построенную на ясных идеях, а не на словах. Лейбниц, напротив, верил, что можно построить универсальную характеристику — искусственный язык, в котором каждый знак будет однозначно соответствовать простой идее, и тогда всякий спор разрешится путём исчисления.",
      "Джон Локк в Опыте о человеческом разумении положил, что слова суть чувственно воспринимаемые знаки идей, а идеи — то, что душа обнаруживает внутри себя при размышлении. Слова не обозначают вещи непосредственно, но лишь постольку, поскольку они суть знаки идей в голове говорящего. Общность языка покоится не на сходстве имён с вещами, но на том, что люди произвольно соединяют определённые звуки с определёнными идеями. Локк первым чётко разделил значение слова (идея) и вещь, к которой оно отсылает, и этим навсегда изменил вопрос о языке.",
    ],
    quote: "Слова суть чувственно воспринимаемые знаки внутренних идей.",
  },
  {
    title: "Эпоха IV. Просвещение: чувство, разум и происхождение речи",
    period: "XVIII в.",
    paragraphs: [
      "Век разума обратился к вопросу, которого древние почти не касались: как зародилась речь? Этьен Бонно де Кондильяк в Опыте о происхождении человеческих знаний предположил, что язык родился из естественных жестов и криков. Два детей, растущие в одиночестве, начнут с мимики и возгласов, затем перейдут к произвольным знакам, а оттуда — к языку. Кондильяк утверждал, что язык не был изобретён раз и навсегда, но развивался постепенно, подобно тому как ребёнок учится говорить. Анализ и метод — вот инструменты, благодаря которым язык совершенствовался от грубых криков к сложным конструкциям.",
      "Жан-Жак Руссо в Рассуждении о происхождении и основаниях неравенства и в Опыте о происхождении языков утверждал нечто иное: первые языки были не аналитическими, но певучими, наполненными страстью и образами. Прежде чем человек стал доказывать, он пел; прежде чем рассуждать, он чувствовал. По Руссо, потребность породила первые жесты, а страсть — первые слова. Иоганн Готфрид Гердер в трактате О происхождении языка пошёл ещё дальше: он отверг как божественное откровение, так и чисто рассудочное изобретение. Язык, по Гердеру, — медленно выработанное средство познания, тесно связанное с чувственным опытом и с сознательной деятельностью человека.",
      "Просвещение создало общую грамматику — учение о всеобщих принципах, лежащих в основе каждого языка. Грамматисты Порт-Рояля утверждали, что всякая Proposition, то есть суждение, состоит из субъекта, атрибута и связки, и что эта структура отражает саму структуру мысли. Они полагали, что грамматические категории суть не произвольные условности, но необходимые формы, в которых разум артикулирует свои идеи. Эта вера в универсальную логику речи определила всю последующую лингвистику вплоть до XX века.",
    ],
    quote: "Страстям мы обязаны первыми словами, а потребностям — первыми жестами.",
  },
  {
    title: "Эпоха V. XIX век: родство языков и дух народа",
    period: "XIX в.",
    paragraphs: [
      "Когда Франц Бопп в 1816 году опубликовал Сравнительное спряжение, он доказал, что санскрит, латинский, греческий, германские и кельтские языки восходят к общему предку. Это открытие изменило всё: язык перестал быть лишь орудием мысли и стал историческим памятником, живым свидетелем перемещений народов. Якоб Гримм сформулировал свой знаменитый закон о чередовании согласных, и сравнительное языкознание превратилось в строгую дисциплину, способную восстанавливать формы, которые никогда не были записаны.",
      "Вильгельм фон Гумбольдт в сочинении О различии строения человеческих языков высказал мысль, что язык не есть продукт, но деятельность. Каждый язык есть органическое целое, обладающее внутренней формой — особым способом, которым народ членит мир и придаёт ему словесную плоть. Дух народа и его язык нераздельны: язык есть орган внутреннего, а не внешнего бытия народа. Гумбольдт утверждал, что изучать язык — значит не описывать его правила, но постигать мировоззрение народа, им владеющего.",
      "В России Александр Афанасьевич Потебня развивал идеи Гумбольдта: он утверждал, что слово есть не знак вещи, а средство создания образа. Слово делится на внешнюю форму, звучание, и внутреннюю, его значение, причём внутренняя форма есть образ, посредством которого народ понимает сущность вещи. Эта мысль стала основой русской лингвистической традиции и одновременно питала литературную критику и поэтику. Язык в XIX веке впервые предстал не как инструмент, но как существо, живущее по собственным законам, растущее и ветвящееся подобно дереву.",
    ],
    quote: "Язык не есть продукт деятельности, но сама деятельность духа.",
  },
  {
    title: "Эпоха VI. XX век: знак, система и порождающее устройство",
    period: "XX в.",
    paragraphs: [
      "Фердинанд де Соссюр в Женевских лекциях совершил переворот, равного которому лингвистика не знала со времён Аристотеля. Он разделил язык на две неравные части: язык как систему знаков и речь как индивидуальный акт. Язык существует в коллективе и не зависит от воли говорящего; речь есть осуществление этой системы в конкретном высказывании. Знак, по Соссюру, состоит из означающего и означаемого, и связь между ними произвольна. Это значит: нет никакого естественного родства между звуком и смыслом — оно установлено обществом.",
      "Соссюр также разделил изучение языка на синхронию и диахронию: первая рассматривает систему в данный момент, вторая — её изменения во времени. Он утверждал, что синхрония должна предшествовать диахронии, так как говорящий не сознаёт исторических изменений. Значение каждого знака определяется не его собственной природой, но его положением в системе, его отношением к другим знакам. Лингвистика стала наукой о системах: языки — как кристаллы, каждый с собственной структурой, каждый — целое по своим правилам.",
      "Во второй половине века Ноам Хомский превратил лингвистику в раздел когнитивной науки. Он предложил различать компетенцию, знание языка, и употребление, то есть практическое владение. Компетенция описывается порождающей грамматикой — конечным набором правил, способным производить бесконечное множество предложений. Глубинная структура предложения, его подлинная форма, трансформируется в поверхностную посредством правил перестановки, удаления и вставки. Хомский доказал, что ребёнок способен усвоить язык лишь потому, что врождённые структуры мозга уже содержат универсальную грамматику.",
    ],
    quote: "Язык — это система знаков, выражающих идеи.",
  },
  {
    title: "Эпоха VII. Конец XX — XXI век: тело, мозг и предсказание",
    period: "конец XX — начало XXI в.",
    paragraphs: [
      "Когнитивная революция 1970–1980-х годов вернула языку его тело. Джордж Лакофф в книге Женщины, огонь и опасные вещи доказал, что человеческие категории строятся не по формальной логике, но на основе телесного опыта, метафор и прототипов. Мы не мыслим абстрактными символами — мы мыслим телом. Понятия — аргумент, время, состояние понимаются через метафоры: спора как войны, времени как движения, состояния как контейнера. Эти метафоры не украшение речи, а основа мышления, коренящаяся в том, как наше тело взаимодействует с миром.",
      "Одновременно нейробиология показала, что язык не локализован в одной зоне мозга, но распределён по обширным сетям. Антонио Дамасио выдвинул гипотезу соматического маркера: каждое решение, каждое высказывание сопровождается телесным ощущением, которое направляет выбор слов и конструкций. Лиза Фельдман Барретт показала, что эмоции не есть врождённые реакции, но предсказания мозга, основанные на интероцепции — непрерывном считывании состояния тела. Язык, следовательно, есть не кодирование мыслей в звуки, а непрерывное действие тела, стремящегося минимизировать разницу между ожиданием и ощущением.",
      "Карл Фристон сформулировал принцип свободной энергии: мозг постоянно строит модель мира и обновляет её, чтобы предсказывать входящие сигналы. Язык в этой картине — не средство передачи информации, а один из каналов, через который мозг снижирует неопределённость. Говорящий не кодирует готовую мысль в слова — он совершает телесное действие, направленное на изменение состояний другого тела. Слушающий не декодирует слова — он использует их как сигналы для обновления собственной предиктивной модели. Язык вернулся к тому, с чего начинал у Гераклита: он есть действие, событие, развертывающееся между телами, а не вещь, которую можно передать из головы в голову.",
    ],
    quote: "Язык есть не код, но действие тела, направленное на другой мир.",
  },
];

// ============================================================
// ASSEMBLE DOCUMENT
// ============================================================

const coverConfig = {
  title: "Язык сквозь эпохи",
  subtitle: "Семь эпох языковой мысли — каждая своими словами",
  englishLabel: "LANGUAGE THROUGH THE AGES",
  metaLines: [
    "Философско-лингвистический эссе",
  ],
  footerLeft: "",
  footerRight: "2026",
  palette: {
    bg: palette.primary,
    titleColor: "F5EDE4",
    subtitleColor: "C4B8A8",
    metaColor: "A89880",
    accent: palette.accent,
    footerColor: "8A7A68",
  },
};

// Build body content
const bodyChildren = [];

for (const epoch of epochs) {
  // Epoch heading
  bodyChildren.push(heading(epoch.title, HeadingLevel.HEADING_1));
  // Period sub-heading
  bodyChildren.push(new Paragraph({
    spacing: { after: 200 },
    children: [new TextRun({ text: epoch.period, size: 22, color: c(palette.accent),
      font: { ascii: "Times New Roman", eastAsia: "SimSun" }, italics: true })],
  }));
  // Paragraphs
  for (const p of epoch.paragraphs) {
    bodyChildren.push(body(p));
  }
  // Quote
  if (epoch.quote) {
    bodyChildren.push(quoteBlock(epoch.quote));
  }
}

const doc = new Document({
  styles: {
    default: {
      document: {
        run: {
          font: { ascii: "Times New Roman", eastAsia: "SimSun" },
          size: 24, color: "000000",
        },
        paragraph: { spacing: { line: 312 } },
      },
      heading1: {
        run: {
          font: { ascii: "Times New Roman", eastAsia: "SimHei" },
          size: 32, bold: true, color: "000000",
        },
        paragraph: { spacing: { before: 480, after: 160, line: 312 } },
      },
      heading2: {
        run: {
          font: { ascii: "Times New Roman", eastAsia: "SimHei" },
          size: 28, bold: true, color: "000000",
        },
        paragraph: { spacing: { before: 300, after: 120, line: 312 } },
      },
    },
  },
  sections: [
    // SECTION 1: Cover
    {
      properties: {
        page: {
          size: { width: 11906, height: 16838, orientation: PageOrientation.PORTRAIT },
          margin: { top: 0, bottom: 0, left: 0, right: 0 },
        },
      },
      children: buildCoverR1(coverConfig),
    },
    // SECTION 2: Body
    {
      properties: {
        page: {
          size: { width: 11906, height: 16838, orientation: PageOrientation.PORTRAIT },
          margin: { top: 1440, bottom: 1440, left: 1701, right: 1417 },
          pageNumbers: { start: 1, formatType: NumberFormat.DECIMAL },
        },
      },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({
              children: [PageNumber.CURRENT],
              size: 18, color: palette.secondary,
              font: { ascii: "Times New Roman" },
            })],
          })],
        }),
      },
      children: bodyChildren,
    },
  ],
});

const OUTPUT = "/home/z/my-project/download/Epohti_jazyka.docx";
Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(OUTPUT, buf);
  console.log("Document saved to:", OUTPUT);
}).catch(err => {
  console.error("Error:", err);
  process.exit(1);
});
