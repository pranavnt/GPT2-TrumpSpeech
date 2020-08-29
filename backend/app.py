from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def generate_trump():
    seed = request.form['seed']
    return "<html><body><p>seed</p></body></html>"


app.run(debug=True, host='localhost', port=5343)
