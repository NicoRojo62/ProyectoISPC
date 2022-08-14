select * from dueno  inner join perro  on dueno.DNI = perro.DNI_dueno inner join historial on perro.id_perro = historial.perro where fecha_nac > '2017-12-31' and fecha not like '2022%';






