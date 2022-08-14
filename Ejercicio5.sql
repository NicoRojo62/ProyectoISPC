create database veterinaria;
use veterinaria;
create table dueno (
	dni int primary key,
    nombre varchar(50),
    apellido varchar(50),
    telefono varchar(10),
    direccion varchar(50)
    );
-- Punto 1
create table perro (
	id_perro int primary key auto_increment,
    nombre varchar(50),
    fecha_nac date,
    sexo char(1),
    DNI_dueno int references dueno(dni)
	);
create table historial (
	id_historial int primary key auto_increment,
    fecha date,
    perro int references perro(id_perro),
    descripcion varchar(200),
    monto float
	);
insert into dueno(dni,nombre,apellido,telefono,direccion) values
(37468144,'cosme','fulanito',3516145497,' evergreen terrace 742'),
(22364885,'paquita','navajas',3704524965,'calle falsa 123'),
(36954255,'reachel','green',3514265698,'sherman calle wallaby 42');

-- punto 2 
insert into perro(nombre,fecha_nac,sexo,DNI_dueno) values
('beethoven','2011-03-15','2',(select dni from dueno where dni=37468144)),
('coraje','2019-5-2','1',(select dni from dueno where dni=22364885)),
('metralleta','1999-8-23','2',(select dni from dueno where dni=36954255));
insert into historial(fecha,perro,descripcion,monto) values
('2011-03-15',(select id_perro from perro where id_perro=1),'baño y corte','3600'),
('2019-5-2',(select id_perro from perro where id_perro=2),'baño y corte','1800'),
('1999-8-23',(select id_perro from perro where id_perro=3),'baño','3600');

-- punto 5
select nombre from perro where DNI_dueno = (select dni from dueno where nombre = 'pedro');