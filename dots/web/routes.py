from flask import Blueprint, render_template, abort

bp = Blueprint('routes', __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/convert")
def convert():
    abort(404)
