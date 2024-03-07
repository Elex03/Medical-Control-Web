from flask import Flask, render_template
from flask_scss import Scss

app = Flask(__name__)
#Habilitamos la compilación automática de archivos .scss
Scss (app)

paciente = [
    {"name": "Sofia Ramirez Moreno", "id": "001-090205-1003N"},
    {"name": "Javier Fernandez Gomez", "id": "001-090205-1003N"},
    {"name": "Ana Martinez Rodriguez", "id": "001-090205-1003N"}
    ]

cita = [
    {"name": "Sofia Ramirez Moreno", "id": "001-090205-1003N", "Fecha": "02/02/2024", "Hora": "12:00pm"},
    {"name": "Javier Fernandez Gomez", "id": "001-090205-1004N", "Fecha": "02/02/2024", "Hora": "12:00pm"},
    {"name": "Ana Martinez Rodriguez", "id": "001-090205-1005N", "Fecha": "02/02/2024", "Hora": "12:00pm"}
    ]

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/pacientes', methods=["GET", "POST"])
def pacientes():
    
    return render_template('index.html', pacientes=paciente)

@app.route('/citas', methods=["GET"])
def citas():
    return render_template('citas.html', citas=cita)

if __name__ == '__main__':
    app.run(debug=True)