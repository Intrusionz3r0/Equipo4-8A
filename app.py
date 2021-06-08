import os,random,string
from flask import Flask,render_template,request,redirect,url_for,abort
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import null
from modelo.models import Empleados,Horario,Usuarios,Turnos,Aulas,Edificios,Alumnos,Grupos,Materia,Calificacion,DocumentosA,DocumentosE,Pagos,PagoColegiatura,AlumnoGrupo,Asistencia
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
        return render_template('home.html')
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
    #registro=tu.consultaGeneral()
    page = int(request.args.get('page', 1))
    post_pagination = tu.all_paginated(page, 5)
    return render_template("Turnos/OpcionesTurnos.html",post_pagination=post_pagination)

@app.route('/filtrarTurno//<string:texto>')
def ventanaFiltradoTurnos(texto):
   tu=Turnos()
   datos=tu.consultaFiltro(texto)
   return render_template("Turnos/FiltroTurno.html",datos=datos)

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
    

    emp = Usuarios()
    emp.id_usuario=id
    empleados = emp.consultaIndividual()

    return render_template("Empleados/modificarEmpleado.html",empleados=empleados)


@app.route('/opcionesEmpleados')
@login_required
def ventanaOpcionesEmpleados():
    usr = Usuarios()
    page = int(request.args.get('page', 1))
    post_pagination = usr.all_paginated2(page, 5)
    return render_template('Empleados/opcionesEmpleados.html',post_pagination=post_pagination)

@app.route('/filtrarEmpleado/<string:texto>')
def filtrarEmpleados(texto):
   users = Usuarios()
   datos=users.consultaFiltro(texto)
   return render_template("Empleados/FiltroEmpleados.html",datos=datos)

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
    page = int(request.args.get('page', 1))
    post_pagination = au.all_paginated(page, 5)
    return render_template("Aulas/Aulas.html", aulas=aulas,edificios=edificios,post_pagination=post_pagination)

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


@app.route('/filtrarAula/<string:texto>')
def filtrarAula(texto):
   au = Aulas()
   aula=au.consultaFiltro(texto)
   return render_template("Aulas/filtroAulas.html",datos=aula)
    

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
    #Doc=edi.consultaGeneral()
    page = int(request.args.get('page', 1))
    post_pagination = edi.all_paginated(page, 5)
    return render_template('Edificios/opcionesEdificios.html',post_pagination=post_pagination)

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

@app.route('/FiltradoEdificios/<string:nombre>')
def ventanaFiltradoEdificios(nombre):
    edi=Edificios()
    Edi=edi.consultaFiltro(nombre)
    return render_template('Edificios/FiltroEdificios.html',EDI=Edi)

#---Calificaciones---#

@app.route('/asignarCalificacion')
@login_required
def ventanaRegistrarCalificacion():
    grupos = Grupos()
    datos = grupos.consultaGeneral()
    return render_template('Calificaciones/registrarCalificaciones.html',datos=datos)


@app.route('/vermiscalificaciones')
def vermiscalificaciones():
    
    
    if(current_user.tipo == "Alumno"):

        usu=Alumnos()
        datos=usu.consultaGeneral()

        for x in datos:
            if(x.id_usuario == current_user.id_usuario):
                print(x.id_alumno)
                calis= Calificacion()
                datos2=calis.consultarCalificacionesAlumno(x.id_alumno)
                
                return render_template('Calificaciones/vermiscalificaciones.html',datos2=datos2)

        return render_template('Calificaciones/vermiscalificaciones.html')
    else:
        return "Eres un docente"

    


@app.route('/verGrupo/<int:id>')
@login_required
def verGrupo(id):
    alu=AlumnoGrupo()
    datos=AlumnoGrupo.query.filter(AlumnoGrupo.id_grupo == id)
    print(datos)

    gru=Grupos()
    gru.id_grupo=id
    datos2= gru.consultaIndividual()


    return render_template('Calificaciones/AsignarCal.html',datos=datos,datos2=datos2,identi=id)

@app.route('/modificarGrupo/<int:id>/<int:un>')
def modificarCalificaciones(id,un):

    gru=Grupos()
    gru.id_grupo=id
    datos2= gru.consultaIndividual()


    cali=Calificacion()
    datos3=Calificacion.query.filter(Calificacion.unidad == un,Calificacion.id_materia==datos2.id_materia ).all()

    return render_template('Calificaciones/modificarCalificaciones.html',datos2=datos2,datos3=datos3,un=un,identi=id)


@app.route('/EliminarGrupo/<int:id>/<int:un>')
def EliminarcalCalificaciones(id,un):
    gru=Grupos()
    gru.id_grupo=id
    datos2= gru.consultaIndividual()


    cali=Calificacion()
    datos3=Calificacion.query.filter(Calificacion.unidad == un,Calificacion.id_materia==datos2.id_materia ).all()

    return render_template('Calificaciones/eliminarCalificaciones.html',datos2=datos2,datos3=datos3,un=un,identi=id)


@app.route('/opcionesCalificacion')
def verGrupos():
    grupos = Grupos()
    datos2 = grupos.consultaGeneral()
    return render_template("Calificaciones/opcionesCalificaciones.html",datos2=datos2)

@app.route('/calificarGrupoAlumnos', methods=['POST','GET'])
def calificarGrupoAlumnos():

    final = request.form['final']
    for x in range(int(final)):
        cali=Calificacion()
        cali.id_alumno=request.form['idalumno{}'.format(x+1)]        
        cali.calificacion=request.form['kali{}'.format(x+1)]
        cali.id_materia=request.form['materia']
        cali.unidad=request.form['unidad']
        cali.validacion="Si"
        cali.insertar()
    return redirect(url_for('homi'))

@app.route('/editarCalificacion', methods=['POST'])
def editarCalificacion():
    final = request.form['final']
    for x in range(int(final)):
        cali=Calificacion()
        cali.id_calificacion=request.form[str('idcali{}'.format(x+1))]
        cali.calificacion=request.form['kali{}'.format(x+1)]
        cali.unidad=request.form['alugrupo']
        cali.actualizar()  
    return redirect(url_for('homi'))

@app.route('/eliminarCalificacion', methods=['POST'])
def eliminarCalificacion():
    final = request.form['final']
    for x in range(int(final)):
        cali=Calificacion()
        cali.id_calificacion=request.form[str('idcali{}'.format(x+1))]
        cali.eliminar()  
    return redirect(url_for('homi'))


#--Inicio de Documentos Alumnos--#

@app.route('/agregarDocumentoAlumno')
@login_required
def ventanaRegistrarDocumentosA():
    DocuA=Alumnos()
    Alu=DocuA.consultaGeneral()
    return render_template('Documentos/RegistrarDocumentosA.html',ALUM=Alu)

@app.route('/OpcionDocumentoAlumno')
@login_required
def ventanaOpcionesDocumentosA():
    docu=DocumentosA()
    AL=Alumnos()
    
    
    page = int(request.args.get('page', 1))
    post_pagination = docu.all_paginated(page, 5)
    return render_template('Documentos/opcionesDocumentosA.html',post_pagination=post_pagination)

@app.route('/editarDocumentosAlumno/<int:id>')
def ventanaEditarDocumentosA(id):
    docu=DocumentosA()
    docu.id_documento=id
    DOC=docu.consultaIndividual()
    return render_template('Documentos/modificarDocumentosA.html',DOCU=DOC)

@app.route("/eliminarDocumentosAlumno/<int:id>/<string:rfc>/<string:doc>")
def ventanaEliminarDocumentosA(id,rfc,doc):
    docu=DocumentosA()
    alu=Alumnos()

    docu.id_documento=id
    #DoA=docu.id_alumno
    
    alu.rfc=rfc
    
    #Alu=alu.consultaIndividual()
    os.remove(app.config['UPLOAD_FOLDER']+ rfc +"/"+ doc +".pdf")
    docu.aprobacion="NO"
    docu.actualizar()
    return redirect(url_for('ventanaOpcionesDocumentosA'))

@app.route('/visualizarPDFAlumno/<int:id>')
def ventanaVerPDFA(id):
    docu=DocumentosA()
    docu.id_documento=id
    Doc=docu.consultaIndividual()
    return render_template('Documentos/verPDFA.html',DOCU=Doc)

@app.route('/insertarDocumentosBDAlumno', methods=['POST'])
def insertarDocumentosBDA():
    docu=DocumentosA()
    alu=Alumnos()
    alu.id_alumno=request.form['Sel_A']
    aluD=alu.consultaIndividual()
    docu.nombre=request.form['NombreDoc']
    docu.descripcion=request.form['DescripcionDoc']
    #docu.archivo=request.form['ArchDoc']
    docu.id_alumno=request.form['Sel_A']
    docu.aprobacion='SI'

    foto=request.files['ArchDoc']
    #os.mkdir("static/uploads/"+alu.rfc)
    filename1 = secure_filename(foto.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER']+aluD.rfc, docu.nombre+".pdf")
    foto.save(path)
    docu.archivo=filename1

    docu.insertar()
    return redirect(url_for('ventanaOpcionesDocumentosA'))

@app.route('/actualizarDocumentosBDAlumno', methods=['POST'])
def actualizarDocumentosBDA():
    docu=DocumentosA()
    ALU=Alumnos()
    
    docu.id_documento=request.form['id_doc']
    docu.nombre=request.form['NombDoc']
    docu.descripcion=request.form['DescriDoc']
    docu.archivo=request.form['ArchiDoc']
    docu.id_usuario=request.form["UserDoc"]
    docu.aprobacion=request.form['AprobDoc']
    docu.actualizar()
    return redirect(url_for('ventanaOpcionesDocumentosA'))
        
@app.route('/filtrarDocAlumnos/<string:texto>')
def filtrarDocumentosAlumnos(texto):
   docuA = DocumentosA()
   DocuA=docuA.consultaFiltro(texto)
   return render_template("Documentos/FiltroDocA.html",DOCA=DocuA)
    #--Fin de Documentos Alumnos--#

  #--Inicio de Documentos Empleados--#

@app.route('/agregarDocumentoEmpleado')
@login_required
def ventanaRegistrarDocumentosE():
    DocuE=Empleados()
    Emp=DocuE.consultaGeneral()
    
    return render_template('Documentos/RegistrarDocumentosE.html',EMP=Emp)

@app.route('/OpcionDocumentoEmpleado')
@login_required
def ventanaOpcionesDocumentosE():
    docu=DocumentosE()
    page = int(request.args.get('page', 1))
    post_pagination = docu.all_paginated(page, 5)
    return render_template('Documentos/opcionesDocumentosE.html',post_pagination=post_pagination)

@app.route('/editarDocumentosEmpleado/<int:id>')
def ventanaEditarDocumentosE(id):
    docu=DocumentosE()
    docu.id_documento=id
    DOC=docu.consultaIndividual()
    return render_template('Documentos/modificarDocumentosE.html',DOCU=DOC)

@app.route('/eliminarDocumentosEmpleado/<int:id>/<string:rfc>/<string:doc>')
def ventanaEliminarDocumentosE(id,rfc,doc):
    docu=DocumentosE()
    docu.id_documento=id
    os.remove(app.config['UPLOAD_FOLDER']+ rfc +"/"+ doc +".pdf")
    docu.aprobacion="NO"
    docu.actualizar()
    return redirect(url_for('ventanaOpcionesDocumentosE'))

@app.route('/visualizarPDFEmpleado/<int:id>')
def ventanaVerPDFE(id):
    docu=DocumentosE()
    docu.id_documento=id
    Doc=docu.consultaIndividual()
    return render_template('Documentos/verPDFE.html',DOCU=Doc)

@app.route('/insertarDocumentosBDEmpleado', methods=['POST'])
def insertarDocumentosBDE():
    docu=DocumentosE()
    emp=Empleados()
    emp.id_empleado=request.form['Sel_A']
    empD=emp.consultaIndividual()
    docu.nombre=request.form['NombreDoc']
    docu.descripcion=request.form['DescripcionDoc']
    #docu.archivo=request.form['ArchDoc']
    docu.id_empleado=request.form['Sel_A']
    docu.aprobacion='SI'

    foto=request.files['ArchDoc']
    #os.mkdir("static/uploads/"+alu.rfc)
    filename1 = secure_filename(foto.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER']+empD.rfc, docu.nombre+".pdf")
    foto.save(path)
    docu.archivo=filename1

    docu.insertar()
    return redirect(url_for('ventanaOpcionesDocumentosE'))

@app.route('/actualizarDocumentosBDEmpleado', methods=['POST'])
def actualizarDocumentosBDE():
    docu=DocumentosE()
    docu.id_documento=request.form['id_doc']
    docu.nombre=request.form['NombDoc']
    docu.descripcion=request.form['DescriDoc']
    docu.archivo=request.form['ArchiDoc']
    docu.id_usuario=request.form["UserDoc"]
    docu.aprobacion=request.form['AprobDoc']
    docu.actualizar()
    return redirect(url_for('ventanaOpcionesDocumentosE'))
        
@app.route('/filtrarDocEmpleados/<string:texto>')
def filtrarDocumentosEmpleados(texto):
   docuE = DocumentosE()
   DocuE=docuE.consultaFiltro(texto)
   return render_template("Documentos/FiltroDocE.html",DOCE=DocuE)
    #--Fin de Documentos Empleados--#

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


@app.route('/filtrarAlumnos/<string:texto>')
def filtrarAlumnos(texto):
   users = Usuarios()
   datos=users.consultaFiltro(texto)
   return render_template("Alumnos/FiltroAlumnos.html",datos=datos)


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
    usr.passwd=request.form['pass2']
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
    emp.engrupo="No"

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
        grupo.id_empleado=request.form['id_empleado']
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
    grupos.estatus=request.form['estatus']


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
    em=Empleados()

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
   em=Empleados()
   docente=em.consultaGeneral()
   tr=Turnos()
   turnos=tr.consultaGeneral()

   return render_template('Grupos/editarGrupo.html',datos=grupos,materia=materia,pudin=docente,turnos=turnos)

 
@app.route('/FiltrarGrupos/<string:texto>')
def filtrarGrupos(texto):
   gr = Grupos()
   grupo=gr.consultaFiltro(texto)
   return render_template("Grupos/FiltrarGrupos.html",datos=grupo)
    

#@app.route('/ejemplo')
#def ex():
 #   return render_template("Grupos/EJ.html")

    
    
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

@app.route('/filtrarMateria/<string:texto>')
def ventanaFiltradoMateria(texto):
   materia=Materia()
   datos=materia.consultaFiltro(texto)
   return render_template("Materias/FiltroMaterias.html",datos=datos)



#--------------------------------------------------------- Fin Materias -------------------------------------------





#-----------------------------HORARIOS KAREN------------------------------------------------------------
@app.route('/insertHorarios', methods = ['POST'])
@login_required
def insertHorario():
    if request.method == 'POST':
        h=Horario()
        h.id_aula =request.form['id_aula']
        h.id_grupo=request.form['id_grupo']
        h.dia=request.form['dia']
        h.hora=request.form['hora']
        h.estatus="Activo"

        h.insertar()

        return redirect(url_for('ConsultarHorario'))

@app.route('/actualizarHorario', methods=['POST'])
@login_required
def actualizarHorario():
    h=Horario()
    h.id_horario=request.form['id_horario']
    h.id_aula =request.form['id_aula']
    h.id_grupo=request.form['id_grupo']
    h.dia=request.form['dia']
    h.hora=request.form['hora']
    h.estatus=request.form['estatus']

    h.actualizar()

    return redirect(url_for('ConsultarHorario'))

@app.route('/eliminarHorario/<int:id>/')
def eliminarHorario(id):
    hr=Horario()
    hr.id_horario=id   
    hr.estatus="Inactivo"
    hr.actualizar()
    
    return redirect(url_for('ConsultarHorario'))

@app.route('/agregarAumnoHorario')
@login_required
def ConsultarHorario():
    ho=Horario()
    h=ho.consultaGeneral()

    a=Aulas()
    aula=a.consultaGeneral()

    g=Grupos()
    grupo=g.consultaGeneral()

    page = int(request.args.get('page', 1))
    post_pagination = ho.all_paginated(page, 5)
    return render_template("Horario/Horario.html", h=h,aula=aula,grupo=grupo,post_pagination=post_pagination)

@app.route('/filtrarHorario/<string:texto>')
def filtrarHorario(texto):
   hr = Horario()
   datos=hr.consultaFiltro(texto)
   return render_template("Horario/filtroHorario.html",datos=datos)

@app.route('/editarHorario/<int:id>')
@login_required
def editarHorarioBD(id):
    hor=Horario()
    hor.id_horario=id
    horario=hor.consultaIndividual()

    a=Aulas()
    aula=a.consultaGeneral()

    g=Grupos()
    grupo=g.consultaGeneral()

    return render_template('Horario/opcionesHorario.html',horario=horario,aula=aula,grupo=grupo)
#-----------------------------------FIN APARTADO "HORARIOS KAREN"-------------------------------------------------

#--Inicio de Pagos--#

@app.route('/agregarPago')
@login_required
def ventanaCrearPagos():
    alu=Alumnos()
    Alu=alu.consultaGeneral()
    return render_template('Pagos/RegistrarPagos.html',ALU=Alu)

@app.route('/opcionesPagos')
@login_required
def ventanaOpcionesPagos():
    pagos=Pagos()
    page = int(request.args.get('page', 1))
    post_pagination = pagos.all_paginated(page, 10)

    pg=Pagos()
    pgs=pg.consultaGeneral()
    return render_template('Pagos/OpcionesPagos.html', post_pagination=post_pagination,PGS=pgs)

@app.route('/editarPago/<int:id>')
@login_required
def ventanaEditarPago(id):
    pagos=Pagos()
    pagos.id_pagos=id
    pago=pagos.consultaIndividual()
    return render_template('Pagos/ModificarPagos.html',PAGO=pago)

@app.route('/eliminarPago/<int:id>')
def ventanaEliminarPago(id):
    pago=Pagos()
    pago.id_pagos=id
    pago.estatus='Rechazado'
    pago.actualizar()
    return redirect(url_for('ventanaOpcionesPagos'))

@app.route('/insertarPagosBD', methods=['POST'])
def InsertarPagos():
    pagos=Pagos()
    pagos.descripcion=request.form['DescriPagos']
    pagos.tipo=request.form['tipoPagos']
    pagos.id_alumno=request.form['PagAlu']
    pagos.monto=request.form['MontoPago']
    pagos.estatus='Aceptado'
    pagos.fechaPgSer=request.form['FchHoy']
    pagos.RespoPago=request.form['RespoPago']
    pagos.ModifiPor='Sin Modificar'
    pagos.insertar()
    return redirect(url_for('ventanaOpcionesPagos'))

@app.route('/actualizarPagosBD',methods=['POST'])
def actualizarPagosBD():
    pagos=Pagos()
    pagos.id_pagos=request.form['id_pag']
    pagos.descripcion=request.form['DescrPago']
    pagos.tipo=request.form['tipoPagos1']
    pagos.id_alumno=request.form['PagoAl']
    pagos.monto=request.form['MontoPago']
    pagos.estatus='Aceptado'
    pagos.fechaPgSer=request.form['FchHoy']
    pagos.RespoPago=request.form['RespoPago']
    pagos.ModifiPor=request.form['ModifiPor']
    pagos.actualizar()
    return redirect(url_for('ventanaOpcionesPagos'))

@app.route('/FiltradoPagos/<string:nombre>')
def ventanaFiltradoPago(nombre):
    pag=Pagos()
    pago=pag.consultaFiltro(nombre)
    return render_template('Pagos/FiltroPagos.html',PG=pago)

@app.route('/Vista&Descarga_PDF/<int:id>')
def ventanaPDFPagos(id):
    pag=Pagos()
    pag.id_pagos=id
    Pag=pag.consultaIndividual()

    
    return render_template('Pagos/PDFServicios.html',PAGO=Pag)




#--Fin de Pagos--#



@app.route('/insertarAlumnoGrupo')
def agregarAlumnoGrupo():

    usu = Alumnos()
    datosalumno = usu.consultaGeneral()

    gr = Grupos()
    datos2=gr.consultaGeneral()

    return render_template("Grupos/AltaGrupoAlumno.html",datos1=datosalumno,datos2=datos2)


@app.route('/agregarAlumnoGrupo')
def opcionesAlumnoGrupos():
    alg = AlumnoGrupo()

    gr = Grupos()
    datos = gr.consultaGeneral()
    page = int(request.args.get('page', 1))
    post_pagination = alg.all_paginated(page, 5)
    return render_template('Grupos/OpcionesAluGrupo.html',post_pagination=post_pagination,datos=datos)
   
@app.route('/EliminarAlumnoGrupo/<int:id>')
def EliminarAlumnoGrupo(id):
    alg = AlumnoGrupo()
    alg.id_ag=id
    alg.estatus="Inactivo"
    alg.actualizar()


    return redirect(url_for('opcionesAlumnoGrupos'))


@app.route('/modificarAlumnoGrupo/<int:id>')
def modificarAlumnoGrupo(id):

    usu = Usuarios()
    datosalumno = usu.consultaGeneral()

    grupos = Grupos()
    datosgrupos = grupos.consultaGeneral()

    turnos = Turnos()
    dataTurnos = turnos.consultaGeneral()

    alg=AlumnoGrupo()
    alg.id_ag=id
    datos4=alg.consultaIndividual()

    return render_template('Grupos/ModificarAltaGrupoAlumno.html',datos1=datosalumno,datos2=datosgrupos,datos3=dataTurnos,datos4=datos4)
   

@app.route('/vincularAlumnoGrupo', methods=['POST'])
def vincularAlumnoGrupo():

    alg = AlumnoGrupo()
    alg.id_grupo = request.form['grupo']
    alg.id_alumno = request.form['alumno']
    alg.estatus = "Activo"
    alg.insertar()

    alu = Alumnos()
    alu.id_alumno = alg.id_alumno
    alu.consultaIndividual()
    alu.engrupo = "Si"
    alu.actualizar()

    
    return redirect(url_for('opcionesAlumnoGrupos'))


@app.route('/updateAlumnoGrupo', methods=['POST'])
def updateAlumnoGrupo():

    alg = AlumnoGrupo()
    alg.id_ag = request.form['id_ag']
    alg.id_grupo = request.form['grupo']
    alg.actualizar()
    return redirect(url_for('opcionesAlumnoGrupos'))


@app.route('/filtrarAluGru/<string:texto>')
def ventanaFiltradoAluGrupos(texto):
   tu=AlumnoGrupo()
   datos=tu.consultaFiltro(texto)
   return render_template("Grupos/FiltroAluGrupo.html",datos=datos)


#--Fin de Pagos--#

#--Inicio de PagosColegiatura--#
@app.route('/agregarPagoColegiatura')
@login_required
def ventanaCrearPagosColeg():
    alu=Alumnos()
    Alu=alu.consultaGeneral()
    pgColeg=PagoColegiatura()
    PGColeg=pgColeg.consultaGeneral()
    
    return render_template('Pagos/RegistrarPagosColegiatura.html',ALU=Alu,PGCG=PGColeg)

@app.route('/opcionesPagosColegiatura')
@login_required
def ventanaOpcionesPagosColeg():
    pagos=PagoColegiatura()
    page = int(request.args.get('page', 1))
    post_pagination = pagos.all_paginated(page, 10)
    pgc=PagoColegiatura()
    pgC=pgc.consultaGeneral()
    return render_template('Pagos/OpcionesPagosColegiatura.html', post_pagination=post_pagination,PGC=pgC)

@app.route('/editarPagoColegiatura/<int:id>')
@login_required
def ventanaEditarPagoColeg(id):
    pagos=PagoColegiatura()
    pagos.id_pagoColegiatura=id
    pago=pagos.consultaIndividual()
    return render_template('Pagos/ModificarPagosColegiatura.html',PAGOCOLEG=pago)

@app.route('/eliminarPagoColegiatura/<int:id>')
def ventanaEliminarPagoColeg(id):
    pago=PagoColegiatura()
    pago.id_pagoColegiatura=id
    pago.estatus='Rechazado'
    pago.actualizar()
    return redirect(url_for('ventanaOpcionesPagosColeg'))

@app.route('/insertarPagosColegiaturaBD', methods=['POST'])
def InsertarPagosColeg():
    pagos=PagoColegiatura()
    pagos.monto=request.form['MontoPago']
    pagos.fechaPagoColeg=request.form['FchHoy']
    pagos.tipo='Colegiatura'
    pagos.codigo=request.form['Codigo']
    pagos.id_alumno=request.form['PagAluColeg']
    pagos.estatus='Aceptado'
    pagos.Responsable=request.form['RespoColeg']
    pagos.ModifiPor='Sin Modificar'
    pagos.insertar()
    return redirect(url_for('ventanaOpcionesPagosColeg'))

@app.route('/actualizarPagosColegiaturaBD',methods=['POST'])
def actualizarPagosBDColeg():
    pagos=PagoColegiatura()
    pagos.id_pagoColegiatura=request.form['id_pag']
    pagos.id_alumno=request.form['PagoAl']
    pagos.monto=request.form['MontoPago']
    pagos.fechaPagoColeg=request.form['fchHoy']
    pagos.tipo='Colegiatura'
    pagos.codigo=request.form['Codigo']
    pagos.estatus='Aceptado'
    pagos.Responsable=request.form['RespoColeg']
    pagos.ModifiPor=request.form['ModifColeg']
    pagos.actualizar()
    return redirect(url_for('ventanaOpcionesPagosColeg'))

@app.route('/FiltradoPagosColegiatura/<string:nombre>')
def ventanaFiltradoPagoColeg(nombre):
    pag=PagoColegiatura()
    pago=pag.consultaFiltro(nombre)
    return render_template('Pagos/FiltroPagosColegiatura.html',PG=pago)

@app.route('/Vista&Descarga-Colegiatura_PDF/<int:id>')
def ventanaPDFPagosColegiatura(id):
    pag=PagoColegiatura()
    pag.id_pagoColegiatura=id
    Pag=pag.consultaIndividual()

    
    return render_template('Pagos/PDFColegiatura.html',PAGO=Pag)

#--Fin de PagosColegiatura--#

#----------------------------------------------------Asistencias--------------------------------#
@app.route('/mostrargrupo/<int:id>')
@login_required
def ventanaCrearAsistencia(id):
    alu=AlumnoGrupo()
    datos=AlumnoGrupo.query.filter(AlumnoGrupo.id_grupo == id)
    print(datos)

    gru=Grupos()
    gru.id_grupo=id
    datos2= gru.consultaIndividual()
    return render_template('Asistencias/registrarAsistencia.html',  datos=datos,datos2=datos2,identi=id)

@app.route('/crearAsistencia')
@login_required
def ventanaRegistrarAsistencia():
    grupos = Grupos()
    datos = grupos.consultaGeneral()
    return render_template('Asistencias/MostrarGrupos.html',datos=datos)


@app.route('/asistenciaGrupoAlumnos2', methods=['POST'])
def asistenciaGrupoAlumnos2():

    final = request.form['final']
    for x in range(int(final)):
        A=Asistencia()
        A.id_alumno=request.form['idalumno{}'.format(x+1)] 
        A.id_materia=request.form['materia']  
        A.asistencia=request.form['asis{}'.format(x+1)]
        A.observaciónes=request.form['obs{}'.format(x+1)]
        A.fecha=request.form['fecha']
        A.estatus = "Activo"
        
        A.insertar()
    return redirect(url_for('homi'))

@app.route('/OpcionesAsistencia')
def verAGrupo():
    grupos = Grupos()
    datos2 = grupos.consultaGeneral()
    return render_template("Asistencias/OpcionesAsistencia.html",datos2=datos2)



@app.route('/eliminarAsistencia/<int:id>')
def ventanaEliminarAsistencia(id):
    A=Asistencia()
    A.idAsistencia=id
    A.estatus="Inactivo"
    A.actualizar()

    return redirect(url_for('ventanaOpcionesAsistencia'))


@app.route('/filtrarAsistencia/<string:texto>')
def ventanaFiltradoAsistencia(texto):
   A=Asistencia()
   datos=A.consultaFiltro(texto)
   return render_template("Asistencias/filtroAsistencia.html",datos=datos)



#-----------------Fin de Asistencias-------------------------------------------------------#

@app.errorhandler(404)
def error_404(e):
    return render_template('comunes/error_404.html'), 404


@app.errorhandler(500)
def error_500(e):
    return render_template('comunes/error_500.html'), 500



if __name__ == '__main__':
    app.run(port = 3000, debug = True)