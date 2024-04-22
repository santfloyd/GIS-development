CREATE EXTENSION pgrouting;

select * from pgr_version();

ALTER TABLE public.malla_vial ADD COLUMN source integer;
ALTER TABLE public.malla_vial ADD COLUMN target integer;


SELECT pgr_createTopology('malla_vial',0.001,'geom','gid');

SELECT pgr_analyzeGraph('malla_vial',0,000002,id:='gid',the_geom:='geom',source:='source',target:='target');

SELECT pgr_analyzeOneway('malla_vial', ARRAY['','B','TF'],
										ARRAY['', 'B', 'FT'], 
						 				ARRAY['', 'B', 'FT'], 
						 				ARRAY['', 'B', 'TF'], oneway:='mvisvia');


ALTER TABLE public.malla_vial ADD COLUMN length double precision;
UPDATE public.malla_vial SET length=st_length(geom);	

ALTER TABLE public.malla_vial ADD COLUMN max_walk_speed double precision;
UPDATE public.malla_vial SET max_walk_speed=1.3;	

ALTER TABLE public.malla_vial ADD COLUMN cost double precision;
UPDATE public.malla_vial SET cost=length/max_walk_speed;

DELETE FROM malla_vial WHERE source IS Null;
SELECT * FROM malla_vial WHERE source IS NULL;	

ALTER TABLE areas_servicio_paraderos_tfm ADD COLUMN length NUMERIC;
UPDATE areas_servicio_paraderos_tfm
SET length = ST_length(geom);	 				

CREATE TABLE buffer_postgis AS SELECT *, (SELECT ST_Buffer(geom, 400)) FROM paraderos_zonales_sitp_proj;

ALTER TABLE buffer_postgis
ADD COLUMN area double precision;

UPDATE buffer_postgis
SET area = ST_AREA(st_buffer);

SELECT area FROM buffer_postgis LIMIT 5;

ALTER TABLE paraderos_zonales_sitp_proj
ADD COLUMN ISAI numeric;




SELECT buffer.* FROM buffer_postgis AS buffer

CREATE INDEX malla_vial_idx
ON malla_vial
USING GIST (geom);

DROP TABLE inter;

ALTER TABLE inters
RENAME TO interseccion_buffer_circular_malla;

create table interseccion_buffer_malla
as
SELECT buffer.gid,buffer.cenefa_par, st_union(ST_INTERSECTION(calles.geom, buffer.st_buffer))
FROM malla_vial AS calles, buffer_postgis AS buffer
WHERE ST_Intersects(calles.geom, buffer.st_buffer)
GROUP BY buffer.gid,buffer.cenefa_par;

ALTER TABLE interseccion_buffer_malla ADD COLUMN length numeric;
UPDATE interseccion_buffer_malla
SET length = ST_length(st_union);

CREATE TABLE paraderos_indicadores AS select 
paradero.cenefa_par, paradero.nombre_par, paradero.direccion_, paradero.localidad_, paradero.via_parade, paradero.geom,
inter.length AS buf_tramo_length,
buffer.area AS buf_circular_area,
tramos_areas_ser.length AS areas_serv_length,
areas_poli.area AS area_serv_area
from paraderos_zonales_sitp_proj AS paradero 
inner join interseccion_buffer_malla AS inter on paradero.cenefa_par = inter.cenefa_par
inner join buffer_postgis AS buffer on inter.cenefa_par=buffer.cenefa_par
inner join areas_servicio_paraderos_tfm AS tramos_areas_ser on buffer.cenefa_par=tramos_areas_ser.cenefa_par
inner join areas_servicio_paraderos_poligonos AS areas_poli on tramos_areas_ser.cenefa_par=areas_poli.cenefa_par;



CREATE INDEX paraderos_indicadores_idx
ON paraderos_indicadores
USING GIST (geom);

ALTER TABLE paraderos_indicadores
ADD COLUMN isai numeric;
UPDATE paraderos_indicadores
SET isai =  buf_tramo_length/buf_circular_area 

ALTER TABLE paraderos_indicadores
ADD COLUMN asai numeric;
UPDATE paraderos_indicadores
SET asai =  areas_serv_length/area_serv_area

ALTER TABLE paraderos_indicadores
ADD COLUMN scri numeric;
UPDATE paraderos_indicadores
SET scri =  buf_circular_area/area_serv_area

ALTER TABLE paraderos_indicadores
ADD COLUMN poblacion_servida numeric;
UPDATE paraderos_indicadores
SET poblacion_servida = i.poblacion_servida FROM (SELECT buffer.cenefa_par, buffer.area/upz.area_mcuadrados * upz.personas AS poblacion_servida FROM buffer_postgis AS buffer, upz_censo AS upz WHERE ST_intersects(buffer.geom, upz.geom)) AS i WHERE paraderos_indicadores.cenefa_par = i.cenefa_par;
