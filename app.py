import os
import shutil
from flask import Flask
from flask import request
from flask import render_template
from flask import send_file
from flask_cors import CORS
from model import style_transfer
from utils import save_image


app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/x", methods=["POST"])
def generate_nst():
    """
        DESCRIPTION
        ___________
        This function has route endpoint x which only has one request i.e. POST
        It recives the content and style images and returns the files

        RETURNS
        _______
        This function returns the genrated nst image.
    """
    if request.method == "POST":
        content_ = request.files["content_image"]
        style_ = request.files["style_image"]
        shutil.rmtree("uploads")
        os.mkdir("uploads")
        content_file_path_ = save_image(content_)
        style_file_path_ = save_image(style_)
        nst_genrated_image = style_transfer(content_image_path=content_file_path_, style_image_path=style_file_path_)
        nst_generated_image = nst_genrated_image.save("uploads/output.png")
        return send_file("uploads/output.png", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
