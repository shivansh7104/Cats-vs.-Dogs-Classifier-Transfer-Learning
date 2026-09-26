from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

base_model = tf.keras.applications.Xception(
    include_top=False,
    weights='imagenet',
    input_shape=(128, 128, 3)
)
base_model.trainable = False

model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.load_weights("models/transfer_learning_model.keras")

CLASS_NAMES = ["cats", "dogs"]

def preprocess_image(image):
    image = image.resize((128, 128))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        file = request.files["file"]

        if file:
            image = Image.open(file)
            image = preprocess_image(image)

            result = model.predict(image)
            confidence = float(result[0][0])

            if confidence > 0.5:
                prediction = f"Dog 🐶 ({confidence*100:.2f}%)"
            else:
                prediction = f"Cat 🐱 ({(1-confidence)*100:.2f}%)"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
