
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
(23876525,'laura','rojas',3810000000,'av. siempreviva 742'),
(30962811,'pablo','diaz',3811111111,'roca 998'),
(19465712,'joe','camber',2222222222,'Castle Rock 999');

insert into perro(nombre,fecha_nac,sexo,DNI_dueno) values
('firulais','2012-01-25','1',(select dni from dueno where dni=23876525)),
('luna','2020-7-4','2',(select dni from dueno where dni=30962811)),
('cujo','1980-7-22','1',(select dni from dueno where dni=19465712));
insert into historial(fecha,perro,descripcion,monto) values
('2022-01-5',(select id_perro from perro where id_perro=1),'baño y corte','2000'),
('2020-12-23',(select id_perro from perro where id_perro=2),'baño y corte','1500'),
('1980-1-5',(select id_perro from perro where id_perro=3),'baño','5');

select * from dueno  inner join perro  on dueno.DNI = perro.DNI_dueno inner join historial on perro.id_perro = historial.perro where fecha_nac > '2017-12-31' and fecha not like '2022%';


