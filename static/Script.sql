CREATE DATABASE IF NOT EXISTS ERP;
USE ERP;

CREATE TABLE  IF NOT EXISTS Turnos(
    id_turno int(11) not null  auto_increment,
    nombre varchar(60) not null,
    hora_entrada time not null,
    hora_salida time not null,
    estatus varchar(25) not null,
    primary key(id_turno)
);


 

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
    telefono varchar(15) not null,
    usuario varchar(45) not null unique,
    passwd varchar(45) not null,
    tipo varchar (35) not null,
    estatus_usuario varchar(35) not null,
    primary key(id_usuario)
);

CREATE TABLE IF NOT EXISTS Empleados(
    id_empleado int(11) not null  auto_increment,
    id_usuario int(11) not null,
    rfc varchar (35) not null,
    salario_diario float not null,
    fecha_contracion date not null,
    nss varchar(30) not null,
    dias_vacaciones int not null,
    dias_permiso int not null,
    foto varchar(200) not null,
    primary key(id_empleado),
    foreign key(id_usuario) references Usuarios(id_usuario)
);

CREATE TABLE  IF NOT EXISTS Materia(
    id_materia int(11) not null auto_increment,
    nombre varchar(50) not null,
    total_unidades int(11) not null,
    estatus varchar(25) not null,
    primary key(id_materia)
);

CREATE TABLE IF NOT EXISTS Grupos(
    id_grupo int (11) not null auto_increment,
    grado int(5) not null,
    grupo varchar(4) not null,
    capacidad int(5) not null,
    id_turno int(11) not null,
    id_usuario int(11) not null,
    estatus varchar(20) not null,
    primary key(id_grupo),
    foreign key(id_turno) references Turnos(id_turno),
    foreign key(id_usuario) references Usuarios(id_usuario)
);



CREATE TABLE IF NOT EXISTS Alumnos(
    id_alumno int(11) not null  auto_increment,
    id_usuario int(11) not null,
    promedio float,
    rfc varchar(25) not null,
    foto varchar(200) not null,
    primary key(id_alumno),
    foreign key(id_usuario) references Usuarios(id_usuario)
);

CREATE TABLE  IF NOT EXISTS Edificios(
    id_edificio int not null  auto_increment,
    nombre varchar(30) not null,
    tipo varchar(15) not null,
    descripcion varchar(50) not null,
    estado varchar(12) not null,
    primary key(id_edificio)
);

CREATE TABLE  IF NOT EXISTS Aulas(
    id_aula int(11) not null  auto_increment,
	id_edificio int(11) not null,
    nombre varchar(75) not null,
    capacidad int(11) not null,
    estado varchar(30) not null,
    primary key(id_aula),
    foreign key (id_edificio) references Edificios(id_edificio)
);

CREATE TABLE  IF NOT EXISTS Calificacion(
    id_calificacion int not null  auto_increment,
	id_materia int(11) not null, 
    id_alumno int(11) not null, 
    calificacion float not null,
    unidad int(11) not null,
    validacion varchar(2) not null,
    primary key(id_calificacion),
    foreign key(id_materia) references Materia(id_materia),
    foreign key(id_alumno) references Alumnos(id_alumno)
);



CREATE TABLE  IF NOT EXISTS DocumentosAlumno(
    id_documento int(11) not null  auto_increment,
    nombre varchar(50) not null,
    descripcion varchar(60) not null,
    archivo varchar(200) not null,
    id_alumno int(11) not null,
    aprobacion varchar(2) not null,

    primary key(id_documento),
    foreign key(id_alumno) references Alumnos(id_alumno)
);

CREATE TABLE  IF NOT EXISTS DocumentosEmpleado(
    id_documento int(11) not null  auto_increment,
    nombre varchar(50) not null,
    descripcion varchar(60) not null,
    archivo varchar(200) not null,
    id_empleado int(11) not null,
    aprobacion varchar(2) not null,

    primary key(id_documento),
    foreign key(id_empleado) references Empleados(id_empleado)
);


CREATE TABLE IF NOT EXISTS Horario(
	id_horario int(11) not null auto_increment,
    id_aula int(11) not null,
    id_grupo int(11) not null,
    id_usuario int(11) not null,
    fecha date not null,
    hora_inicio varchar(8) not null,
    hora_fin varchar(8) not null,
	primary key(id_horario),
    foreign key(id_aula) references Aulas(id_aula),
	foreign key(id_grupo) references Grupos(id_grupo),
	foreign key(id_usuario) references Usuarios(id_usuario)
);


CREATE TABLE IF NOT exists Productos(
	id_producto int (11) not null  auto_increment,
	nombre varchar(50) not null,
	descripcion varchar(50) not null,
	costo_unitario float not null,

    primary key(id_producto)
);

CREATE TABLE IF NOT exists Proveedor(
	id_proveedor int(11) not null  auto_increment,
	nombre varchar(50) not null,	
	telefono varchar(12) not null,
	direccion varchar(200) not null,
	contacto varchar(65) not null,
	correo varchar(80) not null,
    
	primary key(id_proveedor)
);

CREATE TABLE  IF NOT EXISTS Pedidos(
    id_pedido int(11) not null auto_increment,
    id_proveedor int(11) not null,
    id_producto int(11) not null,
    fecha_emitido date not null,
    fecha_entregaEstimada date not null,
    precio_total float not null,
    descripcion varchar(80) not null,
    cantidad int not null,
    forma_pago varchar(50) not null,
    lugar_entrega varchar(50) not null,

    primary key(id_pedido),
    foreign key(id_proveedor) references Proveedor(id_proveedor),
	foreign key(id_producto) references Productos(id_producto)
);

CREATE TABLE  IF NOT EXISTS Nomina(
    id_nomina int (11) not null auto_increment,
    fecha_elaboracion date not null,
    id_empleado int(11) not null,
    fecha_pago date not null,
    subtotal float not null,
    descripcion_retencion varchar(75)not null,
    importe_retencion float not null,
    pago_total float not null,
    descripcion_bonos varchar(75) not null,
    importe_bonos float not null,
    forma_pago varchar(50) not null,
    estatus varchar(25) not null,
    
    primary key(id_nomina),
    foreign key(id_empleado) references Empleados(id_empleado)
);

CREATE TABLE IF NOT EXISTS Pagos(
    id_pagos int(11) not null  auto_increment,
    descripcion varchar(200) not null,
    tipo varchar (59)not null,
    id_usuario int(11) not null,
    monto float not null,
    primary key(id_pagos),
	foreign key(id_usuario) references Usuarios(id_usuario)
);


CREATE table IF NOT EXISTS Asistencias(
    id_asistencia int (11) not null  auto_increment,
    id_empleado int(11) not null,
    llegada datetime not null,
    salida datetime not null,

    primary key(id_asistencia),
    foreign key(id_empleado) references Empleados(id_empleado)
); 

create table if not exists AlumnoGrupo(
	id_ag int(11) not null auto_increment,
    id_grupo int(11) not null,
    id_alumno int(11) not null,
    id_turno int (11)not null,
    estatus varchar(30) not null,
    
    primary key(id_ag),
    foreign key(id_grupo) references Grupos(id_grupo),
    foreign key(id_alumno) references Alumnos(id_usuario),
    foreign key(id_turno) references Turnos(id_turno)
);


#Contar Tablas
SELECT COUNT(*) from Information_Schema.Tables where TABLE_TYPE = 'BASE TABLE' and table_schema = 'ERP';

#Mostar nombre de las tablas
SHOW FULL TABLES FROM ERP;

#Crear usuario para trabajar con flask
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON ERP.* TO 'admin'@'localhost';

insert into Usuarios values(1, "Elon", "Rieve", "Musk", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "admin@add.com",355115233,"admin","admin","Docente","Activo");
insert into Empleados values(1, 1,"MUMM990308M0H", 2500,'2017-03-8', 1701165,15,3,"elon.jpg");
insert into Usuarios values(2, "Chris", "Evans", "Rodrigez", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "crisevanspudin@gmail.com",355115233,"chris","chris","Alumno","Activo");
insert into Turnos values(1, "Matutino", "07:00", "12:00", "Activo");
insert into Edificios values(1, "Principal", "Administracion","Contiene 5 aulas con capacidd de 100 alumnos", "Habilitado");
insert into Materia values(1,"Español",5,"Activa");
insert into Aulas values(1,1,"Global",100,"Activo");
insert into Grupos values(1,1,"A",18,1,1,"Activo");
insert into Alumnos values(1,2,0,"CHRISVAS1998","evans.jpg");


Select * from Usuarios;
Select * from Turnos;
Select * from Edificios;
Select * from Empleados;
Select * from Materia;
Select * from Grupos;
Select * from Alumnos;
Select * from Aulas;
Select * from DocumentosEmpleado;
Select * from DocumentosAlumno;



/*
insert into Usuarios values(26, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente14","admin","Docente","Activo");
insert into Usuarios values(27, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente16","admin","Docente","Activo");
insert into Usuarios values(28, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente126565","admin","Docente","Activo");
insert into Usuarios values(29, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente1254","admin","Docente","Activo");
insert into Usuarios values(30, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente1215","admin","Docente","Activo");
insert into Usuarios values(31, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente18","admin","Docente","Activo");
insert into Usuarios values(32, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente19","admin","Docente","Activo");
insert into Usuarios values(33, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente20","admin","Docente","Activo");
insert into Usuarios values(34, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente21","admin","Docente","Activo");
insert into Usuarios values(35, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente22","admin","Docente","Activo");
insert into Usuarios values(36, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente23","admin","Docente","Activo");
insert into Usuarios values(37, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente24","admin","Docente","Activo");
insert into Usuarios values(38, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente25","admin","Docente","Activo");
insert into Usuarios values(39, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente26","admin","Docente","Activo");
insert into Usuarios values(40, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente27","admin","Docente","Activo");
insert into Usuarios values(41, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente28","admin","Docente","Activo");
insert into Usuarios values(42, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente29","admin","Docente","Activo");
insert into Usuarios values(43, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente30","admin","Docente","Activo");
insert into Usuarios values(44, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente31","admin","Docente","Activo");
insert into Usuarios values(45, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente32","admin","Docente","Activo");
insert into Usuarios values(46, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente33","admin","Docente","Activo");
insert into Usuarios values(47, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente34","admin","Docente","Activo");
insert into Usuarios values(48, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente35","admin","Docente","Activo");
insert into Usuarios values(49, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente36","admin","Docente","Activo");
insert into Usuarios values(50, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente37","admin","Docente","Activo");
insert into Usuarios values(51, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente38","admin","Docente","Activo");
insert into Usuarios values(52, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente834","admin","Docente","Activo");
insert into Usuarios values(53, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente40","admin","Docente","Activo");
insert into Usuarios values(54, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente141","admin","Docente","Activo");
insert into Usuarios values(55, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente42","admin","Docente","Activo");
insert into Usuarios values(56, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente43","admin","Docente","Activo");
insert into Usuarios values(256, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente44","admin","Docente","Activo");
insert into Usuarios values(58, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente45","admin","Docente","Activo");
insert into Usuarios values(59, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente46","admin","Docente","Activo");
insert into Usuarios values(60, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente47","admin","Docente","Activo");
insert into Usuarios values(61, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente48","admin","Docente","Activo");
insert into Usuarios values(62, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente49","admin","Docente","Activo");
insert into Usuarios values(63, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente50","admin","Docente","Activo");
insert into Usuarios values(65, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente51","admin","Docente","Activo");
insert into Usuarios values(66, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente52","admin","Docente","Activo");
insert into Usuarios values(67, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente53","admin","Docente","Activo");
insert into Usuarios values(68, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente155","admin","Docente","Activo");
insert into Usuarios values(69, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente156","admin","Docente","Activo");
insert into Usuarios values(70, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente157","admin","Docente","Activo");
insert into Usuarios values(71, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente1258","admin","Docente","Activo");
insert into Usuarios values(72, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente1259","admin","Docente","Activo");
insert into Usuarios values(73, "Docente12", "Docente12", "Docente12", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "Docente12@add.com",355115233,"Docente80","admin","Docente","Activo");
*/