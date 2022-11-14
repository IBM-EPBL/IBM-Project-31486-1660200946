from flask import Flask , render_template,request,json
app = Flask(__name__)

@app.route('/')
def home():
    return  render_template('index.html')
@app.route("/siginin",methods=['POST'])
def sigmin():
     username=request.form['username']
     password =request.form['password']
     if username and password:
        return json.dumps({'validation':(username,password)})
     return json.dumps({'validation':False})