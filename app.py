from flask import Flask, render_template, request

from src import functions as f

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator', methods=['GET'])
def calculator_show_form():
    return render_template('calculator.html', showForm=True)

@app.route('/calculator', methods=['POST'])
def calculator_process():

    showForm = False if 'angle' in request.form else True

    if not showForm:
        angle = float(request.form['angle'])
        velocity = float(request.form['velocity'])
        gravity = float(request.form['gravity'])

        results = f.calculate(angle, velocity, gravity)

    return render_template('calculator.html', showForm=showForm, results=results)

if __name__ == '__main__':
    app.run(debug=True)