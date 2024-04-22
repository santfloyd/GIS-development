from xml.dom import minidom

domTree = minidom.parse("WitchFireResidenceDestroyed.xml")

print domTree.toxml()
