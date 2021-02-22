from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hi'

@app.route('/home')
def home():
    f = open('../HTML/index.html')
    s = f.read()
    return s

app.run(debug=True)