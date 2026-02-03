"""
PlethoAI — Contextual, Ethical Clinical Logic

PlethoAI is an evolving clinical reasoning engine designed to honor the full
complexity of human health. It rejects reductive, essentialist approaches to
race and identity, and instead centers context, lived experience, and structural
factors as meaningful components of care.

This project began as a simple triage exercise and is growing into a modular,
population-aware framework that can incorporate cultural identity, community
background, environmental exposures, and situational factors such as veteran
status or chronic stress. PlethoAI does not treat identity as biology; it treats
identity as context — a lens through which care is shaped, not predetermined.

The long-term vision is to build a transparent, ethical, and adaptable clinical
logic system that can support education, research, and equitable health-tech
innovation without reinforcing historical biases or flattening the diversity of
human experience.
"""

def extract_data(patient):
    name = patient["name"]
    age = patient["age"]
    gender = patient["gender"]
    ethnicity = patient["ethnicity"]
    systolic = patient["systolic_bp"]
    diastolic = patient["diastolic_bp"]
    heart_rate = patient["heart_rate"]
    temperature = patient["temperature_c"]
    glucose = patient["glucose_count"]
    hemoglobin = patient["hemoglobin_count"]
    return name, age, gender, ethnicity, systolic, diastolic, heart_rate, temperature, glucose, hemoglobin

def create_flags(age, temperature, systolic, diastolic, heart_rate, glucose, hemoglobin):
    fever = temperature >= 38
    senior = age >= 70
    child = age <= 10
    highSBP = systolic > 130
    highDBP = diastolic > 80
    tachy_flag = heart_rate > 100
    diabetes_flag = 80 < glucose < 130
    anemia_flag = hemoglobin < 12.5
    return {
        "fever": fever,
        "senior": senior,
        "child": child,
        "highSBP": highSBP,
        "highDBP": highDBP,
        "tachy_flag": tachy_flag,
        "diabetes_flag": diabetes_flag,
        "anemia_flag": anemia_flag
    }

def triage_patient(flags):
    fever = flags["fever"]
    senior = flags["senior"]
    child = flags["child"]
    highSBP = flags["highSBP"]
    highDBP = flags["highDBP"]
    tachy_flag = flags["tachy_flag"]
    diabetes_flag = flags["diabetes_flag"]
    anemia_flag = flags["anemia_flag"]

    if fever and senior and highSBP and highDBP:
        triage = "X HIGH RISK"
    elif fever and child:
        triage = "X HIGH RISK"
    elif tachy_flag and highSBP and highDBP:
        triage = "HIGH RISK"
    elif anemia_flag:
        triage = "MONITOR"
    elif diabetes_flag:
        triage = "HIGH RISK"
    elif fever and tachy_flag:
        triage = "MODERATE RISK"
    elif senior:
        triage = "MONITOR"
    else:
        triage = "Stable"

    return triage

def process_patient(patient):
    name, age, gender, ethnicity, systolic, diastolic, heart_rate, temperature, glucose, hemoglobin = extract_data(patient)
    flags = create_flags(age, temperature, systolic, diastolic, heart_rate, glucose, hemoglobin)
    triage = triage_patient(flags)
    print(f"Patient: {name}")
    print(f"Triage Category: {triage}")
    print("------------♥------------")