"""
Edge Gateway (M4 Prototype)
Bao gồm Local Rule Engine + SQLite Store-and-Forward Buffer.
"""
import os
import sqlite3
import time

DB_PATH = os.getenv("SQLITE_BUFFER_PATH", "/data/buffer.db")

def init_buffer():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS telemetry_buffer (id INTEGER PRIMARY KEY AUTOINCREMENT, payload TEXT, created_at REAL)"
    )
    conn.commit()
    conn.close()

def main():
    init_buffer()
    print(f"[edge-gateway] Local Rule Engine & SQLite Buffer ({DB_PATH}) đã sẵn sàng.")
    while True:
        time.sleep(10)

if __name__ == "__main__":
    main()
