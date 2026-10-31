# 项目 3：ESP32 联网节点

> 目标：ESP32 采集传感器数据，通过 Wi-Fi 上报到电脑/手机/本地服务。
> 难度 ★★★；1–2 天；成本约 100–150 元。

## BOM

| 数量 | 物料 | 备注 |
| --- | --- | --- |
| 1 | ESP32 | 2.4GHz Wi-Fi |
| 1 | 传感器 | 温湿度/光敏/土壤任选 |
| 1 | 电脑/手机 | 跑本地 HTTP 服务或 MQTT Broker |

## 两条路线

### A. HTTP POST（最容易）

```text
ESP32 → Wi-Fi → HTTP POST JSON → 本地 Python/Node 服务 → 打印/存 CSV
```

- ESP32：`WiFi.h` + `HTTPClient.h` + 手写 JSON（或 ArduinoJson）。
- 电脑：Python `http.server`/Flask/FastAPI 收 POST，打印 JSON。
- 优点：简单、可调试；缺点：每次都要建连接，功耗高。

### B. MQTT（更像 IoT）

```text
ESP32 → Wi-Fi → MQTT Broker → 订阅端/数据库/看板
```

- ESP32：`PubSubClient`；电脑：Mosquitto。
- 优点：长连接、发布/订阅；缺点：要跑 Broker/配置。

## 数据格式

```json
{"node":1,"temp_c":23.45,"humidity_pct":55.2,"soil_pct":41.3,"uptime_ms":12345}
```

- 时间戳由服务端加；ESP32 可 NTP 对时。
- 不要把所有小数都发；温度 2 位、湿度 1 位就够。

## 步骤

1. 先跑 Wi-Fi 连接示例，串口打印 IP。
2. 电脑起一个本地 HTTP 服务，浏览器能访问。
3. ESP32 POST 一条固定 JSON；电脑打印。
4. 加传感器读数；确认 JSON 合法。
5. 加失败处理：Wi-Fi 断了重连、HTTP 非 200 重试/退避。
6. 记录：串口日志、服务端日志、失败与修正。

## 常见失败

| 现象 | 可能原因 |
| --- | --- |
| 连不上 Wi-Fi | 2.4GHz、密码、热点隔离、信号弱 |
| POST 失败 | IP/端口、防火墙、HTTP/HTTPS、URL 路径 |
| JSON 解析失败 | 引号/逗号、Content-Type、编码 |
| 运行一会掉线 | 电源、看门狗、Wi-Fi 省电、内存泄漏 |
| 时间戳不对 | 没 NTP、时区 |

## 面试三句话

1. 这是端到端系统：传感器 → MCU → Wi-Fi → 服务端 → 可视化/存储。
2. 我处理了配网、断线重连、HTTP 状态码和 JSON 格式。
3. 下一步可以加 OTA、低功耗/深睡、离线缓存。

## 安全

- 不要把 Wi-Fi 密码/API key 提交到 GitHub；用 `secrets.h` 并 gitignore。
- 本地服务只开必要端口；不要暴露到公网。
- 低压供电；USB 电源要够。
