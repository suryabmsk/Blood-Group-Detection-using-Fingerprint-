from flask import Flask, render_template, flash, request, session, send_file
from flask import render_template, redirect, url_for, request
import os
import sqlite3

app = Flask(__name__)

app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route("/AdminHome")
def AdminHome():
    conn = sqlite3.connect('database.db')

    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb ")
    data = cur.fetchall()
    conn.close()

    return render_template('AdminHome.html', data=data)


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['Password'] == 'admin':
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb")
            data = cur.fetchall()
            conn.close()

            return render_template('AdminHome.html', data=data)
        else:
            flash("UserName or Password Incorrect!")

            return render_template('AdminLogin.html')


@app.route("/Prediction")
def Prediction():
    return render_template('Prediction.html')


@app.route('/UserLogin')
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        name = request.form['name']

        age = request.form['age']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        Password = request.form['Password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username=?", (username,))
        data = cursor.fetchone()
        if data is None:

            cursor.execute(
                "insert into regtb (Name, Age, Mobile, Email, Address, UserName, Password) values(?, ?, ?, ?, ?, ?, ?)",
                (name, age, mobile, email, address, username, Password))
            conn.commit()
            conn.close()
            return render_template('UserLogin.html')



        else:
            flash('Already Register Username')
            return render_template('NewUser.html')


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['Password']
        session['uname'] = request.form['uname']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username=? and Password=?", (username, password))
        data = cursor.fetchone()
        conn.close()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('UserLogin.html')

        else:
            return render_template('Prediction.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        import tensorflow as tf
        import numpy as np
        import cv2
        from keras.preprocessing import image
        file = request.files['file']
        file.save('static/upload/Test.BMP')
        org1 = 'static/upload/Test.BMP'

        img1 = cv2.imread('static/upload/Test.BMP')

        dst = cv2.fastNlMeansDenoisingColored(img1, None, 10, 10, 7, 21)
        # cv2.imshow("Nosie Removal", dst)
        noi = 'static/upload/noi.BMP'

        cv2.imwrite(noi, dst)

        import warnings
        warnings.filterwarnings('ignore')

        # Load the trained model
        classifierLoad = tf.keras.models.load_model('model.h5')

        # Load and preprocess the test image
        test_image = image.load_img('static/upload/Test.BMP', target_size=(200, 200))
        test_image = image.img_to_array(test_image)  # Convert to array
        test_image = test_image / 255.0  # Rescale as done during training
        test_image = np.expand_dims(test_image, axis=0)  # Expand dimensions for batch format

        # Make prediction
        result = classifierLoad.predict(test_image)
        print(result)



        ind = np.argmax(result)

        out = ''
        if ind == 0:
            out = "A+"
        elif ind == 1:
            out = "A-"
        elif ind == 2:
            out = "AB+"
        elif ind == 3:
            out = "AB-"
        elif ind == 4:
            out = "B+"
        elif ind == 5:
            out = "B-"
        elif ind == 6:
            out = "O+"
        elif ind == 7:
            out = "O-"
        else:
            out = "Unknown"

        return render_template('Result.html', result=out, org=org1, noi=noi)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
