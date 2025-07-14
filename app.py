from flask import Flask, request, render_template
from conversion import calc_length, calc_temperature, calc_weight

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        origin = request.form['origin']
        value = float(request.form['value'])
        unit_from = request.form['unit_from']
        unit_to = request.form['unit_to']

        if origin == 'weight':
            result = calc_weight(value, unit_from, unit_to)
            return render_template('weight.html', result=result)
        elif origin == 'length':
            result = calc_length(value, unit_from, unit_to)
            return render_template('length.html', result=result)
        elif origin == 'temperature':
            result = calc_temperature(value, unit_from, unit_to)
            return render_template('temperature.html', result=result)

    #.. GET request
    origin = request.args.get('origin', 'temperature')
    
    if origin == 'weight':
        return render_template('weight.html')
    elif origin == 'length':
        return render_template('length.html')
    else:
        return render_template('temperature.html')



if __name__ == '__main__':
    app.run(debug=True)
