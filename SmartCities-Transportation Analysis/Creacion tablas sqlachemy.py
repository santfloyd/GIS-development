# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:33:26 2019

@author: ASUS
"""


from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Float, Boolean, DateTime, insert




engine = create_engine('postgresql://postgres:POSTGRES@localhost:5432/postgres')
connection = engine.connect()
metadata = MetaData()
# Define a new table with a name, count, amount, and valid column: data
agency = Table('gtfs_bogota_agency', metadata,
             Column('agency_id',String(5),primary_key=True),
             Column('agency_name', String(50)),
             Column('agency_url', String(255)),
             Column('agency_timezone', String(50)),
             Column('agency_lang', String(50)),
             Column('agency_phone', String(50)),
             Column('agency_fare_url', String(50))
)

# Define a new table with a name, count, amount, and valid column: data
calendar = Table('gtfs_bogota_calendar', metadata,
             Column('service_id',String(5),primary_key=True),
             Column('monday', Boolean()),
             Column('tuesday', Boolean()),
             Column('wednesday', Boolean()),
             Column('thursday', Boolean()),
             Column('friday', Boolean()),
             Column('saturday', Boolean()),
             Column('sunday', Boolean()),
             Column('start_date', DateTime),
             Column('end_date', DateTime)
)
calendar_dates = Table('gtfs_bogota_calendar_dates', metadata,
             Column('service_id',String(5)),
             Column('date', DateTime),
             Column('exception_type', Boolean())
             
)
routes = Table('gtfs_bogota_routes', metadata,
             Column('route_id',String(50),primary_key=True),
             Column('agency_id', String(5)),
             Column('route_long_name', String(50)),
             Column('route_desc', String(250)),
             Column('route_short_name', String(50)),
             Column('route_type', String(5)),
             Column(',route_url', String(250)),
             Column('route_color', String(50)),
             Column('route_text_color', String(50))
)
shapes = Table('gtfs_bogota_shapes', metadata,
             Column('shape_id',String(250),primary_key=True),
             Column('shape_pt_lat', Float()),
             Column('shape_pt_lon', Float()),
             Column('shape_pt_sequence', Integer())
)
stop_times = Table('gtfs_bogota_stop_times', metadata,
             Column('trip_id',String(50)),
             Column('arrival_time', DateTime),
             Column('departure_time', DateTime),
             Column('stop_id', String(250)),
             Column('stop_sequence', Integer()),
             Column('stop_headsign', String(50))
)

stops = Table('gtfs_bogota_stops', metadata,
             Column('stop_id',String(250),primary_key=True),
             Column('stop_code', String(250)),
             Column('stop_name', String(250)),
             Column('stop_desc', String(250)),
             Column('stop_lat', Float()),
             Column('stop_lon', Float()),
             Column('stop_url', String(50)),
             Column('wheelchair_boarding', String(5))
)

trips = Table('gtfs_bogota_trips', metadata,
             Column('route_id',String(250)),
             Column('service_id', String(5)),
             Column('trip_id', String(250),primary_key=True),
             Column('trip_headsign', String(250)),
             Column('shape_id', String(250)),
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print table details
print(repr(agency))

