from flask_sqlalchemy import SQLAlchemy                                                                                                                                                          
from sqlalchemy import Column,Integer,String,ForeignKey,Date,DateTime,BLOB,Float
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
        return usuaempleadorio
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