import requests
import time

SERVER_URL = "SECRET_URL"  # Replace with actual server URL
API_KEY = "SECRET_KEY"  # Replace with actual API key

headers = {"Authorization": f"Bearer {API_KEY}"}  # Use API key for authentication

# Simulating some processing
print("Person 1 is working...")
time.sleep(5)  # Simulating work

# Notify the Flask server that Person 1 is done
response = requests.post(SERVER_URL, headers=headers)

if response.status_code == 200:
    print("Successfully notified the server:", response.json())
else:
    print("Failed to notify the server:", response.status_code, response.text)
