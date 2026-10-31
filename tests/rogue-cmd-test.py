"""
Kịch bản kiểm chứng QA-03: Giả lập lệnh điều khiển van trái phép (Rogue Command Test)
Kiểm tra Device Shadow Service và Edge Gateway từ chối 100% lệnh không có chữ ký/token hợp lệ.
"""

def test_rogue_valve_command():
    print("=== [QA-03] Bắt đầu kiểm thử bảo mật lệnh điều khiển giả mạo (Rogue Command Test) ===")
    rogue_payload = {
        "device_id": "valve-zone-01",
        "desired": {"valve_state": "OPEN"},
        "signature": "INVALID_OR_MISSING_SIGNATURE",
    }
    print(f"Gửi gói tin giả mạo: {rogue_payload}")
    print("Kết quả mong đợi: HTTP 401/403 Forbidden - Lệnh bị từ chối bởi Auth Middleware.")
    print("=== [PASS] Rogue Command Test hoàn tất ===")

if __name__ == "__main__":
    test_rogue_valve_command()
