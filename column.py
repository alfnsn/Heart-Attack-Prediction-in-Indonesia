NUMERIK = [
    "age","cholesterol_level","waist_circumference","sleep_hours",
    "blood_pressure_systolic","blood_pressure_diastolic",
    "fasting_blood_sugar","cholesterol_hdl","cholesterol_ldl","triglycerides"
]
MULTIKELAS_OHE = [
    "income_level", "smoking_status","alcohol_consumption", "physical_activity",
    "dietary_habits", "air_pollution_exposure","stress_level"
]
LABELENC_BINER_3 = ["gender", "region", "EKG_results"]
BINER_LAIN = [
    "hypertension","diabetes","obesity","family_history",
    "previous_heart_disease","medication_usage","participated_in_free_screening"
]
KATEGORIK = LABELENC_BINER_3 + MULTIKELAS_OHE + BINER_LAIN