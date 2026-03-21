📚 AI Study Time Recommendation System
 Project Overview

The AI Study Time Recommendation System is a web-based application that uses Deep Learning techniques to analyze student study behavior and generate personalized study recommendations.

The system collects student academic data and recent study activity, processes it using multiple neural network models, and provides insights such as:

 Recommended study hours

Study habit classification

 Predicted next exam score

 Weekly study pattern visualization

This helps students understand their learning behavior and improve their academic performance.

* Key Features

✔ Personalized study time recommendation
✔ Study habit analysis using sequential data
✔ Exam score prediction using neural networks
✔ Interactive web application using Streamlit
✔ Visualization of weekly study patterns

System Architecture

The system processes user input through multiple deep learning models.

Student Input
      │
      ▼
Data Preprocessing
      │
      ▼
Deep Neural Network (DNN)
Study Time Prediction
      │
      ▼
LSTM Model
Study Pattern Analysis
      │
      ▼
Artificial Neural Network (ANN)
Exam Score Prediction
      │
      ▼
Results Dashboard (Streamlit)
 System Architecture Diagram

Add your architecture image here.

docs/architecture.png

Example:

 Deep Learning Models Used
 Deep Neural Network (DNN)

Used to predict recommended study hours.

Inputs

Previous exam score

Attendance

Sleep hours

Study sessions

Number of subjects

Output

Recommended study time per day

 Long Short-Term Memory (LSTM)

Used to analyze study patterns over time.

Input

Study hours for the last 7 days

Example:

[2, 3, 4, 2, 5, 3, 4]

Output

Study consistency analysis

Study habit classification
Artificial Neural Network (ANN)

Used to predict expected exam performance.

Inputs

Previous marks

Recommended study time

Attendance

Study consistency

Output

Predicted next exam score

 Application Interface

The system provides a Streamlit dashboard where students can enter their information.

Example inputs:

Exam Score

Attendance

Sleep Hours

Study Sessions

Number of Subjects

Last 7 Days Study Hours

 Example Output

The system generates an AI study report containing:

Recommended Study Time

Study Habit Classification

Predicted Next Exam Score

Weekly Study Pattern Graph

Example screenshot:

docs/result.png

Example:

📉 Weekly Study Pattern Visualization

The system generates a graph showing the student's study trend.

Example:

🛠 Technologies Used
Programming Language

Python

Deep Learning Framework

TensorFlow / Keras

Libraries

NumPy

Pandas

Matplotlib

Scikit-learn

Web Framework

Streamlit

Development Environment

Visual Studio Code

📂 Project Structure
AI-Study-Time-Recommendation-System
│
├── app.py
├── generate_data.py
├── generate_lstm_data.py
├── train_model.py
├── train_lstm.py
├── train_performance_model.py
│
├── study_model.h5
├── lstm_model.h5
├── performance_model.h5
│
├── scaler.pkl
├── performance_scaler.pkl
│
├── requirements.txt
└── README.md
⚙ Installation

Clone the repository

git clone https://github.com/yourusername/ai-study-time-recommendation-system.git

Move to the project folder

cd ai-study-time-recommendation-system

Install dependencies

pip install -r requirements.txt
▶ Running the Application

Start the Streamlit application:

streamlit run app.py

The web interface will open in your browser.

🎯 Results

The system successfully demonstrates the use of Deep Learning models to analyze study behavior and generate personalized recommendations.

Outputs include:

Recommended study hours

Study habit analysis

Predicted exam performance

Study trend visualization

🚀 Future Improvements

Integration with real student datasets

Mobile application support

Personalized subject-wise study plans

Advanced deep learning models

👩‍💻 Author

Vaishnavi
Project for Principles of Deep Learning and Neural Networks

⭐ Acknowledgement

This project was developed as part of an academic deep learning course to demonstrate how AI can assist students in improving study planning and academic performance.
