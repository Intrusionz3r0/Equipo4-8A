CREATE DATABASE IF NOT EXISTS ERP;
USE ERP;

CREATE TABLE IF NOT EXISTS Usuarios(
    id_usuario int(11) not null  auto_increment,
    nombre varchar(100) not null,
    apellido_paterno varchar(100) not null,
    apellido_materno varchar(100) not null,
    genero varchar(15) not null,
    estado varchar(35) not null,
    municipio varchar(35) not null,
    colonia varchar(65) not null,
    calle varchar(65) not null,
    numero_casa int(11) not null,
    fecha_nacimiento date not null,
    fecha_registro date not null,
    correo varchar(60) not null,
    telefono varchar(12) not null,
    usuario varchar(45) not null,
    passwd varchar(45) not null,
    estatus_usuario varchar(35) not null,
    primary key(id_usuario)
);

CREATE TABLE IF NOT EXISTS Alumnos(
	id_alumno int not null auto_increment,
	creditos_total
	hora_entrada varchar(8) not null,
	hora_salida varchar(8) not null,
);

CREATE TABLE IF NOT EXISTS Asignaturas(
	id_catalogo int not null auto_increment,
	nombre varchar(65) not null,
	creditos int not null,
	id_aula int not null,
	id_Empleado int not null
);

CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON InstitucionED.* TO 'admin'@'localhost';
