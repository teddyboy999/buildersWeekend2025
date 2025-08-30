import requests
import time

SERVER_URL = "https://riju-pant.ap.xpressai.cloud/api/data-processing//set_done"  # Replace with actual server URL
API_KEY = "b2e29137-aa08-4594-b60e-72ac511e952a"  # Replace with actual API key

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}  # Use API key for authentication

# Simulating some processing
print("Person 1 is working...")
time.sleep(5)  # Simulating work

# Notify the Flask server that Person 1 is done
response = requests.post(SERVER_URL, headers=headers, json={})

if response.status_code == 200:
    print("Successfully notified the server:", response.json())
else:
    print("Failed to notify the server:", response.status_code, response.text)
