import os
from werkzeug.utils import secure_filename
from config import Config

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def save_image(image, fornecedor):
    
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        filename_path = f'{fornecedor}_{filename}'
        image_path = os.path.join(Config.UPLOAD_FOLDER, filename_path)
        image.save(image_path)
        return f"/static/logos/{filename_path}"
    return None
