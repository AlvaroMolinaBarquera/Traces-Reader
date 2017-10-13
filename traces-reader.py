import xml.etree.ElementTree as ET
import json
from os import listdir
from os.path import isfile, join
import re
pattern = ''
ROOT_DIR = 'C:\\Users\\alvaro.barquera\\Desktop\\TracesReader\\traces\\'
DEST_FILE = 'C:\\Users\\alvaro.barquera\\Desktop\\TracesReader\\traces-output\\traces.txt'


# Lee cada archivo linea a linea y la somete a la expresión regular
# Que se ha introducido, luego en el archivo de destino introduce las lineas.
# Es importante que el encoding esté en UTF8
def readFile(file):
    linesToPrint = []
    with open(ROOT_DIR + file, 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            if re.search(pattern, line) is not None:
                linesToPrint.append(line)
    with open(DEST_FILE, 'a') as dest_file:
        for l in linesToPrint:
            dest_file.write(l)



pattern = input("Introduce la expresión regular a buscar: ")           
onlyfiles = [f for f in listdir(ROOT_DIR) if isfile(join(ROOT_DIR, f))]
# Si el directorio tiene algo más que archivo solo lee los archivos
for file in onlyfiles:
    readFile(file)
print('Busqueda finalizada, introduce una nueva busqueda o cierra la aplicación')


