flask-login-app/          ← root of your repo
│
├── app.py               ← your Flask backend
└── templates/           ← folder for all HTML files
     ├── login.html      ← login form
     └── welcome.html    ← subjects page after login

app.py :

from flask import Flask, request, render_template

app = Flask(__name__)

# Home page → shows login form
@app.route("/")
def login():
    return render_template("login.html")

# Form submission → handle login
@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    # Example users with details
    users = {
        "admin": {
            "password": "123",
            "is_topper": True,
            "subjects": ["Maths", "Science", "History"]
        },
        "gowi": {
            "password": "456",
            "is_topper": False,
            "subjects": ["Physics", "Chemistry", "Biology"]
        },
        "gie": {
            "password": "789",
            "is_topper": True,
            "subjects": ["English", "Geography", "Computer"]
        }
    }

    if username in users and users[username]["password"] == password:
        user_info = users[username]
        # Send info to welcome.html
        return render_template(
            "welcome.html",
            name=username,
            is_topper=user_info["is_topper"],
            subjects=user_info["subjects"]
        )
    else:
        return "Invalid credentials"

if __name__ == "__main__":
    app.run(debug=True)



login.html

<!DOCTYPE html>
<html>
<head>
    <title>My Form</title>
</head>
<body>
    <h2>Login Form</h2>
    <form action="/submit" method="POST">

        <label>Username:</label>
        <input type="text" name="username" required placeholder="enter username"><br><br>
        <label>Password:</label>
        <input type="password" name="password" required placeholder="enter password"><br><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>



welcome.html

<!DOCTYPE html>
<html>
<head>
    <title>Subjects</title>
</head>
<body>
    <h2>Welcome, {{ name }}!</h2>

    <h3>Your Subjects:</h3>
    <ul>
        {% for subject in subjects %}
            <li>{{ subject }}</li>
        {% endfor %}
    </ul>
</body>
</html>
