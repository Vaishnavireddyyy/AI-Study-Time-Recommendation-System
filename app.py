import streamlit as st
from tensorflow.keras.models import load_model
import joblib
import numpy as np
import pandas as pd

# Load model
model = load_model("study_model.h5", compile=False)
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="AI Study Timetable Generator", layout="wide")

st.title("🤖 AI Study Timetable Generator")
st.write("Enter your subject details to generate a personalized study timetable.")

# ------------------------------
# SESSION STATE
# ------------------------------
if "generate" not in st.session_state:
    st.session_state.generate = False

# ------------------------------
# FUNCTION
# ------------------------------
def convert_time(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours} hrs {mins} mins" if hours > 0 else f"{mins} mins"

# ------------------------------
# SUBJECT INPUT
# ------------------------------
num_subjects = st.number_input("How many subjects?", 1, 10, 3)

subjects = []
scores = []

st.subheader("📘 Enter Subject Details")

for i in range(num_subjects):
    col1, col2 = st.columns(2)

    with col1:
        subject = st.text_input(f"Subject {i+1}")

    with col2:
        score = st.number_input(f"Marks {i+1}", 0, 100, 60)

    subjects.append(subject.strip())
    scores.append(score)

# ------------------------------
# EXAM INFO
# ------------------------------
st.subheader("📅 Exam Info")

days_left = st.number_input("Days left", 1, 60, 7)
hours_per_day = st.number_input("Hours per day", 1, 12, 6)

# ------------------------------
# BUTTON
# ------------------------------
if st.button("Generate AI Timetable"):
    st.session_state.generate = True

# ------------------------------
# PROCESS
# ------------------------------
if st.session_state.generate:

    difficulty = []

    for score in scores:
        input_data = np.array([[score, 80, 7, 5, 5, 3]])
        input_scaled = scaler.transform(input_data)
        pred = model.predict(input_scaled, verbose=0)[0][0]
        difficulty.append(abs(pred))

    # Hardest subject
    max_index = difficulty.index(max(difficulty))
    hardest_subject = subjects[max_index]

    st.warning(f"⚠️ Focus more on **{hardest_subject}** (highest difficulty)")

    # Chart
    df = pd.DataFrame({"Subject": subjects, "Difficulty": difficulty})
    df = df[df["Subject"] != ""]
    st.bar_chart(df.set_index("Subject"))

    # Time allocation
    total_diff = sum(difficulty)
    study_minutes = [(d / total_diff) * hours_per_day * 60 for d in difficulty]

    # Combine + sort
    data = []
    for i in range(num_subjects):
        if subjects[i] != "":
            data.append((subjects[i], difficulty[i], study_minutes[i]))

    data.sort(key=lambda x: x[1], reverse=True)

    # Output
    st.subheader("📅 AI Study Timetable")

    for i, (sub, diff, mins) in enumerate(data):
        time = convert_time(int(mins))

        if i == 0:
            st.error(f"🔥 {sub} → {time} (Highest Priority)")
        else:
            st.write(f"📖 {sub} → {time}")

    st.divider()
    st.write(f"Total Time Available: {days_left * hours_per_day} hours")