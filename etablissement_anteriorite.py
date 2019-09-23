# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 12:46:20 2019

@author: malou
"""

import datetime

def load_date(ch): #pour transformer les string en objets date
    chdate=""
    if len(ch)==19: #1996-03-07 09:32:42
        chdate=datetime.datetime.strptime(ch,'%Y-%m-%d %H:%M:%S')
    elif len(ch)==17: #1996-03-07  10:32
        chdate=datetime.datetime.strptime(ch,'%Y-%m-%d  %H:%M')
    return chdate

#pour comparer les dates et trier 
#utiliser les identifiants uniques ? 
#par ex colonne "antérieur à" dans laquelle on met tous les id des fichiers de même nom plus récents ?
#regarder les fichiers qui ont les mêmes noms, comparer leurs dates 
#-> s’il y en a qui n’ont pas de dates, comparer le contenu et classer avec fichiers qui ont le même contenu 
#-> si seuls à avoir ce contenu, regarder à la main pour voir si ça a l’air plus récent ou non ?
#établir antérieur à, contemporain ?

source=open("D:/stage_derrida/all_info_w_good_dates.csv","r",encoding="utf-8")

with open("D:/stage_derrida/all_info_w_chronology.csv","w",encoding="utf-8") as cible:
    cible.write('"id","path","name","dir_id","key_MD5","date_modif","anterieur_a","frere","jumeau"\n')

with open("D:/stage_derrida/chronologie_correspondance.csv","w",encoding="utf-8") as cible2:
    cible2.write('"id","anterieur_a","frere","jumeau"\n')
    
with open("D:/stage_derrida/md5_correspondance.csv","w",encoding="utf-8") as cible3:
    cible3.write('"md5","id","id2"\n')


#récupérer tous les infos dans un dict
#rassembler par noms
    #-> créer un dict à chaque nouveau nom ? ou alors écrire chaque groupe dans un nouveau fichier
    #mettre tous ces fichiers dans un dossier, puis parcourir le dossier et à chaque fichier lire toutes les lignes + comparer
    #et tout mettre dans le fichier cible ?
#comparer les fichiers dans chaque groupe -> date et contenu
    
cible=open("D:/stage_derrida/all_info_w_chronology.csv","a",encoding="utf-8")

cible2=open("D:/stage_derrida/chronologie_correspondance.csv","a",encoding="utf-8")

cible3=open("D:/stage_derrida/md5_correspondance.csv","a",encoding="utf-8")

dico_name={}

dico_md5={}

i=0

line=source.readline()
while line:
    #print(line)
    i+=1
    #print(i)
    row=line[1:-2].split('","')
    #print(row)
    idf=row[0]
    path=row[1]
    name=row[2]
    dir_id=row[3]
    md5=row[4]
    modif=row[5]
    modifctrl=row[6]
    modifimg=row[7]
    creat=row[8]
    
    if row[0].startswith('f'): #pour ne regarder que les lignes qui commencent avec un id de fichier type f1, f52, f368...
        
        #mettre dans dico_name en triant par nom : chaque clé est un nom unique
        if name in dico_name:
            dico_name[name].append([idf,md5,modif,path,dir_id])
        else:
            dico_name[name]=[[idf,md5,modif,path,dir_id]]
            
        if md5 in dico_md5:
            dico_md5[md5].append(idf)
        else:
            dico_md5[md5]=[idf]
    
    line=source.readline()

#print(len(dico_name))
#print(dico_md5)

for elem in dico_name:
    l=len(dico_name[elem])
    if l==1: #qu'un seul élément donc pas de chronologie à établir
        for sub in dico_name[elem]:
            sub.append("")
            sub.append("")
            sub.append("")
    else:
        #d'abord on récupère les dates
        dates=[]
        #on récupère aussi la correspondance dates / identifiant
        dateid={}
        #et la liste des identifiants
        ids=[]
        
        for subelem in dico_name[elem]:
            subelem[2]=load_date(subelem[2]) #on transforme la string en un objet date
            
            #récupération des identifiants
            ids.append(subelem[0])
            
            #récupération des dates
            if subelem[2] in dates:
                pass
            elif subelem[2]=="":
                pass
            else:
                dates.append(subelem[2])
            
            #correspondances dates/id
            if subelem[2] in dateid:
                dateid[subelem[2]].append(subelem[0])
            else:
                dateid[subelem[2]]=[subelem[0]]

        
        l2=len(dates)
        dates=sorted(dates)
        #print("DATES : ",dates)
        #print("IDS: ",ids)
        #on compare. cas de figure :
        #toutes les dates sont nulles donc aucune n'a été ajoutée à la liste dates
        if l2==0:
            #print(l2)
            ids3=ids.copy()
            for sub in dico_name[elem]:
                #print(ids3)
                #print("identifiant : ",sub[0])
                ids1=ids.remove(sub[0]) #on récupère tous les id et on enlève juste celui correspondant à l'élément sur lequel on travaille
                sub.append("")
                sub.append(ids1)
                sub.append("")
                ids3.remove(sub[0])
                for identifiant in ids3:
                    cible2.write('"'+sub[0]+'","","'+identifiant+'",""\n')
            #on ajoute tous les id des éléments partageant un nom à la colonne "frère"
        
        #il y a une seule date valide
        elif l2==1:
            #print(l2)
            ids3=ids.copy()
            ids4=[]
            for sub in dico_name[elem]:
                if sub[2]==dates[0]:
                    ids4.append(sub[0])
            for sub in dico_name[elem]:
                if sub[2]==dates[0]:
                    #print("date de l'elem", sub[2])
                    #print("id de l'elem", sub[0])
                    #récupérer l'ensemble des id correspondant à cette date
                    ids2=dateid[dates[0]].copy()
                    ids2.remove(sub[0])
                    sub.append("")
                    sub.append("")
                    sub.append(ids2) #on ajoute les identifiants correspondant à la même date dans la colonne "jumeau"
                    ids4.remove(sub[0])
                    for identifiant in ids4:
                        cible2.write('"'+sub[0]+'","","","'+identifiant+'"\n')
                        
                elif sub[2]=="":
                    ids1=ids.remove(sub[0]) #on récupère tous les id et on enlève juste celui correspondant à l'élément sur lequel on travaille
                    sub.append("")
                    sub.append(ids1) #on ajoute dans la colonne "frere"
                    sub.append("")
                    ids3.remove(sub[0])
                    for identifiant in ids3:
                        cible2.write('"'+sub[0]+'","","'+identifiant+'",""\n')
            
        #il y a deux ou plus dates valides
        else:
            #print(l2)
            ids3=ids.copy()
            for sub in dico_name[elem]:
                if sub[2]=="": #pour les éléments qui ont des dates vides
                    ids1=ids.remove(sub[0]) #on récupère tous les id et on enlève juste celui correspondant à l'élément sur lequel on travaille
                    sub.append("")
                    sub.append(ids1)
                    sub.append("")
                    ids3.remove(sub[0])
                    for identifiant in ids3:
                        cible2.write('"'+sub[0]+'","","'+identifiant+'",""\n')
                else: #pour les éléments qui ont des dates valides, sachant qu'il y a au moins 2 dates différentes
                    datesub=sub[2]
                    #print("date du sous élém", datesub)
                    #chercher l'index de la date dans dates
                    index1=dates.index(datesub)
                    index2=index1+1
                    if index2==l2: #si on se retrouve avec index out of range
                        sub.append("")
                        sub.append("")
                        sub.append("")
                    else:
                        datepost=dates[index2]
                        #récupérer les id correspondant à cette date postérieure
                        ids4=dateid[datepost].copy()
                        sub.append(ids4) #on ajoute les ids correspondant dans la colonne "anterieur a"
                        sub.append("")
                        sub.append("")
                        for identifiant in ids4:
                            cible2.write('"'+sub[0]+'","'+identifiant+'","",""\n')
        #print(dico_name[elem],"\n\n")
    
for elem in dico_name:
    for sub in dico_name[elem]:
        cible.write('"'+sub[0]+'","'+sub[3]+'","'+elem+'","'+sub[4]+'","'+sub[1]+'","'+str(sub[2])+'","'+str(sub[5])+'","'+str(sub[6])+'","'+str(sub[7])+'"\n')

cible.close()
cible2.close()
source.close()

j=0

#établissement des correspondances entre fichiers qui ont la même clé MD5
for elem in dico_md5:
    #s'il y a un seul identifiant
    if len(dico_md5[elem])==1:
        pass
    #s'il y en a plus d'un
    else:
        while len(dico_md5[elem]) > 1:
            j+=1
            index=len(dico_md5[elem])-1
            cible3.write('"'+elem+'","'+dico_md5[elem][0]+'","'+dico_md5[elem][index]+'"\n')
            dico_md5[elem].remove(dico_md5[elem][index])

#print(j)
cible3.close()
#print(dico_name)