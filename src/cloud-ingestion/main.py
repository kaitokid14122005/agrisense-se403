"""
Cloud Ingestion (M4 Prototype)
MQTT Consumer + HTTP Protocol Adapter + Stream Processor.
"""
import time

def main():
    print("[cloud-ingestion] Protocol Adapter & Stream Processor đang lắng nghe...")
    while True:
        time.sleep(10)

if __name__ == "__main__":
    main()
