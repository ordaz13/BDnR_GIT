//TP2.1
create keyspace agencia with replication = { 'class' : 'SimpleStrategy','replication_factor' : 1}; 

//Creacion de la tabla
use agencia;
create table agencia (
marca varchar,
modelo varchar,
noSerie varchar,
anio int,
placa varchar,
color varchar,
tipo varchar,
servicios map<timestamp,text>,
costo map <timestamp,decimal>,
primary key ((marca, modelo), noSerie));

//Insercion de datos iniciales
use agencia;
insert into agencia (marca, modelo, noSerie, anio, placa, color, tipo) values ('vw', 'golf', '123A5678B', 2018, '789abc', 'rojo', 'deportivo');
insert into agencia (marca, modelo, noSerie, anio, placa, color, tipo) values ('vw', 'jetta', '123B5678C', 2017, '123def', 'negro', 'equipado');
insert into agencia (marca, modelo, noSerie, anio, placa, color, tipo) values ('nissan', 'sentra', '123456789', 2018, '123abc', 'blanco', 'equipado');
insert into agencia (marca, modelo, noSerie, anio, placa, color, tipo) values ('nissan', 'versa', '12345678A', 2018, '456abc', 'blanco', 'deportivo');

//Insercion de datos de los servicios
use agencia;
update agencia set servicios={'2018-01-02':'0 km'} where marca='vw' and modelo='golf' and noSerie='123A5678B';
update agencia set servicios={'2017-01-02':'0 km'} where marca='vw' and modelo='jetta' and noSerie='123B5678C';
update agencia set servicios= servicios+{'2018-01-02':'10000 kms'} where marca='vw' and modelo='jetta' and noSerie='123B5678C';

//Insercion de datos de los costo
use agencia;
update agencia set costo={'2018-01-02':2500} where marca='vw' and modelo='golf' and noSerie='123A5678B';
update agencia set costo={'2017-01-02':2500} where marca='vw' and modelo='jetta' and noSerie='123B5678C';
update agencia set costo=costo+{'2018-01-02':3500} where marca='vw' and modelo='jetta' and noSerie='123B5678C';

//Seleccionamos todo de la tabla de agencia
use agencia;
select * from agencia;