# from flask import Flask, request, jsonify
# import requests  # Used to send HTTP requests to the agent

# app = Flask(__name__)

# # Endpoint to communicate with the intelligent agent
# @app.route('/query-agent', methods=['POST'])
# def query_agent():
#     data = request.json  # Get the JSON data sent from the client

#     # URL where the intelligent agent is running
#     AGENT_URL = "https://riju-pant.ap.xpressai.cloud/api/data-processing/"  # Change this if necessary

#     try:
#         # Forward the request to the agent
#         response = requests.post(AGENT_URL, json=data)

#         # Return the agent's response to the client
#         return jsonify(response.json()), response.status_code
#     except requests.exceptions.RequestException as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)

# app.py


# from flask import Flask, render_template, request, redirect, session

# app = Flask(__name__)

# # Set a secret key for encrypting session data
# app.secret_key = 'my_secret_key'

# # dictionary to store user and password
# users = {
# 	'kunal': '1234',
# 	'user2': 'password2'
# }

# # To render a login form 
# @app.route('/')
# def view_form():
# 	return render_template('login.html')

# # For handling get request form we can get
# # the form inputs value by using args attribute.
# # this values after submitting you will see in the urls.
# # e.g http://127.0.0.1:5000/handle_get?username=kunal&password=1234
# # this exploits our credentials so that's 
# # why developers prefer POST request.
# @app.route('/handle_get', methods=['GET'])
# def handle_get():
# 	if request.method == 'GET':
# 		username = request.args['username']
# 		password = request.args['password']
# 		print(username, password)
# 		if username in users and users[username] == password:
# 			return '<h1>Welcome!!!</h1>'
# 		else:
# 			return '<h1>invalid credentials!</h1>'
# 	else:
# 		return render_template('login.html')

# # For handling post request form we can get the form
# # inputs value by using POST attribute.
# # this values after submitting you will never see in the urls.
# @app.route('/handle_post', methods=['POST'])
# def handle_post():
# 	if request.method == 'POST':
# 		username = request.form['username']
# 		password = request.form['password']
# 		print(username, password)
# 		if username in users and users[username] == password:
# 			return '<h1>Welcome!!!</h1>'
# 		else:
# 			return '<h1>invalid credentials!</h1>'
# 	else:
# 		return render_template('login.html')

# if __name__ == '__main__':
# 	app.run()

from flask import Flask, request, jsonify
#from openai import OpenAI

app = Flask(__name__)

# Xpress AI Agent API details
XPRESS_AI_URL = "https://riju-pant.ap.xpressai.cloud/api/data-processing/"
XPRESS_AI_KEY = "53bf7cb8-f809-4511-b00a-dd573ea0964a"  # Replace with your actual API key



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)