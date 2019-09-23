# -*- coding: utf-8 -*-

##################### IMPORT

import os
from datetime import datetime
import subprocess
from subprocess import PIPE

##################### FUNCTIONS

#examine tous les dossiers contenus dans l'arborescence, compile les information des dossiers et fichiers dans les deux fichiers CSV indiqués en argument
def get_file_from(path,dicfile,dicdir):
    for entry in os.scandir(path): #pour chaque élément trouvé dans le dossier indiqué par le chemin "path"
        if entry.is_file(): #si c'est un fichier
            name=entry.name
            path=entry.path
            datem=os.path.getmtime(os.path.join(dirpath, entry))
            datemodif=datetime.fromtimestamp(datem)
            dicfile[path]=[name,datemodif]
            #print(name, path, datemodif,'\n')
            
        elif entry.is_dir(): #si c'est un dossier
            name=entry.name
            path=entry.path
            dicdir[path]=[name]
            get_file_from(entry.path,dicfile,dicdir)

##################### PROGRAM

#dirpath=input("Entrez le chemin du dossier à examiner : ")
dirpath="A:\Fichiers"

#https://codereview.stackexchange.com/questions/186699/using-os-scandir-to-get-all-txt-files-in-subfolders
#os.scandir(dirpath) #répertorie tous les fichiers/dossiers dans le dossier

dictfiles={}
dictdirs={}

get_file_from(dirpath,dictfiles,dictdirs)

i=0
for elem in dictfiles:
    i+=1
    identifiant="f"+str(i)
    dictfiles[elem].append(identifiant)

j=0
for elem in dictdirs:
    j+=1
    identifiant="d"+str(j)
    dictdirs[elem].append(identifiant)

#constituer dico recensant l'id des dossiers
dir_id={}
dir_id[0]=("d0","A:\\Fichiers\\")
i=0
for d in dictdirs:
    #print("DIRECTORY",d[1])
    i+=1
    dir_id[i]=(d[1],d[0]) #id, path
        
#faire correspondre chemins des dossiers entre eux pour savoir quels dossiers sont dans quels autres
with open("./derrida_dirs.csv", "w", encoding="utf-8") as dirs2:
    dirs2.write('"id","path","name","dir_id"\n')
    for elem in dictdirs:
        path_d=elem
        name_d=dictdirs[elem][1]
        id_d=dictdirs[elem][0]
        #print("PATH ", path)
        for elem2 in dir_id:
            values=dir_id.get(elem2)
            if path_d==values[1]:
                line='"'+id_d+'","'+path_d+'","'+name_d+'","'+values[0]+'"\n"'
                #print(linew)
                dirs2.write(line)


#faire correspondre chemin des fichiers et chemin des dossiers pour savoir dans quels dossiers sont les fichiers
#créer la clé MD5
with open("./derrida_files.csv","w",encoding="utf-8") as files2:
    files2.write('"id","path","name","date_modif","dir_id","key_MD5"\n')
    i=0
    for elem in dictfiles:
        i+=1
        path_f=elem
        name_f=dictfiles[elem][0]
        datemod=dictfiles[elem][1]
        id_f=dictfiles[elem][2]
        #création de la clé MD5
        cmd='CertUtil -hashfile ' + str(path_f) + '" MD5'
        x=subprocess.run(cmd, stdout=PIPE).stdout
        out=str(x).split("\\r\\n")
        if out[1].startswith("CertUtil"): #si la commande CertUtil n'a pas fonctionné correctement
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
        for elem2 in dir_id:
            values=dir_id.get(elem2)
            if path_f==values[1]:
                line='"'+id_f+'","'+elem+'","'+name_f+'","'+datemod+'","'+values[0]+ '","'+md5key+'"\n'
                print(line)
                files2.write(line)
