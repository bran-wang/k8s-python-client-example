# -*- coding: utf-8 -*-
from jinja2 import Template, Environment, FileSystemLoader
import os, sys, yaml, copy, json, shutil

def dataPath(fileName):
    currentDir = os.path.dirname(__file__)
    parentDir = os.path.join(currentDir, "./")
    return os.path.join(parentDir, fileName)

def jinjaEnv(templates_path):
    env = Environment(
        loader=FileSystemLoader(templates_path),
        trim_blocks=True,
        lstrip_blocks=True
    )
    return env

def render(nfsServer, clusterName):
    isExists=os.path.exists(clusterName)
    if not isExists:
        os.makedirs(clusterName)
    else:
        print(clusterName + " is existing")
    templatesDir = dataPath("templates")
    env = jinjaEnv(templatesDir)
    items = os.listdir(templatesDir)
    for fileName in items:
       if fileName.startswith('.'):
           continue
       portion = os.path.splitext(fileName)
       newName = portion[0] + ".yaml"
       template = env.get_template(fileName)
       output = template.render(clusterName=clusterName, nfsServer=nfsServer)
       with open(newName, "w") as f:
          f.write(output)
          f.close()
       shutil.move(newName, clusterName)

if __name__ == "__main__":
    nfsServer='10.160.40.95'
    clusterName='testcluster'

    render(nfsServer, clusterName)

