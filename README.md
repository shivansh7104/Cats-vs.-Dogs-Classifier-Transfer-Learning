# 📘 CNN-Image-Classification-System

A modern and highly accurate Cat vs Dog Image Classification System built using:
 - **Transfer Learning (97% accuracy)**
 - **TensorFlow / Keras**
 - **Flask Backend API**
 - **HTML + CSS + JavaScript Frontend**

This version provides a **full UI** where users can upload an image and instantly get predictions — no Postman required. </br></br>

## 🚀 Features

- 🧠 **Transfer Learning Model** (97% test accuracy)
- 🖼️ **Upload image directly from browser**
- ⚡ Real-time prediction using Flask API
- 🎨 Clean and simple web frontend
- 🔥 Automatically loads and preprocesses images
- 📦 Easy to deploy anywhere (local / cloud / VPS) </br></br>

## 📁 Project Structure

```
/project
│── models
|   |── transfer_learning_model.keras
│── notebooks
|   |── transfer_learning.ipynb
│── templates
|   |── index.html
│── static
|   |── style.css
│── img
|   |── home.png
|   |── prediction.png
│── main.py
│── requirements.txt
│── README.md
│── License
```

## 🧰 Technologies Used

- **Backend**
  - Python
  - Flask
  - TensorFlow / Keras
  - NumPy
  - Pillow (PIL)

- **Fronend**
  - HTML5
  - HTML5
  - JavaScript

- **ML Model**
  - Transfer Learning using: Xception </br></br>

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/CNN-Image-Classification-System.git
   cd CNN-Image-Classification-System
   ```

2. Create virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate   # For Windows
   # OR
   source venv/bin/activate  # For macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask server:
   ```bash
   python main.py
   ```

   Server will start at:</br>
   👉 `http://127.0.0.1:5000` </br></br>

## 🖼️ Using the Web Interface

1. Open your browser
   → `http://127.0.0.1:5000`
2. Click **Choose Image**
3. Select a `.jpg`, `.jpeg`, or `.png`
4. Click Predict
5. You will see:
```
  {
    "prediction": "dog",
    "confidence": 0.9123
  }
```
or
```
  {
  "prediction": "cat",
  "confidence": 0.7344
  }
```
## 📸 Screenshots

### Home Screen
![image](./img/home.png)

### Prediction
![image](./img/prediction.png)

## 📄 Requirements

The `requirements.txt` file includes all necessary packages:
 - flask
 - tensorflow
 - numpy
 - pillow </br></br>

## 🤝 Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to improve. </br></br>

## 📜 License

This project is licensed under the MIT License – see the `LICENSE` file for details.

