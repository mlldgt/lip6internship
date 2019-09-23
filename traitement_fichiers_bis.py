# -*- coding: utf-8 -*-

##################### IMPORT

import os
from datetime import datetime
import pickle

##################### FUNCTIONS

#examine tous les dossiers contenus dans l'arborescence, compile les information des dossiers et fichiers dans les deux fichiers CSV indiqués en argument
def get_file_from(path,dicfile,dicdir):
    for entry in os.scandir(path): #pour chaque élément trouvé dans le dossier indiqué par le chemin "path"
        if entry.is_file(): #si c'est un fichier
            name=entry.name
            path=entry.path
            datem=os.path.getmtime(os.path.join(path, entry))
            datemodif=datetime.fromtimestamp(datem)
            dicfile[path]=[name,datemodif]
            #with open(csvfile,"a",encoding="utf-8") as file:
               # file.write('"' + path + '","' + name + '","' + str(datemodif) + '"\n')
            #print(name, path, datemodif,'\n')
            
        elif entry.is_dir(): #si c'est un dossier
            name=entry.name
            path=entry.path
            datem=os.path.getmtime(os.path.join(path, entry))
            datemodif=datetime.fromtimestamp(datem)
            dicdir[path]=[name,datem]
            
            #with open(csvdir,"a",encoding="utf-8") as file2:
                #file2.write('"' + path + '","' + name + '"\n')
            get_file_from(entry.path,dicfile,dicdir)

def in_pickle_dict(path,namepkdirs,namepkfiles):
    dictfiles={}
    dictdirs={}
    
    get_file_from(path,dictfiles,dictdirs)

    pickle.dump(dictdirs,namepkdirs)
    pickle.dump(dictfiles,namepkfiles)

##################### PROGRAM
    
listpaths=["./M_Conner","./syquest1","./syquest2","./scsi_b03b"]

for elem in listpaths:
    if elem=="./M_Conner":
        named="./dicos_img_disque/dirs_mac_derrida.pickle"
        namef="./dicos_img_disque/files_mac_derrida.pickle"
    else:
        named="./dicos_img_disque/dirs_"+elem+".pickle"
        namef="./dicos_img_disque/files_"+elem+".pickle"
    in_pickle_dict(elem,named,namef)