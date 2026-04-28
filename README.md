# Blood Type Classification Prediction 🩸

This project is a Machine Learning web application built with **Flask**, **TensorFlow**, and **OpenCV**. It allows users to upload a high-resolution fingerprint image, which is then processed through an advanced deep learning model to accurately predict the individual's blood type.

## Features
- **User Authentication:** Secure registration and login system for users and administrators.
- **Image Processing:** Uses OpenCV (`fastNlMeansDenoisingColored`) to automatically remove noise and enhance the quality of uploaded fingerprint images.
- **Deep Learning Model:** A pre-trained TensorFlow/Keras model (`model.h5`) that classifies the fingerprint into one of 8 standard blood groups (A+, A-, B+, B-, AB+, AB-, O+, O-).
- **Serverless Database:** Utilizes SQLite for a zero-configuration, self-contained database that makes deployment seamless.
- **Cloud-Ready:** Fully containerized with a `Dockerfile` and `requirements.txt` for one-click deployment on Hugging Face Spaces or Render.

## Tech Stack
- **Backend:** Python 3.10, Flask, Gunicorn
- **Machine Learning:** TensorFlow 2.x, Keras, NumPy
- **Computer Vision:** OpenCV (cv2)
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap

## How to Run Locally

1. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Initialize the database:
   ```bash
   python init_db.py
   ```
3. Run the application:
   ```bash
   flask run
   ```
4. Open your browser and navigate to `http://127.0.0.1:5000`
