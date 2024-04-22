--ejmeplo de Integrdad referencial de animales rescatados por abandono en ciudades o tráfico ilegal.
create schema SO;

--dominios
CREATE DOMAIN SO.clase as varchar check(VALUE IN('mamifero','reptil','pez','insecto'));
CREATE DOMAIN SO.dieta as varchar check(VALUE IN('omnivoro', 'herbívoros' , 'carnivoro','descomponedores','Parásitos','Coprófagos'));
CREATE DOMAIN SO.cultura_sagrado as varchar check(Value in('China','India','Mesoamérica','Egipto','Vietnam','Ghana','Norteamerica','ninguno'));

--tablas con check, claves primarias, uso de dominios y valores por defecto
CREATE TABLE SO.animales(id_clase varchar primary key,
					  reino varchar(20) not null,
					  clase SO.clase not null,
					  extremidades BOOLEAN 
					  );

Create table SO.refugio(
			id varchar primary key,
			nombre varchar(40),
			capacidad_individuos integer,
			id_clase varchar not null
			
	);

create table so.subespecie (
				   subespecie varchar(20) constraint check_subespecie unique,
				   id_refugio varchar not null,
				   id_subespecie varchar not null primary key,
				   dieta SO.dieta not null,
				   extinta BOOLEAN,
				   lista_roja BOOLEAN,
				   cultura_sagrado SO.cultura_sagrado DEFAULT 'ninguno',
				   comido_en varchar(20) DEFAULT 'ninguno',
				   poblacion numeric DEFAULT 0
				   );
				  


create table so.individuo (
						nombre_individuo varchar(20),
						id_individuo serial primary key,
						id_subespecie varchar not null,
						edad numeric,
						peso_kg numeric,
	
						constraint id_y_peso_animal check(id_subespecie = '1' and (peso_kg >= 50 and peso_kg <= 500) OR id_subespecie = '2' and (peso_kg >= 5 and peso_kg <= 50) OR id_subespecie = '3' and (peso_kg >= 2 and peso_kg <= 4) OR id_subespecie = '4' and (peso_kg >= 0.05 and peso_kg <= 0.30) OR id_subespecie = '5' and (peso_kg >= 2 and peso_kg <= 4) OR id_subespecie = '6' and (peso_kg >= 60 and peso_kg <= 1400) OR id_subespecie = '7' and (peso_kg >= 0.05 and peso_kg <= 0.085) OR id_subespecie = '8' and (peso_kg >= 45 and peso_kg <= 113) OR id_subespecie = '9' and (peso_kg >= 1 and peso_kg <= 100) OR id_subespecie = '10' and (peso_kg >= 5 and peso_kg <= 250) OR id_subespecie = '11' and (peso_kg >= 40 and peso_kg <= 450) OR id_subespecie = '12' and (peso_kg >= 1 and peso_kg <= 4) OR id_subespecie = '13' and (peso_kg >= 45 and peso_kg <= 1000) OR id_subespecie = '14' and (peso_kg >= 0.9 and peso_kg <= 1100) OR id_subespecie = '15' and (peso_kg >= 6 and peso_kg <= 12) OR id_subespecie = '16' and (peso_kg >= 200 and peso_kg <= 18400) OR id_subespecie = '17' and (peso_kg >= 200 and peso_kg <= 12000) )
						   );

--comportamiento cuando se actualizan y eleminan registros 
ALTER TABLE SO.refugio add constraint id_clase FOREIGN KEY (id_clase) REFERENCES SO.animales(id_clase) ON UPDATE CASCADE;
ALTER TABLE SO.subespecie add constraint id_refugio FOREIGN KEY (id_refugio) REFERENCES SO.refugio(id) ON UPDATE CASCADE;
ALTER TABLE SO.individuo add constraint id_subespecie FOREIGN KEY (id_subespecie) REFERENCES SO.subespecie(id_subespecie) ON UPDATE CASCADE;
ALTER TABLE SO.refugio add constraint id_clase_DEL FOREIGN KEY (id_clase) REFERENCES SO.animales(id_clase) ON DELETE CASCADE;


-- inserciones para evaluar la integridad referencial
INSERT INTO SO.animales (id_clase,reino, clase,extremidades) VALUES('1','animal','mamifero',true);
INSERT INTO SO.animales (id_clase,reino, clase,extremidades) VALUES('2','animal','pez',false);
INSERT INTO SO.animales (id_clase,reino, clase,extremidades) VALUES('3','animal','reptil',true);
INSERT INTO SO.animales (id_clase,reino, clase,extremidades) VALUES('4','animal','insecto',true);

INSERT INTO SO.refugio (id,nombre,capacidad_individuos,id_clase) VALUES('1','Refugio distrital para mamiferos',45,'1');
INSERT INTO SO.refugio (id,nombre,capacidad_individuos,id_clase) VALUES('2','Refugio distrital para peces',150,'2');
INSERT INTO SO.refugio (id,nombre,capacidad_individuos,id_clase) VALUES('3','Refugio distrital para reptiles',38,'3');
INSERT INTO SO.refugio (id,nombre,capacidad_individuos,id_clase) VALUES('4','Refugio distrital para insectos',1000,'4');


INSERT INTO SO.subespecie (subespecie,id_refugio, id_subespecie, dieta,extinta,lista_roja) VALUES('Mammut','1','17','herbívoros',true,false);
INSERT INTO SO.subespecie (subespecie,id_refugio, id_subespecie, dieta,extinta,lista_roja,cultura_sagrado,comido_en,poblacion) VALUES('perro','1','2','carnivoro',false,false,'India','China',525000000);
INSERT INTO SO.subespecie (subespecie,id_refugio, id_subespecie, dieta,extinta,lista_roja,cultura_sagrado,comido_en,poblacion) VALUES('liebre','1','5','herbívoros',false,true,'China','China',7000000);
INSERT INTO SO.subespecie (subespecie,id_refugio, id_subespecie, dieta,extinta,lista_roja,cultura_sagrado,comido_en,poblacion) VALUES('cocodrilo','3','14','carnivoro',false,true,'China','China',7000000);
INSERT INTO SO.subespecie (subespecie,id_refugio, id_subespecie, dieta,extinta,lista_roja,comido_en,poblacion) VALUES('cucaracha','4','4','descomponedores',false,false,'China',700000000);
INSERT INTO SO.subespecie (subespecie,id_refugio, id_subespecie, dieta,extinta,lista_roja,comido_en,poblacion) VALUES('oso pardo','1','1','omnivoro',false,true,'China',7000);
INSERT INTO SO.subespecie (subespecie,id_refugio, id_subespecie, dieta,extinta,lista_roja) VALUES('Tyrannosaurus Rex','3','16','carnivoro',true,false);
INSERT INTO SO.subespecie (subespecie,id_refugio, id_subespecie, dieta,extinta,lista_roja,poblacion) VALUES('caballo','1','13','herbívoros',false,false,10000000);
INSERT INTO SO.subespecie (subespecie,id_refugio, id_subespecie, dieta,extinta,lista_roja, poblacion) VALUES('león','1','10','carnivoro',false,true,230000);

INSERT INTO SO.individuo (id_subespecie, peso_kg) VALUES('17',5000);
INSERT INTO SO.individuo (nombre_individuo,id_subespecie, edad, peso_kg) VALUES('jack','14',18,500);
INSERT INTO SO.individuo (id_subespecie, peso_kg) VALUES('4',0.27);
INSERT INTO SO.individuo (nombre_individuo,id_subespecie, edad, peso_kg) VALUES('Motas','2',4,10);
INSERT INTO SO.individuo (nombre_individuo,id_subespecie, edad, peso_kg) VALUES('Rafa','2',10,40);
INSERT INTO SO.individuo (nombre_individuo,id_subespecie, edad, peso_kg) VALUES('Bruno','1',11,300);
INSERT INTO SO.individuo (nombre_individuo,id_subespecie, edad, peso_kg) VALUES('Thor','16',18,5000);
INSERT INTO SO.individuo (nombre_individuo,id_subespecie, edad, peso_kg) VALUES('Scarface','10',8,230);
INSERT INTO SO.individuo (nombre_individuo,id_subespecie, edad, peso_kg) VALUES('Tarantino','14',17,500);
INSERT INTO SO.individuo (nombre_individuo,id_subespecie, edad, peso_kg) VALUES('Kora','2',9,16);
INSERT INTO SO.individuo (nombre_individuo,id_subespecie, edad, peso_kg) VALUES('Laika','2',5,20);
INSERT INTO SO.individuo (nombre_individuo,id_subespecie, edad, peso_kg) VALUES('Cesar','13',12,500);


--violacion not null
INSERT INTO SO.animales (id_clase, clase,extremidades) VALUES('1','mamifero',true);

--violacion clave primaria subespecie
INSERT INTO SO.subespecie (subespecie,id_refugio, id_subespecie, dieta,extinta,lista_roja) VALUES('colibrí','1','2','herbívoros',false,false);

--violacion check tabla individuos
INSERT INTO SO.individuo (nombre_individuo,id_subespecie, edad, peso_kg) VALUES('Alfred','20',12,500);


--violacion de integridad referencial al insertar un individuo cuyo id_subespecie no esta registrado en la tabla subespecie
INSERT INTO SO.individuo (nombre_individuo,id_subespecie, edad,peso_kg) VALUES('María','20',12,25);



					