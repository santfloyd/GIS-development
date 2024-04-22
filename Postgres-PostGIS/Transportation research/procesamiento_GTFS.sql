CREATE TABLE agency (agency_id char(50),
					 agency_name char(50),
					 agency_url char(100),
					 agency_timezone char(50),
					 agency_lang char(50),
					 agency_phone char(50),
					 agency_fare_url char(100))
					 
COPY agency
FROM 'E:\C\Tesina_master_sig\datos_abiertos_bogota\DATOS_ACTUALES\GTFS\agency.txt'
DELIMITER ','
CSV HEADER;

CREATE TABLE calendar (service_id CHAR(10),
					   monday CHAR(10),
					   tuesday CHAR(10),
					   wednesday CHAR(10),
					   thursday CHAR(10),
					   friday CHAR(10),
					   saturday CHAR(10),
					   sunday CHAR(10),
					   start_date date,
					   end_date date)
					   
COPY calendar
FROM 'E:\C\Tesina_master_sig\datos_abiertos_bogota\DATOS_ACTUALES\GTFS\calendar.txt'
DELIMITER ','
CSV HEADER;

CREATE TABLE calendar_dates (service_id char(10),
					   "date" date,
					   exception_type char(10))
					   
COPY calendar_dates
FROM 'E:\C\Tesina_master_sig\datos_abiertos_bogota\DATOS_ACTUALES\GTFS\calendar_dates.txt'
DELIMITER ','
CSV HEADER;

CREATE TABLE feed_info (feed_publisher_name CHAR(50),
							 feed_publisher_url CHAR(50),
							 feed_lang CHAR(50),
							 feed_start_date DATE,
							 feed_end_date DATE,
							 feed_version CHAR(50))
							 
COPY feed_info
FROM 'E:\C\Tesina_master_sig\datos_abiertos_bogota\DATOS_ACTUALES\GTFS\feed_info.txt'
DELIMITER ','
CSV HEADER;

CREATE TABLE routes (route_id CHAR(50),
					 agency_id CHAR(50),
					 route_long_name CHAR(50),
					 route_desc CHAR(50),
					 route_short_name CHAR(50),
					 route_type CHAR(50),
					 route_url CHAR(50),
					 route_color CHAR(50),
					 route_text_color CHAR(50))
					 
COPY routes
FROM 'E:\C\Tesina_master_sig\datos_abiertos_bogota\DATOS_ACTUALES\GTFS\routes.txt'
DELIMITER ','
CSV HEADER;

CREATE TABLE shapes (shape_id CHAR(50),
					 shape_pt_lat numeric,
					 shape_pt_lon numeric,
					 shape_pt_sequence integer)
					 
COPY shapes
FROM 'E:\C\Tesina_master_sig\datos_abiertos_bogota\DATOS_ACTUALES\GTFS\shapes.txt'
DELIMITER ','
CSV HEADER;

CREATE TABLE stop_times (trip_id CHAR(50),
						 arrival_time INTERVAL,
						 departure_time INTERVAL,
						 stop_id CHAR(50),
						 stop_sequence INTEGER,
						 stop_headsign CHAR(50))
						 
COPY stop_times
FROM 'E:\C\Tesina_master_sig\datos_abiertos_bogota\DATOS_ACTUALES\GTFS\stop_times.txt'
DELIMITER ','
CSV HEADER;

CREATE TABLE stops (stop_id CHAR(50),
					stop_code CHAR(50), 
					stop_name CHAR(100),
					stop_desc CHAR(50),
					stop_lat NUMERIC,
					stop_lon NUMERIC,
					stop_url CHAR(50),
					wheelchair_boarding CHAR(50))
						 
COPY stops
FROM 'E:\C\Tesina_master_sig\datos_abiertos_bogota\DATOS_ACTUALES\GTFS\stops.txt'
DELIMITER ','
CSV HEADER;

CREATE TABLE trips (route_id CHAR(50),
					service_id CHAR(50),
					trip_id CHAR(50),
					trip_headsign CHAR(50),
					shape_id CHAR(50))
					
COPY trips
FROM 'E:\C\Tesina_master_sig\datos_abiertos_bogota\DATOS_ACTUALES\GTFS\trips.txt'
DELIMITER ','
CSV HEADER;

ALTER TABLE stops DROP COLUMN geom;
ALTER TABLE stops ADD COLUMN geom geometry(Point, 3116);
UPDATE stops SET geom = ST_Transform(ST_SetSRID(ST_MakePoint(stop_lon, stop_lat), 4686),3116);

ALTER TABLE shapes ADD COLUMN geom geometry(Point, 3116);
UPDATE shapes SET geom = ST_Transform(ST_SetSRID(ST_MakePoint(shape_pt_lon, shape_pt_lat), 4686),3116);

CREATE TABLE rutas_SITP_GTFS AS SELECT shape.shape_id , ST_SetSRID(ST_MakeLine(shape.geom),3116) AS route FROM try_mmqgis_shapes_gtfs AS shape 
GROUP BY shape.shape_id;

CREATE TABLE rutas_SITP_GTFS_num_viajes AS SELECT shape.shape_id, COUNT(trips.shape_id) AS num_viajes, shape.route FROM rutas_sitp_gtfs AS shape
INNER JOIN trips
ON shape.shape_id = trips.shape_id
GROUP BY shape.shape_id, shape.route;