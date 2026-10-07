from flask import Flask, request, jsonify
from datetime import datetime, timezone, timedelta
import csv
import os

app = Flask(__name__)
CSV_PATH = "data_log.csv"
KST = timezone(timedelta(hours=9))

if not os.path.exists(CSV_PATH):
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["timestamp_kst", "timestamp_utc", "device_ip", "ambient_c", "object_c"])

@app.post("/api/sensor")
def ingest():
    data = request.get_json(force=True, silent=True) or {}
    ambient = data.get("ambient_c")
    obj = data.get("object_c")

    ts_utc = datetime.now(timezone.utc)
    ts_kst = ts_utc.astimezone(KST)

    device_ip = request.remote_addr

    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([ts_kst.isoformat(), ts_utc.isoformat(), device_ip, ambient, obj])

    return jsonify({
        "ok": True,
        "stored_at_kst": ts_kst.isoformat(),
        "stored_at_utc": ts_utc.isoformat()
    })

@app.get("/api/latest")
def latest():
    try:
        with open(CSV_PATH, "r", encoding="utf-8") as f:
            lines = f.read().strip().splitlines()
        if len(lines) <= 1:
            return jsonify({"ok": False, "message": "no data"})
        last = lines[-1].split(",")
        return jsonify({
            "ok": True,
            "timestamp_kst": last[0],
            "timestamp_utc": last[1],
            "device_ip": last[2],
            "ambient_c": last[3],
            "object_c": last[4],
        })
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
