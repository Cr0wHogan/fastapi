 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import collections
import nltk
from nltk.metrics.scores import precision, recall, f_measure
from random import shuffle
import pickle
import os
from datetime import datetime

pattern_classifier = None

"""
def dump_classifier(classifier,description=""):
    # Once created, it will dump the clasifier into a pickle.
    # Change the name to whatever you see fit
    name = 'classifier-%s.pickle' % datetime.now().strftime('%Y-%m-%d-%H-%M')
    f = open(name, 'wb')
    folder = os.path.join("utils","classifiers")
    pickle.dump(,classifier), f)
    f.close()    
    #dumps the descriptino in a txt file
    f_desc = open(name.replace("pickle","txt"),"w+")
    f_desc.write(description)
    f_desc.close()
"""

def get_features(project):
    # Loas tributos y su prioridad son las features
    attributes = {}
    for attr in project.attributes:
        attributes[attr.template.slug] =  attr.prioridad
    # {operability:5, mantainability:5,...}    
    # Guardo atributos a la izquierda y prediccion esperada a la derecha
    return attributes


def train(projects):
    global pattern_classifier
    # Extraigo las features de cada proyecto
    features = []
    for p in projects:       
        features.append((get_features(p),p.architecture_pattern.title))
    
    print(features)
    # Train and test sets
    limit = int(len(features)*0.9)
    training_set = features[:limit]
    testing_set = features[limit:]

    # Entrenar clasificador
    pattern_classifier = nltk.NaiveBayesClassifier.train(training_set)
    accuracy = nltk.classify.accuracy(pattern_classifier, testing_set)*100
    print("Precisión del clasificador estimada:"+str(accuracy))

def classify(project):
    if not pattern_classifier:
        print("NO HAY CLASIFICADOR CARGADO!")
        return None
    features = get_features(project)
    return pattern_classifier.classify(features)