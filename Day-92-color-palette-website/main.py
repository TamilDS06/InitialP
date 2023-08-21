from flask import Flask, render_template, request, jsonify
from PIL import Image
from collections import Counter
import webcolors
import numpy as np
import io

app = Flask(__name__)

def get_top_colors(image):
    colors = []
    with Image.open(image) as img:
        img_array = np.array(img)
        height, width, _ = img_array.shape
        for y in range(height):
            for x in range(width):
                r, g, b = img_array[y, x, :3]  # Extract RGB values
                colors.append(webcolors.rgb_to_name((r, g, b)))
    color_counts = Counter(colors)
    top_colors = color_counts.most_common(10)
    return top_colors

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            image = uploaded_file.read()
            top_colors = get_top_colors(io.BytesIO(image))
            return jsonify(top_colors)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
