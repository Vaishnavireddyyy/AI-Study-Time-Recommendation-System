import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# Load models
dnn_model = load_model("study_model.h5", compile=False)
lstm_model = load_model("lstm_model.h5", compile=False)
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="AI Study System", layout="wide")

st.title("📚 AI Study Time Recommendation System")

st.header("🔹 Personal Details")

col1, col2 = st.columns(2)

with col1:
    marks = st.slider("Exam Score (%)", 0, 100, 60)
    attendance = st.slider("Attendance (%)", 0, 100, 75)
    sleep = st.slider("Sleep Hours", 3, 10, 7)

with col2:
    distraction = st.slider("Distraction Level", 1, 10, 5)
    stress = st.slider("Stress Level", 1, 10, 5)
    sessions = st.slider("Study Sessions", 1, 6, 3)

st.divider()

# -------- LSTM INPUT --------

st.header("📅 Enter Last 7 Days Study Hours")

days = []
for i in range(7):
    val = st.slider(f"Day {i+1}", 0, 12, 3)
    days.append(val)

st.divider()

if st.button("🔍 Generate AI Report"):

    # ----- DNN Prediction -----
    input_data = np.array([[marks, attendance, sleep, distraction, stress, sessions]])
    input_scaled = scaler.transform(input_data)
    study_time = dnn_model.predict(input_scaled)[0][0]

    # ----- LSTM Prediction -----
    lstm_input = np.array(days).reshape((1,7,1))
    consistency = lstm_model.predict(lstm_input)[0][0]

    # Convert to label
    if consistency < 1.5:
        habit = "Highly Consistent 👍"
    elif consistency < 3:
        habit = "Moderately Consistent 🙂"
    else:
        habit = "Irregular Study Pattern ⚠️"

    # ----- Extra Metrics -----
    focus_score = max(0, 100 - distraction*5 - stress*3)
    burnout = "High" if stress > 7 else "Moderate" if stress > 4 else "Low"

    st.success(f"📖 Recommended Study Time: {round(study_time,2)} hrs/day")

    col1, col2, col3 = st.columns(3)
    col1.metric("🎯 Focus Score", f"{focus_score}%")
    col2.metric("⚠️ Burnout Risk", burnout)
    col3.metric("📊 Study Habit", habit)

    st.divider()

    # ----- Weekly Chart -----
    st.subheader("📊 Weekly Study Pattern")

    fig, ax = plt.subplots()
    ax.plot(days, marker="o")
    ax.set_ylabel("Hours")
    ax.set_title("Your Study Trend")

    st.pyplot(fig)
