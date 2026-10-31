# M3 — Đánh giá Kiến trúc theo ATAM (Architecture Tradeoff Analysis Method)

## 1. Cây Tiện ích (Utility Tree)
- **Availability (High, High):** Hoạt động độc lập tại biên (Edge Autonomy) khi đứt kết nối WAN (QA-01).
- **Scalability (High, High):** Chịu tải >= 1.000 cảm biến và hiện tượng Thundering Herd khi kết nối lại (QA-02).
- **Security (High, Medium):** Chống lệnh điều khiển van giả mạo (QA-03).
- **Modifiability (Medium, Low):** Hỗ trợ đa giao thức MQTT & HTTP qua Protocol Adapter (QA-04).

## 2. Phân tích Điểm Nhạy cảm (Sensitivity Points) & Điểm Đánh đổi (Trade-off Points)

| Quyết định Kiến trúc | Sensitivity Point | Trade-off Point |
| :--- | :--- | :--- |
| **Store-and-Forward tại Edge Gateway (SQLite)** | Dung lượng lưu trữ và tốc độ ghi I/O của SQLite ảnh hưởng trực tiếp tới khả năng không mất dữ liệu khi mất mạng kéo dài | Tăng **Availability** & **Data Integrity** tại biên nhưng đánh đổi bằng **Eventual Consistency** trên Cloud Dashboard và nguy cơ **Thundering Herd** khi mạng khôi phục |
| **Device Shadow Pattern (desired / reported)** | Thời gian đồng bộ trạng thái giữa Cloud và Edge | Tăng **Reliability** và tách biệt giao diện người dùng khỏi độ trễ vật lý, nhưng làm tăng độ phức tạp xử lý xung đột trạng thái (State Reconciliation) |
| **MQTT Broker + Stream Processor** | Cấu hình QoS (QoS 0 vs QoS 1) trên MQTT | Dùng QoS 1 đảm bảo **Reliability** (at-least-once) nhưng tăng **Latency** và băng thông so với QoS 0 |

## 3. Rủi ro (Risks) & Phi rủi ro (Non-Risks)
- **Risk R1:** Khi mất mạng lâu ngày, lệnh `desired` trên Cloud của người dùng có thể xung đột với quyết định tự động của `Local Rule Engine` tại Edge.
- **Mitigation:** Quy định rõ mức độ ưu tiên và timestamp/version trong Device Shadow (xem `adr-004.md`).
