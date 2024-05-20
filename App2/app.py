import os
from flask import Flask, render_template, jsonify, request, url_for
import xml.etree.ElementTree as ET

app = Flask(__name__)


def rm_xml(xmls):
    carpeta_archivos = r'C:/catalogos'
    for i in obtener_archivos_xml(carpeta_archivos):
        os.remove(carpeta_archivos+"/"+i)


@app.route('/')
def index():
    carpeta_archivos = r'C:/catalogos'
    archivos_xml = obtener_archivos_xml(carpeta_archivos)
    return render_template('index.html', archivos_xml=archivos_xml)




@app.route('/<nombre_archivo>')
def obtener_contenido_xml(nombre_archivo):
    carpeta_archivos = r"C:/catalogos"
    ruta_archivo = os.path.join(carpeta_archivos, nombre_archivo)

    with open(ruta_archivo, 'r') as file:
        contenido = file.read()
    return jsonify({'contenido_xml': contenido})


def obtener_archivos_xml(carpeta):
    archivos_xml = []
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.xml'):
            archivos_xml.append(archivo)
    print(archivos_xml)
    return archivos_xml




@app.route('/simulator')
def count_characters():


    directory = r"C:/catalogos"
    descripcion_lengths = []
    xml_files = [f for f in os.listdir(directory) if f.endswith('.xml')]

    for xml_file in xml_files:
        xml_path = os.path.join(directory, xml_file)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        for elemento in root:
            descripcion_element = elemento.find('descripcion')
            if descripcion_element is not None and descripcion_element.text is not None:
                descripcion = descripcion_element.text
                descripcion_lengths.append(len(descripcion))
    return render_template('simulador.html', descripcion_lengths=descripcion_lengths)


@app.route('/remove')
def delete():
    
    rm_xml(obtener_archivos_xml)
    return "goku eta vaina e seria"


if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)
