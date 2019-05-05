from flask import Blueprint, render_template, abort, request, jsonify
from ..image import ImageLoader
from ..threshold import threshold_function, available_threshold_functions
from ..output import output_function, available_output_functions
import numpy as np

bp = Blueprint('routes', __name__)

@bp.route("/")
def index():
    return render_template("index.html",
        threshold_functions = available_threshold_functions(),
        output_functions = available_output_functions())

@bp.route("/convert", methods=["POST"])
def convert():
    image_file = request.files["image"]
    image = ImageLoader.from_bytes(image_file.read())

    resize_factor = float(request.form["resize_factor"])
    if resize_factor != 1:
        image.resize_with_factor(resize_factor)

    threshold_fn = threshold_function(request.form["threshold_function"])
    binary_matrix = threshold_fn(image.as_grayscale())

    if request.form["invert"] == "true":
        binary_matrix = np.invert(binary_matrix)
    
    transparency_mask = image.transparency_mask()
    binary_matrix = np.logical_and(binary_matrix, np.invert(transparency_mask))

    output_fn = output_function(request.form["output_function"])
    output = output_fn(binary_matrix)
    
    return jsonify(output=output)

