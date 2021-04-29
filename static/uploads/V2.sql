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
    id_materia int(11) not null,
    id_usuario int(11) not null,
    estatus varchar(20) not null,
    primary key(id_grupo),
    foreign key(id_turno) references Turnos(id_turno),
    foreign key(id_materia) references Materia(id_materia),
    foreign key(id_usuario) references Usuarios(id_usuario)
);

CREATE TABLE IF NOT EXISTS Alumnos(
    id_alumno int(11) not null  auto_increment,
    id_usuario int(11) not null,
    id_grupo int(11),
    rfc varchar(25) not null,
    foto varchar(200) not null,
    primary key(id_alumno),
    foreign key(id_usuario) references Usuarios(id_usuario),
    foreign key(id_grupo) references Grupos(id_grupo)
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

CREATE TABLE  IF NOT EXISTS Documentos(
    id_documento int(11) not null  auto_increment,
    nombre varchar(50) not null,
    descripcion varchar(60) not null,
    archivo varchar(200) not null,
    id_usuario int(11) not null,
    aprobacion varchar(2) not null,

    primary key(id_documento),
    foreign key(id_usuario) references Usuarios(id_usuario)
);


insert into Usuarios values(1, "Admin", "Administrator", "sysadmin", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "admin@add.com",355115233,"admin","admin","Docente","Activo");
insert into Usuarios values(2, "Chris", "Evans", "Rodrigez", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "crisevanspudin@gmail.com",355115233,"chris","chris","Docente","Activo");
insert into Usuarios values(3, "Jose", "Perez", "Rodrigez", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "crisevanspudin@gmail.com",355115233,"chris2","chris","Docente","Activo");
insert into Usuarios values(4, "Luis", "solorio", "Rodrigez", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "crisevanspudin@gmail.com",355115233,"chris3","chris","Docente","Activo");
insert into Usuarios values(5, "Pedro", "ceja", "Rodrigez", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "crisevanspudin@gmail.com",355115233,"chris4","chris","Alumno","Activo");
insert into Usuarios values(6, "Toño", "Leon", "Rodrigez", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "crisevanspudin@gmail.com",355115233,"chris5","chris","Alumno","Activo");
insert into Usuarios values(7, "Carlos", "Mero", "Rodrigez", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "crisevanspudin@gmail.com",355115233,"chris6","chris","Alumno","Activo");

insert into Empleados values(1, 1,"MUMM990308M0H", 2500,'2017-03-8', 1701165,15,3,"elon.jpg");
insert into Empleados values(2, 2,"MUMM990308M0H", 2500,'2017-03-8', 1701165,15,3,"elon.jpg");


insert into Turnos values(1, "Matutino", "07:00", "12:00", "Activo");
insert into Turnos values(2, "Vespertino", "12:00", "18:00", "Activo");
insert into Turnos values(3, "Extra", "14:00", "19:00", "Activo");

insert into Materia values(1,"Español",4,"Activa");
insert into Materia values(2,"Matematicas",5,"Activa");
insert into Materia values(3,"Ingles",8,"Activa");

insert into Grupos values(1,1,"A",30,1,1,1,"Activo");
insert into Grupos values(2,2,"A",20,2,2,2,"Activo");


insert into Alumnos values(1,5,1,"CHRISVAS1998","evans.jpg");
insert into Alumnos values(2,6,2,"CHRISVAS1998","evans.jpg");


insert into Edificios values(1, "Patio", "Administracion","Contiene 5 aulas con capacidd de 100 alumnos", "Habilitado");
insert into Edificios values(2, "Auditorio", "Administracion","Contiene 2 aulas con capacidd de 80 alumnos", "Habilitado");
insert into Edificios values(3, "Audiovisual", "Administracion","Contiene 3 aulas con capacidd de 170 alumnos", "Habilitado");

insert into Aulas values(1,1,"AE31j",50,"Activo");
insert into Aulas values(2,2,"AE32j",40,"Activo");
insert into Aulas values(3,3,"AE33j",65,"Activo");

insert into Calificacion values(1,1,1,10,1,"Si");
insert into Calificacion values(2,1,1,10,2,"Si");
insert into Calificacion values(3,1,1,10,3,"Si");
insert into Calificacion values(4,2,1,10,1,"Si");
insert into Calificacion values(5,2,1,10,2,"Si");
insert into Calificacion values(6,2,1,10,3,"Si");

insert into Documentos values(1,"CURP","ORIGINAL","ALGO.png",1,"SI");
insert into Documentos values(2,"CURP","Copia","ALGO.png",1,"SI");
insert into Documentos values(3,"CURP","ORIGINAL","ALGO.png",2,"SI");
insert into Documentos values(4,"CURP","Copia","ALGO.png",2,"SI");
insert into Documentos values(5,"CURP","Acta Nacimiento","ALGO.png",1,"SI");

CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON ERP.* TO 'admin'@'localhost';

Select * from Usuarios;
Select * from Turnos;
Select * from Edificios;
Select * from Empleados;
Select * from Materia;
Select * from Grupos;
Select * from Alumnos;
Select * from Aulas;
Select * from Calificacion;


CREATE TABLE IF NOT EXISTS Horario(
	id_horario int(11) not null auto_increment,
    id_asignatura int(11) not null,
    id_aula int(11) not null,
    dia varchar(10) not null,
    hora_inicio varchar(8) not null,
    hora_fin varchar(8) not null,
	primary key(id_horario)
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


#Contar Tablas
SELECT COUNT(*) from Information_Schema.Tables where TABLE_TYPE = 'BASE TABLE' and table_schema = 'ERP';

#Mostar nombre de las tablas
SHOW FULL TABLES FROM ERP;


