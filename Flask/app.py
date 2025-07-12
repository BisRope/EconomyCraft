from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='web', static_url_path='')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    full_path = os.path.join(app.static_folder, path)
    if os.path.isfile(full_path):
        return send_from_directory(app.static_folder, path)
    else:
        # Fallback to index.html WITHOUT 404
        return send_from_directory(app.static_folder, 'index.html')
