# server.py
print("Starting server.py...")
from flask import Flask, jsonify
import subprocess
from flask_cors import CORS

print("Imports completed.")
app = Flask(__name__)
CORS(app)

@app.route('/run-python', methods=['GET'])
def run_python():
    print("Endpoint /run-python called.")
    try:
        result = subprocess.run(['python3', '/Users/bhushithgh/University/BuildersWeekend2025/morph-test1/src/python/morphSendRequest.py'], capture_output=True, text=True)
        print("Subprocess completed.")
        return jsonify({
            'output': result.stdout,
            'error': result.stderr,
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'output': '',
            'error': str(e),
            'status': 'error'
        })

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True, port=5000)