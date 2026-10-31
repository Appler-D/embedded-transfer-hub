"""Three-minute self-introduction timer.

Run from the repository root:
    python tools/interview_timer.py
    python tools/interview_timer.py --demo
"""

from __future__ import annotations

import argparse
import csv
import sys
import time
from pathlib import Path

SECTIONS = [
    ("开场 + 个人/家庭", 20),
    ("学业基本情况", 25),
    ("转专业理由", 35),
    ("对专业的理解", 35),
    ("实践/成绩/获奖", 40),
    ("学业规划", 20),
    ("收尾", 5),
]


def run(demo: bool, out: Path | None) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    print("目标 3:00；每段讲完按 Enter。\n")
    for name, target in SECTIONS:
        if demo:
            actual = float(target + (5 if name.startswith("转") else -2))
        else:
            print(f"{name}（目标 {target}s）")
            input("按 Enter 开始，讲完再按 Enter...")
            started = time.monotonic()
            input()
            actual = time.monotonic() - started
        rows.append(
            {
                "section": name,
                "target_s": target,
                "actual_s": round(actual, 1),
                "delta_s": round(actual - target, 1),
            }
        )

    print(f"\n{'段落':<16}{'目标':>6}{'实际':>8}{'偏差':>8}")
    for row in rows:
        print(
            f"{row['section']:<16}{row['target_s']:>6}"
            f"{row['actual_s']:>8}{row['delta_s']:>+8}"
        )
    total = sum(float(row["actual_s"]) for row in rows)
    print(f"\n总计：{total:.1f}s（目标 180s，偏差 {total - 180:+.1f}s）")

    if out is not None:
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["section", "target_s", "actual_s", "delta_s"],
            )
            writer.writeheader()
            writer.writerows(rows)
        print(f"saved {out}")
    return rows


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="simulate timings without input")
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    run(args.demo, args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
