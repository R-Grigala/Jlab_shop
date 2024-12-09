from flask import render_template, Blueprint, send_from_directory
from os import path
import os

from src.config import Config
from src.models import Slides

TEMPLATES_FOLDER = path.join(Config.BASE_DIR, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)

@main_blueprint.route("/")
def index():
        # Query slides from the database
    slides = Slides.query.all()

    return render_template("index.html", user_type="admin", slides=slides)
