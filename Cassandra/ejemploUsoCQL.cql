//Creacion del keyspace
create keyspace ejemplo with replication = { 'class' : 'SimpleStrategy', 'replication_factor' : 1};
//Para indicar el keyspace que queremos usar: use ejemplo;
//Creamos una tabla nueva
use ejemplo;
create table emp (
 	depId int,
 	empId int,
 	nombre varchar,
 	apellido varchar,
 	primary key (depId, empId)); 
//Algunos valores para insertar la tabla
use ejemplo;
insert into emp (depId, empId, nombre, apellido) values (1, 1, 'Ana', 'Suarez');
insert into emp (depId, empId, nombre, apellido) values (1, 2, 'Roberto', 'Aldama');
insert into emp (depId, empId, nombre, apellido) values (2, 3, 'Cecilia', 'Campos');
insert into emp (depId, empId, nombre, apellido) values (2, 4, 'David', 'Flores');
insert into emp (depId, empId, nombre, apellido) values (3, 5, 'Ana', 'Macedo'); 
//Selecciona todo de la tabla empleado
use ejemplo;
select * from emp;
//Selecciona todo de la tabla empleado donde el id del departamento sea 1
use ejemplo;
select * from emp where depid=1;
//Como busca en algo compuesto necesitamos utilizar el 'allow filtering'
use ejemplo;
select * from emp where empid=1 allow filtering; 
//Creamos un indice sobre el nombre para poder usar un select
use ejemplo;
create index on emp(nombre); 
//Selecciona todo de la tabla empleado cuyo nombre sea 'Ana'
use ejemplo;
select * from emp where nombre='Ana'; 
//Crea un campo del tipo 'set' cuyo contenido sea texto
use ejemplo;
alter table emp add tels set<text>; 
//Agregamos datos al campo de telefono
use ejemplo;
update emp set tels={'11','12'} where depid=1 and empid=1;
update emp set tels= tels+{'13'} where depid=1 and empid=1; 
//Añade una columna del tipo lista para los hijos
use ejemplo;
alter table emp add hijos list<text>; 
//Insertamos datos en la lista de hijos
use ejemplo;
update emp set hijos=['Samuel','Diana'] where depid=1 and empid=1;
//Añadimos un map (diccionario) para los cargos 
use ejemplo;
alter table emp add cargos map<int,text>; 
//Insertamos datos
use ejemplo;
update emp set cargos={1:'Asistente'} where depid=1 and empid=1;
update emp set cargos=cargos+{2:'Tecnico'} where depid=1 and empid=1; 
//Otro mapa como ejemplo
use ejemplo;
alter table emp add sueldos map<timestamp,text>;
update emp set sueldos={'2017-01-02':'5000'} where depid=2 and empid=3; 
//Ejemplo de eliminar datos de la tabla, lo deja null
use ejemplo;
delete apellido from emp where depid=2 and empid=4;