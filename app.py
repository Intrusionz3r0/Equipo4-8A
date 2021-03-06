import os
from flask import Flask,render_template,request,redirect,url_for,abort
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from modelo.models import Empleados,Usuarios
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.secret_key = "s3cr3t"


@app.route('/')
def login():
    return render_template('Login.html')

@app.route('/template')
def principal():
    return render_template('template.html')

#Apartado de Alejandra

@app.route('/crearTurno')
def ventanaCrearTurno():
    return render_template('Turnos/registrarTurnos.html')

@app.route('/OpcionesTurnos')
def ventanaOpcionesTurno():
    return render_template('Turnos/OpcionesTurnos.html')    


#Apartado de Adrian

@app.route('/registrarEmpleado')
def ventanaRegistrarEmpleado():
   return render_template("Empleados/registrarEmpleado.html")





   


if __name__ == '__main__':
    app.run(port = 3000, debug = True)