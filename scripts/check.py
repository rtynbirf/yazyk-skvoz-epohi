#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Страж дома — приёмка артефактов «Язык сквозь эпохи · Дом-Автомат».

Сам страж устроен как детерминированный конечный автомат:
  G = (Qg, Σg, δg, q₀, Fg),
где символы алфавита — артефакты дома, а каждый δ-переход — блок проверок.
Любая неудачная проверка собирается в протокол; после прогона:
  ω ∈ L(G) → ПРИНЯТО (exit 0)   ·   иначе ОТВЕРГНУТО (exit 1), fail-closed.

Запуск: python3 scripts/check.py            (полная приёмка)
        python3 scripts/check.py --xml      (только XML-ленты и карта)
Только стандартная библиотека — ноль зависимостей, как и сам дом.
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

SITE = "https://rtynbirf.github.io/yazyk-skvoz-epohi/"
ANCHORS = ["cover", "e1", "e2", "e3", "e4", "e5", "e6", "e7", "after", "automaton"]
ATOM = "{http://www.w3.org/2005/Atom}"
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"

problems = []


def fail(msg):
    problems.append(msg)


def read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except OSError as e:
        fail(f"{path}: файл не читается ({e})")
        return None


class Guard:
    """ДКА стража: δ(состояние, артефакт) → состояние. Принимает дом, если все переходы чисты."""

    def __init__(self):
        self.state = "q₀"
        self.trace = []

    def transition(self, q_from, symbol, q_to, checks):
        if self.state != q_from:  # недостижимый порядок — ошибка записи таблицы, а не дома
            fail(f"страж: недостижимый переход δ({q_from}, {symbol}); текущее состояние {self.state}")
            return
        errors_before = len(problems)
        checks()
        ok = len(problems) == errors_before
        self.trace.append(f"δ({q_from}, {symbol}) → {q_to} {'✓' if ok else '✗'}")
        self.state = q_to


def check_index(html):
    if html is None:
        return
    # 1) секции-состояния: ровно десять, по порядку q0…q9, с якорями дома
    #    (в разметке порядок атрибутов различается — снимаем оба порядка)
    pairs = set(re.findall(r'<section[^>]*data-q="(q\d)"[^>]*id="([^"]+)"', html))
    pairs |= {(m.group(2), m.group(1)) for m in
              re.finditer(r'<section[^>]*id="([^"]+)"[^>]*data-q="(q\d)"', html)}
    got = sorted(pairs, key=lambda t: int(t[0][1:]))
    want = [(f"q{i}", a) for i, a in enumerate(ANCHORS)]
    if got != want:
        fail(f"index.html: состояния и якоря не совпадают с картой дома\n  ждём: {want}\n  есть: {got}")

    # 2) id уникальны
    ids = re.findall(r'\bid="([^"]+)"', html)
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup:
        fail(f"index.html: дубликаты id: {dup}")

    # 3) голова: канон, og:url, обе ленты с hreflang
    if f'<link rel="canonical" href="{SITE}">' not in html:
        fail("index.html: нет canonical на " + SITE)
    if f'<meta property="og:url" content="{SITE}">' not in html:
        fail("index.html: нет og:url")
    for feed, lang in (("feed.xml", "ru"), ("feed-la.xml", "la")):
        if f'href="{SITE}{feed}" hreflang="{lang}"' not in html:
            fail(f"index.html: в head нет <link rel=alternate> на {feed} (hreflang={lang})")

    # 4) подвал: ленты и счётчик
    if 'id="visitsLine"' not in html:
        fail('index.html: в подвале нет id="visitsLine" (дисплей счётчика)')
    if "feed.xml" not in html or "feed-la.xml" not in html:
        fail("index.html: в подвале нет ссылок на δ-ленты")

    # 5) язык документа
    if '<html lang="ru"' not in html:
        fail('index.html: отсутствует <html lang="ru">')


def check_feed(path, lang, channel_marker):
    raw = read(path)
    if raw is None:
        return None
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        fail(f"{path}: XML не well-formed ({e})")
        return None
    if root.tag != "rss" or root.get("version") != "2.0":
        fail(f'{path}: корень должен быть <rss version="2.0">')
        return None
    ch = root.find("channel")
    if ch is None:
        fail(f"{path}: нет <channel>")
        return None
    title = (ch.findtext("title") or "").strip()
    if channel_marker not in title:
        fail(f"{path}: title канала не содержит «{channel_marker}»: {title!r}")
    if (ch.findtext("link") or "").strip() != SITE:
        fail(f"{path}: link канала должен быть {SITE}")
    if not (ch.findtext("description") or "").strip():
        fail(f"{path}: пустое description канала")
    if (ch.findtext("language") or "").strip() != lang:
        fail(f"{path}: language канала должен быть «{lang}»")
    lbd = (ch.findtext("lastBuildDate") or "").strip()
    try:
        parsedate_to_datetime(lbd)
    except Exception:
        fail(f"{path}: lastBuildDate не разбирается как RFC-822: {lbd!r}")
    self_links = [e for e in ch.findall(ATOM + "link") if e.get("rel") == "self"]
    if len(self_links) != 1 or self_links[0].get("href") != f"{SITE}{path}":
        fail(f"{path}: нужен ровно один atom:link rel=self href={SITE}{path}")

    items = ch.findall("item")
    if len(items) != 10:
        fail(f"{path}: должно быть 10 позиций (q₀…q₉), есть {len(items)}")
    guids = []
    for i, it in enumerate(items):
        for tag in ("title", "link", "description", "guid", "pubDate"):
            if not (it.findtext(tag) or "").strip():
                fail(f"{path}: позиция {i + 1} без <{tag}>")
        g = (it.findtext("guid") or "").strip()
        if g:
            guids.append(g)
            if not g.startswith(SITE + "#"):
                fail(f"{path}: guid не на якорь дома: {g}")
            elif g.rsplit("#", 1)[-1] not in ANCHORS:
                fail(f"{path}: guid указывает на неизвестный якорь «{g.rsplit('#', 1)[-1]}»")
    if len(set(guids)) != len(guids):
        fail(f"{path}: guid повторяются — лента должна быть инъективной по δ-переходам")
    return {g.rsplit("#", 1)[-1] for g in guids}


def check_traffic(path):
    raw = read(path)
    if raw is None:
        return
    try:
        d = json.loads(raw)
    except json.JSONDecodeError as e:
        fail(f"{path}: не разбирается как JSON ({e})")
        return
    if d.get("schema") != 1:
        fail(f"{path}: schema должна быть 1")
    for key in ("total", "window", "history", "updated"):
        if key not in d:
            fail(f"{path}: нет поля {key}")
            return
    for grp in ("total", "window"):
        v, u = d[grp].get("views"), d[grp].get("uniques")
        if not (isinstance(v, int) and v >= 0 and isinstance(u, int) and u >= 0):
            fail(f"{path}: {grp}.views/.uniques должны быть целыми ≥ 0")
    from datetime import datetime
    try:
        datetime.fromisoformat(str(d["updated"]).replace("Z", "+00:00"))
    except Exception:
        fail(f"{path}: updated не ISO-8601: {d['updated']!r}")
    dates = []
    for e in d["history"]:
        if not (isinstance(e.get("views"), int) and isinstance(e.get("uniques"), int)
                and e["views"] >= 0 and e["uniques"] >= 0):
            fail(f"{path}: запись истории без целых views/uniques: {e}")
            dates.append(None)
            continue
        dates.append(e.get("date"))
    if dates and (dates != sorted(d for d in dates if d) or len(set(dates)) != len(dates)):
        fail(f"{path}: история должна быть отсортирована по датам без повторов")
    s = sum(e.get("views", 0) for e in d["history"] if isinstance(e.get("views"), int))
    if isinstance(d["total"].get("views"), int) and s != d["total"]["views"]:
        fail(f"{path}: total.views ({d['total']['views']}) ≠ сумме истории ({s})")


def check_sitemap(path):
    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError) as e:
        fail(f"{path}: не разбирается ({e})")
        return
    urls = root.findall(f"{SITEMAP_NS}url")
    if len(urls) != 1:
        fail(f"{path}: должна быть ровно одна страница (дом — один документ), есть {len(urls)}")
    for u in urls:
        loc = (u.findtext(f"{SITEMAP_NS}loc") or "").strip()
        if loc != SITE:
            fail(f"{path}: loc должен быть {SITE}, есть {loc}")


def check_robots(path):
    raw = read(path)
    if raw is None:
        return
    if f"Sitemap: {SITE}sitemap.xml" not in raw:
        fail(f"{path}: нет строки Sitemap: {SITE}sitemap.xml")
    if "Allow: /" not in raw:
        fail(f"{path}: дом открыт для ботов, ждём «Allow: /»")


def check_404(path):
    raw = read(path)
    if raw is None:
        return
    if 'name="robots" content="noindex"' not in raw:
        fail(f"{path}: 404 должен быть noindex")
    if SITE not in raw:
        fail(f"{path}: 404 обязан показывать возврат в q₀ (ссылка на {SITE})")
    if "charset" not in raw.lower():
        fail(f"{path}: нет объявления charset")


def check_nojekyll(path):
    import os
    if not os.path.exists(path):
        fail(f"{path}: нет — Pages начнёт гонять Jekyll")


def check_guard_self(path):
    import py_compile
    import tempfile
    fd, cfile = tempfile.mkstemp(suffix=".pyc")
    import os
    os.close(fd)
    try:
        py_compile.compile(path, cfile=cfile, doraise=True)
    except py_compile.PyCompileError as e:
        fail(f"{path}: страж сам не компилируется ({e})")
    finally:
        os.unlink(cfile)


def main():
    xml_only = "--xml" in sys.argv
    html = read("index.html")  # нужен и лентам — сверка якорей
    g = Guard()

    def t_index():
        check_index(html)

    def t_feed_ru():
        anchors = check_feed("feed.xml", "ru", "Язык сквозь эпохи")
        if anchors and html is not None:
            missing = anchors - set(ANCHORS)
            if missing:
                fail(f"feed.xml: якоря ленты не существуют в документе: {missing}")

    def t_feed_la():
        anchors = check_feed("feed-la.xml", "la", "Lingua per Aetates")
        if anchors and html is not None:
            missing = anchors - set(ANCHORS)
            if missing:
                fail(f"feed-la.xml: якоря ленты не существуют в документе: {missing}")

    g.transition("q₀", "index.html", "q₁", t_index)
    g.transition("q₁", "feed.xml", "q₂", t_feed_ru)
    g.transition("q₂", "feed-la.xml", "q₃", t_feed_la)
    g.transition("q₃", "traffic.json", "q₄", lambda: check_traffic("traffic.json"))
    g.transition("q₄", "sitemap.xml", "q₅", lambda: check_sitemap("sitemap.xml"))
    g.transition("q₅", "robots.txt", "q₆", lambda: check_robots("robots.txt"))
    g.transition("q₆", "404.html", "q₇", lambda: check_404("404.html"))
    if not xml_only:
        g.transition("q₇", ".nojekyll", "q₈", lambda: check_nojekyll(".nojekyll"))
        g.transition("q₈", "scripts/check.py", "q₉", lambda: check_guard_self("scripts/check.py"))

    for line in g.trace:
        print(line)
    if problems:
        print("\nОТВЕРГНУТО — ω ∉ L(G). Протокол:")
        for p in problems:
            print(f"  ✗ {p}")
        return 1
    print(f"\nω ∈ L(G) · дом принят ({g.state} — акцептирующее состояние)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
