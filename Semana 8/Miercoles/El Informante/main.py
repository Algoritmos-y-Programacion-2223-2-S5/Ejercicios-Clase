from seccion import Seccion
from empleado import Redactor, RedactorJefe
from articulo import Articulo
from anuncios import AnuncioComercial

def create_section(list_sections, name):
    list_sections.append(Seccion(name))
    print("Section created!")

def create_comercial_anouncement(comercial_anouncement_list,section_list):
    for index, section in enumerate(section_list):
        print(index,section.nombre)
    seccion = int(input("Please enter a section: "))
    comercial_anouncement_list.append(AnuncioComercial(input("Please enter the person name:"),input("Please enter the person id card:"),section_list[seccion],input("Please enter the anouncement title:"),input("Please enter the anouncement body:")))
    print("Anouncement created!")
    

def create_writer(section_list, name,idcard,option2,writer_list,writer_supervisor_list):
    for index, section in enumerate(section_list):
        print(index,section.nombre)
    seccion = int(input("Please enter a section: "))
    if option2 == "1":
        writer_supervisor_list.append(RedactorJefe(name,idcard,section_list[seccion]))
    else:
        writer_list.append(Redactor(name,idcard,section_list[seccion],[]))
    print("Writer created!")

def create_article(writer_list):
    for index, writer in enumerate(writer_list):
        print(index,writer.nombre, "in section",writer.seccion.nombre)
    escritor = int(input("Please enter a writer: "))
    writer_list[escritor].escribir_articulo()

def show_article(writer_list):
    for writer in writer_list:
        print(writer.nombre, "in section",writer.seccion.nombre, "have these articles")
        for article in writer.articulos:
            print(article.titulo)

def show_comercial_anouncement(comercial_anouncement_list):
    for anouncement in comercial_anouncement_list:
        print(anouncement.título, anouncement.cuerpo,"in section",anouncement.seccion.nombre)


def main():
    section_list = []
    writer_list = []
    writer_supervisor_list = []
    comercial_anouncement_list = []
    clasified_anouncement_list = []
    section_list.append(Seccion("Sports"))
    writer_list.append(Redactor("Antonio","5555",section_list[0],[]))
    while True:
        option = input("Please enter a option: \n1- Crear seccion\n2- Crear redactor\n3- Crear Articulo\n4- Publicar Anuncio Comercial\n5-Publicar Articulo Clasificado\n6-Mostrar Articulo\n7-Mostrar Anuncios activos\n8-Exit\n ->")
        if option == "1":
            create_section(section_list, input("Please enter a section name:"))
        elif option == "2":
            option2 = input("Select type: \n1-Supervisor\n2-Regular")
            create_writer(section_list, input("Please enter the writer name"),input("Please enter id Card"),option2,writer_list,writer_supervisor_list)
        elif option == "3":
            create_article(writer_list)
        elif option == "4":
            create_comercial_anouncement(comercial_anouncement_list,section_list)
        elif option == "5":
            pass
        elif option == "6":
            show_article(writer_list)
        elif option == "7":
            show_comercial_anouncement(comercial_anouncement_list)
        elif option == "8":
            break
        else: 
            print("Error")
    

main()