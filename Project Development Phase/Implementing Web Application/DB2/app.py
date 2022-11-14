import ibm_db

try:
    conn=ibm_db.connect('DATABASE=Db2-xx;'
                        'HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;'
                        'PORT=32286;'
                        'PROTOCOL=TCPIP;'
                        'UID=hvy33302;'
                        'PWD=2c38FddyFrKTmo0H;','','')
    print("connected")

except:
     print("not connected")


from flask import Flask;
from flask import render_template;
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
 return render_template('home.html')

@app.route("/index")
def index():
 return render_template('index.html')

@app.route("/about")
def about():
 return render_template('about.html')

@app.route("/signup")
def signup():
 return render_template('signup.html')

@app.route("/welcome")
def welcomepage():
 return render_template('welcome.html')


@app.route("/welcomepage")
def welcomepage():
 return render_template('welcomepage.html')


if __name__=='__main__':
 app.run(debug=True)