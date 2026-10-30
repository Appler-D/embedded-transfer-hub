# 术语表

| 中文 | English | 一句话 |
| --- | --- | --- |
| 电压 | voltage | 两点电势差，单位 V |
| 电流 | current | 电荷流动速率，单位 A |
| 电阻 | resistance | 对电流的阻碍，单位 Ω |
| 地 | ground / GND | 电路的参考 0V；所有信号相对它测量 |
| 电源正 | VCC / VDD | 供电正极；注意 3.3V/5V |
| 欧姆定律 | Ohm's law | V = I × R |
| 功率 | power | P = V × I |
| 分压 | voltage divider | 用两个电阻取一部分电压 |
| 上拉/下拉 | pull-up / pull-down | 给悬空输入确定电平 |
| 去抖 | debounce | 消除按键机械抖动 |
| 模拟信号 | analog signal | 连续变化的信号 |
| 数字信号 | digital signal | 用高低电平表示 0/1 |
| 模数转换 | ADC | 模拟电压 → 数字量 |
| 数模转换 | DAC | 数字量 → 模拟电压 |
| 脉宽调制 | PWM | 用占空比控制平均功率 |
| 占空比 | duty cycle | 高电平时间占周期的比例 |
| 采样率 | sample rate | 每秒采样次数 |
| 分辨率 | resolution | ADC 能区分的最小电压变化 |
|  GPIO | general-purpose input/output | 通用输入输出引脚 |
| 中断 | interrupt | 事件触发，打断当前流程 |
| 轮询 | polling | 主循环反复检查状态 |
| 定时器 | timer | 计数/定时/PWM/捕获 |
| 看门狗 | watchdog | 程序卡死时复位 |
| 直接内存访问 | DMA | 外设与内存直接搬数据，减少 CPU 占用 |
| 串口 | UART | 异步串行通信 |
| I2C | Inter-Integrated Circuit | 两线、带地址、多设备总线 |
| SPI | Serial Peripheral Interface | 四线、高速、主从总线 |
| CAN | Controller Area Network | 汽车/工业多节点总线 |
| 单片机 | MCU | 集成 CPU/Flash/RAM/外设的芯片 |
| 片上系统 | SoC | 把更多功能集成到一颗芯片 |
| 单板计算机 | SBC | 跑 Linux 的小型计算机，如树莓派 |
| 可编程逻辑控制器 | PLC | 工业控制器，模块化、抗干扰 |
| 固件 | firmware | 跑在设备上的底层软件 |
| 启动程序 | bootloader | 上电后先运行，负责加载/升级固件 |
| 实时操作系统 | RTOS | 以任务调度保证实时性的操作系统 |
| 裸机 | bare metal | 没有操作系统，直接跑主循环 |
| 硬件抽象层 | HAL | 对寄存器的封装，便于移植 |
| 数据手册 | datasheet | 芯片/器件的电气与使用说明 |
| 印制电路板 | PCB | 承载并连接元件的板子 |
| 柔性电路板 | FPC | 可弯折的电路板 |
| 表面贴装 | SMT | 把元件焊到 PCB 表面的工艺 |
| 物料清单 | BOM | 项目需要的元件/数量/规格 |
| 电磁兼容 | EMC | 不干扰别人、也不被别人干扰 |
| 静电放电 | ESD | 静电损坏器件；操作要防静电 |
| 射频 | RF | 无线通信相关的高频电路 |
| 基带 | baseband | 通信协议处理部分 |
| 电源管理 | PMIC | 多路电源、充电、电池保护 |
| 图像信号处理 | ISP | 相机数据处理 |
| 传感器 | sensor | 物理量 → 电信号 |
| 执行器 | actuator | 电信号 → 动作 |
| 开环 | open loop | 不测量结果，按预设执行 |
| 闭环 | closed loop | 测量结果并修正 |
| 比例-积分-微分 | PID | 常用闭环控制算法 |
| 滞回 | hysteresis | 用两个阈值避免临界抖动 |
| 状态机 | state machine | 用状态和转移组织逻辑 |
| 实时性 | real-time | 在截止时间内完成响应 |
| 延迟 | latency | 从输入到输出的时间 |
| 抖动 | jitter | 时间/周期的不稳定 |
| 掉压 | brownout | 电源电压瞬间跌落导致复位 |
| 共地 | common ground | 不同模块共享参考地 |
| 去耦电容 | decoupling capacitor | 靠近芯片电源脚，滤瞬态电流 |
| 续流二极管 | flyback diode | 给电感/继电器线圈提供泄放回路 |

面试时不必背英文缩写全称，但要能用自己的话解释它解决什么问题。
