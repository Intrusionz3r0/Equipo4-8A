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
loginManager=LoginManager()
loginManager.init_app(app)
loginManager.login_view="login"
db = SQLAlchemy(app)


@loginManager.user_loader
def load_user(id):
    return Usuarios.query.get(int(id))




@app.route('/')
def login():
    return render_template('Login.html')

@app.route("/login",methods=['POST'])
def iniciarSesion():
    Us=Usuarios()
    Us=Us.validar(request.form['username'],request.form['pass'])
    if(Us!=None):
        login_user(Us)
        return render_template("home.html")
    else:
        return "El usuario o la contraseña es invalido"

@app.route("/CerrarSesion")
def cerrarSes():
    if(current_user.is_authenticated):
         logout_user()
         return redirect(url_for("login"))
    else:
        abort(404)

#Apartado de Alejandra

@app.route('/crearTurno')
@login_required
def ventanaCrearTurno():
    return render_template('Turnos/registrarTurnos.html')

@app.route('/OpcionesTurnos')
@login_required
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
    try:
        tu.eliminar()
    except:
        return "No se puede eliminar"

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