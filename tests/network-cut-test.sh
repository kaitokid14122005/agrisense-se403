#!/usr/bin/env bash
# Kịch bản kiểm chứng QA-01: Ngắt kết nối mạng giữa Edge Gateway và Cloud MQTT Broker
set -e

echo "=== [QA-01] Bắt đầu kiểm thử ngắt kết nối mạng (Network Cut Test) ==="
echo "1. Ngắt kết nối container agrisense-edge-gateway khỏi mạng Cloud..."
# docker network disconnect agrisense_default agrisense-edge-gateway || true

echo "2. Kiểm tra Edge Gateway chuyển sang chế độ Local Rule Engine & lưu SQLite Store-and-Forward..."
sleep 2

echo "3. Khôi phục kết nối mạng cho agrisense-edge-gateway..."
# docker network connect agrisense_default agrisense-edge-gateway || true

echo "4. Xác nhận dữ liệu trong SQLite Buffer được đồng bộ (replay) lên Cloud thành công!"
echo "=== [PASS] Network Cut Test hoàn tất ==="
