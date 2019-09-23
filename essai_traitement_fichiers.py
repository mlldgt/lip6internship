# -*- coding: utf-8 -*-

import os
from datetime import datetime
import csv
import subprocess
from subprocess import PIPE

#https://codereview.stackexchange.com/questions/186699/using-os-scandir-to-get-all-txt-files-in-subfolders
dirpath="A:\Fichiers"
os.scandir(dirpath) #répertorie tous les fichiers/dossiers dans le dossier

#récursif pour examiner tous les dossiers jusqu'à ce qu'il n'y en ait plus
def get_file_from(path,csvfile,csvdir):
    for entry in os.scandir(path):
        if entry.is_file():
            name=entry.name
            path=entry.path
            datem=os.path.getmtime(os.path.join(dirpath, entry))
            datemodif=datetime.fromtimestamp(datem)
            with open(csvfile,"a",encoding="utf-8") as file:
                file.write('"' + path + '","' + name + '","' + str(datemodif) + '"\n')
            #print(name, path, datemodif,'\n')
            
        elif entry.is_dir():
            name=entry.name
            path=entry.path
            with open(csvdir,"a",encoding="utf-8") as file2:
                file2.write('"' + path + '","' + name + '"\n')
            get_file_from(entry.path,csvfile,csvdir)

get_file_from(dirpath,"csv_f_derrida.csv","csv_d_derrida.csv")

#compile files
with open("csv_derrida_files.csv","w",encoding="utf-8") as f2:
    f2.write('"id","path","nom","date_modification"\n')
    
with open("csv_f_derrida.csv","r",encoding="utf-8") as f:
    with open("csv_derrida_files.csv","a",encoding="utf-8") as f2:
        i=0
        line=f.readline()
        while line:
            i+=1
            f2.write('"f'+str(i) + '",' + line)
            line=f.readline()

"""#compile directories
with open("csv_derrida_dir.csv","w",encoding="utf-8") as f3:
    f3.write('"id","path","name"\n')
    
with open("csv_d_derrida.csv","r",encoding="utf-8") as f4:
    with open("csv_derrida_dir.csv","a",encoding="utf-8") as f3:
        i=0
        line=f4.readline()
        while line:
            i+=1
            f3.write('"d'+str(i) + '",' + line)
            line=f4.readline()"""

#constituer dir d'id des dossiers
dir_id={}
dir_id[0]=("d0","A:/Fichiers/")
i=0
with open("csv_derrida_dir.csv",newline='',encoding="utf-8") as directories:
    dirs=csv.reader(directories)
    for d in dirs:
        #print("DIRECTORY",d[1])
        i+=1
        dir_id[i]=(d[0],d[1]) #id, path
        
#faire correspondre path des dossiers entre eux pour savoir quels dossiers sont dans quels autres
"""with open("csv_derrida_dir.csv", "r",encoding="utf-8") as dirs:
    with open("csv_derrida_dir2.csv", "w", encoding="utf-8") as dirs2:
        dirs2.write('"id","path","name","dir_id"\n')
        line=dirs.readline()
        while line:
            line=line[:-2] #pour enlever le \n
            line_l=line.split('",')
            #print(line_l)
            path_d=line_l[1]
            name_d=line_l[2]
            path=path_d[1:-(len(name_d))] #pour enlever le / supplémentaire
            #print("PATH ", path)
            for elem in dir_id:
                values=dir_id.get(elem)
                if path==values[1]:
                    linew=line+'","'+values[0]+'"\n'
                    print(linew)
                    dirs2.write(linew)
            line=dirs.readline()"""


#faire correspondre path des fichiers et path des dossiers pour savoir dans quels dossiers sont les fichiers
with open("csv_derrida_files.csv","r",encoding="utf-8") as files:
    with open("csv_derrida_files2.csv","w",encoding="utf-8") as files2:
        files2.write('"id","path","name","date_modif","dir_id","key_MD5"\n')
        line=files.readline()
        i=0
        while line:
            i+=1
            line=line[:-2] #pour enlever le \n
            line_l=line.split('",')
            #print(line_l)
            path_f=line_l[1]
            name_f=line_l[2]
            path=path_f[1:-(len(name_f))] #pour enlever le / supplémentaire
            if i!=1: #pour éviter la première ligne
                #création du md5
                cmd='CertUtil -hashfile ' + str(path_f) + '" MD5'
                x=subprocess.run(cmd, stdout=PIPE).stdout
                out=str(x).split("\\r\\n")
                if out[1].startswith("CertUtil"):
                    print("problème certutil")
                    cmd2="D:/HashConsole/HashConsole.exe -f " + path_f + '"'
                    x2=subprocess.run(cmd2, stdout=PIPE).stdout
                    out2=str(x2).split("\\r\\n\\r\\n")
                    if len(out2) >= 14:
                        md5key=out2[14][-32:]
                        print("MD5 EXE")
                    else:
                        print("len out2 inf à 14")
                        md5key=""
                else:
                    md5key=out[1]
                #fin création md5
            for elem in dir_id:
                values=dir_id.get(elem)
                if path==values[1]:
                    linew=line+'","'+values[0]+ '","'+md5key+'"\n'
                    print(linew)
                    files2.write(linew)
            line=files.readline()
            
"""prendre le derrida_files2.csv et lire ligne par ligne (ajouter nom des colonnes dans la première ligne)
vérifier si le fichier de cette ligne a une correspondance dans les fichiers avec info supplémentaire
si oui, écrire les infos supplémentaires dans le fichier
si non, ajouter des colonnes vides"""