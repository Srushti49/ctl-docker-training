from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

def run_script(script_path, *args):
    try:
        result = subprocess.run(['python3', script_path, *args], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    operation = request.form['operation']
    num1 = request.form['num1']
    num2 = request.form['num2']

    script_path = f'{operation}_script.py'  # Replace with the actual path to your scripts
    result = run_script(script_path, str(num1), str(num2))
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
