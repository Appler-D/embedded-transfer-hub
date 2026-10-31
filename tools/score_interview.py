"""Score a mock transfer interview on the seven rubric dimensions."""

from __future__ import annotations

import argparse
import sys

DIMENSIONS = [
    ("动机真实、不贬低原专业", "把“为什么转”讲成拉，不讲成逃"),
    ("对 EE/目标专业的理解", "能说出课程、方向、为什么"),
    ("学业/能力证据", "GPA、排名、课程、英语"),
    ("实践/项目（真实）", "做了什么、哪里失败、怎么修正"),
    ("补课/规划可执行", "先补什么、怎么排、时间"),
    ("不会时诚实、会查证", "说边界 + 查证方法"),
    ("表达清楚、不背稿", "停顿、眼神、结构"),
]


def ask_score(label: str, advice: str) -> int:
    while True:
        raw = input(f"{label}（1-5）: ").strip()
        try:
            value = int(raw)
        except ValueError:
            print("请输入 1-5")
            continue
        if 1 <= value <= 5:
            return value
        print("请输入 1-5")


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="use sample scores")
    args = parser.parse_args()

    demo_scores = [4, 3, 5, 2, 4, 3, 4]
    rows = []
    for index, (label, advice) in enumerate(DIMENSIONS):
        score = demo_scores[index] if args.demo else ask_score(label, advice)
        rows.append((label, score, advice))

    print(f"\n{'维度':<24}{'分数':>4}")
    for label, score, _ in rows:
        print(f"{label:<24}{score:>4}")
    total = sum(score for _, score, _ in rows)
    print(f"\n总分：{total}/35")

    weakest = min(rows, key=lambda row: row[1])
    print(f"最弱：{weakest[0]}（{weakest[1]}/5）")
    print(f"建议：{weakest[2]}")
    if total < 21:
        print("结论：先补最弱两项，再完整模拟一次。")
    elif total < 28:
        print("结论：基本可用，重点练追问与不会时的回答。")
    else:
        print("结论：结构稳，练自然表达和临场追问。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
