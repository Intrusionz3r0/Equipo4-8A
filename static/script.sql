CREATE DATABASE IF NOT EXISTS EPR;
USE ERP;

CREATE TABLE IF NOT EXISTS Usuarios(
    id_usuario int(11) not null  auto_increment,
    nombre varchar(100) not null,
    apellido_paterno varchar(100) not null,
    apellido_materno varchar(100) not null,
    genero varchar(15) not null,
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
    id_alumno int(11) not null  auto_increment,
    id_usuario int(11) not null,
    id_grupo int(11) not null
    primary key(id_alumno),
    foreign key(id_usuario) references Usuarios(id_usuario),
    foreign key(id_grupo) references Grupos(id_grupo)
    /*foreign key(id_turno) references Turnos(id_turno)*/
);

CREATE TABLE  IF NOT EXISTS Materia(
    id_materia int(11) not null auto_increment, 
    nombre varchar(50) not null,
    total_unidades int(11) not null,
    primary key(id_asignatura),
    foreign key(id_Empleado) references Empleados(id_empleado)
);

CREATE TABLE IF NOT EXISTS Grupos(
    id_grupo int not null auto_increment
    grado varchar(2) not null,
    grupo varchar(2) not null,
    id_turno int not null,
    id_materia int not null,
    primary key(id_grupo)
    foreign key(id_turno) references Turnos(id_turno),
    foreign key(id_materia) references Materia(id_materia)
);

CREATE TABLE IF NOT EXISTS Empleados(
    id_empleado int(11) not null  auto_increment,
    id_usuario int(11) not null,
    id_grupo int(11) not null,
    tipo varchar (35) not null,
    rfc varchar (20) not null,
    salario_diario float not null,
    fecha_contracion date not null,
    nss varchar(10) not null,
    dias_vacaciones int not null,
    dias_permiso int not null,
    foto varchar(200) not null,
    primary key(id_empleado),
    foreign key(id_usuario) references Usuarios(id_usuario),
    foreign key(id_grupo) references Grupos(id_grupo)
);



CREATE TABLE  IF NOT EXISTS Edificios(
    id_edificio int not null  auto_increment,
    nombre varchar(30) not null,
    tipo varchar(10) not null,
    descripcion varchar(50) not null,
    estado varchar(13) not null,
    primary key(id_edificio)
);

CREATE TABLE  IF NOT EXISTS Aulas(
    id_aula int(11) not null  auto_increment,
    id_edificio int(11) not null,
    nombre varchar(10) not null,
    capacidad int(11) not null,
    estado varchar(13) not null,
    
    primary key(id_aula),
    foreign key (id_edificio) references Edificios(id_edificio)
);

CREATE TABLE  IF NOT EXISTS Turnos(
    id_turno int(11) not null  auto_increment,
    nombre varchar(45) not null,
    hora_entrada varchar(8) not null,
    hora_salida varchar(8) not null,
    primary key(id_turno)
);


CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON ERP.* TO 'admin'@'localhost';
