import os
import shutil
import zipfile
import subprocess
from .handlers import odm, yolo
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, send_file

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')

    files = request.files.getlist('images')
    upload_folder = current_app.config['UPLOAD_FOLDER']

    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    for file in files:
        filename = secure_filename(file.filename)
        temp_path = os.path.join(upload_folder, filename)
        file.save(temp_path)

        results = yolo.run(temp_path) 

        processed_file_path = os.path.join(upload_folder, f"processed_{filename}")
        results[0].save(processed_file_path)

        os.remove(temp_path) 

    return redirect(url_for('main.processing'))

@main_bp.route('/processing')
def processing():
    upload_folder = current_app.config['UPLOAD_FOLDER']
    images_folder = os.path.join(upload_folder, 'datasets', 'project', 'images')

    try:
        os.makedirs(images_folder, exist_ok=True)

        isPicture = lambda file: file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))
        movePicture = lambda filename: shutil.move(os.path.join(upload_folder, filename), os.path.join(images_folder, filename)) if isPicture(filename) else None

        list(map(movePicture, os.listdir(upload_folder)))

        odm.run(os.path.join(upload_folder, 'datasets'))

        return redirect(url_for('main.results'))

    except Exception as e:
        return f"Error during processing: {e}", 500

@main_bp.route('/results')
def results():
    upload_folder = current_app.config['UPLOAD_FOLDER']
    output_folder = os.path.join(upload_folder, 'datasets', 'project')

    try:
        result_files = [f for f in os.listdir(output_folder) if os.path.isfile(os.path.join(output_folder, f))]

        return render_template('results.html', files=result_files)
    except Exception as e:
        print(f"Error displaying results: {e}")
        return f"Error displaying results: {e}", 500

@main_bp.route('/download/<filename>')
def download(filename):
    upload_folder = current_app.config['UPLOAD_FOLDER']
    output_folder = os.path.join(upload_folder, 'datasets', 'project')
    zip_filename = os.path.join(upload_folder, 'processed_output.zip')
    
    if (filename != 'all'):
        try:
            return send_file(os.path.join(output_folder, filename), as_attachment=True)

        except FileNotFoundError:
            return f"File {filename} not found in {output_folder}.", 404

    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(output_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, output_folder)
                    zipf.write(file_path, arcname)

        response = send_file(zip_filename, as_attachment=True)

        shutil.rmtree(os.path.join(upload_folder, 'datasets','output'))
        shutil.rmtree(output_folder) 
        os.makedirs(output_folder)

        return response

    except Exception as e:
        return f"Error creating or serving ZIP: {e}", 500
