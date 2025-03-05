# Face Detection & Recognition System

## 📌 Project Overview
This project implements a **Face Detection & Recognition System** using **OpenCV** for face detection and **DeepFace** for face recognition. It can identify known faces by comparing them to a database of stored images.

## 🎯 Features
✔️ Real-time face detection using OpenCV  
✔️ Face recognition using DeepFace  
✔️ Train with custom images for personalized recognition  
✔️ Web-based interface using **Streamlit**  

## 🛠️ Tech Stack
- **Python**
- **OpenCV** (Face Detection)
- **DeepFace** (Face Recognition)
- **Streamlit** (Web App)
- **Numpy** (Image Processing)

## 📂 Dataset
- You can use **Labeled Faces in the Wild (LFW)** dataset ([Download from Kaggle](https://www.kaggle.com/datasets/jessicali9530/lfw-dataset)) or collect your own images.

---

## 🚀 Installation & Setup
### **1️⃣ Install Dependencies**
Run the following command:
```bash
pip install opencv-python numpy face-recognition streamlit deepface
```

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/your-repo/face-recognition.git
cd face-recognition
```

### **3️⃣ Prepare Face Database**
- Create a folder named `faces_db`
- Add images of known people (e.g., `faces_db/person1.jpg`, `faces_db/person2.jpg`)

### **4️⃣ Run Face Detection**
```bash
python face_detector.py
```
This will open your webcam and detect faces in real-time.

### **5️⃣ Run Face Recognition**
```bash
python face_recognition.py
```
This will compare detected faces to images in `faces_db`.

### **6️⃣ Run the Web App (Streamlit)**
```bash
streamlit run app.py
```
Go to **http://localhost:8501/** in your browser.

---

## 📜 Project Structure
```
📂 face-recognition
│-- app.py              # Streamlit web app
│-- face_detector.py    # Real-time face detection
│-- face_recognition.py # Face recognition script
│-- faces_db/           # Folder containing known faces
│-- README.md           # Project documentation
```

---

## 📌 Future Enhancements
✔ Improve accuracy with **FaceNet** or **OpenFace**  
✔ Implement an **Attendance System** based on recognition  
✔ Add **Real-time Alerts** when an unknown person is detected  

---

## 🤝 Contributing
Feel free to **fork** this repository and submit a **pull request** with improvements!

---

## 📝 License
This project is **open-source** under the MIT License.

