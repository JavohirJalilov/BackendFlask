from flask import Flask,request
import json
app = Flask(__name__)

@app.route('/')
def country():
    return 'ok'

@app.route('/capital',methods=['GET','POST'])
def capital():
    if request.method == 'GET':
        r = request.args
        country = r.get('country')
        return {country:0}


    if request.method == 'POST':
        r = request.form
        f = open('capital.json').read()
        data = json.loads(f)
        country = r.get('country')
        city = 'Not Fount'
        for i in data:
            if i['country'] == country:
                city = i['city']
                break
            
        return {'country':country,'city':city}

if __name__ == '__main__':
    app.run(debug=True)