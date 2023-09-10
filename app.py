from flask import Flask, request,redirect, render_template
import os
from werkzeug.utils import secure_filename
import main5

app = Flask(__name__)

UPLOAD_FOLDER = 'sample'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods = ["GET"])
def index():
    return render_template('index.html')

@app.route('/pricing', methods = ["GET"])
def pricing():
    return render_template('pricing.html')

@app.route('/process', methods = ["GET"])
def process():
    return render_template('process.html')

@app.route('/chats', methods = ["GET"])
def chats():
    return render_template('chats.html')

@app.route('/contactus', methods = ["GET"])
def contactus():
    return render_template('contactus.html')

@app.route('/login', methods = ["GET"])
def login():
    return render_template('login.html')

@app.route('/profile', methods = ["GET"])
def profile():
    return render_template('profile.html')

@app.route('/aboutus', methods = ["GET"])
def aboutus():
    return render_template('aboutus.html')

@app.route('/result', methods = ["GET"])
def result():
    return render_template('result.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Get the user's preference from the form
        preference = request.form.get('preference')

        # Call the predictss function from main.py to calculate compatibility
        most_compatible_resume, compatibility_score_normalized= main5.predictss(
            "Female"
        )

        return render_template(
            'result.html',
            compatible_resume=most_compatible_resume, score=compatibility_score_normalized
        )

if __name__ == '__main__':
    app.run(debug=True)

