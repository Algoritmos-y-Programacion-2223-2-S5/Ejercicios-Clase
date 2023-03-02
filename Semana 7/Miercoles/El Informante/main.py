from seccion import Seccion
from empleado import Redactor, RedactorJefe
def main():
    section_list = []
    create_sections(section_list)
    writer_list = []
    writer_supervisor_list = []
    comercial_anouncement_list = []
    clasified_anouncement_list = []
    option = input("Please enter a option: 1- Crear seccion\n2- Crear redactor\n3- Crear Articulo\n4- Publicar Anuncio Comercial\n 5-Publicar Articulo Clasificado\n ->")
    if option == "1":
    if option == "2":
    if option == "3":
    if option == "4":
    if option == "5":
    else: 
        break
    

main()