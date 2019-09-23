# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 11:50:33 2019

@author: malou
"""

#à modifier pour ne pas examiner les éléments qui ne sont pas dans le disque dur tout (mis à la fin du fichier all_info_compile.csv)

import datetime

def load_date(ch): #pour transformer les string en objets date
    chdate=""
    if len(ch)==19: #1996-03-07 09:32:42
        chdate=datetime.datetime.strptime(ch,'%Y-%m-%d %H:%M:%S')
    elif len(ch)==17: #1996-03-07  10:32
        chdate=datetime.datetime.strptime(ch,'%Y-%m-%d  %H:%M')
    return chdate

def year_test(date,yearmin,yearmax): #date, 1985, 2004 pour nous ; pour vérifier que la date est bien une date possible
    if date=="": #si la date est vide: on ne fait rien
        pass
    elif date.year==yearmax: #si la date est de 2004, année de la mort de Derrida
        if (date.month>=10 and date.day>=9):
            #print(date.month, date.day)
            #print("x")
            date="" #si la date est postérieure à la date de mort de Derrida (9 octobre 2004) : on supprime
        else:
            #print(date.month, date.day)
            #print("y", date)
            pass #si la date est antérieure à la date de mort de Derrida (9 octobre 2004) : ok
    elif yearmin <= date.year <= yearmax: #si la date est bien comprise entre les deux années données : on ne fait rien (on garde la date telle quelle)
        pass
    else: #si la date n'est PAS compris entre les deux années : on la supprime
        date=""
    return date

file=open(r"D:\stage_derrida\all_info_compile.csv","r",encoding="utf-8")
#0 = "id",1 = "path",2 = "name",3 = "date_modif",4 = "dir_id",5 = "key_MD5"
#3 = date_modif (files2.csv) 1996-03-07 09:32:42
#8 = create (fichiers contrôle) 1996-03-07  10:32
#9 = modify (fichiers contrôle) 1996-03-07  10:32
#13 = datemodif (images disque) 1996-03-07 11:32:41

#https://stackabuse.com/converting-strings-to-datetime-in-python/

with open(r"D:\stage_derrida\all_info_w_good_dates.csv","w",encoding="utf-8") as cible:
    cible.write('"id","path","name","dir_id","key_MD5","date_modif","date_modif_ctrl","date_modif_img_disque","date_creation_ctrl"\n')
    
cible=open(r"D:\stage_derrida\all_info_w_good_dates.csv","a",encoding="utf-8")


line=file.readline()
i=0
while line:
    i+=1
    #pour éviter les deux premières lignes qui sont seulement du texte
    if i==1 or i==2:
        pass
    else:
        row=line.split('","')
        #0 = "id",1 = "path",2 = "name",3 = "date_modif",4 = "dir_id",5 = "key_MD5"
        #3 = date_modif (files2.csv) 1996-03-07 09:32:42
        #8 = create (fichiers contrôle) 1996-03-07  10:32
        #9 = modify (fichiers contrôle) 1996-03-07  10:32
        #13 = datemodif (images disque) 1996-03-07 11:32:41
        
        otherinfo=row[0]+'","'+row[1]+'","'+row[2]+'","'+row[4]+'","'+row[5]+'","'
    
        #récupérer les dates dans chaque ligne et les transformer en objets date
        modif_files2=load_date(row[3])
        modif_ctrl=load_date(row[9])
        modif_img=load_date(row[13])
        create_ctrl=load_date(row[8])
        #print(modif_files2)
        
        dates=[modif_files2, modif_ctrl, modif_img]
        #print(dates)
        
        #vérifier que l'année est bien comprise entre 1985 et 2004 -> si non, ne pas prendre en compte
        #si la date n'existe pas, on la garde vide
        j=0
        for elem in dates:
            #print(type(elem), elem)
            if elem=="":
                pass
            else:
                dates[j]=year_test(elem,1985,2004) #on remplace l'élément dans la liste par le résultat du test
            j+=1
        #print(dates)
        #on le fait aussi pour la date de création supposée:
        create_ctrl=year_test(create_ctrl, 1985, 2004)
        #si la date de création respecte ces limites en principe elle ne pose pas de problème
        #mais si on s'aperçoit plus tard que certaines dates de création sont postérieures à la date de modif on pourra filtrer
        
        #comparer et vérifier que dates de modif identiques pour les jours + mois + année
        date=True
        #on récupère un date de référence
        ref=""
        x=0
        while ref=="":
            ref=dates[x]
            #print(ref)
            x+=1
            if x>2 : #si on a parcouru la liste mais que tout est vide
                break
        #on compare à la date de réf
        if ref=="":
            pass
        else:
            for elem in dates:
                if elem=="": #si élément vide
                    pass # on ne fait rien, on réutilisera réf ensuite pour indiquer la date de modif
                elif ref.day==elem.day and ref.month==elem.month and ref.year==elem.year: #si on a la même date (sans se préoccuper de l'heure : on gardera l'heure récupérée sur les fichiers qu'on a)
                    pass
                else: #si élément non vide et non identique à la réf
                    date=False #on signale qu'il y a des différences et on restituera la liste entière

        #on écrit dans le fichier cible ce qu'on a trouble
        cible.write(otherinfo)
        if date==True:
            cible.write(str(ref)+'","","",""\n')
        else: #si date == False
            cible.write(str(dates[0])+'","'+str(dates[1])+'","'+str(dates[2])+'","'+str(create_ctrl)+'"\n')
            
            
            
    
    line=file.readline()


#si les dates ne sont pas les mêmes : garder les deux/trois, les mettre dans leurs colonnes respectives
#si les heures ne sont pas les mêmes mais les dates si : garder l'heure inscrite dans files2.csv, correspondant à ce qui a été trouvé directement sur le fichier

file.close()
cible.close()