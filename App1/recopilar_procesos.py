import psutil
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom
from tkinter import messagebox
import os

catalogos_dir= os.path.join("C:/", "catalogos")
if not os.path.exists(catalogos_dir):
    os.makedirs(catalogos_dir)

lista_procesos = []
procss = []

def recopilar_procesos(id, nombre_catalogo, num_procesos, orden):
    if not str(num_procesos).isdigit() or int(num_procesos) < 1:
        messagebox.showerror("Error Cantidad Procesos", "El Numero de procesos no debe ser cero")
        return
    
    global lista_procesos
    global procss


    # Obtener la lista de procesos
    
    for proc in psutil.process_iter(["pid", "name", "username", "cpu_percent", "memory_info"]):
        try:
            pinfo = proc.as_dict(attrs=["pid", "name", "username", "cpu_percent", "memory_info"])

            if not pinfo["username"]:
                pinfo["username"] = "Local Service"

            username_so = "NT AUTHORITY\SYSTEM"
            if pinfo["username"] == username_so:
                pinfo["priority"] = 1
            else:
                pinfo["priority"] = 0

            lista_procesos.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    # Ordenar la lista de procesos
    if orden == "memoria":
        lista_procesos = sorted(lista_procesos, key=lambda p: p["memory_info"].rss, reverse=True)
    else:
        lista_procesos = sorted(lista_procesos, key=lambda p: p["cpu_percent"], reverse=True)
    
    # Limitar la lista de procesos al número solicitado
    lista_procesos = lista_procesos[:int(num_procesos)] 
    # Crear el elemento raíz del XML
    root = Element("procesos")
    root.append(Comment("Listado de procesos"))
    
    # Crear un elemento para cada proceso y agregarlo al XML
    for proceso in lista_procesos:
        elem_proceso = SubElement(root, "proceso")
        elem_pid = SubElement(elem_proceso, "pid")
        elem_pid.text = str(proceso["pid"])
        elem_nombre = SubElement(elem_proceso, "nombre")
        elem_nombre.text = proceso["name"]
        elem_descripcion = SubElement(elem_proceso, "descripcion")
        elem_descripcion.text = proceso["name"]
        elem_usuario = SubElement(elem_proceso, "usuario")
        elem_usuario.text = proceso["username"]
        elem_memoria = SubElement(elem_proceso, "memoria")
        elem_memoria.text = str(round(proceso["memory_info"].rss / (1024*1024), 2)) + " MB"
        elem_cpu = SubElement(elem_proceso, "cpu")
        elem_cpu.text = f"{proceso['cpu_percent']:.2f}"
        elem_prioridad = SubElement(elem_proceso, "prioridad")
        elem_prioridad.text = str(proceso["priority"])
    
    # Guardar el XML en un archivo con el nombre del archivo compuesto por el ID y el nombre del catálogo
    file_name = f"{nombre_catalogo}_{id}.xml"
    file_path = os.path.join(catalogos_dir, file_name)
    xml_string = tostring(root, encoding="unicode")
    xml_pretty = minidom.parseString(xml_string).toprettyxml(indent=" ")
    
    with open(file_path, "w") as f:
        f.write(xml_pretty)


    for p in lista_procesos:
        for key in p.keys():
            if key == "memory_info":
                p["memory_info"] = str(round(p["memory_info"].rss / (1024*1024), 2)) + " MB"
        procss.append(p)
        print(proc)