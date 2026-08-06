# 🔐 Smart Face Recognition Door Lock System

A real-time face recognition based access control system developed using **Python** and **OpenCV**. The system authenticates users through facial recognition, grants access to authorized users, logs successful entries, and captures images of unauthorized visitors.

---

## 📌 Project Overview

This project demonstrates a smart security system that uses computer vision for user authentication. Instead of relying on passwords or keys, the system identifies a person using facial recognition. Authorized users are granted access, while unknown users are denied and their images are stored for security purposes.

---

## ✨ Features

- 👤 Real-time face detection using a webcam
- ✅ Recognizes authorized users using the LBPH Face Recognizer
- 🔓 Displays **ACCESS GRANTED** for recognized users
- ❌ Displays **ACCESS DENIED** for unknown users
- 📝 Automatically logs authorized entries with timestamp
- 📷 Saves images of unknown visitors
- 🔔 Plays an alert sound when an unknown person is detected
- 💻 Runs entirely on a computer without requiring external hardware

---

## 🛠 Technologies Used

- Python 3
- OpenCV
- OpenCV Contrib
- NumPy
- Pandas

---

## 📁 Project Structure

```
face-recognition-door-lock/
│
├── dataset/                 # Training images
├── Screenshots/             # Project screenshots
│   ├── home.png
│   ├── access_granted.png
│   └── access_denied.png
│
├── face_capture.py          # Capture training images
├── face_train.py            # Train LBPH face recognition model
├── face_recognition.py      # Main application
├── face_model.yml           # Trained face recognition model
├── report.py
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/soundaryasivaraj06-star/face-recognition-door-lock.git
```

Go to the project folder:

```bash
cd face-recognition-door-lock
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Step 1 – Capture Face Images

```bash
python face_capture.py
```

---

### Step 2 – Train the Model

```bash
python face_train.py
```

---

### Step 3 – Start Face Recognition

```bash
python face_recognition.py
```

The webcam will open and begin recognizing faces.

---

## 📸 Screenshots

### Home Screen

![Home](Screenshots/home.png)

### Authorized User

![Access Granted](Screenshots/access_granted.png)

### Unauthorized User

![Access Denied](Screenshots/access_denied.png)

---

## 🔄 Workflow

1. Capture images of the authorized user.
2. Train the LBPH face recognition model.
3. Start the recognition system.
4. Detect faces using the webcam.
5. Compare detected faces with the trained model.
6. Grant access if the face is recognized.
7. Log the entry with the current timestamp.
8. Save an image and trigger an alert if the face is unknown.

---

## 🚀 Future Improvements

- Support for multiple authorized users
- Face mask detection
- Liveness detection to prevent photo spoofing
- Cloud-based attendance logging
- Mobile application integration
- Email notifications for unknown visitors

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Soundarya S**

GitHub: https://github.com/soundaryasivaraj06-star

---

⭐ If you found this project useful, consider giving it a star!