from flask_admin.form import FileUploadField, ImageUploadInput
import os
import uuid

from src.admin.base import SecureModelView
from src.config import Config


class UUIDFileUploadField(FileUploadField):
    def generate_name(self, obj, file_data):
        # Generate a unique filename using UUID
        extension = os.path.splitext(file_data.filename)[1]
        return f"{uuid.uuid4().hex[:12]}{extension}"

    def _get_file_name(self, file_data):
        """
        Overrides the default behavior to return the generated unique file name.
        """
        return super()._get_file_name(file_data)


class CustomImageUploadInput(ImageUploadInput):
    """
    Custom widget to display a preview of the uploaded image.
    """
    def get_url(self, field):
        if field.data:
            # Construct the relative URL for the image
            slide_url = f"/uploads/slides/{field.data}"
            return slide_url
        return None


class SlidesView(SecureModelView):
    # can_export = True

    form_extra_fields = {
        'slidePath': UUIDFileUploadField(
            'Slide Image',
            base_path=os.path.join(Config.UPLOAD_FOLDER, 'slides'),
            allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'webp'],
            widget=CustomImageUploadInput(),  # Use custom widget
            render_kw={'accept': 'image/*'}
        )
    }

    def on_model_delete(self, model):
        """
        This hook is called before a model is deleted.
        Delete the associated file from the filesystem.
        """
        if model.slidePath:
            # Construct the full path to the file
            file_path = os.path.join(Config.UPLOAD_FOLDER, 'slides', model.slidePath)
            # Remove the file if it exists
            if os.path.exists(file_path):
                os.remove(file_path)