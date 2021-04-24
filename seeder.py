import requests
import json

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

def add_user(id_virtual_world,nombre):
    data = {"id_virtual_world":id_virtual_world,"nombre":nombre}
    response = requests.post('http://fastapi-testing1.herokuapp.com/users/create', headers=headers, data=data)

def add_project(name,description):
    data = {"title":name,"description":description}
    response = requests.post('http://fastapi-testing1.herokuapp.com/projects/create', headers=headers, data=json.dumps(data))

def add_attribute_template(name, slug, description):
    data = {"name":name,"slug":slug,"description":description}
    response = requests.post('http://fastapi-testing1.herokuapp.com/attribute_templates/create', headers=headers,  data=json.dumps(data))

def add_architecture_pattern(name,description):
    data = '{"title":"'+name+'","description":"'+description+'"}'
    response = requests.post('http://fastapi-testing1.herokuapp.com/patterns/create', headers=headers, data=data)

def add_attribute(attribute,project_id,text):
    params = (
        ('attribute_name', attribute),
        ('project_id',project_id),
        ('requirement_text', text),
    )
    response = requests.get('http://fastapi-testing1.herokuapp.com/projects/add_attribute', headers=headers, params=params)

def add_pattern(pattern_id, project_id):

    params = (
        ('pattern_id', pattern_id),
        ('project_id', project_id),
    )

    response = requests.get('http://fastapi-testing1.herokuapp.com/projects/add_pattern', headers=headers, params=params)

def seed():
    # Users
    users = ["joaco","galo","nico","palmi","mau"]

    print("Agregando usuarios...")
    count = 1
    for user in users_email:
        add_user(count,user)
        count=count+1
    
    # Attributes templates
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
    
    # Attributes
    attributes_data = [
        ("availability","Que este siempre disponible"),
        ("fault_tolerance","Que sea tolerante a fallos"),
        ("maintainability","Que sea facil de mantener"),
        ("performance","Que funcione rápido"),
        ("scalability","Que sea escalable"),
        ("security","Que sea seguro"),
        ("usability","Que sea facil de usar"),
        ("portability","Que funcione bien en muchas plataformas"),
        ("interoperability","Que sea facil de conectar con otros componentes")
    ]

    print("Agregando templates de atributos....")
    # Projects
    for name, slug, description in attributes_templates_data:
        add_attribute_template(name,slug,description)

    patterns_data = [
        ("Capas","La arquitectura de capas, permite la independizacion de cambios, el cambio de una capa no afecta a las demas, refleja claramente la estructura y niveles de cada componente y da la funcionalidad de poner usar en una capa lo que otra brinda."),
        ("Broker","La arquitectura broker permite cambios dinámicos, agregar, eliminar y reubicar los componentes, y hace que la distribución sea transparente para el desarrollador."),
        ("Model-View-Controller","La arquitectura model view controleer permite la separacion de datos, de su  representacion virtual, facilita el manejo de errores y aumenta la escabilidad. "),
        ("Cliente-Servidor","La arquitectura cliente-servidor permite gran escabilidad ya que cualquier elemento puede ser aumentado en cualquier momento, y ademas los cambios en los servidores no afectan a  los clientes. "),
        ("Peer to peer","La arquitectura peer to peer, permite la descentralizacion del sistema, es altamente seguro  ante la falla de cualquier nodo y altamente escalable en terminos de recursos. "),
        ("Pipes and filters","La arquitectura pipe and filter permite el procesamiento concurrente, el agreado de filtros al sistema se realiza facilmente y ademas son reutilizables para diferentes funciones, además se caracteriza por la eficiencia en el desarrollo de soluciones para aplicaciones que requieran trabajos de multitarea")
    ]

    print("Agregando patrones de arquitectura...")    
    for name, description in patterns_data:
        add_architecture_pattern(name,description)

    projects_data = [
        # Nombre             Descripcion                            # atributos                               #pattern
        ("Capas 1","Proyecto de prueba numero 1",                  [1,1,4,4,6,6,7,7]                             ,1),
        ("Capas 2","Proyecto de prueba numero 2",                  [1,1,1,1,4,4,4,4,6,6,6,6,7,7,7,7]             ,1),
        ("Capas 3","Proyecto de prueba numero 3",                  [1,1,1,1,1,1,1,4,4,6,6,6,7,7]                ,1),
        ("Broker 1","Proyecto de prueba numero 4",                 [4,4,6,6,7,7,8,8]                             ,2),
        ("Broker 2","Proyecto de prueba numero 5",                 [4,4,4,4,6,6,6,6,7,7,7,7,8,8,8,8]             ,2),
        ("Broker 3","Proyecto de prueba numero 6",                 [4,4,4,4,4,4,6,6,6,6,6,6,6,7,7,8,8,8,8]       ,2),
        ("Model-View-Controller","Proyecto de prueba numero 7",    [2,2,6,6]                                     ,3),
        ("Model-View-Controller","Proyecto de prueba numero 8",    [2,2,2,2,6,6,6,6]                             ,3),
        ("Model-View-Controller","Proyecto de prueba numero 9",    [2,2,2,2,2,2,2,2,6,6,6]                       ,3),
        ("Cliente Servidor 4","Proyecto de prueba numero 4",       [2,2,2,7]                                     ,4),
        ("Cliente Servidor 4.1","Proyecto de prueba numero 4.1",   [2,2,7,7]                                     ,4),
        ("Cliente Servidor 4.2","Proyecto de prueba numero 4.2",   [2,2,7,7,7]                                   ,4),
        ("Pipes and filters 5","Proyecto de prueba numero 5",      [2,2,2]                                       ,5),
        ("Pipes and filters 5.1","Proyecto de prueba numero 5.1",  [2]                                           ,5),
        ("Pipes and filters 5.2","Proyecto de prueba numero 5.2",  [2,2,2,2,2,2,2]                               ,5),
        ("Peer to Peer 6","Proyecto de prueba numero 6",           [0,0,0,7,8]                                   ,6),
        ("Peer to Peer 6.1","Proyecto de prueba numero 6.1",       [0,0,7,7,8,8]                                 ,6),
        ("Peer to Peer 6.2","Proyecto de prueba numero 6.2",       [0,7,7,7,8,8,8]                               ,6)
    ]

    print("Agregando proyectos con patrones y atributos...")
    for idx, p in enumerate(projects_data):
        name, description, attributes_id, pattern_id = p
        add_project(name,description)
        for attribute_id in attributes_id:
            attr_name, text = attributes_data[attribute_id]
            add_attribute(attr_name,idx+1,text)   
        add_pattern(pattern_id, idx+1)

    
if __name__=="__main__":
    # Correr con la base vacia!!!
    seed()