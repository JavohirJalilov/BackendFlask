from flask import Flask,request

app = Flask(__name__)


@app.route('/api',methods=['GET','POST'])
def api():
    if request.method == 'GET':
        r = request.args
        a = int(r.get('a',0))
        b = int(r.get('b',0))
        return {'sum':a+b}
    
    if request.method == 'POST':
        r = request.json
        a = r.get('a',0)
        b = r.get('b',0)
        print(r)
        return {'sum':a+b}
        
@app.route('/form',methods=['GET','POST'])
def get_form():
    if request.method == 'GET':
        a = request.form.get('a',0)
        b = request.form.get('b',0)
        return {'sum':int(a)+int(b)}

    if request.method == 'POST':
        a = request.form.get('a',0)
        b = request.form.get('b',0)
        return {'sum':int(a)+int(b)}

@app.route('/index')
@app.route('/')
def home():
    path = request.path
    full_path= request.full_path
    root=request.script_root
    base_url=request.base_url
    url = request.url
    total = f"""
       <p> path: {path}</p>
       <p> full_path: {full_path}</p>
       <p> script_root: {root}</p>
        <p> base_url:{base_url}</p>
       <p> url: {url}</p>
        """
        
    return total
if __name__ == '__main__':
    app.run(debug=True)