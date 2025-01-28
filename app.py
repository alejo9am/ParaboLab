from flask import Flask, render_template, request

from src.physics import calculate as calculate_params
from src.graph import calculate_points, plot_points

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator', methods=['GET'])
def calculator_show_form():
    # show form with values if they are present in the query string
    params = {'angle': '', 'velocity': ''}
    
    if 'angle' in request.args:
        params['angle'] = request.args['angle']
    if 'velocity' in request.args:
        params['velocity'] = request.args['velocity']

    return render_template('calculator.html', showForm=True, params=params)

@app.route('/calculator', methods=['POST'])
def calculator_process():

    showForm = False if 'angle' in request.form else True

    if not showForm:
        angle = float(request.form['angle'])
        velocity = float(request.form['velocity'])
        gravity = float(request.form['gravity'])

        # Calculate the parabola parameters
        results = calculate_params(angle, velocity, gravity)

        # Calculate the x and y points for rendering the parabola
        x_points, y_points = calculate_points(velocity, angle, gravity, results['time'])

        # Encode the plot to base64
        image = plot_points(x_points, y_points)
        

    return render_template('calculator.html', showForm=showForm, results=results, image=image)

if __name__ == '__main__':
    app.run(debug=True)