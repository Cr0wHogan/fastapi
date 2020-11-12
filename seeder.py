import requests
import json

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

def add_user(email):
    data = '{"email":"'+email+'"}'
    response = requests.post('http://fastapi-training1.herokuapp.com/users/create', headers=headers, data=data)

def add_project(name,description):
    data = {"title":name,"description":description}
    response = requests.post('http://fastapi-training1.herokuapp.com/projects/create', headers=headers, data=json.dumps(data))

def add_attribute_template(name, slug, description):
    data = {"name":name,"slug":slug,"description":description}
    response = requests.post('http://fastapi-training1.herokuapp.com/attribute_templates/create', headers=headers,  data=json.dumps(data))

def add_architecture_pattern(name,description):
    data = '{"title":"'+name+'","description":"'+description+'"}'
    response = requests.post('http://fastapi-training1.herokuapp.com/patterns/create', headers=headers, data=data)

def seed():
    # Data
    users_email = ["joacosaralegui@gmail.com","galopiancola@gmail.com","nicoerrea@gmail.com","palmibenavente@hotmail.com","mandres10@yahoo.com.ar"]

    for email in users_email:
        add_user(email)
    
    projects_data = [
        ("Proyecto 1","Proyecto de prueba numero 1"),
        ("Proyecto 2","Proyecto de prueba numero 2"),
        ("Proyecto 3","Proyecto de prueba numero 3")
    ]

    for name,description in projects_data:
        add_project(name,description)

    attributes_templates_data = [
        ("Disponibilidad","availability","Hace referencia a la probabilidad de que un artículo funcione satisfactoriamente en un momento dado cuando se utilice en condiciones indicadas en un entorno de soporte ideal."),
        ("Tolerancia a fallos","fault_tolerance","La tolerancia a fallos es la propiedad que le permite a un sistema seguir funcionando correctamente en caso de fallo de uno o varios de sus componentes. Si disminuye su calidad de funcionamiento, la disminución es proporcional a la gravedad de la avería, en comparación con un sistema diseñado ingenuamente de forma que hasta un pequeño fallo puede causar el colapso total del sistema. Tolerancia a fallos es particularmente buscado en sistemas de alta disponibilidad."),
        ("Mantenibilidad","maintainability","la capacidad de mantenimiento es la facilidad con la que se puede mantener un producto para: corregir defectos o su causa, reparar o reemplazar componentes defectuosos o desgastados sin tener que reemplazar piezas de trabajo, evitar condiciones de trabajo inesperadas, maximizar la vida útil de un producto, maximizar la eficiencia, fiabilidad y seguridad, cumplir con los nuevos requisitos, facilitar el mantenimiento futuro, o hacer frente a un entorno cambiado."),
        ("Rendimiento","performance","La capacidad del sistema de resolver las tareas necesarias en los tiempos que requiere el problema y están dentro de los límites establecidos por las restricciones del problema."),
        ("Escalabilidad","scalability","La escalabilidad es propiedad de un sistema para manejar una cantidad creciente de trabajo agregando recursos al sistema"),
        ("Seguridad","security","La seguridad es el estado de ser 'seguro', la condición de estar protegido de daños u otros resultados no deseables. La seguridad también puede referirse al control de los peligros reconocidos para lograr un nivel aceptable de riesgo."),
        ("Usabilidad","usability","La usabilidad se puede describir como la capacidad de un sistema para proporcionar una condición para que sus usuarios realicen las tareas de forma segura, eficaz y eficiente mientras disfrutan de la experiencia"),
        ("Portabilidad","portability","La portabilidad en la programación informática de alto nivel es la usabilidad del mismo software en diferentes entornos. El requisito previo para la portabilidad es la abstracción generalizada entre la lógica de la aplicación y las interfaces del sistema. Cuando se produce software con la misma funcionalidad para varias plataformas informáticas,la portabilidad es el problema clave para la reducción de costos de desarrollo."),
        ("Interoperabilidad","interoperability","La interoperabilidad es una característica de un producto o sistema, cuyas interfaces se entienden completamente, para trabajar con otros productos o sistemas, en el presente o en el futuro, ya sea en la implementación o el acceso, sin ninguna restricción.")
    ]
    
    for name, slug, description in attributes_templates_data:
        add_attribute_template(name,slug,description)

    patterns_data = [
        ("Capas",""),
        ("Broker",""),
        ("Model-View-Controller",""),
        ("Cliente-Servidor",""),
        ("Peer to peer",""),
        ("Pipes and filters","")
    ]

    for name, description in patterns_data:
        add_architecture_pattern(name,description)

    
if __name__=="__main__":
    seed()