display_names = {
    "age": "Usia (tahun)",
    "cholesterol_level": "Kadar Kolesterol (mg/dL)",
    "waist_circumference": "Lingkar Pinggang (cm)",
    "sleep_hours": "Jam Tidur (jam)",
    "blood_pressure_systolic": "Tekanan Darah Sistolik (mmHg)",
    "blood_pressure_diastolic": "Tekanan Darah Diastolik (mmHg)",
    "fasting_blood_sugar": "Gula Darah Ketika Puasa (mg/dL)",
    "cholesterol_hdl": "Kolesterol HDL (mg/dL)",
    "cholesterol_ldl": "Kolesterol LDL (mg/dL)",
    "triglycerides": "Trigliserida (mg/dL)",

    "gender": "Jenis Kelamin",
    "region": "Wilayah",
    "income_level": "Tingkat Pendapatan",
    "smoking_status": "Status Merokok",
    "alcohol_consumption": "Konsumsi Alkohol",
    "physical_activity": "Aktivitas Fisik",
    "dietary_habits": "Pola Makan",
    "air_pollution_exposure": "Paparan Polusi Udara",
    "stress_level": "Tingkat Stres",
    "EKG_results": "Hasil EKG",
    "hypertension": "Hipertensi",
    "diabetes": "Diabetes",
    "obesity": "Obesitas",
    "family_history": "Riwayat Keluarga (Ada Yang Terkena Penyakit Jantung)",
    "previous_heart_disease": "Penyakit Jantung Sebelumnya",
    "medication_usage": "Sedang / Pernah Menggunakan Obat",
    "participated_in_free_screening": "Ikut Skrining Gratis"
}

ohe_map = {
    "income_level": {"Rendah": "Low", "Menengah": "Middle", "Tinggi": "High"},
    "smoking_status": {"Tidak Merokok": "Never", "Mantan Perokok": "Past", "Perokok Aktif": "Current"},
    "alcohol_consumption": {"Tidak": "None", "Sedang": "Moderate", "Tinggi": "High"},
    "physical_activity": {"Rendah": "Low", "Sedang": "Moderate", "Tinggi": "High"},
    "dietary_habits": {"Sehat": "Healthy", "Tidak Sehat": "Unhealthy"},
    "air_pollution_exposure": {"Rendah": "Low", "Sedang": "Moderate", "Tinggi": "High"},
    "stress_level": {"Rendah": "Low", "Sedang": "Moderate", "Tinggi": "High"},
}

labelenc_map = {
    "gender": {"Perempuan": 0, "Laki-laki": 1},
    "region": {"Pedesaan": 0, "Perkotaan": 1},
    "EKG_results": {"Abnormal": 0, "Normal": 1},
}

bin_map = {"Tidak": 0, "Iya": 1}