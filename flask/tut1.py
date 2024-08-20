from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/vish")
def vish():
    name = "vishvith"
    return render_template('about.html',name = name)

@app.route("/bootstrap")
def bootstrap():
    return render_template('bootstrap.html')

app.run(debug=True) 




# /**# from flask import Flask, render_template, request
# # from keras.models import model_from_json
# # from tensorflow.keras.preprocessing.image import load_img, img_to_array
# # import numpy as np
# # import os
# # from werkzeug.utils import secure_filename

# # app = Flask(__name__)


# # UPLOAD_FOLDER = './images/'
# # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # @app.route('/upload', methods=['POST'])
# # def upload_files():
# #     if 'fileInputControl' not in request.files:
# #         return "No file part in the request", 400

# #     user_name = request.form['user_name']  # Get the user's name from the form

# #     if user_name == '':
# #         return "Please enter your name", 400

# #     file_input = request.files.getlist('fileInputControl')

# #     if file_input:
# #         user_folder = os.path.join(app.config['UPLOAD_FOLDER'], user_name)
# #         if not os.path.exists(user_folder):
# #             os.makedirs(user_folder)

# #         for file in file_input:
# #             if file.filename == '':
# #                 return "No selected file", 400
# #             if file:
# #                 filename = secure_filename(file.filename)
# #                 file.save(os.path.join(user_folder, filename))

# #         return "Files uploaded successfully", 200

# #     return "No files found in the request", 400
# # json_file = open("facialexpression.json", "r")
# # model_json = json_file.read()
# # json_file.close()
# # model = model_from_json(model_json)
# # model.load_weights("facialexpression.h5")

# # label = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# # def ef(image):
# #     img_array = img_to_array(image)
# #     img_array = img_array.reshape(1, 48, 48, 1)
# #     return img_array / 255.0

# # @app.route("/", methods=['GET'])
# # def home():
# #     return render_template('index.html')

# # @app.route("/about")
# # def about():
# #     return render_template('about.html')

# # @app.route("/contact")
# # def contact():
# #     return render_template('contact.html')

# # @app.route("/post")
# # def post():
# #     return render_template('post.html')

# # @app.route('/', methods=['POST'])
# # def predict():
# #     imagefile = request.files['imagefile']
# #     image_path = "./images/" + imagefile.filename
# #     imagefile.save(image_path)

# #     image = load_img(image_path, grayscale=True, target_size=(48, 48))
# #     img_array = ef(image)
# #     pred = model.predict(img_array)
# #     pred_label = label[pred.argmax()]

# #     classification = pred_label

# #     return render_template('index.html', prediction=classification)

# # if __name__ == '__main__':
# #     app.run(debug=True)

# from flask import Flask, render_template, request
# from tensorflow.keras.models import model_from_json 
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
# import numpy as np
# import os
# from werkzeug.utils import secure_filename

# app = Flask(__name__)


# UPLOAD_FOLDER = './images/'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# print(os.getcwd())
# json_file = open("c:/Users/MAHESH KULAL/Downloads/major_project (1)/flask/facialexpression.json", "r")
# model_json = json_file.read()
# json_file.close()
# model = model_from_json(model_json)
# model.load_weights("c:/Users/MAHESH KULAL/Downloads/major_project (1)/flask/facialexpression.h5")

# label = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# def ef(image):
#     img_array = img_to_array(image)
#     img_array = img_array.reshape(1, 48, 48, 1)
#     return img_array / 255.0

# def calculate_weighted_average_stress_score(expression_counts):
#     # Define expression weights and scores
#     expression_weights = {
#         "Happy": 10,
#         "Sad": 80,
#         "Angry": 70,
#         "Fear": 90,
#         "Surprise": 60,
#         "Disgust": 70,
#         "Neutral": 50
#     }
#     expression_scores = {
#         "Happy": 20,
#         "Sad": 70,
#         "Angry": 60,
#         "Fear": 80,
#         "Surprise": 50,
#         "Disgust": 65,
#         "Neutral": 40
#     }

#     # Initialize variables for weighted sum and total count
#     weighted_sum = 0 
#     total_weight = 0

#     # Iterate through expression counts and calculate weighted sum and total weight
#     for expression, count in expression_counts.items():
#         if expression in expression_weights and expression in expression_scores:
#             weighted_sum += expression_weights[expression] * expression_scores[expression] * count
#             total_weight += expression_weights[expression] * count

#     if total_weight > 0:
#         return weighted_sum / total_weight
#     else:
#         return 0


# @app.route("/", methods=['GET'])
# def home():
#     return render_template('index.html')

# @app.route("/about")
# def about():
#     return render_template('video.html')

# @app.route("/contact")
# def contact():
#     return render_template('contact.html')

# @app.route("/post")
# def post():
#     return render_template('post.html')

# @app.route('/upload', methods=['POST'])
# def upload_files():
#     if 'fileInputControl' not in request.files:
#         return "No file part in the request", 400

#     user_name = request.form['user_name']  # Get the user's name from the form

#     if user_name == '':
#         return "Please enter your name", 400

#     file_input = request.files.getlist('fileInputControl')

#     if file_input:
#         user_folder = os.path.join(app.config['UPLOAD_FOLDER'], user_name)
#         if not os.path.exists(user_folder):
#             os.makedirs(user_folder)

#         predictions = {}  # Initialize predictions dictionary for counting expressions

#         for file in file_input:
#             if file.filename == '':
#                 return "No selected file", 400
#             if file:
#                 filename = secure_filename(file.filename)
#                 file.save(os.path.join(user_folder, filename))

#                 # Perform prediction for each uploaded image
#                 image_path = os.path.join(user_folder, filename)
#                 image = load_img(image_path, grayscale=True, target_size=(48, 48))
#                 img_array = ef(image)
#                 pred = model.predict(img_array)
#                 pred_label = label[pred.argmax()]

#                 if pred_label in predictions:
#                     predictions[pred_label] += 1
#                 else:
#                     predictions[pred_label] = 1
        
#         predictions_title_case = {key.capitalize(): value for key, value in predictions.items()} 
#         p = calculate_weighted_average_stress_score(predictions_title_case)  # Move the return statement outside the loop
#         score = int(p)
#         if score <= 25:
#             score_class = 'low'
#         elif score >= 75:
#             score_class = 'high'
#         else:
#             score_class = ''

#         if score <= 25 or score >= 75:
#             animate_class = 'animate-color'
#         else:
#             animate_class = ''
#         return render_template('output.html', score=score, score_class=score_class, animate_class=animate_class)  # Move the return statement outside the loop

#     return "No files found in the request", 400



# @app.route('/', methods=['POST'])
# def predict():
#     imagefile = request.files['imagefile']
#     image_path = "./images/" + imagefile.filename
#     imagefile.save(image_path)

#     image = load_img(image_path,color_mode='grayscale', target_size=(48, 48))
#     img_array = ef(image)
#     pred = model.predict(img_array)
#     pred_label = label[pred.argmax()]

#     classification = pred_label

#     return render_template('index.html', prediction=classification)

# if __name__ == '__main__':
#     app.run(debug=True)
