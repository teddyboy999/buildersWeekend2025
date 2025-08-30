import requests
import time

SERVER_URL = "https://riju-pant.ap.xpressai.cloud/api/data-processing//check_status"  # Replace with actual server URL
API_KEY = "b2e29137-aa08-4594-b60e-72ac511e952a"  # Replace with actual API key

headers = {"Authorization": f"Bearer {API_KEY}"}  # Use API key for authentication

while True:
    response = requests.get(SERVER_URL, headers=headers)
    
    if response.status_code == 200:
        status = response.json()
        if status.get("person1_done"):
            print("Person 1 is done! Person 2 can start now.")
            break
        else:
            print("Waiting for Person 1 to finish...")
    else:
        print("Failed to check status:", response.status_code, response.text)

    time.sleep(2)  # Check every 2 seconds

# Now Person 2's actual work can start
print("Person 2 is now starting their task.")