# AgriSense — SE403 Software Architecture Project

Hệ thống IoT Nông nghiệp thông minh (Smart Agriculture IoT Architecture) được thiết kế theo hướng tiếp cận **Attribute-Driven Design (ADD)** và mô hình **C4 Model**.

## Cấu trúc thư mục

```text
agrisense-se403/
├── docs/                  # Tài liệu M1 (Drivers), M3 (ATAM), M5 (Final SAD)
├── adr/                   # Chứa 6 file ADR (adr-001.md -> adr-006.md)
├── diagrams/              # Mã nguồn PlantUML/Mermaid cho C4 (L1, L2, L3), Deployment, Sequence
├── src/                   # Mã nguồn Prototype (M4) ánh xạ 1-1 với Container View
│   ├── sensor-simulator/  # Giả lập >= 1.000 cảm biến (MQTT & HTTP) + Thundering Herd test
│   ├── edge-gateway/      # Local Rule Engine + SQLite Store-and-Forward Buffer
│   ├── cloud-ingestion/   # MQTT Broker + Protocol Adapter + Stream Processor
│   ├── device-shadow-svc/ # Quản lý trạng thái van (desired/reported) + Auth/OTA + AI API
│   └── dashboard-ui/      # Giao diện giám sát thời gian thực (Grafana hoặc React Web UI)
├── tests/                 # Script kiểm chứng QA (network-cut-test.sh, rogue-cmd-test.py)
├── docker-compose.yml     # Khởi chạy toàn bộ hệ thống bằng 1 lệnh duy nhất
└── ai-log.md              # Nhật ký sử dụng AI xuyên suốt các mốc M1 -> M5
```

## Khởi chạy nhanh

```bash
docker compose up --build -d
```

## Kiểm thử Quality Attributes (QA Tests)

- **Kiểm thử mất kết nối mạng (Store-and-Forward & Local Autonomy):**
  ```bash
  bash tests/network-cut-test.sh
  ```
- **Kiểm thử bảo mật lệnh điều khiển trái phép (Security / Rogue Command):**
  ```bash
  python tests/rogue-cmd-test.py
  ```
