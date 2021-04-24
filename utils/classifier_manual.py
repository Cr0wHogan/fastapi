import models, schemas

def similarity(attributes1,attributes2):
    matched = []
    score = 0
    for att1 in attributes1:
        found = False
        priority2 = 0
        for att2 in attributes2:
            if att2.template.slug == att1.template.slug:
                priority2 = att2.prioridad
                found = True    
                matched.append(att2.template.slug)    
                break

        if found:
            d = abs(priority2 - att1.prioridad)
            if d == 0:
                score += 1
            else:
                if d < 10:
                    score += 1*(1 - d/10)
        else:
            score -= 1

    for attribute in attributes2:
        if not attribute in matched:
            score -= 1

    return score

# 1 2 5    3 5 8

def classify(db, project):
    # Obtengo atributos
    project_attributes = project.attributes

    all_projects = db.query(models.Project).filter(models.Project.id != project.id).filter(models.Project.architecture_pattern != None).all()

    if not any(all_projects):
        return []

    # tuplas (distancia, proyecto) para cada proyecto
    similarities = [(similarity(p.attributes,project_attributes), p) for p in all_projects]
    # sort by distance
    similarities = sorted(similarities, key=lambda x: x[0],reverse=True)

    closest_sim = similarities[0][0]
    # if the distances between the architecture and the next is lower to this then they are close enough
    treshold = 1

    # Load all who are closer between than treshold
    closest = []
    for distance, project_to_compare in similarities:
        if abs(distance-closest_sim) < treshold:
            closest.append(project_to_compare.architecture_pattern.title)
    
    patterns_data = [      #NUEVO (AGREGAR RESPUESTAS PREDEFINIDAS DE SUGERENCIA)
        ("Capas",""),
        ("Broker",""),
        ("Model-View-Controller",""),
        ("Cliente-Servidor",""),
        ("Peer to peer",""),
        ("Pipes and filters","")
    ]
    for pattern in patterns_data:
        if pattern[0] == closest:
            print(pattern[1])

    return closest