### 🎮FitPlay - Human Activity Recognition Using Machine Learning and mpu_6050 Sensors

> FitPlay is an interactive exergame that uses real-time human activity recognition (HAR) to create an immersive fitness gaming experience. The game encourages physical exercise by mimicking activities such as jogging, squatting, jumping, and standing, using data from wearable motion sensors i.e. mpu_6050.
---

## 📸 Game Preview

<img src="assets/screenshot-gameplay.png" alt="FitPlay Gameplay" width="700"/>

---

## 🧠 Overview

**FitPlay** combines motion sensing and machine learning to create an engaging fitness game. By performing real-world actions like jumping, squatting, or jogging, players control an in-game avatar—promoting health while having fun.

---

## 🖼️ System Architecture

<img src="assets/fitplay-architecture.png" alt="System Architecture" width="700"/>

---

## 🧰 Tech Stack

| Component | Tool |
|----------|------|
| Hardware | MPU6050 Sensors ×3 (Chest, Left Ankle, Right Ankle), Microcontroller, USB HID |
| Software | Unity (Game Engine), Python (HAR Model), SVM (scikit-learn), Serial Communication |
| Model    | SVM Classifier with 80% accuracy for 4-class activity recognition |

---

## 🦾 Activities Recognized

- 🏃‍♂️ Jogging  
- 🧍 Standing  
- 🏋️ Squatting  
- 🕴️ Jumping  

---

## 👣 Sensor Placement

<img src="assets/sensor-setup.png" alt="Sensor Setup" width="600"/>

> 3 MPU6050 sensors: one on the chest and one on each ankle.

---

## 📊 Classification Visualization

<img src="assets/activity-classification.png" alt="Activity Classification Graph" width="700"/>

---

## 🔧 Setup Instructions

```bash
# Install dependencies
pip install pandas numpy matplotlib scikit-learn pyserial
