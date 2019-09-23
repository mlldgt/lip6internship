# -*- coding: utf-8 -*-
import os

dirpath="A:/Fichiers"
entries={}

def get_dirs(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            path=entry.path
            name=entry.name
            entries[path]=[name]
            for elem in os.scandir(path):
                entries[path].append(str(elem)[9:-1]) #pour avoir seulement le nom et pas <DirEntry ... >
            get_dirs(path)

get_dirs(dirpath)
#chaque élément dans entries est : [chemin]: [nom du dossier, élément dans le dossier, élément, élément...]

#print(entries)

#comparer quels dossier ont le même nom et s'ils ont le même contenu
#en enlevant le nom, comparer le contenu des dossiers

entries2=entries.copy() #pour que la comparaison soit un peu plus claire

#comparaison contenu seulement
sim_cont={} #où on va mettre contenu : chemin, chemin, chemin...
for elem in entries:
    for elem2 in entries2:
        if entries[elem][1:]==entries2[elem2][1:]: #on élimine le premier élément qui est le nom du dossier
            #pour chaque dossier on parcourt la liste de tous les dossier et on compare le contenu
            if elem == elem2: #si c'est le même chemin
                pass
            else:
                key=" ; ".join(entries[elem][1:])
                #si contenu déjà vu
                if key in sim_cont:
                    if elem2 in sim_cont[key]:
                        pass
                    else:
                        sim_cont[key].append(elem2)
                #si première fois
                else:
                    sim_cont[key]=[elem, elem2]
#print(sim_cont)

with open("sim_cont.txt","w",encoding="utf-8") as file:
    for elem in sim_cont:
        file.write("\n"+"CONTENU : "+elem+ "\n"+"CHEMINS : "+"\n")
        for subelem in sim_cont[elem]:
            file.write("\t"+str(subelem)+"\n")

#comparaison par noms pour voir si contenus similaires ou non
sim_name={} #où on va mettre nom : contenu + chemin, contenu + chemin, contenu + chemin...
for elem in entries: #entries & entries 2 => chemin: nom dossier, élément dans dossier, élément dans dossier...
    for elem2 in entries2:
        if entries[elem][0]==entries2[elem2][0]: #si même nom
            name=entries[elem][0] #nom du dossier
            content=entries2[elem2][1:] #contenu du dossier
            if content==[]:
                content="[vide]"
            #print(content)
            #print(entries2[elem2])
            path=elem2 #chemin du dossier
            #print(elem2)
            contpath=[path,content] #chemin, contenu
            #print(contpath)
            if name in sim_name: #si le nom est déjà dans le dict
                if contpath in sim_name[name]: #si on a déjà le chemin + contenu
                    #print("x")
                    pass
                else:
                    sim_name[name].append(contpath)
            else: #si c'est la première fois qu'on rencontre le nom
                sim_name[name]=[contpath]

#print(sim_name)

with open("sim_name.txt","w",encoding="utf-8") as file:
    file.write("Il y a "+str(len(sim_name))+" noms de dossiers différents.")
    for nom in sim_name:
        #print(sim_name[nom],"\n")
        #print(len(sim_name[nom]))
        file.write("\n" + "NOM : " + nom + "\n")
        for subelem in sim_name[nom]:
            #print(nom,"SUBELEM",subelem)
            file.write("\t"+str(subelem[1])+"\t\t"+str(subelem[0])+"\n")
        #for subelem in sim_name[n]:
            #print(n, "TOUT",subelem,"\n\n")
            #print("CHEMIN",subelem[0],"\n\n")
            #print("CONTENU",subelem[1],"\n\n")
            #if len(subelem)=="[vide]":
                #file.write("\t"+str(subelem)+"\n")
            #else:
                #file.write("\t" + str(subelem[1]) + "\t" + str(subelem[0])+"\n")

nameslist=[]
sim_name2={} #on va mettre dedans tous les noms de dossier qui correspondent à plusieurs contenus différents
for nom in sim_name:
    if len(sim_name[nom]) <=1: #s'il n'y a qu'un seul élément : pas la peine de tester, forcément il n'y en aura pas un autre différent
        pass
    else:
        ref=sim_name[nom][0][1:]
        for elem in sim_name[nom]:
            #print(elem[1:])
            if elem[1:]==ref:
                pass
            else:
                nameslist.append(nom)

for name in nameslist:
    sim_name2[name]=sim_name.get(name)

with open("meme_nom_contenu_different.txt","w",encoding="utf-8") as file2:
    file2.write("Il y a "+str(len(sim_name2))+" noms de dossiers distincts correspondant à des contenus différents.")
    for nom in sim_name2:
        file2.write("\n" + "NOM : " + nom + "\n")
        for subelem in sim_name2[nom]:
            file2.write("\t"+str(subelem[1])+"\t\t"+str(subelem[0])+"\n")
            
with open("meme_nom_meme_contenu.txt","w",encoding="utf-8") as file3:
    i=0
    for nom in sim_name:
        if nom not in nameslist:
            file3.write("NOM : "+nom+"\n")
            if len(sim_name[nom])==1:
                file3.write("un seul élément"+"\n")
                file3.write("\t"+str(sim_name[nom][0])+"\n")
            else:
                for elem in sim_name[nom]:
                    file3.write("\t"+str(elem[1])+"\t\t"+str(elem[0])+"\n")