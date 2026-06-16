from flask import Flask, request, render_template
import numpy as np
import pickle
import tensorflow as tf

app = Flask(__name__)

model = tf.keras.models.load_model('student_model.keras')
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    study_hours = float(request.form['study_hours'])
    sleep_hours = float(request.form['sleep_hours'])
    attendance = float(request.form['attendance'])
    prev_score = float(request.form['prev_score'])

    features = np.array([[study_hours, sleep_hours, attendance, prev_score]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    score = round(float(prediction[0][0]), 2)

    return render_template('index.html', prediction=score)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)