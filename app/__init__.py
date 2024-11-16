from flask import Flask
import os
import logging

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
    app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # Limit to 50 MB
    app.config['SECRET_KEY'] = os.urandom(24)  # Add this line


    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
