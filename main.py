#!/bin/python3
from sys import stdin
import pickle
from datetime import date

#DEFAULT VALUES
database_name="db"
projects=[]
f=open(database_name,"r+")
projects=pickle.load(f)
f.close()


def database_load():
    pass
    #a=[["gcc","linux,programming"],[["12-07-2014",3],["12-06-2014",2]]]
    #b=[["vlan","network"],[["13-07-2014",3],["12-07-2014",1]]]
    #c=[["apache","linux"],[["11-07-2014",3],["12-08-2014",5]]]
    #projects=[a,b,c]
    

def project_list():
    for p in projects:
        #print("Project Name:")
        print(p[0][0])
        #print("Project total hour")
        #print(p[1])
        print(project_total_hours(p))
        print("")

def project_total_hours(p):
    total_hours=0
    for w in p[1]:
        total_hours=total_hours+int(w[1])
    return total_hours

def project_create():
    #print("What is project name\n")
    name=raw_input("What is project name\n")
    #print("Have any hours before\n")
    hours=raw_input("How many hours before\n")
    projects.append([[name],[[date.today(),hours]]])
    

def project_del():
    name=raw_input("What is project name\n")
    counter=0
    for p in projects:
        if(p[0][0]==name):
            projects.pop(counter)
            break
        
        counter=counter+1
        
    
def project_add_hours():
    name=raw_input("What is project name?\n")
    
    for p in projects:
        if(p[0][0] == name):
            hours=raw_input("How many hours\n")
            print(date.today())
            p[1].append([date.today(),hours])
       
            

database_load()

while(1):
    print("p Add Project")
    print("a Add Hours To Project")
    print("s Save")
    print("l List")
    print("q Quit")
    
    
    a=raw_input("")
    if a == "p":
        project_create()
    elif a=="a":
        project_add_hours()
    elif a=="l":
        project_list()
    elif a=="d":
        project_del()
    elif a=="s":
        f=open(database_name,"r+")
        pickle.dump(projects, f)
        f.close()
    else:
        print("Quitting")
        break

