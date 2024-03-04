from flask import Flask, render_template
from flask_scss import Scss

app = Flask(__name__)
#Habilitamos la compilación automática de archivos .scss
Scss (app)

@app.route('/')
def index():
    return render_template('login.html')