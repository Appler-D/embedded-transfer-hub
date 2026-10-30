# 资源：少而准，不要囤课

> 一条原则：一门主课 + 一块板子 + 一个项目。收藏不等于学会。

## 零、浙农林官方（转专业/培养方案）

- 教务处通知公告：https://jwc.zafu.edu.cn/tzgg.htm
- 2026-10-26 报送计划通知（本轮面向 2025 级）：https://jwc.zafu.edu.cn/info/1012/9972.htm
- 2025-11-21 受理 2024 级通知（报名窗口参考）：https://jwc.zafu.edu.cn/info/1012/9721.htm
- 光机电 2026-06-18 转专业面试通知（GPA 70% + 面试 30%）：https://gjdxy.zafu.edu.cn/info/1083/7717.htm
- 光机电 2025-06-09 面试工作总结（86 人、考核组、个人陈述+问答）：https://gjdxy.zafu.edu.cn/info/1082/7084.htm
- 2026-2027 第一学期转专业结果（371 人）：https://jwc.zafu.edu.cn/info/1012/9932.htm
- 电子信息工程培养方案：https://gjdxy.zafu.edu.cn/info/1026/1013.htm
- 光机电通知公告：https://gjdxy.zafu.edu.cn/index/tzgg.htm

> GitHub 上没有找到有意义的“浙农林转专业经验”仓库；ZAFU 相关仓库多为工具类。转专业信息以教务处/学院官方通知为准，详见 [12-zafu-transfer-playbook.md](12-zafu-transfer-playbook.md)。

## 一、系统路线与清单

| 资源 | 说明 |
| --- | --- |
| [m3y54m/Embedded-Engineering-Roadmap](https://github.com/m3y54m/Embedded-Engineering-Roadmap)（约 13.7k） | 嵌入式工程师路线图，覆盖 C/C++、MCU、RTOS、通信、调试 |
| [nhivp/Awesome-Embedded](https://github.com/nhivp/Awesome-Embedded)（约 9.3k） | 嵌入式编程资源清单 |
| [kitspace/awesome-electronics](https://github.com/kitspace/awesome-electronics)（约 8.3k） | 电子工程与爱好者资源 |
| [embedded-boston/awesome-embedded-systems](https://github.com/embedded-boston/awesome-embedded-systems)（约 1k） | RTOS、库、模块、参考 |

## 二、中文入门

| 资源 | 说明 |
| --- | --- |
| [wujique/stm32_tech](https://github.com/wujique/stm32_tech)（约 69） | 基于 STM32F103 的嵌入式入门教学 |
| [Lighter-z/51-Single-chip](https://github.com/Lighter-z/51-Single-chip)（约 546） | 51 单片机入门资料 |
| [zhangshengasdf/embedded-stm32](https://github.com/zhangshengasdf/embedded-stm32)（约 3） | STM32 HAL + 寄存器双视角 + Wokwi 仿真 |
| [MorkenMooooo/SovereignEngine](https://github.com/MorkenMooooo/SovereignEngine)（约 6） | ESP-IDF 入门：GPIO → FreeRTOS → UART → 中断 |

## 三、项目参考（看别人怎么组织，不要直接抄）

| 资源 | 说明 |
| --- | --- |
| [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)（约 32k） | ESP32 语音聊天机器人，看音频链路、设备端/服务端分工 |
| [stack-chan/stack-chan](https://github.com/stack-chan/stack-chan)（约 1.8k） | 小型表情机器人，看舵机与桌面形态 |
| [pollen-robotics/reachy_mini](https://github.com/pollen-robotics/reachy_mini)（约 1.6k） | 开源表情机器人 SDK，看动作/表情原语 |
| [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber)（约 14.5k） | 语音 + Live2D 陪伴，看语音打断与适配层 |

## 四、官方文档（最终以这里为准）

- Arduino：https://docs.arduino.cc/
- ESP32 Arduino Core：https://docs.espressif.com/projects/arduino-esp32/en/latest/
- Espressif 文档：https://docs.espressif.com/
- STM32：https://www.st.com/
- PlatformIO：https://docs.platformio.org/
- KiCad（以后画 PCB）：https://www.kicad.org/

## 五、仿真器（没有硬件也能练）

- Wokwi：https://wokwi.com/ （ESP32/Arduino 仿真，适合练逻辑）
- Tinkercad Circuits：https://www.tinkercad.com/circuits （图形化，适合入门）
- Falstad Circuit Simulator：https://www.falstad.com/circuit/ （看电路波形）

## 六、书

| 书 | 适合 |
| --- | --- |
| 《Make: Electronics》Charles Platt | 零基础电子，图多、动手多 |
| 《Code》Charles Petzold | 从电到逻辑门到计算机，补底层直觉 |
| 《Arduino Cookbook》Michael Margolis | 查具体用法，不必从头读 |
| 《The Art of Electronics》Horowitz & Hill | 以后当参考书，初学不要硬啃 |
| 《计算机组成原理》 | 以后补体系结构 |

## 七、视频与搜索词

不绑定具体链接，避免失效；用搜索词找当前最好的版本：

- Ben Eater（数字逻辑、计算机组成）
- 硬件茶谈（电子基础、硬件科普）
- 野火 / 正点原子（STM32 教程）
- GreatScott（电子项目）
- 关键词：`STM32 HAL 入门`、`ESP32 Arduino 教程`、`I2C OLED 接线`、`继电器 驱动 电路`、`PID 入门`

## 八、造手机相关

- iFixit 拆解：https://www.ifixit.com/Teardown （看真实结构、排线、电池、模块化）
- 选一个手机 SoC/传感器 datasheet，看电源、时钟、接口、封装。
- 通信基础：调制、频段、天线、信噪比；先建立概念，不要求推导。
- 制造：SMT、组装、校准、测试、良率、认证；搜“手机 生产线 流程”“SMT 贴片 流程”。

## 九、面试相关

- 本仓库 [04 自动化](04-automation.md)、[05 造手机](05-how-a-phone-is-made.md)、[06 面试问答](06-interview-qa.md)。
- 把每个概念压缩成“定义 → 组成 → 例子 → 取舍 → 我的理解”。

## 十、怎么筛选资源

- 先看目录和更新时间；太旧的教程可能用的库已不兼容。
- 优先官方文档和 datasheet；教程只用来入门。
- 一门课看不懂就换一门，但不要同时开五门。
- 每看 20 分钟，至少动手 10 分钟。
- 收藏夹不是进度；[PROGRESS.md](../PROGRESS.md) 才是。

## 说明

以上 Star 数为 2026-10-30 检索值，会变化。外部链接与资源归原作者所有；复用代码前确认 LICENSE。本仓库不隶属于任何机构或厂商。
