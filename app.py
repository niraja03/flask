from flask import Flask, request, render_template

app = Flask(__name__)
app.secret_key = "supersecret"
app=Flask(__name__)

# Home / Login page
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    
    #for multiple users
    valid_users ={
        'admin' : '123',
        'gowi' : '456',
        'gie' : '789'
    }
    if username in valid_users and valid_users[username] == password:
        return render_template("welcome.html", name=username)
    else:
        return "invalid ccredentials"
    

if __name__ == "__main__":
    app.run(debug=True)
