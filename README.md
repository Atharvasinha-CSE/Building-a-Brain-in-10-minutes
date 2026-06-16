# 🧠 Student Exam Score Predictor
* A subset of the nvidia Deep learning Institute Course name Building a Brain in 10 Minutes
A Neural Network-powered web app that predicts a student's exam score based on their study habits and academic history — built with TensorFlow and Flask.

---

## 🚀 Live Demo

> Deploy on Render / Railway and add your link here

## 📌 Features

- Predicts exam score using a deep neural network
- Takes 4 inputs: Study Hours, Sleep Hours, Attendance, Previous Score
- Clean and responsive web UI
- REST API backend with Flask
- Trained and saved model ready to use

---

## 🧠 How It Works

The model was trained on 200 synthetic student records. Three neural network architectures were compared, and the best one was selected:

| Model | Layers | Epochs |
|-------|--------|--------|
| Model 1 | 64 → 32 → 1 | 100 |
| Model 2 | 128 → 64 → 32 → 1 | 200 |
| Model 3 ✅ (Best) | 256 → 128 → 64 → 32 → 1 | 500 |

The target score is calculated as:

```
exam_score = 3.5 × study_hours + 2.0 × sleep_hours + 0.3 × attendance + 0.4 × prev_score + noise
```

---

## 📥 Input Features

| Feature | Range | Description |
|---|---|---|
| Study Hours | 1 – 10 | Hours spent studying per day |
| Sleep Hours | 4 – 10 | Hours of sleep per night |
| Attendance | 50 – 100 | Class attendance percentage |
| Previous Score | 40 – 100 | Score in the previous exam |

---

## 🗂️ Project Structure

```
student-score-predictor/
├── app.py                        # Flask backend
├── student_model.keras           # Trained neural network model
├── scaler.pkl                    # StandardScaler for input normalization
├── Procfile                      # For deployment (Render/Heroku)
├── requirements.txt              # Python dependencies
├── code_student_predictor.ipynb  # Full ML training notebook
└── templates/
    └── index.html                # Frontend UI
```

---

## ⚙️ Installation & Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/student-score-predictor.git
cd student-score-predictor
```

### 2. Install dependencies
```bash
pip install flask numpy tensorflow scikit-learn
```

### 3. Run the app
```bash
python app.py
```

### 4. Open in browser
```
http://localhost:5000
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS |
| Backend | Python, Flask |
| ML Model | TensorFlow / Keras |
| Preprocessing | Scikit-learn (StandardScaler) |

---

## 📓 Notebook

The `code_student_predictor.ipynb` notebook covers:

- Dataset generation
- Exploratory Data Analysis (scatter plots)
- Data preprocessing & train/test split
- Training 3 neural network models
- Evaluation (MSE, R² Score)
- Saving the best model and scaler

---

## 📄 License

This project is licensed under the **Apache 2.0** — see the Apache 2.0 file for details.

---

## 👤 Author

**Your Name**
- GitHub Username: Atharvasinha-CSE 
- LinkedIn: https://www.linkedin.com/in/atharva-sinha-79667535a/
