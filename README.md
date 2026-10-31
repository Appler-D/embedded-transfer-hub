# Embedded Transfer Hub

从化学 / 材料背景转向电子信息工程：嵌入式入门、系统思维与转专业面试准备。

> 这不是“速成答案”，而是一条能讲清楚、能动手、能被追问的学习路线。
> 面试老师问“怎么实现自动化”“怎么造手机”，通常不是要你造一台，而是看你能否把复杂系统拆开、讲清层次与取舍。

## 先看这三篇（面试急救）

1. [怎么实现自动化](docs/04-automation.md) — 感知 → 决策 → 执行 → 反馈
2. [怎么造手机](docs/05-how-a-phone-is-made.md) — 芯片、屏幕、电池、软件、制造与供应链
3. [转专业面试问答](docs/06-interview-qa.md) — 25 个问题与回答结构

## 浙农林转专业专用（时间敏感）

> 2026-10-26 教务处已启动面向 **2025 级**的新一轮转专业；按 2024 级节奏，学生报名可能在 11 月下旬–12 月初。以教务处最新通知为准。

- [12 浙农林转专业攻略](docs/12-zafu-transfer-playbook.md)：官方时间线、GPA 70% + 面试 30%、资格限制、行动清单。
- [13 3 分钟自述逐字稿](docs/13-zafu-3min-script.md)：按光机电官方六个采分点写，含时间分配与追问。
- [光机电 2026-06-18 面试通知](https://gjdxy.zafu.edu.cn/info/1083/7717.htm)：3 分钟中文自述、5–7 分钟、三组线下、面试 <60 不录取。
- [教务处 2026-10-26 通知](https://jwc.zafu.edu.cn/info/1012/9972.htm)：本轮面向 2025 级，学院 10/30 前报计划。

## 7 天急救包

| 天 | 做什么 | 产出 |
| --- | --- | --- |
| 1 | 读 [转专业叙事](docs/01-transfer-story.md) + [自动化](docs/04-automation.md) | 画出“传感器 → 控制器 → 执行器 → 反馈”图 |
| 2 | 读 [造手机](docs/05-how-a-phone-is-made.md) | 画出手机 6 层结构图 |
| 3 | 读 [电子基础](docs/02-electronics-basics.md) + [嵌入式基础](docs/03-embedded-basics.md) | 能解释电压/电流、GPIO、ADC、PWM |
| 4 | 做 [项目 1：LED + 按钮](projects/01-led-button/README.md) 或 Wokwi 仿真 | 代码 + 照片/截图 |
| 5 | 做项目 2：传感器 + OLED（或仿真） | 一段 30 秒演示视频 |
| 6 | 读 [面试问答](docs/06-interview-qa.md)，写 3 个故事 | 60 秒自我介绍 + 3 个回答 |
| 7 | 模拟面试，录 3 分钟 demo | 复盘清单 |

## 仓库内容

| 文档 | 内容 |
| --- | --- |
| [00 从这里开始](docs/00-start-here.md) | 7 天 / 30 天 / 12 周怎么用 |
| [01 转专业叙事](docs/01-transfer-story.md) | 为什么转、化学背景怎么用、怎么补短板 |
| [02 电子基础](docs/02-electronics-basics.md) | 电压电流、元件、万用表、信号链 |
| [03 嵌入式基础](docs/03-embedded-basics.md) | MCU、GPIO、ADC/PWM、总线、中断、RTOS |
| [04 自动化](docs/04-automation.md) | 自动化闭环、开环/闭环、PID、PLC vs MCU |
| [05 造手机](docs/05-how-a-phone-is-made.md) | 手机的系统分层、制造流程与取舍 |
| [06 面试问答](docs/06-interview-qa.md) | 25 个问题、回答结构、不会时怎么说 |
| [07 学习路线](docs/07-learning-path.md) | 7 天 / 30 天 / 12 周计划 |
| [08 入门项目](docs/08-projects.md) | 5 个项目、BOM、面试讲法 |
| [09 资源](docs/09-resources.md) | 课程、书、仿真器、GitHub 清单 |
| [10 术语](docs/10-glossary.md) | 中英对照，面试不卡词 |
| [11 演示脚本](docs/11-demo-script.md) | 3 分钟项目演示与录制 |
| [12 浙农林转专业攻略](docs/12-zafu-transfer-playbook.md) | 官方时间线、GPA/面试规则、资格与行动清单 |
| [13 浙农林 3 分钟自述](docs/13-zafu-3min-script.md) | 按官方六个采分点写的逐字稿模板 |
| [14 游戏服务端路径](docs/14-game-server-path.md) | 从 EE 到游戏服务端/后端的差距、项目与补法 |
| [15 模拟面试](docs/15-mock-interview.md) | 三场完整对话 + 打分表 |
| [16 课程地图](docs/16-course-map.md) | EE 课程一句话 + 学习顺序 + 方向选课 |
| [17 30 天计划](docs/17-30-day-plan.md) | 转专业冲刺版周计划 |
| [18 FAQ](docs/18-faq.md) | 转专业/四级/项目/方向常见问题 |
| [PROGRESS.md](PROGRESS.md) | 自己的进度与每周记录 |
| [notes/TEMPLATE.md](notes/TEMPLATE.md) | 实验笔记模板 |
| [projects/](projects/) | 项目代码与文档模板 |
| [tools/interview_timer.py](tools/interview_timer.py) | 3 分钟自述分段计时器 |

## 12 周路线（摘要）

- 第 1–2 周：电子基础 + C + Arduino，点亮 LED、读按钮。
- 第 3–4 周：传感器、ADC、I2C OLED；做一个小型环境监测器。
- 第 5–6 周：舵机、继电器、电机驱动；理解 PWM 与供电。
- 第 7–8 周：ESP32 Wi-Fi、串口/网络；做一个能上报数据的节点。
- 第 9–10 周：控制（开关控制 / PID）、状态机；做自动夜灯或智能风扇。
- 第 11–12 周：项目整理、面试表达、demo 视频、复盘。

完整计划见 [07-learning-path.md](docs/07-learning-path.md)。

## 怎么用这个仓库（诚实）

- 只记录你真正做过的事；不要编造项目、证书或成绩。
- 面试官更看重“你怎么想、怎么学、怎么验证”，而不是你背了多少名词。
- 每学一个概念，至少写一句“它解决什么问题、用什么替代方案、代价是什么”。
- 每做一个项目，留下代码、接线图、照片/视频、失败记录和 3 句面试讲法。
- 外部链接属于原作者；复用代码前确认 LICENSE。

## 适合谁

- 想从化学、材料、生物等专业转向电子信息工程 / 嵌入式方向的学生。
- 刚开始学单片机，需要一条不被资料淹没的路线。
- 需要准备转专业面试，尤其是“自动化怎么实现”“手机怎么造”这类开放题。

## 不适合谁

- 想要“三天速成嵌入式工程师”的人。
- 想要背诵标准答案、不愿意动手的人。
- 想把别人的项目写成自己的经历的人。

## License

本仓库原创内容采用 MIT License；外部链接与引用资源归原作者所有，使用前请确认其许可证。
