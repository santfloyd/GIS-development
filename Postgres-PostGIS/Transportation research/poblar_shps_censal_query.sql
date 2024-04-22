CREATE TABLE upz_censo AS SELECT upla.*, informacion_demografica.* FROM upla_proj AS upla LEFT JOIN informacion_demografica ON informacion_demografica.upz=upla.uplcodigo;

CREATE TABLE localidad_censo AS SELECT localidad.*, SUM(upz_censo.Personas) AS suma_personas FROM loca_proj AS localidad JOIN upz_censo ON (st_intersects(localidad.geom,upz_censo.geom)) GROUP BY localidad.gid;

ALTER TABLE upz_censo ADD COLUMN area_mcuadrados NUMERIC;

UPDATE upz_censo SET area_mcuadrados=st_area(geom);

CREATE OR REPLACE FUNCTION public.proportional_sum(geometry, geometry, numeric) RETURNS numeric AS
$BODY$
SELECT $3 * areacalc FROM (
SELECT (ST_Area(ST_Intersection($1, $2))/ST_Area($2))::numeric AS areacalc
) AS areac; 
$BODY$
LANGUAGE sql VOLATILE;

CREATE TABLE zat_censo AS SELECT a.*, ROUND(SUM(public.proportional_sum(a.geom, b.geom, b.personas))) FROM
public.zat_proj AS a, public.upz_censo as b WHERE ST_Intersects(a.geom, b.geom) GROUP BY a.gid;