from flask import Flask, request, redirect, render_template
from Morse_Converter import MorseConverter

app = Flask(__name__)

@app.route('/', methods=['POST', "GET"])
def home():
    output_string = None
    input_string = None
    if request.method == 'POST':
        input_string = request.form['string']
        morseconverter = MorseConverter()
        output_string = morseconverter.to_morse_code(input_string)
        return render_template('index.html', output_string=output_string, input_string=input_string)
    return render_template('index.html', output_string=output_string, input_string=input_string)


if '__main__' == __name__:
    app.run(host='127.0.0.1', port=5000, debug=True)