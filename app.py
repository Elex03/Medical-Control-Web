from flask import Flask, render_template
from flask_scss import Scss

app = Flask(__name__)
#Habilitamos la compilación automática de archivos .scss
Scss (app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/pacientes', methods=["POST"])
def pacientes():
    
    pacientes = [
    {"name": "Sofia Ramirez Moreno", "id": "001-090205-1003N"},
    {"name": "Javier Fernandez Gomez", "id": "001-090205-1003N"},
    {"name": "Ana Martinez Rodriguez", "id": "001-090205-1003N"}
    ]
    

    return render_template('index.html', pacientes=pacientes)