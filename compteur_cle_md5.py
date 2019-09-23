# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:01:12 2019

@author: malou
"""
from operator import itemgetter

dico={} #dictionnaire avec clé + file id + path + name
dico_name={} #dictionnaire avec juste clé + nom des fichiers correspondants : clé = nom, nom, nom
dico_key={} #dictionnaire avec les noms + clés des fichiers correspondants : nom = clé, clé, clé
nullkey={} #où on met les fichiers n'ayant pas de clé : on vérifie après le premier traitement que sa longueur est 0
errors=[] #où l'on met les infos des fichiers dont les noms ne passent pas comme clés dans dico_key

with open("D:/stage_derrida/csv_derrida_files2.csv","r",encoding="utf-8") as file:
    line=file.readline()
    i=0
    while line:
        i+=1
        if i==1:
            pass #passer première ligne des noms de colonnes
        else:
            #print(line)
            row=line.split('","')
            #print(row)
            key=str(row[5])[:-2]  #pour enlever le \n et le guillemet à la fin
            #print(key)
            fileid=row[0][1:]+", "+row[3]+", "+row[1]+", "+row[2] #file id, date modif, file path, file name
            filename=row[2] #file name only
            fileinfo=key+", "+row[3]+", "+row[0][1:]+", "+row[1] #clé md5, date modif, file id, file path
            name=str(row[2])
            #print(fileinfo)
            if key=='': #s'il n'y a pas de clé md5
                nullkey[i]=row[0]
            else:
                ############
                if key in dico: #s'il y a une clé md5, pour trier sur les clés
                    dico[key][0]+=1
                    dico[key].append(fileid)
                    #
                    dico_name[key][0]+=1
                    dico_name[key].append(filename)
                else:
                    dico[key]=[1,fileid]
                    dico_name[key]=[1,filename]
                ##################
                if name in dico_key: #si la clé est non nulle et si le nom est déjà une clé dans dico_key
                    dico_key[name][0]+=1
                    dico_key[name].append(fileinfo)
                else:
                    dico_key[name]=[1,fileinfo]
        line=file.readline()

f=open('resultats.txt','w',encoding='utf-8')
for elem in dico:
    if dico[elem][0] > 1:
        #print(elem, dico[elem])
        f.write(elem+", "+str(dico[elem])+"\n")
f.close()

f=open('resultats_noms.txt','w',encoding='utf-8')
for elem in dico_name:
    if dico_name[elem][0] > 1:
        f.write(elem+", "+str(dico_name[elem])+"\n")
f.close()

print(len(nullkey))
print(len(dico_key))
print(errors)
    
####### comparaison des fichiers selon les clés & les noms de fichiers associés aux clés

keyslist=[]

for k in dico_name:
    values=dico_name.get(k)
    values=values[1:]
    if len(values)==1: #s'il y a seulement un fichier, pas intéressant, on veut voir quelles clés ont plusieurs fichiers et quelles différences entre ces fichiers
        pass
    else:
        ref=values[0]
        for v in values:
            if v==ref:
                pass
            else:
                keyslist.append(k)

dico2={} #dictionnaire dans lequel on va mettre les clés correspondant à des fichiers de noms différents + lesdits fichiers

for key in keyslist:
    dico2[key]=dico.get(key)

print("il y a ", len(dico2), " clés correspondant à des fichiers de noms différents.")

#print(dico2)

f=open("cles_noms_fichiers_differents.txt","w",encoding="utf-8")
f.write("Le nombre de clés différentes avec plusieurs fichiers est de "+str(len(keyslist))+"."+"\n")
for elem in dico2:
    #print(elem)
    f.write(elem+"\n")
    #print(dico2[elem][1:])
    for subelem in dico2[elem][1:]:
        sub=subelem.split(',')
        #print(sub)
        f.write("\t"+sub[3]+"\t"+sub[1]+"\t"+sub[2]+"\n")
        #print(subelem[2])
f.close()

####### comparaison des fichiers selons les noms et les clés associées aux noms

nameslist=[]

for k in dico_key:
    values=dico_key.get(k)
    values2=values[1:]
    ref=values2[0]
    for v in values2:
        if v==ref:
            pass
        else:
            nameslist.append(k)

dico3={} #dict dans lequel on associe les noms ayant plusieurs clés leur correspondant à leurs infos

for name in nameslist:
    dico3[name]=dico_key.get(name)

f=open("noms_fichiers_et_fichiers_correspondants.txt","w",encoding="utf-8")
f.write("Le nombre de noms de fichiers différents trouvé est "+str(len(dico_key))+"."+"\n")
for name in dico_key:
    values=dico_key.get(name) #name: md5 key, date modif, file id, file path
    #print(name,values,"\n")
    f.write(name+"("+str(values[0])+")"+"\n")
    values=values[1:]
    values=sorted(values,key=itemgetter(0)) #trié par clé pour que les résultats soient rassemblés selon les clés
    for subelem in values:
        sub=subelem.split(",")
        f.write("\t"+sub[0]+"\t"+sub[1]+"\t"+sub[3]+"\t"+sub[2]+"\n")
f.close()

f=open("noms_fichiers_avec_plusieurs_cles.txt","w",encoding="utf-8")
f.write("Le nombre de noms de fichiers différents ET auxquels plusieurs clés MD5 correspondent est "+str(len(dico3))+"."+"\n")
for name in dico3:
    values=dico3.get(name)
    print(values)
    f.write(name+"("+str(values[0])+")"+"\n")
    values=values[1:]
    values=sorted(values,key=itemgetter(0)) #trié par clé pour que les résultats soient rassemblés selon les clés
    for subelem in values:
        sub=subelem.split(",")
        f.write("\t"+sub[0]+"\t"+sub[1]+"\t"+sub[3]+"\t"+sub[2]+"\n")
f.close()