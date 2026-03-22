import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="AI Study Timetable Generator", layout="wide")

st.title("📚 AI Study Timetable Generator")
st.write("Enter your subject details to generate a personalized study timetable.")

# ------------------------------
# CONVERT MINUTES FUNCTION
# ------------------------------
def convert_time(minutes):
    hours = minutes // 60
    mins = minutes % 60
    if hours > 0:
        return f"{hours} hrs {mins} mins"
    else:
        return f"{mins} mins"

# ------------------------------
# NUMBER OF SUBJECTS
# ------------------------------
num_subjects = st.number_input(
    "How many courses/subjects do you have?",
    min_value=1,
    max_value=10,
    value=3
)

subjects = []
scores = []

st.subheader("Enter Subject Details")

for i in range(num_subjects):

    col1, col2 = st.columns(2)

    with col1:
        subject = st.text_input(f"Subject {i+1} Name")

    with col2:
        score = st.number_input(
            f"Marks for Subject {i+1}",
            min_value=0,
            max_value=100,
            value=60
        )

    subjects.append(subject.strip())
    scores.append(score)

# ------------------------------
# EXAM INFO
# ------------------------------
st.subheader("Exam Preparation Information")

days_left = st.number_input(
    "Days left for exam",
    min_value=1,
    max_value=60,
    value=7
)

hours_per_day = st.number_input(
    "Available study hours per day",
    min_value=1,
    max_value=12,
    value=6
)

# ------------------------------
# GENERATE TIMETABLE
# ------------------------------
if st.button("Generate AI Study Timetable"):

    difficulty = []

    # 🔥 SIMPLE AI LOGIC (REPLACES ANN)
    for score in scores:
        diff = (100 - score) / 100   # higher if marks low
        difficulty.append(diff)

    # ------------------------------
    # HARDEST SUBJECT
    # ------------------------------
    max_diff = max(difficulty)
    max_index = difficulty.index(max_diff)
    hardest_subject = subjects[max_index]

    if max_diff > 0.6:
        st.warning(f"⚠️ Focus more on **{hardest_subject}** (highest difficulty)")
    else:
        st.success("✅ Subjects are balanced. Follow timetable.")

    # ------------------------------
    # DIFFICULTY CHART
    # ------------------------------
    st.subheader("📊 Subject Difficulty Levels")

    df = pd.DataFrame({
        "Subject": subjects,
        "Difficulty": difficulty
    })

    df = df[df["Subject"] != ""]
    st.bar_chart(df.set_index("Subject"))

    # ------------------------------
    # TIME ALLOCATION
    # ------------------------------
    total_difficulty = sum(difficulty)

    study_minutes = []

    for diff in difficulty:
        hrs = (diff / total_difficulty) * hours_per_day
        mins = int(hrs * 60)
        study_minutes.append(mins)

    # ------------------------------
    # SORT + DISPLAY
    # ------------------------------
    st.subheader("📅 Recommended Study Timetable")

    subject_data = []

    for i in range(num_subjects):
        if subjects[i] != "":
            subject_data.append((subjects[i], difficulty[i], study_minutes[i]))

    subject_data.sort(key=lambda x: x[1], reverse=True)

    for i, (sub, diff, mins) in enumerate(subject_data):

        formatted_time = convert_time(mins)

        if i == 0:
            st.error(f"🔥 {sub} → {formatted_time} per day (Highest Priority)")
        else:
            st.write(f"📖 {sub} → {formatted_time} per day")

    st.divider()

    total_hours = days_left * hours_per_day
    st.write(f"📊 Total preparation time: **{total_hours} hours**")
st.write("✅ New Version Running")