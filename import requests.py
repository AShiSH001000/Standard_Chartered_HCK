import requests

# Base URL of the Flask server
base_url = 'http://localhost:5000'
# Dummy user credentials for testing
username = 'user1'
password = 'password1'
# POST request to the /login route for authentication
login_url = f'{base_url}/login'
login_response = requests.post(login_url, auth=(username, password))
print('Login Response:', login_response.json())
# POST request to the /start_kyc route to initiate KYC session
start_kyc_url = f'{base_url}/start_kyc'
start_kyc_response = requests.post(start_kyc_url, auth=(username, password))
print('Start KYC Response:', start_kyc_response.json())
# POST request to the /upload_video route to upload a video file
upload_video_url = f'{base_url}/upload_video'
file_path = 'path/to/your/video/file.mp4'  # Replace with the actual file path
files = {'file': open(file_path, 'rb')}
upload_video_response = requests.post(upload_video_url, auth=(username, password), files=files)
print('Upload Video Response:', upload_video_response.json())
