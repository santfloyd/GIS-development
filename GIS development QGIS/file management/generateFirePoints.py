#!/Python26/ArcGIS10.0/python
import  sys, string

## HTTP Content Type
contentType = "Content-Type: application/vnd.google-earth.kml+xml\n"

## KML Header
kmlHeader = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<kml xmlns=\"http://earth.google.com/kml/2.1\">\n"

## KML Body
kmlBody = (
    "<Folder>\n"
    "<Style id=\"fireIcon\">\n"
    "<IconStyle>\n"
    "<Icon>\n"
    "<href>http://maps.google.com/mapfiles/kml/shapes/firedept.png</href>\n"
    "</Icon>\n"
    "</IconStyle>\n"
    "</Style>\n"
    )

## KML Footer
kmlFooter = "</Folder>\n</kml>"

## open the file
f = open('N_America.A2007275.txt','r')

## read the list of fires into a list
lstFires = f.readlines()
cntr = 1
## loop through the list of fires, pull out coordinates, and generate KML
for fire in lstFires:
    lstValues = fire.split(",")
    latitude = float(lstValues[0])
    longitude = float(lstValues[1])
    confid = int(lstValues[8])
    kml = (
        "<Placemark>\n"
        "<name>Wildland Fire</name>\n"
        "<styleUrl>#fireIcon</styleUrl>\n"
        "<description>Confidence Value: %i</description>\n"
        "<Point>\n"
        "<coordinates>%f,%f</coordinates>\n"
        "</Point>\n"
        "</Placemark>\n"
        ) %(confid,longitude,latitude)
    
    kmlBody = kmlBody + kml

kmlOutput = kmlHeader + kmlBody + kmlFooter

## close the file
f.close()

print contentType
print kmlOutput


