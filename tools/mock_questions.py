"""Draw random transfer-interview questions for practice."""

from __future__ import annotations

import argparse
import random
import sys

QUESTIONS = [
    "为什么转专业？",
    "你了解电子信息工程吗？",
    "你成绩不错，为什么不在原专业继续？",
    "你没有任何项目，凭什么转？",
    "你没过四级，怎么读英文资料？",
    "你为什么不选计算机？",
    "你基础比同学差，怎么跟上？",
    "转过去要补很多课，你怎么安排？",
    "如果没转成怎么办？",
    "你以后想做什么？",
    "怎么实现自动化？",
    "怎么造手机？",
    "信号与系统学什么？",
    "数字电子学什么？",
    "模拟电子学什么？",
    "C 语言你学到哪？",
    "I2C 和 SPI 的区别？",
    "中断是什么？",
    "PWM 是什么？",
    "PID 是什么？",
    "你做过什么项目？具体讲一个。",
    "你遇到的最大困难/失败是什么？",
    "你最近在读什么？",
    "你如何看待 AI 对电子信息的影响？",
    "你最大的缺点是什么？",
    "你还有什么问题问我们？",
]


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=5)
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()
    if not 1 <= args.count <= len(QUESTIONS):
        parser.error(f"--count must be 1..{len(QUESTIONS)}")

    picked = random.Random(args.seed).sample(QUESTIONS, args.count)
    print(f"随机抽题（{args.count} 道）\n")
    for index, question in enumerate(picked, start=1):
        print(f"{index}. {question}")
    print("\n建议：先口述 60–90 秒，再对照 docs/06 与 docs/15 的结构复盘。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
