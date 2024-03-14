from flask import Flask, request, jsonify, abort
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Dummy user data (for demonstration purposes)
users = {
    'user1': {'password': 'password1', 'kyc_status': 'pending'},
    'user2': {'password': 'password2', 'kyc_status': 'pending'}
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Server is running!'})

@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Authentication failed!'}), 401

    if auth.username not in users or users[auth.username]['password'] != auth.password:
        return jsonify({'message': 'Authentication failed!'}), 401

    return jsonify({'message': 'Login successful!'}), 200

@app.route('/start_kyc', methods=['POST'])
def start_kyc():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Authentication failed!'}), 401

    if auth.username not in users or users[auth.username]['password'] != auth.password:
        return jsonify({'message': 'Authentication failed!'}), 401

    if users[auth.username]['kyc_status'] != 'pending':
        return jsonify({'message': 'KYC already completed!'}), 400

    return jsonify({'message': 'KYC session started successfully!'}), 200

@app.route('/upload_video', methods=['POST'])
def upload_video():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Authentication failed!'}), 401

    if auth.username not in users or users[auth.username]['password'] != auth.password:
        return jsonify({'message': 'Authentication failed!'}), 401

    if 'file' not in request.files:
        return jsonify({'message': 'No file part!'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file!'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        users[auth.username]['kyc_status'] = 'completed'
        return jsonify({'message': 'File uploaded successfully!'}), 200

    return jsonify({'message': 'Invalid file type!'}), 400

if __name__ == '__main__':
    app.run(debug=True)






# OCR Implementation
#LLM
