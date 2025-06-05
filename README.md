### 🎮FitPlay - Human Activity Recognition Using Machine Learning and mpu_6050 Sensors

> FitPlay is an interactive exergame that uses real-time human activity recognition (HAR) to create an immersive fitness gaming experience. The game encourages physical exercise by mimicking activities such as jogging, squatting, jumping, and standing, using data from wearable motion sensors i.e. mpu_6050.
---

## 📸 Game Preview
**FitPlay** combines motion sensing and machine learning to create an engaging fitness game. By performing real-world actions like jumping, squatting, or jogging, players control an in-game avatar—promoting health while having fun.

<img src="assets/idle.png" alt="FitPlay Gameplay" width="700"/>   <img src="assets/run.png" alt="FitPlay Gameplay" width="700"/>

---

## 🖼️ System Architecture
# How it works?
The sensors capture 6-axis motion data (accelerometer + gyroscope).

Data is classified in real-time using an SVM model.

The game responds to classified actions—jump, squat, run—triggering the in-game avatar.


<img src="assets/system arch.png" alt="System Architecture" width="700"/>

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

<img src="assets/ckt diagram.png" alt="Sensor Setup" width="600"/>

> 3 MPU6050 sensors: one on the chest and one on each ankle.

---

## 📊 Classification Visualization

<img src="assets/prediction.png" alt="Activity Classification Graph" width="700"/>  <img src="assets/learning curve.png" alt="Activity Classification Graph" width="700"/> <img src="assets/confusion matrix.png" alt="Activity Classification Graph" width="700"/>



---

## 🔧 Setup Instructions

# Requirements
Unity (2021 or later)

Python 3.8+

Microcontroller (e.g., Arduino Leonardo or Pro Micro with USB HID support)

MPU6050 Sensors ×3

USB cable to connect microcontroller to PC

# Install dependencies
pip install pandas numpy matplotlib scikit-learn pyserial

# Steps

1.Connect sensors to microcontroller.

2.Upload firmware to microcontroller.

3.Collect and label data using Python scripts i.e. data_collection.py And prepare Datasets for the model.

4.Train SVM model.

5.Launch Unity and link it to your Python classifier(modify the data_collection.py inserting your trained model for real time classification).

6.Start the game and move to play!

---

## Contributions
Contributions are welcome! Feel free to:

Open an issue

Fork the repo

Submit a pull request

Let’s make fitness fun together.

---

## Author
Manik Syangtan
📍 Nepal
🎓 Electronics, Communication & IT Engineer
🔗 Connect with Me

- [LinkedIn](https://www.linkedin.com/in/maniksyangtan)


---

## License
This project is licensed under the MIT License – see the LICENSE file for details.



