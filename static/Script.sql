CREATE DATABASE IF NOT EXISTS ERP;
USE ERP;



-- -----------------------------------------------------
-- Table `turnos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Turnos(
  id_turno INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(60) NOT NULL,
  hora_entrada TIME NOT NULL,
  hora_salida TIME NOT NULL,
  estatus VARCHAR(25) NOT NULL,
  PRIMARY KEY (id_turno));

-- -----------------------------------------------------
-- Table usuarios
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Usuarios(
  id_usuario INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  apellido_paterno VARCHAR(100) NOT NULL,
  apellido_materno VARCHAR(100) NOT NULL,
  genero VARCHAR(15) NOT NULL,
  colonia VARCHAR(65) NOT NULL,
  calle VARCHAR(65) NOT NULL,
  numero_casa INT NOT NULL,
  fecha_nacimiento DATE NOT NULL,
  fecha_registro DATE NOT NULL,
  correo VARCHAR(60) NOT NULL,
  telefono VARCHAR(15) NOT NULL,
  usuario VARCHAR(45) NOT NULL,
  passwd VARCHAR(45) NOT NULL,
  tipo VARCHAR(35) NOT NULL,
  estatus_usuario VARCHAR(35) NOT NULL,
  PRIMARY KEY (id_usuario));



-- -----------------------------------------------------
-- Table empleados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Empleados (
  id_empleado INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  rfc VARCHAR(35) NOT NULL,
  salario_diario FLOAT NOT NULL,
  fecha_contracion DATE NOT NULL,
  nss VARCHAR(30) NOT NULL,
  dias_vacaciones INT NOT NULL,
  dias_permiso INT NOT NULL,
  foto VARCHAR(200) NOT NULL,
  PRIMARY KEY (id_empleado),
  foreign key(id_usuario) references Usuarios(id_usuario))
;


-- -----------------------------------------------------
-- Table materia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Materia (
  id_materia INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  total_unidades INT NOT NULL,
  estatus VARCHAR(25) NOT NULL,
  PRIMARY KEY (id_materia));


-- -----------------------------------------------------
-- Table grupos
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Grupos(
  id_grupo INT NOT NULL AUTO_INCREMENT,
  grado INT NOT NULL,
  grupo VARCHAR(4) NOT NULL,
  capacidad INT NOT NULL,
  id_turno INT NOT NULL,
  id_materia INT NOT NULL,
  id_empleado INT NOT NULL,
  estatus VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_grupo),
  foreign key(id_turno) references Turnos(id_turno),
  foreign key(id_materia) references Materia(id_materia),
  foreign key(id_empleado) references Empleados(id_empleado));


-- -----------------------------------------------------
-- Table alumnos
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Alumnos (
  id_alumno INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  promedio FLOAT NULL DEFAULT NULL,
  rfc VARCHAR(25) NOT NULL,
  foto VARCHAR(200) NOT NULL,
  engrupo VARCHAR(200) NOT NULL,
  PRIMARY KEY (id_alumno),
  foreign key(id_usuario) references Usuarios(id_usuario));


-- -----------------------------------------------------
-- Table edificios
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Edificios (
  id_edificio INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(30) NOT NULL,
  tipo VARCHAR(15) NOT NULL,
  descripcion VARCHAR(50) NOT NULL,
  estado VARCHAR(12) NOT NULL,
  PRIMARY KEY (id_edificio));


-- -----------------------------------------------------
-- Table aulas
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Aulas(
  id_aula INT NOT NULL AUTO_INCREMENT,
  id_edificio INT NOT NULL,
  nombre VARCHAR(75) NOT NULL,
  capacidad INT NOT NULL,
  estado VARCHAR(30) NOT NULL,
  PRIMARY KEY (id_aula),
  foreign key (id_edificio) references Edificios(id_edificio));


-- -----------------------------------------------------
-- Table alumnogrupo
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS AlumnoGrupo (
  id_ag INT NOT NULL AUTO_INCREMENT,
  id_grupo INT NOT NULL,
  id_alumno INT NOT NULL,
  estatus VARCHAR(30) NOT NULL,
  PRIMARY KEY (id_ag),
  foreign key(id_grupo) references Grupos(id_grupo),
  foreign key(id_alumno) references Alumnos(id_alumno));
  
  
-- -----------------------------------------------------
-- Table calificacion
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Calificacion (
  id_calificacion INT NOT NULL AUTO_INCREMENT,
  calificacion FLOAT NOT NULL,
  unidad INT NOT NULL,
  validacion VARCHAR(2) NOT NULL,
  id_alumnogrupo int(11) not NULL,
  PRIMARY KEY (id_calificacion),
  foreign key(id_alumnogrupo) references AlumnoGrupo(id_ag));


-- -----------------------------------------------------
-- Table documentosalumno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS DocumentosAlumno(
  id_documento INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  descripcion VARCHAR(60) NOT NULL,
  archivo VARCHAR(200) NOT NULL,
  id_alumno INT NOT NULL,
  aprobacion VARCHAR(2) NOT NULL,
  PRIMARY KEY (id_documento),
  foreign key(id_alumno) references Alumnos(id_alumno)
);

-- -----------------------------------------------------
-- Table documentosempleado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS DocumentosEmpleado (
  id_documento INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  descripcion VARCHAR(60) NOT NULL,
  archivo VARCHAR(200) NOT NULL,
  id_empleado INT NOT NULL,
  aprobacion VARCHAR(2) NOT NULL,
  PRIMARY KEY (id_documento),
  foreign key(id_empleado) references Empleados(id_empleado)
);


-- -----------------------------------------------------
-- Table horario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Horario (
  id_horario INT NOT NULL AUTO_INCREMENT,
  id_aula INT NOT NULL,
  id_grupo INT NOT NULL,
  dia VARCHAR(20) NOT NULL,
  hora VARCHAR(20) NOT NULL,
  estatus varchar(25) not null,
  PRIMARY KEY (id_horario),
  foreign key(id_aula) references Aulas(id_aula),
  foreign key(id_grupo) references Grupos(id_grupo));


-- -----------------------------------------------------
-- Table pagos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Pagos (
  id_pagos INT NOT NULL AUTO_INCREMENT,
  descripcion VARCHAR(200) NOT NULL,
  tipo VARCHAR(59) NOT NULL,
  id_usuario INT NOT NULL,
  monto FLOAT NOT NULL,
  estatus varchar(25) not null,
  PRIMARY KEY (id_pagos),
  foreign key(id_usuario) references Usuarios(id_usuario)
);

-- -----------------------------------------------------
-- Table Asistencia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Asistencia (
  idAsistencia INT NOT NULL AUTO_INCREMENT,
  id_alumno INT NULL,
  id_materia INT NULL,
  fecha DATE NULL,
  observaciónes VARCHAR(200) NULL,
  estatus VARCHAR(45) NULL,
  PRIMARY KEY (idAsistencia),
  foreign key(id_alumno) references Alumnos(id_alumno),
  foreign key(id_materia) references Materia(id_materia)
);


-- -----------------------------------------------------
-- Table pagoColegiatura`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS PagoColegiatura (
  id_pagoColegiatura INT NOT NULL AUTO_INCREMENT,
  monto FLOAT NOT NULL,
  fechaPago DATE NULL,
  id_alumno INT NOT NULL,
  estatus varchar(25) not null,
  Responsable varchar(15) not null,
  PRIMARY KEY (id_pagoColegiatura),
  foreign key(id_alumno) references Alumnos(id_alumno)
  
);

CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON ERP.* TO 'admin'@'localhost';

insert into Usuarios values(1, "Jesús de", "Nazaret", "", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "admin@add.com",355115233,"admin","admin","Docente","Activo");
insert into Usuarios values(2, "Chris", "Evans", "Rodrigez", "Masculino", "Mar", "Arriaga", 51, '1999-03-8','2020-03-3', "crisevanspudin@gmail.com",355115233,"chris","chris","Alumno","Activo");
insert into Empleados values(1, 1,"MUMM990308M0H", 2500,'2017-03-8', 1701165,15,3,"elon.jpg");
insert into Alumnos values(1,2,1,"CHRISVAS1998","evans.jpg","Si");

#Contar Tablas
SELECT COUNT(*) from Information_Schema.Tables where TABLE_TYPE = 'BASE TABLE' and table_schema = 'ERP';

#Mostar nombre de las tablas

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
select* from Horario;