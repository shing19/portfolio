from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
<<<<<<< HEAD
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')
=======
    return render_template('index.html')
>>>>>>> 41813097e4030903ac1a3b4aa115226a69af741e
