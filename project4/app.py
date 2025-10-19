from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route (Feedback Form)
@app.route('/')
def feedback():
    return render_template('feedback.html')

# When user submits the feedback form
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    feedback = request.form['feedback']
    
    # You can later save this to a database or file
    print(f"Feedback received from {name}: {feedback}")
    
    # After submitting, redirect to Thank You page
    return redirect(url_for('thankyou'))

# Thank you page route
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
