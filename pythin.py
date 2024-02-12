import xml.etree.ElementTree as ET
from openpyxl import Workbook

# XML-Datei laden
xml_datei = 'FL_992907445A_X200_TESTSWLENKUNG_V001_E.odx'
tree = ET.parse(xml_datei)
root = tree.getroot()

# Name des XML-Elements, das abgefragt werden soll
ziel_element_name = 'ENCRYPT-COMPRESS-METHOD'

# Excel-Datei erstellen
excel_datei = 'ergebnisse.xlsx'
wb = Workbook()
ws = wb.active

# Überschriften für Excel-Tabelle setzen
ws.append(['Element Name', 'Element Wert'])

# Funktion zum Durchlaufen der XML-Daten und Schreiben in Excel
def durchlaufen_xml(element=root):
    for child in element:
        if child.tag == ziel_element_name:
            ws.append([child.tag, child.text])
        durchlaufen_xml(child)

# XML durchlaufen und Daten in Excel schreiben
durchlaufen_xml()

# Excel-Datei speichern
wb.save(filename=excel_datei)
