	   
SELECT st_AsText(pgr_alphaShape((SELECT ST_Collect(the_geom) FROM malla_vial_vertices_pgr),1.5));	  

CREATE TEMPORARY TABLE node AS
SELECT id, ST_X(geometry) AS x, ST_Y(geometry) AS y, geometry
	FROM (
	    SELECT source AS id,
		ST_Startpoint(geom) AS geometry
		FROM malla_vial
	    UNION
	    SELECT target AS id,
		ST_Startpoint(geom) AS geometry
		FROM malla_vial) AS node;
		
SELECT ST_SetSRID(ST_MakePolygon(ST_AddPoint(foo.openline, ST_StartPoint(foo.openline))),3116) AS geometry
	FROM (
	  SELECT ST_Makeline(points ORDER BY id) AS openline
	  FROM (
	    SELECT row_number() over() AS id, ST_MakePoint(x, y) AS points 
	    FROM pgr_alphashape('
		SELECT *
		FROM node
		    JOIN
		    (SELECT * FROM pgr_drivingDistance('SELECT gid AS id, source, target, cost AS cost FROM malla_vial',
										36, 400)) AS dd ON node.id = dd.node'::text)
	  ) AS a
	) AS foo;
	

--la clausula with sirve para nombrar una subquery, es como hacer una tabla temporal
WITH DD AS (SELECT seq, node, cost FROM pgr_drivingDistance(
										'SELECT gid AS id, source, target, cost AS cost FROM malla_vial',
										ARRAY(SELECT paraderos_id FROM paraderos WHERE paraderos_id BETWEEN 36 and 50), 400)),

dd_points AS (SELECT the_geom
FROM malla_vial_vertices_pgr AS mvvp, DD AS d --es necesario ponerle un alias a DD para que funciones
WHERE mvvp.id = d.node)
SELECT * FROM dd_points;
--OTRO INTENTO
WITH DD AS (SELECT seq, node, cost FROM pgr_drivingDistance(
										'SELECT gid AS id, source, target, cost AS cost FROM malla_vial',
										36, 400)),


dd_points AS (SELECT id::int4, the_geom as the_geom 
FROM malla_vial_vertices_pgr AS mvvp, DD AS d
WHERE mvvp.id = d.node)

--SELECT * FROM dd_points;
--SELECT st_Collect(the_geom) FROM dd_points;
SELECT pgr_alphaShape(st_Collect(the_geom)) FROM dd_points;
