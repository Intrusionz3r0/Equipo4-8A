import os,random,string
from flask import Flask,render_template,request,redirect,url_for,abort
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from modelo.models import Empleados,Usuarios,Turnos,Aulas,Edificios,Alumnos,Grupos,Materia,Documentos,Calificacion
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, current_user, logout_user, login_required




app = Flask(__name__)
app.secret_key = "s3cr3t"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin@localhost/ERP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 100
app.config['UPLOAD_FOLDER'] = "static/uploads/"
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
    if(Us!=None and Usuarios.is_active(Us)):
        login_user(Us)
        return render_template("home.html")
    else:
        return "El usuario o la contraseña es invalido"

@app.route('/homebase')
@login_required
def homi():
    return render_template("home.html")
    
@app.route('/template')
def template():
   return render_template('template.html')

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
@login_required
def ventanaEditarTurno(id):
    tu=Turnos()
    tu.id_turno=id
    registro=tu.consultaIndividual()
    return render_template('Turnos/modificarTurnos.html', rg=registro)


@app.route('/eliminarTurno/<int:id>')
def ventanaEliminarTurno(id):
    tu=Turnos()
    tu.id_turno=id
    tu.estatus="Inactivo"
    tu.actualizar()

    return redirect(url_for('ventanaOpcionesTurno'))


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
@login_required
def ventanaRegistrarEmpleado():
   return render_template("Empleados/registrarEmpleado.html")

@app.route('/editarEmpleado/<int:id>')
@login_required
def ventanaEditarEmpleado(id):
    
    emp = Empleados()
    emp.id_empleado=id
    empleados = emp.consultaIndividual()

    usr= Usuarios()
    usr.id_usuario=empleados.id_usuario
    usuarios=usr.consultaIndividual()
    
    return render_template("Empleados/modificarEmpleado.html",usuarios=usuarios,empleados=empleados)


@app.route('/opcionesEmpleados')
@login_required
def ventanaOpcionesEmpleados():
    usr = Usuarios()
    page = int(request.args.get('page', 1))
    post_pagination = usr.all_paginated(page, 10)
    return render_template('Empleados/opcionesEmpleados.html',post_pagination=post_pagination)
   

@app.route('/eliminarEmpleado/<int:id>')
def eliminarEmpleado(id):
    usr=Usuarios()
    usr.id_usuario=id
    datos=usr.consultaIndividual()
    usr.estatus_usuario="Inactivo"
    usr.actualizar()
    
    return redirect(url_for('ventanaOpcionesEmpleados'))
   


@app.route('/insertarEmpleado', methods=['POST'])
def registrarEmpleadoBD():
    usr = Usuarios()
    emp = Empleados()
    usr.nombre=request.form['nombre']
    usr.apellido_paterno=request.form['apaterno']
    usr.apellido_materno=request.form['amaterno']
    usr.genero=request.form['genero']
    usr.tipo =request.form['tusuario'] 
    emp.salario_diario=request.form['sdiario']
    emp.fecha_contracion=request.form['fcontratacion']
    emp.nss=request.form['nss']
    usr.fecha_nacimiento=request.form['fnacimiento']
    usr.fecha_registro=request.form['fregistro']
    usr.correo=request.form['correo']
    usr.telefono=request.form['telefono']
    emp.dias_vacaciones=request.form['dvacaciones']
    emp.dias_permiso=request.form['dpermiso']
    usr.colonia=request.form['colonia']
    usr.calle=request.form['calle']
    usr.numero_casa=request.form['ncasa']
    usr.usuario=request.form['usuario']
    usr.passwd=request.form['pass1']
    usr.estatus_usuario="Activo"
    RFC= usr.apellido_paterno[:2]+usr.apellido_materno[:1]+usr.nombre[:1]+str(usr.fecha_nacimiento.split("-")[0][2:])+str(usr.fecha_nacimiento.split("-")[1])+usr.fecha_nacimiento.split("-")[2]+random.choice(string.ascii_letters)+str(random.randrange(10))+random.choice(string.ascii_letters)
    emp.rfc=RFC.upper()
    

    foto=request.files['file']
    os.mkdir("static/uploads/"+emp.rfc)
    filename1 = secure_filename(foto.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER']+emp.rfc, foto.filename)
    foto.save(path)
    emp.foto=filename1

    usr.insertar()

    emp.id_usuario=usr.id_usuario
    emp.insertar()
    return redirect(url_for('ventanaOpcionesEmpleados'))


@app.route('/actualizarEmpleado', methods=['POST'])
def actualizarEmpleadoDB():

    usr = Usuarios()
    emp = Empleados()
    usr.id_usuario=request.form['idusuario']
    emp.id_empleado=request.form['idemp']
    usr.nombre=request.form['nombre']
    usr.apellido_paterno=request.form['apaterno']
    usr.apellido_materno=request.form['amaterno']
    usr.genero=request.form['genero']
    emp.tipo =request.form['tusuario'] 
    emp.salario_diario=request.form['sdiario']
    emp.fecha_contracion=request.form['fcontratacion']
    emp.nss=request.form['nss']
    usr.fecha_nacimiento=request.form['fnacimiento']
    usr.fecha_registro=request.form['fregistro']
    usr.correo=request.form['correo']
    usr.telefono=request.form['telefono']
    emp.dias_vacaciones=request.form['dvacaciones']
    emp.dias_permiso=request.form['dpermiso']
    usr.colonia=request.form['colonia']
    usr.calle=request.form['calle']
    usr.numero_casa=request.form['ncasa']
    usr.usuario=request.form['usuario']
    usr.passwd=request.form['pass1']
    usr.estatus_usuario="Activo"
    usr.actualizar()
    emp.actualizar()

    return redirect(url_for('ventanaOpcionesEmpleados'))


#APARTADO KAREN-------------------------------------
@app.route('/insertAulas', methods = ['POST'])
@login_required
def insertAulas():
    if request.method == 'POST':
        aulas=Aulas()
        aulas.id_edificio =request.form['id_edificio']
        aulas.nombre=request.form['nombre']
        aulas.capacidad = request.form['capacidad']
        aulas.estado="Activo"

        aulas.insertar()

        return redirect(url_for('ConsultarAulas'))

@app.route('/actualizarAulas', methods=['POST'])
@login_required
def actualizarAulas():
    aulas1=Aulas()
    aulas1.id_aula=request.form['idaula']
    aulas1.nombre=request.form['nombre']
    aulas1.capacidad = request.form['capacidad']
    aulas1.estado=request.form['estadoAula']
    aulas1.id_edificio=request.form['id_edificio']

    aulas1.actualizar()

    return redirect(url_for('ConsultarAulas'))

@app.route('/eliminarAula/<int:id>/')
def eliminarAulas(id):
    aulas=Aulas()
    aulas.id_aula=id   
    aulas.estado="Inactivo"
    aulas.actualizar()
    
    return redirect(url_for('ConsultarAulas'))

@app.route('/aulas')
@login_required
def ConsultarAulas():
    au=Aulas()
    ed=Edificios()
    edificios=ed.consultaGeneral()
    aulas=au.consultaGeneral()
    return render_template("Aulas/Aulas.html", aulas=aulas,edificios=edificios)


@app.route('/editarAula/<int:id>')
@login_required
def editarAulaBD(id):
    au=Aulas()
    au.id_aula=id
    aula=au.consultaIndividual()

    ed=Edificios()
    edificios=ed.consultaGeneral()
    print(Edificios)

    return render_template('Aulas/editarAula.html',edificios=edificios,aula=aula)

#-FIN KAREN--------------------------------------------



#Apartado de Geovanni

@app.route('/crearEdificio')
@login_required
def ventanaRegistroEdificios():
    return render_template('Edificios/registrarEdificios.html')

@app.route('/opcionesEdificios')
@login_required
def ventanaOpcionesEdificios():
    edi=Edificios()
    Doc=edi.consultaGeneral()
    return render_template('Edificios/opcionesEdificios.html',Edi=Doc)

@app.route('/editarEdificios/<int:id>')
@login_required
def ventanaEditarEdificios(id):
    edi=Edificios()
    edi.id_edificio=id
    Doc=edi.consultaIndividual()
    return render_template('/Edificios/modificarEdificios.html',Edi=Doc)

@app.route('/eliminarEdificio/<int:id>')
def ventanaEliminarEdificios(id):
    Ed=Edificios()
    Ed.id_edificio=id
    Ed.estado="Inhabilitado"
    Ed.actualizar()
    return redirect(url_for('ventanaOpcionesEdificios'))

@app.route('/insertarEdificiosBD', methods=['POST'])
def insertarEdificiosBD():
    Ed=Edificios()
    Ed.nombre=request.form['NombreEdif']
    Ed.tipo=request.form['TipoEdif']
    Ed.descripcion=request.form['DescripcionEdif']
    Ed.estado='Habilitado'
    Ed.insertar()
    return redirect (url_for('ventanaOpcionesEdificios'))

@app.route('/actualizarEdificiosBD', methods=['POST'])
def actualizarEdificiosBD():
    Ed=Edificios()
    Ed.id_edificio=request.form['id_Edif']
    Ed.nombre=request.form['NombreEdif']
    Ed.tipo=request.form['TipoEdif']
    Ed.descripcion=request.form['DescripcionEdif']
    Ed.estado=request.form['EstatusEdif']
    Ed.actualizar()
    return redirect(url_for('ventanaOpcionesEdificios'))

#---Calificaciones---#

@app.route('/registrarCalificacion')
@login_required
def ventanaRegistrarCalificacion():
    return render_template('Calificaciones/registrarCalificaciones.html')

@app.route('/opcionesCalificaciones')
@login_required
def ventanaOpcionesCalificaciones():
    cali=Calificacion()
    Cal=cali.consultaGeneral()
    return render_template('Calificaciones/opcionesCalificaciones.html',Cali=Cal)

@app.route('/editarCalificacion/<int:id>')
@login_required
def ventanaEditarCalificaciones(id):
    cali=Calificacion()
    cali.id_calificacion=id
    Cal=cali.consultaIndividual()
    return render_template('Calificaciones/modificarCalificaciones.html',Cali=Cal)

@app.route('/eliminarCalificacion/<int:id>')
def ventanaEliminarCalificaciones(id):
    cali=Calificacion()
    cali.id_calificacion=id
    cali.validacion='NO'
    cali.actualizar()
    return redirect(url_for('ventanaOpcionesCalificaciones'))

@app.route('/insertarCalificacionesBD', methods=['POST'])
def insertarCalificacionesBD():
    cali=Calificacion()
    cali.id_materia=request.form['Materia']
    cali.id_alumno=request.form['Alumno']
    cali.calificacion=request.form['Calificacion']
    cali.unidad=request.form['Unidad']
    cali.validacion='SI'
    cali.insertar()
    return redirect(url_for('ventanaOpcionesCalificaciones'))

@app.route('/actualizarCalificacionesBD', methods=['POST'])
def actualizarCalificacionesBD():
    cali=Calificacion()
    cali.id_calificacion=request.form['id_Calif']
    cali.id_materia=request.form['id_Materia']
    cali.id_alumno=request.form['id_Alumno']
    cali.calificacion=request.form['Calificacion']
    cali.unidad=request.form['Unidad']
    cali.validacion=request.form['ValidaCalif']
    cali.actualizar()
    return redirect(url_for('ventanaOpcionesCalificaciones'))

#--Fin Calificaciones--#



 #--Inicio de Documentos--#

@app.route('/agregarDocumento')
@login_required
def ventanaRegistrarDocumentos():
    usu=Usuarios()
    usr=usu.consultaGeneral()
    return render_template('Documentos/RegistrarDocumentos.html',USU=usr)

@app.route('/OpcionDocumento')
@login_required
def ventanaOpcionesDocumentos():
    docu=Documentos()
    #DOC=docu.consultaGeneral()
    page = int(request.args.get('page', 1))
    post_pagination = docu.all_paginated(page, 5)
    return render_template('Documentos/opcionesDocumentos.html',post_pagination=post_pagination)

@app.route('/editarDocumentos/<int:id>')
def ventanaEditarDocumentos(id):
    docu=Documentos()
    docu.id_documento=id
    DOC=docu.consultaIndividual()
    return render_template('Documentos/modificarDocumentos.html',DOCU=DOC)

@app.route('/eliminarDocumentos/<int:id>')
def ventanaEliminarDocumentos(id):
    docu=Documentos()
    docu.id_documento=id
    docu.aprobacion="NO"
    docu.actualizar()
    return redirect(url_for('ventanaOpcionesDocumentos'))

@app.route('/insertarDocumentosBD', methods=['POST'])
def insertarDocumentosBD():
    docu=Documentos()
    docu.nombre=request.form['NombreDoc']
    docu.descripcion=request.form['DescripcionDoc']
    docu.archivo=request.form['ArchDoc']
    docu.id_usuario=request.form['ID']
    docu.aprobacion='SI'
    docu.insertar()
    return redirect(url_for('ventanaOpcionesDocumentos'))

@app.route('/actualizarDocumentosBD', methods=['POST'])
def actualizarDocumentosBD():
    docu=Documentos()
    docu.id_documento=request.form['id_doc']
    docu.nombre=request.form['NombDoc']
    docu.descripcion=request.form['DescriDoc']
    docu.archivo=request.form['ArchiDoc']
    docu.id_usuario=request.form["UserDoc"]
    docu.aprobacion=request.form['AprobDoc']
    docu.actualizar()
    return redirect(url_for('ventanaOpcionesDocumentos'))
        

    #--Fin de Documentos--#

#Fin apartado Geovanni


#################################################################
###################Segunda Entrega###############################
#################################################################


##---------------------------Apartado de Adrian (Alumnos)------------------------------------
@app.route('/inscribirAlumno')
@login_required
def ventanaRegistroAlumno():
    return render_template("Alumnos/registrarAlumno.html")


@app.route('/opcionesAlumnos')
@login_required
def ventanaOpcionesAlumnos():
    usr = Usuarios()
    #alumnos = usr.consultaGeneral()
    page = int(request.args.get('page', 1))
    post_pagination = usr.all_paginated(page, 5)
    return render_template("Alumnos/opcionesAlumnos.html",post_pagination=post_pagination)

@app.route('/editarAlumno/<int:id>')
@login_required
def ventanaEditarAlumno(id):
    usr = Usuarios()
    usr.id_usuario=id
    datos = usr.consultaIndividual()
    return render_template("Alumnos/modificarAlumno.html",datos=datos)

@app.route('/eliminarAlumno/<int:id>')
def eliminarAlumno(id):
    usr=Usuarios()
    usr.id_usuario=id
    datos=usr.consultaIndividual()
    usr.estatus_usuario="Inactivo"
    usr.actualizar()
    
    return redirect(url_for('ventanaOpcionesAlumnos'))

@app.route('/modificarAlumno', methods=['POST'])
def modificarAlumno():
    usr = Usuarios()
    

    usr.id_usuario=request.form['idusuario']
    usr.nombre=request.form['nombre']
    usr.apellido_paterno=request.form['apaterno']
    usr.apellido_materno=request.form['amaterno']
    usr.genero=request.form['genero']
    usr.fecha_nacimiento=request.form['fnacimiento']
    usr.fecha_registro=request.form['fregistro']
    usr.correo=request.form['correo']
    usr.telefono=request.form['telefono']
    usr.colonia=request.form['colonia']
    usr.calle=request.form['calle']
    usr.numero_casa=request.form['ncasa']
    usr.actualizar()
    



    return redirect(url_for('ventanaOpcionesAlumnos'))

@app.route('/registrarAlumno', methods=['POST'])
def method_name():
    usr = Usuarios()
    emp = Alumnos()

    usr.nombre=request.form['nombre']
    usr.apellido_paterno=request.form['apaterno']
    usr.apellido_materno=request.form['amaterno']
    usr.genero=request.form['genero']
    usr.fecha_nacimiento=request.form['fnacimiento']
    usr.fecha_registro=request.form['fregistro']
    usr.correo=request.form['correo']
    usr.telefono=request.form['telefono']
    usr.colonia=request.form['colonia']
    usr.calle=request.form['calle']
    usr.numero_casa=request.form['ncasa']
    usr.usuario=request.form['usuario']
    usr.passwd=request.form['pass1']
    usr.estatus_usuario="Activo"
    usr.tipo="Alumno"
    
    Clave= usr.apellido_paterno[:2]+usr.apellido_materno[:1]+usr.nombre[:1]+str(usr.fecha_nacimiento.split("-")[0][2:])+str(usr.fecha_nacimiento.split("-")[1])+usr.fecha_nacimiento.split("-")[2]+random.choice(string.ascii_letters)+str(random.randrange(10))+random.choice(string.ascii_letters)
    Clave=Clave.upper()
    emp.rfc=Clave.upper()

    foto=request.files['file']
    os.mkdir("static/uploads/"+Clave)
    filename1 = secure_filename(foto.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER']+Clave, foto.filename)
    foto.save(path)
    emp.foto=filename1

    usr.insertar()
    
    emp.id_usuario=usr.id_usuario
    emp.insertar()
    return redirect(url_for('ventanaOpcionesAlumnos'))



#-INICIO KAREN "GRUPOS"----------------------------------------------------------------------------------------
@app.route('/insertGrupos', methods = ['POST'])
@login_required
def insertGrupos():
    if request.method == 'POST':
        grupo=Grupos()
        grupo.grado =request.form['grado']
        grupo.grupo=request.form['grupo']
        grupo.capacidad = request.form['capacidad']
        grupo.id_turno=request.form['id_turno']
        grupo.id_materia=request.form['id_materia']
        grupo.id_usuario=request.form['id_empleado']
        grupo.estatus="Activo"

        grupo.insertar()
        return redirect(url_for('ConsultarGrupos'))


@app.route('/actualizarGrupos', methods=['POST'])
@login_required
def actualizarGrupos():
    grupos=Grupos()
    grupos.id_grupo=request.form['idgrupo']
    grupos.grado=request.form['grado']
    grupos.grupo = request.form['grupo']
    grupos.capacidad=request.form['capacidad']
    grupos.id_turno=request.form['id_turno']
    grupos.id_materia=request.form['id_materia']
    grupos.id_empleado=request.form['id_empleado']


    grupos.actualizar()

    return redirect(url_for('ConsultarGrupos'))

@app.route('/eliminarGrupo/<int:id>/')
def eliminarGrupo(id):
    tu=Grupos()
    tu.id_grupo=id
    tu.estatus="Inactivo"
    tu.actualizar()
    
    return redirect(url_for('ConsultarGrupos'))

@app.route('/crearGrupo')
@login_required
def ConsultarGrupos():
    gr=Grupos()
    tr=Turnos()
    mat=Materia()
    em=Usuarios()

    grupos=gr.consultaGeneral()
    turnos=tr.consultaGeneral()
    materia=mat.consultaGeneral()
    docente=em.consultaGeneral()

    page = int(request.args.get('page', 1))
    post_pagination = gr.all_paginated(page, 5)

    return render_template("Grupos/Grupos.html", grupos=grupos,turnos=turnos,materia=materia, pudin=docente, post_pagination=post_pagination )

@app.route('/ediGrupo/<int:id>')
def ventanaEdtiGrupo(id):
   gr = Grupos()
   gr.id_grupo=id
   grupos=gr.consultaIndividual()

   mat=Materia()
   materia=mat.consultaGeneral()
   em=Usuarios()
   docente=em.consultaGeneral()
   tr=Turnos()
   turnos=tr.consultaGeneral()

   return render_template('Grupos/editarGrupo.html',datos=grupos,materia=materia,pudin=docente,turnos=turnos)

@app.route('/opcionesGrupos/<int:id>')
@login_required
def editarGrupoBD(id):
    gr=Grupos()
    gr.id_grupo=id
    grupo=gr.consultaIndividual()

    tr=Turnos()
    Turnos=tr.consultaGeneral()
    mat=materia.consultaGeneral()

    return render_template('Grupos/opcionesGrupos.html')

    
    
#- FIN DE GRUPOS---KAREN------------------------------------------------------------------------------------------


#------- Alejandra --------------------------------- Materias ---------------------------------------------------

@app.route('/crearMateria')
@login_required
def ventanaCrearMateria():
    return render_template('Materias/registrarMateria.html')

@app.route('/OpcionesMaterias')
@login_required
def ventanaOpcionesMateria():
    materia=Materia()
    #registro=materia.consultaGeneral()
    page = int(request.args.get('page', 1))
    post_pagination = materia.all_paginated(page, 10)
    return render_template('Materias/OpcionesMateria.html', post_pagination=post_pagination)



@app.route('/editarMateria/<int:id>')
@login_required
def ventanaEditarMateria(id):
    materia=Materia()
    materia.id_materia=id
    registro=materia.consultaIndividual()
    return render_template('Materias/modificarMaterias.html', rg=registro)

@app.route('/eliminarMateria/<int:id>')
def ventanaEliminarMateria(id):
    materia=Materia()
    materia.id_materia=id
    materia.estatus="Inactivo"
    materia.actualizar()

    return redirect(url_for('ventanaOpcionesMateria'))


@app.route('/insertarMateriaBD', methods=['POST'])
def insertMateriaBD():
    materia=Materia()
    materia.nombre=request.form['nombre']
    materia.total_unidades=request.form['nunidad']
    materia.estatus='Activa'
    
    materia.insertar()
    return redirect (url_for('ventanaOpcionesMateria')) 


@app.route('/actualizarMateriasBD', methods=['POST'])
def actualizarMateriasBD():
    materia=Materia()
    materia.id_materia=request.form['idmateria']
    materia.nombre=request.form['nombre']
    materia.total_unidades=request.form['nunidad']
    materia.estatus=request.form['estatus']
    materia.actualizar()
    return redirect(url_for('ventanaOpcionesMateria'))



#--------------------------------------------------------- Fin Materias -------------------------------------------

@app.errorhandler(404)
def error_404(e):
    return render_template('comunes/error_404.html'), 404


@app.errorhandler(500)
def error_500(e):
    return render_template('comunes/error_500.html'), 500



if __name__ == '__main__':
    app.run(port = 3000, debug = True)