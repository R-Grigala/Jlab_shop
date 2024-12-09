from flask import Blueprint, send_from_directory
from os import path
import os

from src.config import Config
from src.models import Slides

# TEMPLATES_FOLDER = path.join(Config.BASE_DIR, "templates", "main")
uploads_blueprint = Blueprint("uploads", __name__)


@uploads_blueprint.route('/uploads/slides/<path:filename>')
def uploaded_slodes(filename):
    uploads_dir = os.path.join(Config.UPLOAD_FOLDER, 'slides')
    return send_from_directory(uploads_dir, filename)