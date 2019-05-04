from flask import Blueprint, render_template, abort, request
from ..image import ImageLoader
from ..threshold import threshold_function
from ..output import output_function

bp = Blueprint('routes', __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/convert", methods=["POST"])
def convert():
    image_file = request.files["image"]
    image = ImageLoader.from_bytes(image_file.read())
    threshold_fn = threshold_function("adaptive_gaussian")
    binary_matrix = threshold_fn(image.as_grayscale())
    output_fn = output_function("braille_4x2")
    output = output_fn(binary_matrix)
    return render_template("convert.html", output=output)

