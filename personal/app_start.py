from flask import (
    Flask,
    g, 
    redirect,
    render_template,
    request,
    session,
    url_for
)

import RPi.GPIO as GPIO

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='huhjb1020@naver.com', password='8250'))

app = Flask(__name__)
app.secret_key = 'junbeom_personal_project'


@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

@app.route("/", methods=['GET', 'POST'])
def loginPage():
    if request.method == 'POST':
        session.pop('user_id', None)

        #get inputUser
        username = request.form['inputEmail']
        password = request.form['inputPassword']
        
        #check defineUser vs inputUser 
        userInput = [x for x in users if x.username == username] 

        #wrong email
        if not userInput:
            return redirect(url_for('home'))
        #right email
        else:
            user = userInput[0]

        #right password -> login success
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('home'))
        #wrong password -> login fail
        else:
            return redirect(url_for('loginPage'))

    return render_template("login.html")


@app.route("/index")
def home():
    if not g.user:
        return redirect(url_for('loginPage'))

    return render_template("index.html")

@app.route("/car")
def car():
    state = request.args.get("state", "error")
    
    if state == "forward":
        print("forward")
    elif state == "left":
        print("left")
    elif state == "stop":
        print("stop")
    elif state == "right":
        print("right")
    elif state == "backward":
        print("backward")
    elif state == "error":
        print("miss querystring")
    else:
        print("wrong querystring")
    
    return "car " + state

@app.route("/camera")
def camera():
    state = request.args.get("state", "error")
    
    if state == "camera-left":
        print("camera-left")
    elif state == "camera-right":
        print("camera-right")
    elif state == "stop":
        print("stop")
    elif state == "error":
        print("miss querystring")
    else:
        print("wrong querystring")
    
    return "camera " + state


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
