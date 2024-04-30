import os
from flask import Flask, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
from detection import run_detection_script
from typing import List, Optional

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.jpeg', '.mp4']
app.config['UPLOAD_PATH'] = 'static/uploads'

class Detector:
    # set up the upload directory and what extensions are allowed (for file safety)
    def __init__(self, upload_dir: str, allowed_extensions: List[str]):
        self.upload_dir = upload_dir
        self.allowed_extensions = allowed_extensions

    # see if a file has the right extension
    def is_file_allowed(self, filename: str) -> bool:
        file_ext = os.path.splitext(filename)[1]
        return filename != '' and file_ext in self.allowed_extensions

    # save a file to flask's static directory
    def save_file(self, file) -> Optional[str]:
        filename = secure_filename(file.filename)
        if filename and self.is_file_allowed(filename):
            file_path = os.path.join(self.upload_dir, filename)
            file.save(file_path)
            return file_path
        return None

    # run inference on the file using the detection script
    def process_file(self, file_path: str) -> str:
        return run_detection_script(file_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    label_path = None
    if request.method == 'POST':
        uploaded_file = request.files['file']
        # initialize detector
        d = Detector(app.config['UPLOAD_PATH'], app.config["UPLOAD_EXTENSIONS"])
        file_path = d.save_file(uploaded_file)
        if file_path is None:
            abort(400)
        # run detection script       
        label_path = d.process_file(file_path)
        # save to static folder
        label_path = url_for('static', filename=label_path)
    return render_template('index.html', filename=label_path) 