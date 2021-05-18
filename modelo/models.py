from flask_sqlalchemy import SQLAlchemy                                                                                                                                                          
from sqlalchemy import Column,Integer,String,ForeignKey,Date,DateTime,BLOB,Float,Time
from sqlalchemy.orm import relationship                                                                                                                                                          
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db=SQLAlchemy()                                                                                                                                                                                  
                                                                                                                                                                                                 
class Usuarios(db.Model):                                                                                                                                                                        
    __tablename__='Usuarios'
    id_usuario=Column(Integer,primary_key=True)
    nombre=Column(String,nullable=False)
    apellido_paterno=Column(String,nullable=False)
    apellido_materno=Column(String,nullable=False)
    genero=Column(String,nullable=False)
    colonia=Column(String,nullable=False)
    calle=Column(String,nullable=False)
    numero_casa=Column(Integer,nullable=False)
    fecha_nacimiento=Column(Date,nullable=False)
    fecha_registro=Column(Date,nullable=False)
    correo=Column(String,nullable=False)
    telefono=Column(String,nullable=False)
    usuario=Column(String,nullable=False)
    passwd=Column(String,nullable=False)
    tipo =Column(String,nullable=False)
    estatus_usuario=Column(String,nullable=False)
    grupos=relationship('Grupos',backref='gr')
    docum=relationship('Documentos',backref='docs')
    califi2=relationship('Alumnos',backref='aluUsu')
    #EmpUsu=relationship('Empleados',backref='empusu')
    
    def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit()                                                                                                                                                                      
    def consultaGeneral(self):                                                                                                                                                                   
        usuario=self.query.all()                                                                                                                                                                   
        return usuario
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        usuario=self.consultaIndividual()
        db.session.delete(usuario)
        db.session.commit()
    def consultaIndividual(self):
        usuario=self.query.get(self.id_usuario)
        return usuario


    @staticmethod
    def all_paginated(page=1, per_page=20):
        return Usuarios.query.filter(Usuarios.tipo == 'Alumno').\
            paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def all_paginated2(page=1, per_page=20):
        return Usuarios.query.filter(Usuarios.tipo == 'Docente').\
            paginate(page=page, per_page=per_page, error_out=False)

    def consultaFiltro(self,texto):
        users = self.query.filter(Usuarios.nombre.like('{}%'.format(texto))).all()
        return users

    @property
    def password(self):
        raise AttributeError('El atributo password no es de lectura')
    
    def validarPassword(self,passs):
        pwd = Usuarios.query.filter_by(passwd=passs).first()
        return pwd

    def is_active(self):
        if self.estatus_usuario=='Activo':
            return True
        else:
            return False
    
    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.id_usuario
    
    def getTipo(self):
        return "Tipo"
    
    def validar(self,us,ps):
        emp=Usuarios.query.filter_by(usuario=us).first()
        if(emp!=None):
            if(emp.validarPassword(ps)):
                return emp
            else:
                return None

    

class Empleados(db.Model):                                                                                                                                                                        
    __tablename__='Empleados'
    id_empleado=Column(Integer,primary_key=True)
    id_usuario=Column(Integer,ForeignKey('Usuarios.id_usuario'))
    rfc=Column(String,nullable=False)
    salario_diario=Column(Float,nullable=False)
    fecha_contracion=Column(Date,nullable=False)
    nss=Column(String,nullable=False)
    dias_vacaciones=Column(Integer,nullable=False)
    dias_permiso=Column(Integer,nullable=False)
    foto=Column(String,nullable=False)
    usuario=relationship('Usuarios',backref='emp')

    def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit()                                                                                                                                                                      
    def consultaGeneral(self):                                                                                                                                                                   
        empleado=self.query.all()                                                                                                                                                                   
        return empleado
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        empleado=self.consultaIndividual()
        db.session.delete(empleado)
        db.session.commit()
    def consultaIndividual(self):
        empleado=self.query.get(self.id_empleado)
        return empleado

    
   # NomEmp=relationship('Nomina',backref='nomemp')



class Alumnos(db.Model):
    __tablename__='Alumnos'
    id_alumno=Column(Integer,primary_key=True)
    id_usuario=Column(Integer,ForeignKey('Usuarios.id_usuario'))
    id_grupo=Column(Integer)
    rfc=Column(String,nullable=False)
    foto=Column(String,nullable=False)
    usuario=relationship('Usuarios',backref='alm')
    califi1=relationship('Calificacion',backref='califis')
    usus=relationship('Usuarios',backref='UA')
    

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        al = self.consultaIndividual()
        db.session.delete(al)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.id_alumno)


class Turnos(db.Model):                                                                                                                                                                        
    __tablename__='Turnos'
    id_turno =Column(Integer,primary_key=True)
    nombre =Column(String,nullable=False)
    hora_entrada =Column(Time,nullable=False)
    hora_salida =Column(Time,nullable=False)
    estatus= Column(String,nullable=False)


    def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit() 
    def consultaGeneral(self):                                                                                                                                                                   
        tu=self.query.all()                                                                                                                                                                   
        return tu
    def consultaIndividual(self):
        tu=self.query.get(self.id_turno)
        return tu
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        tu=self.consultaIndividual()
        db.session.delete(tu)
        db.session.commit()
    Grupos=relationship('Grupos',backref='Turnos')


    @staticmethod
    def all_paginated(page=1, per_page=10):
        return Turnos.query.order_by(Turnos.id_turno.asc()).\
            paginate(page=page, per_page=per_page, error_out=False)

    

class Aulas(db.Model):
    __tablename__='Aulas'
    id_aula=Column(Integer,primary_key=True)
    id_edificio=Column(Integer,ForeignKey('Edificios.id_edificio'))
    nombre=Column(String, nullable=False)
    capacidad=Column(Integer,nullable=False)
    estado=Column(String,nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        Aulas = self.consultaIndividual()
        db.session.delete(aula)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.id_aula)


class Edificios(db.Model):
    __tablename__='Edificios'
    id_edificio=Column(Integer,primary_key=True)
    nombre=Column(String, nullable=False)
    tipo=Column(String, nullable=False)
    descripcion=Column(String, nullable=False)
    estado=Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        ed = self.consultaIndividual()
        db.session.delete(ed)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.id_edificio)
    Aulas=relationship('Aulas',backref='Edificios')

class Calificacion(db.Model):
    __tablename__='Calificacion'
    id_calificacion=Column(Integer,primary_key=True)
    id_materia=Column(Integer,ForeignKey('Materia.id_materia'))
    id_alumno=Column(Integer,ForeignKey('Alumnos.id_alumno'))
    calificacion=Column(Float,nullable=False)
    unidad=Column(Integer,nullable=False)
    validacion=Column(String,nullable=False)
    
    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        califi=self.consultaIndividual()
        db.session.delete(califi)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.id_calificacion)

    def consultarCalificacionesAlumno(self,id):
        cali = self.query.filter(Calificacion.id_alumno==id).all()
        return cali
    
    @staticmethod
    def all_paginated(page=1, per_page=5):
        return Calificacion.query.order_by(Calificacion.id_calificacion.asc()).\
            paginate(page=page, per_page=per_page, error_out=False)


class Grupos(db.Model):
    __tablename__='Grupos'
    id_grupo =Column(Integer,primary_key=True)
    grado=Column(Integer, nullable=False) 
    grupo=Column(String,nullable=False) 
    capacidad=Column(Integer,nullable=False) 
    id_turno=Column(Integer,ForeignKey('Turnos.id_turno')) 
    id_materia=Column(Integer,ForeignKey('Materia.id_materia'))
    id_usuario=Column(Integer,ForeignKey('Usuarios.id_usuario')) 
    estatus=Column(String,nullable=False)
    

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        Aulas = self.consultaIndividual()
        db.session.delete(grupo)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.id_grupo)

    @staticmethod
    def all_paginated(page=1, per_page=5):
        return Grupos.query.order_by(Grupos.id_grupo.asc()).\
            paginate(page=page, per_page=per_page, error_out=False)


class Materia(db.Model):                                                                                                                                                                        
    __tablename__='Materia'
    id_materia =Column(Integer,primary_key=True)
    nombre =Column(String,nullable=False)
    total_unidades =Column(Integer,nullable=False)
    estatus= Column(String,nullable=False)
    califa=relationship('Calificacion',backref='califis2')
    GrupoMateria=relationship('Grupos',backref='grumat')
    

    
    def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit() 

    def consultaGeneral(self):
        materia=self.query.all()
        return materia

    def consultaIndividual(self):
        materia=self.query.get(self.id_materia)
        return materia

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
        
    def eliminar(self):
        materia=self.consultaIndividual()
        db.session.delete(materia)
        db.session.commit()

    @staticmethod
    def all_paginated(page=1, per_page=10):
        return Materia.query.order_by(Materia.id_materia.asc()).\
            paginate(page=page, per_page=per_page, error_out=False)

    Grupos=relationship('Grupos',backref='materia')

    def consultarFiltro(self,texto):
        materia = self.query.filter(Materia.nombre.like('{}%'.format(texto))).all()
        return materia

class Documentos(db.Model):
    __tablename__='Documentos'
    id_documento=Column(Integer,primary_key=True)
    nombre=Column(String,nullable=False)
    descripcion=Column(String,nullable=False)
    archivo=Column(String,nullable=False)
    id_usuario=Column(Integer,ForeignKey('Usuarios.id_usuario'))
    aprobacion=Column(String,nullable=False)

    

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        DOC=self.consultaIndividual()
        db.session.delete(DOC)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.id_documento)

    @staticmethod
    def all_paginated(page=1, per_page=10):
        return Documentos.query.order_by(Documentos.id_documento.asc()).\
            paginate(page=page, per_page=per_page, error_out=False)
