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
    estatus_usuario=Column(String,nullable=False)
    
    
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
    tipo =Column(String,nullable=False)
    rfc=Column(String,nullable=False)
    salario_diario=Column(Float,nullable=False)
    fecha_contracion=Column(Date,nullable=False)
    nss=Column(String,nullable=False)
    dias_vacaciones=Column(Integer,nullable=False)
    dias_permiso=Column(Integer,nullable=False)
    foto=Column(String,nullable=False)

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
    
