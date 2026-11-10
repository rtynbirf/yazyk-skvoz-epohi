#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Счётчик-автомат: слить окно GitHub traffic (последние 14 дней) в traffic.json.

Дом смотрит на визиты раз в сутки; API отдаёт лишь скользящее окно из 14 дней.
Идея: накапливать историю по дням в traffic.json (каждый день — max из того,
что видел дом), тогда сумма истории = честный счёт «за всё время наблюдения».

Идемпотентность: если новое состояние равно прежнему — файл не перезаписывается,
скрипт завершается с кодом 0 и пометкой «нет перехода».

Запуск: python3 scripts/update_traffic.py /tmp/views.json traffic.json
Только стандартная библиотека.
"""
import json
import sys
from datetime import datetime, timezone


def iso_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def empty_state():
    return {"schema": 1,
            "total": {"views": 0, "uniques": 0},
            "window": {"views": 0, "uniques": 0, "updated": iso_now()},
            "history": [],
            "updated": iso_now()}


def main():
    if len(sys.argv) != 3:
        print("использование: update_traffic.py <окно-от-API.json> <traffic.json>")
        return 2
    src, dst = sys.argv[1], sys.argv[2]

    with open(src, encoding="utf-8") as f:
        window = json.load(f)
    # ответ GET /repos/{owner}/{repo}/traffic/views:
    # {"count": N, "uniques": M, "views": [{"timestamp": "...", "count": n, "uniques": m}, ...]}
    w_views = int(window.get("count", 0))
    w_uniques = int(window.get("uniques", 0))
    days = window.get("views", []) or []

    try:
        with open(dst, encoding="utf-8") as f:
            state = json.load(f)
        if state.get("schema") != 1:
            state = empty_state()
    except (OSError, json.JSONDecodeError, ValueError):
        state = empty_state()

    merged = {e.get("date"): e for e in state.get("history", []) if e.get("date")}
    for d in days:
        date = str(d.get("timestamp", ""))[:10]
        if not date:
            continue
        prev = merged.get(date, {"date": date, "views": 0, "uniques": 0})
        merged[date] = {"date": date,
                        "views": max(int(prev.get("views", 0)), int(d.get("count", 0))),
                        "uniques": max(int(prev.get("uniques", 0)), int(d.get("uniques", 0)))}

    history = [merged[k] for k in sorted(merged)]
    new_state = {
        "schema": 1,
        "total": {"views": sum(e["views"] for e in history),
                  "uniques": sum(e["uniques"] for e in history)},
        "window": {"views": w_views, "uniques": w_uniques, "updated": iso_now()},
        "history": history,
        "updated": iso_now(),
    }

    if new_state == state or (new_state["history"] == state.get("history")
                              and new_state["total"] == state.get("total")):
        print(f"δ: состояние не изменилось — перехода нет "
              f"(total.views={new_state['total']['views']})")
        return 0

    with open(dst, "w", encoding="utf-8") as f:
        json.dump(new_state, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"δ: traffic.json обновлён — визитов за всё время наблюдения: "
          f"{new_state['total']['views']}, читателей (по дням): {new_state['total']['uniques']}, "
          f"дней в истории: {len(history)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
