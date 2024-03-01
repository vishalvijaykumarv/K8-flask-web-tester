from flask import Flask, request, jsonify, render_template
import time
from lib_platform import platform as sys_platform

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/hello/<name>', methods=['GET'])
def hello_name(name):
    return f"Hello, {name}!"

@app.route('/system_info', methods=['GET'])
def system_info():
    info = {
        'system': sys_platform.system(),
        'node': sys_platform.node(),
        'release': sys_platform.release(),
        'version': sys_platform.version(),
        'processor': sys_platform.processor()
    }
    return jsonify(info), 200

@app.route('/calculator', methods=['POST'])
def calculator():
    data = request.json
    num1 = data.get('num1')
    num2 = data.get('num2')
    
    if num1 is None or num2 is None:
        return jsonify({'error': 'Please provide both numbers'}), 400
    
    result = int(num1) + int(num2)
    return jsonify({'result': result}), 200

@app.route('/sleep', methods=['POST'])
def sleep_function():
    data = request.json
    digit = data.get('digit')
    if digit is None:
        return jsonify({'error': 'Please provide a digit'}), 400
    
    start_time = time.time()
    time.sleep(int(digit))
    end_time = time.time()

    return jsonify({'start_time': start_time, 'end_time': end_time}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

