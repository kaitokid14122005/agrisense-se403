# M1 — Architectural Drivers (AgriSense)

## 1. Mục tiêu Nghiệp vụ (Business Goals)
- Tự động hóa giám sát độ ẩm đất, nhiệt độ, độ ẩm không khí và điều khiển van tưới cho nông trại quy mô lớn (>= 1.000 cảm biến).
- Đảm bảo cây trồng vẫn được tưới tự động ngay cả khi mất kết nối Internet từ nông trại lên Cloud (Local Autonomy).

## 2. Kịch bản Thuộc tính Chất lượng (Quality Attribute Scenarios - QAS)

| ID | Thuộc tính (QA) | Tác nhân (Source) | Kích thích (Stimulus) | Môi trường (Environment) | Thành phần (Artifact) | Phản hồi (Response) | Đo lường (Response Measure) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **QA-01** | Availability / Resilience | Đường truyền WAN | Đứt kết nối Internet giữa Nông trại và Cloud | Đang vận hành bình thường | `edge-gateway` | Tự động chuyển sang chế độ Local Rule Engine và lưu dữ liệu cảm biến vào SQLite Buffer | Không mất bản tin nào trong tối đa 72h; van tưới bật/tắt nội bộ trong `< 2 giây` |
| **QA-02** | Scalability / Performance | >= 1.000 cảm biến + Edge Gateway | Đồng loạt đẩy dữ liệu định kỳ & xả bộ đệm sau khi có mạng lại (Thundering Herd) | Tải đỉnh (Peak load) | `cloud-ingestion` | Tiếp nhận và xử lý bất đồng bộ qua MQTT Broker & Stream Processor | Độ trễ xử lý p95 `< 500ms`, tỷ lệ rớt gói `0%` |
| **QA-03** | Security | Kẻ tấn công / Thiết bị giả mạo | Gửi lệnh điều khiển mở/đóng van trái phép (Rogue Command) | Vận hành thực tế | `device-shadow-svc` & `edge-gateway` | Xác thực token/chữ ký lệnh, từ chối và ghi log cảnh báo bảo mật | `100%` lệnh không hợp lệ bị chặn (HTTP 401/403 hoặc MQTT ACL deny) |
| **QA-04** | Modifiability / Interoperability | Cảm biến đa giao thức | Bổ sung cảm biến gửi dữ liệu qua cả MQTT và HTTP | Mở rộng phần cứng | `cloud-ingestion` / `edge-gateway` | Protocol Adapter chuẩn hóa payload về định dạng thống nhất | Thêm giao thức mới không phải sửa đổi Stream Processor hay Shadow Service |
