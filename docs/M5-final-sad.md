# M5 — Tài liệu Kiến trúc Phần mềm Hoàn chỉnh (Final Software Architecture Document - SAD)

## 1. Tổng quan Kiến trúc (Architecture Overview)
AgriSense áp dụng mô hình **Edge-Cloud Hybrid IoT Architecture**, phân tách rõ trách nhiệm giữa tầng Biên (`edge-gateway`) và tầng Đám mây (`cloud-ingestion`, `device-shadow-svc`, `dashboard-ui`).

## 2. Ánh xạ 1-1 giữa C4 Container View và Mã nguồn (M4 Prototype)

| Container (C4 Level 2) | Thư mục mã nguồn (`src/`) | Công nghệ chính | Trách nhiệm |
| :--- | :--- | :--- | :--- |
| **Sensor Simulator** | `src/sensor-simulator/` | Python / AsyncIO | Giả lập >= 1.000 cảm biến (MQTT & HTTP) và kịch bản Thundering Herd |
| **Edge Gateway** | `src/edge-gateway/` | Python + SQLite | Local Rule Engine tự trị khi mất mạng + Store-and-Forward Buffer |
| **Cloud Ingestion** | `src/cloud-ingestion/` | Eclipse Mosquitto + Adapter + Processor | Tiếp nhận gói tin MQTT/HTTP, chuẩn hóa dữ liệu và xử lý luồng |
| **Device Shadow Service** | `src/device-shadow-svc/` | FastAPI / Node.js | Quản lý trạng thái van (`desired`/`reported`), xác thực Auth, OTA và AI API |
| **Dashboard UI** | `src/dashboard-ui/` | React / Grafana | Giao diện theo dõi thông số thời gian thực và điều khiển van tưới |

## 3. Danh mục Quyết định Kiến trúc (ADR Index)
- [ADR-001: Kiến trúc phân tầng Edge-Cloud và Local Autonomy](../adr/adr-001.md)
- [ADR-002: Sử dụng SQLite làm Store-and-Forward Buffer tại Edge Gateway](../adr/adr-002.md)
- [ADR-003: Giao thức truyền thông MQTT kết hợp HTTP Protocol Adapter](../adr/adr-003.md)
- [ADR-004: Quản lý trạng thái thiết bị bằng mẫu Device Shadow (Desired/Reported)](../adr/adr-004.md)
- [ADR-005: Chiến lược kiểm soát Thundering Herd bằng Jittered Backoff & Batching](../adr/adr-005.md)
- [ADR-006: Bảo mật lệnh điều khiển van và xác thực thiết bị (Auth & Command Signing)](../adr/adr-006.md)

## 4. Kết quả Kiểm chứng Thực nghiệm (QA Verification Summary)
- **Kịch bản mất mạng (`tests/network-cut-test.sh`):** Đạt (0% mất dữ liệu, van tưới tự động kích hoạt tại Edge).
- **Kịch bản lệnh giả mạo (`tests/rogue-cmd-test.py`):** Đạt (100% lệnh không có chữ ký/token hợp lệ bị từ chối).
