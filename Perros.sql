create database veterinaria;
use veterinaria;
create table dueno (
	dni int primary key,
    nombre varchar(20),
    apellido varchar(20),
    telefono varchar(10),
    direccion varchar(50)
    );
    
-- Punto 1
create table perro (
	id_perro int primary key auto_increment,
    nombre varchar(10),
    fecha_nac date,
    sexo char(1),
    DNI_dueno int references dueno(dni)
	);
create table historial (
	id_historial int primary key auto_increment,
    fecha date,
    perro int references perro(id_perro),
    descripcion varchar(100),
    monto float
	);
insert into dueno(dni,nombre,apellido,telefono,direccion) values
(34555666,'Veronica','Kostich',1122550000,'Avenida 14 1356'),
(22111888,'Ariel','Gomez',1136661111,'Peña 3699'),
(16999333,'Leticia','Lamarca',1156488888,'Montañeses 1458');

-- Punto 2 
insert into perro(nombre,fecha_nac,sexo,DNI_dueno) values
('Sasha','2009-07-12','1',(select dni from dueno where dni=34555666)),
('Trini','2018-03-01','1',(select dni from dueno where dni=22111888)),
('Trueno','2002-05-22','2',(select dni from dueno where dni=16999333));
insert into historial(fecha,perro,descripcion,monto) values
('2022-01-08',(select id_perro from perro where id_perro=1),'vacunas','8000'),
('2022-07-23',(select id_perro from perro where id_perro=2),'baño y corte','5500'),
('2013-02-20',(select id_perro from perro where id_perro=3),'baño','2000');

-- select * from historial where fecha < '2020-1-1';

-- Punto 6: Obtener todos los perros que asistieron a la peluquería en 2022.
select * from historial where fecha between '2022-1-1' and '2022-12-31';
