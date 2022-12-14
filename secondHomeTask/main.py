import sys

import requests
from graphviz import Digraph

def getDependencies(packageName,depth):
    if depth >= maxdepth:
        return
    url = "https://pypi.python.org/pypi/{}/json".format(packageName)
    try:
        r = requests.get(url)
        return r.json()["info"]["requires_dist"]
    except:
        print("Unexpected error on", packageName, ":", sys.exc_info()[0])
        return []



def drawDependenciesGraph(name, dependencies, depth):
    global dot
    for i in range(len(dependencies)):
        dependencies[i] = dependencies[i].split()[0]
    for dependency in dependencies:
        dot.edge(name, dependency)
        temp = getDependencies(dependency,depth+1)
        if temp:
            drawDependenciesGraph(dependency, temp, depth+1)
    print(dot.source)


startName = sys.argv[1]
maxdepth = 2
dot = Digraph()
dependencies = getDependencies(startName, 0)
#print(dependencies)
if dependencies:
    drawDependenciesGraph(startName, dependencies, 0)
else:
    print("No dependencies found for", startName)
dot.render('test-output/round-table.gv', view=True)

#requests is looking nice
#graphviz is looking not nice