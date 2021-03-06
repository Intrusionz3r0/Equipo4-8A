import os
from flask import Flask,render_template,request,redirect,url_for,abort
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from modelo.models import Empleados,Usuarios,Turnos
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, current_user, logout_user, login_required



app = Flask(__name__)
app.secret_key = "s3cr3t"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin@localhost/ERP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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
    tu=Turnos()
    registro=tu.consultaGeneral()
    return render_template('Turnos/OpcionesTurnos.html',rg=registro) 


@app.route('/editarTurno/<int:id>')
def ventanaEditarTurno(id):
    tu=Turnos()
    tu.id_turno=id
    registro=tu.consultaIndividual()
    return render_template('Turnos/modificarTurnos.html', rg=registro)


@app.route('/eliminarTurno/<int:id>')
def ventanaEliminarTurno(id):
    tu=Turnos()
    tu.id_turno=id
    tu.eliminar()
    return render_template('Turnos/registrarTurnos.html')


@app.route('/insertarTurnosBD', methods=['POST'])
def insertTurnosBD():
    tu=Turnos()
    tu.nombre=request.form['nombre']
    tu.hora_entrada=request.form['hentrada']
    tu.hora_salida=request.form['hsalida']
    tu.estatus='Activo'
    tu.insertar()
    return redirect (url_for('ventanaOpcionesTurno')) 

@app.route('/actualizarTurnosBD', methods=['POST'])
def actualzarTurnosBD():
    tu=Turnos()
    tu.id_turno=request.form['idturno']
    tu.nombre=request.form['nombre']
    tu.hora_entrada=request.form['hentrada']
    tu.hora_salida=request.form['hsalida']
    tu.estatus=request.form['estatus']
    tu.actualizar()
    return redirect(url_for('ventanaOpcionesTurno'))




   

#Apartado de Adrian

@app.route('/registrarEmpleado')
def ventanaRegistrarEmpleado():
   return render_template("Empleados/registrarEmpleado.html")





   


if __name__ == '__main__':
    app.run(port = 3000, debug = True)