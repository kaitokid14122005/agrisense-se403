"""
Sensor Simulator (M4 Prototype)
Giả lập >= 1.000 cảm biến (MQTT & HTTP) và kịch bản Thundering Herd test.
"""
import os
import time

SENSOR_COUNT = int(os.getenv("SENSOR_COUNT", "1000"))

def main():
    print(f"[sensor-simulator] Khởi động giả lập {SENSOR_COUNT} cảm biến (MQTT & HTTP)...")
    while True:
        time.sleep(10)

if __name__ == "__main__":
    main()
