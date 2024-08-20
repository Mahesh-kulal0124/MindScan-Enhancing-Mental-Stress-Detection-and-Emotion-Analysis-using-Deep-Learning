from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array # type: ignore
from keras.models import model_from_json
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = './images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Load the model
with open("E:/major_project (1)/flask/facialexpression.json", "r") as json_file:
    model_json = json_file.read()
model = model_from_json(model_json)
model.load_weights("E:/major_project (1)/flask/facialexpression.h5")

labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

def preprocess_image(image):
    img_array = img_to_array(image)
    img_array = img_array.reshape(1, 48, 48, 1)
    return img_array / 255.0

def calculate_weighted_average_stress_score(expression_counts):
    expression_weights = {
        "Happy": 10,
        "Sad": 80,
        "Angry": 70,
        "Fear": 90,
        "Surprise": 60,
        "Disgust": 70,
        "Neutral": 50
    }
    expression_scores = {
        "Happy": 20,
        "Sad": 70,
        "Angry": 60,
        "Fear": 80,
        "Surprise": 50,
        "Disgust": 65,
        "Neutral": 40
    }

    weighted_sum = 0
    total_weight = 0

    for expression, count in expression_counts.items():
        if expression in expression_weights and expression in expression_scores:
            weighted_sum += expression_weights[expression] * expression_scores[expression] * count
            total_weight += expression_weights[expression] * count

    return weighted_sum / total_weight if total_weight > 0 else 0

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('video.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'fileInputControl' not in request.files:
        return "No file part in the request", 400

    user_name = request.form.get('user_name')

    if not user_name:
        return "Please enter your name", 400

    file_input = request.files.getlist('fileInputControl')

    if file_input:
        user_folder = os.path.join(app.config['UPLOAD_FOLDER'], user_name)
        os.makedirs(user_folder, exist_ok=True)

        predictions = {}

        for file in file_input:
            if file.filename == '':
                return "No selected file", 400
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(user_folder, filename))

                image_path = os.path.join(user_folder, filename)
                image = load_img(image_path, color_mode='grayscale', target_size=(48, 48))
                img_array = preprocess_image(image)
                pred = model.predict(img_array)
                pred_label = labels[pred.argmax()]

                predictions[pred_label] = predictions.get(pred_label, 0) + 1
        
        predictions_title_case = {key.capitalize(): value for key, value in predictions.items()}
        p = calculate_weighted_average_stress_score(predictions_title_case)
        score = int(p)
        score_class = 'low' if score <= 25 else 'high' if score >= 75 else ''
        animate_class = 'animate-color' if score <= 25 or score >= 75 else ''
        
        return render_template('output.html', score=score, score_class=score_class, animate_class=animate_class)

    return "No files found in the request", 400

@app.route('/', methods=['POST'])
def predict():
    imagefile = request.files.get('imagefile')
    if imagefile:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(imagefile.filename))
        imagefile.save(image_path)

        image = load_img(image_path, color_mode='grayscale', target_size=(48, 48))
        img_array = preprocess_image(image)
        pred = model.predict(img_array)
        pred_label = labels[pred.argmax()]

        return render_template('index.html', prediction=pred_label)

    return "No file uploaded", 400

if __name__ == '__main__':
    app.run(debug=True)
