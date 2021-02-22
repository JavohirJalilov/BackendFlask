from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    s = 'Hello <a href="http://127.0.0.1:5000/home">flask</a>'
    return s

@app.route('/home')
def home():
    f = open('../HTML/index.html')
    s = f.read()
    return s

if __name__ == '__main__':
    app.run(debug=True)