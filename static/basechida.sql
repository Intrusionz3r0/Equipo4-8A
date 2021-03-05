
CREATE DATABASE IF NOT EXISTS InstitucionED;

USE InstitucionED;

CREATE TABLE IF NOT EXISTS Login(
    id_login int(11) not null primary key auto_increment,
    usuario varchar(45) not null,
    passwd varchar(45) not null,
    id_usuario int(11) not null
);

CREATE TABLE IF NOT EXISTS Usuarios(
    id_usuario int(11) not null primary key auto_increment,
    nombre varchar(100) not null,
    apellido varchar(100) not null,
    fecha_nacimiento date not null,
    direccion varchar(200) not null,
    telefono varchar(12) not null,
    correo varchar(60) not null,
    genero varchar(15) not null,
    tipo_usuario varchar(35) not null,
    estatus varchar(35) not null,
    fecha_registro date not null
);

CREATE TABLE IF NOT EXISTS Alumnos(
    id_alumno int(11) not null primary key auto_increment,
    nivel varchar(35) not null,
    certificado varchar(200) not null,
    id_usuario int(11) not null,
    id_documento int(11) not null
);

CREATE TABLE  IF NOT EXISTS Administrativo(
    id_administrativo int(11) not null primary key auto_increment,
    salario float not null,
    id_usuario int(11) not null,
    id_documento int(11) not null

);

CREATE TABLE IF NOT EXISTS Profesor(
    id_profesor int(11) not null primary key auto_increment,
    salario float not null,
    id_usuario int(11) not null,
    id_documento int(11) not null
);

CREATE TABLE  IF NOT EXISTS Aulas(
    id_aula int(11) not null primary key auto_increment,
    nombre varchar(65) not null,
    id_edificio int(11) not null
);

CREATE TABLE  IF NOT EXISTS Edificios(
    id_edificio int not null primary key auto_increment,
    nombre varchar(30) not null,
    tipo varchar(30) not null
);

CREATE TABLE  IF NOT EXISTS Cursos(
    id_curso int(11) not null primary key auto_increment,
    id_edificio int(11) not null,
    id_aula int (11) not null,
    id_profesor int(11) not null,
    id_turno int(11) not null,
    nombre varchar(50) not null
);

CREATE TABLE  IF NOT EXISTS Turnos(
    id_turno int(11) not null primary key auto_increment,
    nombre varchar(45) not null
);


CREATE TABLE  IF NOT EXISTS Compras(
    id_Compra int(11) not null,
    nombre varchar(50) not null,
    productoDescripcion varchar(70) not null,
    proveedor varchar(60) not null,
    costo float not null,
    cantidad int not null
);

CREATE TABLE  IF NOT EXISTS Nomina(
    id_nomina int (11) not null,
    id_administrativo int(11) not null,
    id_profesor int(11) not null,
    periodo_inicio date not null,
    periodo_fin date not null,
    rfc varchar(18) not null,
    bonos float not null,
    pago_total float not null
);

CREATE TABLE  IF NOT EXISTS Documentos(
    id_documento int(11) not null primary key auto_increment,
    foto varchar(200) not null,
    acta_nacimiento varchar(200) not null,
    curp varchar(200) not null,
    id_usuario varchar(11) not null
);

CREATE TABLE IF NOT EXISTS Pagos(
    id_pagos int(11) not null primary key auto_increment,
    descripcion varchar(200) not null,
    monto float not null
);

CREATE TABLE IF NOT EXISTS Colegiatura(
    id_colegiatura int not null primary key auto_increment,
    monto float not null,
    id_alumno int(11) not null
);


CREATE TABLE  IF NOT EXISTS Calificacion(
    id_calificacion int not null primary key auto_increment,
    calificacion float not null, 
    id_alumno int(11) not null, 
    id_curso int(11) not null, 
    unidad_evaluacion float not null
);

CREATE TABLE  IF NOT EXISTS Boleta(
    id_boleta int not null primary key auto_increment,
    id_curso int not null,
    id_profesor int not null,
    id_calificacion int not null,
    promedio float not null
);

