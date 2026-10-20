import numpy as np
import json
from datetime import datetime

print("==================================================================")
print(" AI-BASED DEFORESTATION DRIVER CLASSIFICATION SYSTEM")
print(" Narasumber : Dr. Bart Slachter (Wageningen University)")
print(" Mata Kuliah: Informatics Practitioner Lecture Series 2026")
print(" Penyusun   : Aldi Mulya Fajar (G1A025091 - S1 Informatika UNIB)")
print("==================================================================\n")

# 1. Dataset Simulasi Peringatan Dini Deforestasi & Fitur Spasial
print("[INFO] Tahap 1: Memuat Data Indikator Spasial & Peringatan Dini Hutan...")

# Kelas Penyebab Deforestasi
class_names = [
    "Pertanian Skala Kecil", 
    "Pertanian Skala Besar", 
    "Pembalakan Selektif", 
    "Pertambangan", 
    "Kebakaran Hutan"
]

# Data Sampel Peringatan Dini (Simulasi Fitur Citra Radar Sentinel-1 & Optik Sentinel-2)
alerts_data = [
    {"id": "ALT-101", "region": "Asia Tenggara (Bengkulu)", "driver_pred": "Pertanian Skala Kecil", "confidence": 0.92, "area_ha": 2.5},
    {"id": "ALT-102", "region": "Amerika Selatan (Amazon)", "driver_pred": "Pertanian Skala Besar", "confidence": 0.97, "area_ha": 150.0},
    {"id": "ALT-103", "region": "Afrika Tengah (Kongo)", "driver_pred": "Pembalakan Selektif", "confidence": 0.88, "area_ha": 12.0},
    {"id": "ALT-104", "region": "Asia Tenggara (Kalimantan)", "driver_pred": "Pertambangan", "confidence": 0.95, "area_ha": 45.0},
    {"id": "ALT-105", "region": "Amerika Selatan (Cerrado)", "driver_pred": "Kebakaran Hutan", "confidence": 0.99, "area_ha": 310.0}
]

for alert in alerts_data:
    print(f"Peringatan [{alert['id']}] - Wilayah: {alert['region']}")
    print(f"  - Prediksi Penyebab (Driver) : {alert['driver_pred']}")
    print(f"  - Tingkat Keyakinan AI (Conf): {alert['confidence']*100:.1f}%")
    print(f"  - Estimasi Luas Gangguan      : {alert['area_ha']} Hektar")
    print("-" * 66)

# 2. Rekapitulasi Statistik Klasifikasi Penyebab Deforestasi
print("\n[INFO] Tahap 2: Evaluasi Distribusi Penyebab Deforestasi Global...")
total_area_affected = sum(item["area_ha"] for item in alerts_data)

summary_by_driver = {}
for alert in alerts_data:
    driver = alert["driver_pred"]
    summary_by_driver[driver] = summary_by_driver.get(driver, 0) + alert["area_ha"]

for driver, area in summary_by_driver.items():
    percentage = (area / total_area_affected) * 100
    print(f"  * {driver}: {area} Hektar ({percentage:.1f}% dari total gangguan)")

# 3. Menyusun Laporan Format JSON untuk Integrasi Platform Global Nature Watch
evaluation_report = {
    "metadata": {
        "project_title": "AI-Based Deforestation Driver Classification Report",
        "author": "Aldi Mulya Fajar",
        "npm": "G1A025091",
        "study_program": "S1 Informatika - Universitas Bengkulu",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    "classification_classes": class_names,
    "total_alerts_processed": len(alerts_data),
    "total_area_affected_hectares": total_area_affected,
    "alerts_summary": alerts_data
}

print("\n==================================================================")
print(" LAPORAN AKHIR FORMAT JSON (GLOBAL NATURE WATCH INTEGRATION)")
print("==================================================================")
print(json.dumps({
    "metadata": evaluation_report["metadata"],
    "total_alerts_processed": evaluation_report["total_alerts_processed"],
    "total_area_affected_hectares": evaluation_report["total_area_affected_hectares"]
}, indent=2))
print("==================================================================\n")
print("[SUCCESS] Pipeline klasifikasi gangguan hutan selesai dieksekusi!")