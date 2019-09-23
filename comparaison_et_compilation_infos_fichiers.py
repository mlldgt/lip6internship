# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:38:21 2019

@author: malou
"""
#########################################################################################################
### comparaison des files path : lectures des fichiers, mettre tout dans un dictionnaire, comparaison ###
### des chemins récupérés dans les dictionnaires, retranscription dans le fichier de compilation où   ###
### on associe les comparaisons réussies, et on ajoutera à la fin les fichiers pour lesquels les comp ###
### n'ont rien donnée                                                                                 ###
#########################################################################################################

#####définition de fonction de remplacement des termes avec caractères spéciaux pour la comparaison
#comme tous les mots ont des codes hexa complètement différents même lorsqu'ils sont censé donner les mêmes caractères,
#on va devoir simplement lister tous les mots qui posent problème et les faire remplacer par le mot normal
#on regarde les fichiers répertoriés par problematic_names_detection.py
def err_remplace(ch):
    #ERROR : les infos récupérés sur les fichiers image généralement
    if "ERRORtERROR95" in ch:
        ch=ch.replace("ERRORtERROR95","Été95")
    if "ERRORtERROR" in ch:
        ch=ch.replace("ERRORtERROR","été")
    if "AcadERRORmie-Presse" in ch:
        ch=ch.replace("AcadERRORmie-Presse","Académie-Presse")
    if "After DarkERROR 3.0" in ch:
        ch=ch.replace("After DarkERROR 3.0","After Dark 3.0")
    if "BoERRORtes" in ch:
        ch=ch.replace("BoERRORtes","Boîtes")
    if "montERRORes" in ch:
        ch=ch.replace("montERRORes","montées")
    if "ModERRORle" in ch:
        ch=ch.replace("ModERRORle","Modèle")
    if "SystERRORme" in ch:
        ch=ch.replace("SystERRORme","Système")
    if "dERRORmarrage" in ch:
        ch=ch.replace("dERRORmarrage","démarrage")
    if "PrERRORfERRORrences" in ch:
        ch=ch.replace("PrERRORfERRORrences","Préférences")
    if "HerinERRORdits" in ch:
        ch=ch.replace("HerinERRORdits","Herinédits")
    if "HyperCardERROR Player" in ch:
        ch=ch.replace("HyperCardERROR Player","HyperCard Player")
    if "PERRORrimERROR" in ch:
        ch=ch.replace("PERRORrimERROR","Périmé")
    if "pERRORrimERROR" in ch:
        ch=ch.replace("pERRORrimERROR","périmé")
    if "RERRORserve" in ch:
        ch=ch.replace("RERRORserve","Réserve")
    if "RERRORSERVE" in ch:
        ch=ch.replace("RERRORSERVE","RESERVE")
    if "rERRORcent" in ch:
        ch=ch.replace("rERRORcent","récent")
    if "rERRORcente" in ch:
        ch=ch.replace("rERRORcente","récente")
    if "SERRORmin" in ch:
        ch=ch.replace("SERRORmin","Sémin")
    if "sERRORm-secret" in ch:
        ch=ch.replace("sERRORm-secret","sém-secret")
    if "guidERRORe" in ch:
        ch=ch.replace("guidERRORe","guidée")
    if "A la vie ERROR la mort" in ch:
        ch=ch.replace("A la vie ERROR la mort","A la vie à la mort")
    if "AnimalERRORvilac" in ch:
        ch=ch.replace("AnimalERRORvilac","Animalévilac")
    if "TERROR" in ch: #Té, Tém, Témo...
        ch=ch.replace("TERROR","Té")
    if "BERRORte" in ch:
        ch=ch.replace("BERRORte","Bte")
    if "bERRORte" in ch:
        ch=ch.replace("bERRORte","bte")
    if "non-publiERRORs" in ch:
        ch=ch.replace("non-publiERRORs","non-publiés")
    if "rangERRORs" in ch:
        ch=ch.replace("rangERRORs","rangés")
    if "fERRORvrier" in ch:
        ch=ch.replace("fERRORvrier","février")
    if "20 fERRORv" in ch:
        ch=ch.replace("20 fERRORv","20 fév")
    if "SERRORlecteur" in ch:
        ch=ch.replace("SERRORlecteur","Sélecteur")
    if "En-tERRORte" in ch:
        ch=ch.replace("En-tERRORte","En-tête")
    if "tERRORlERRORcopie" in ch:
        ch=ch.replace("tERRORlERRORcopie","télécopie")
    if "DonnERRORes" in ch:
        ch=ch.replace("DonnERRORes","Données")
    if "donnERRORes" in ch:
        ch=ch.replace("donnERRORes","données")
    if "RERRORponse" in ch:
        ch=ch.replace("RERRORponse","Réponse")
    if "rERRORsultat" in ch:
        ch=ch.replace("rERRORsultat","résultat")
    if "EncadrERROR" in ch:
        ch=ch.replace("EncadrERROR","Encadré")
    if "FranERRORais" in ch:
        ch=ch.replace("FranERRORais","Français")
    if "CERRORsure" in ch:
        ch=ch.replace("CERRORsure","Césure")
    if "rERRORseau" in ch:
        ch=ch.replace("rERRORseau","réseau")
    if "RERRORseau" in ch:
        ch=ch.replace("RERRORseau","Réseau")
    if "CinERRORma" in ch:
        ch=ch.replace("CinERRORma","Cinéma")
    if "jusqu'ERROR" in ch:
        ch=ch.replace("jusqu'ERROR","jusqu'à")
    if "EnchaERRORnERROR" in ch:
        ch=ch.replace("EnchaERRORnERROR","Enchaîné")
    if "MERRORtamorphose" in ch:
        ch=ch.replace("MERRORtamorphose","Métamorphose")
    if "SphERRORre" in ch:
        ch=ch.replace("SphERRORre","Sphère")
    if "ContrERRORle" in ch:
        ch=ch.replace("ContrERRORle","Contrôle")
    if "DERRORmarrage" in ch:
        ch=ch.replace("DERRORmarrage","Démarrage")
    if "GERRORnERRORral" in ch:
        ch=ch.replace("GERRORnERRORral","Général")
    if "MERRORmoire" in ch:
        ch=ch.replace("MERRORmoire","Mémoire")
    if "accERRORs" in ch:
        ch=ch.replace("accERRORs","accès")
    if "PlanisphERRORre" in ch:
        ch=ch.replace("PlanisphERRORre","Planisphère")
    if "PrERRORsentation" in ch:
        ch=ch.replace("PrERRORsentation","Présentation")
    if "RERRORglages" in ch:
        ch=ch.replace("RERRORglages","Réglages")
    if "2ERRORme" in ch:
        ch=ch.replace("2ERRORme","2ème")
    if "antERRORrieur" in ch:
        ch=ch.replace("antERRORrieur","antérieur")
    if "tERRORlecom" in ch:
        ch=ch.replace("tERRORlecom","télécom")
    if "matiERRORres" in ch:
        ch=ch.replace("matiERRORres","matières")
    if "NAVERROR 7.0 QuickScan" in ch:
        ch=ch.replace("NAVERROR 7.0 QuickScan","NEV 7.0 QuickScan")
    if "ParERROR 97-98" in ch:
        ch=ch.replace("ParERROR 97-98","Par 97-98")
    if "AdERRORle" in ch:
        ch=ch.replace("AdERRORle","Adèle")
    if "GrERRORce" in ch:
        ch=ch.replace("GrERRORce","Grèce")
    if "BensaERRORd" in ch:
        ch=ch.replace("BensaERRORd","Bensaïd")
    if "LERRORvinas" in ch:
        ch=ch.replace("LERRORvinas","Lévinas")
    if "PriERRORre d'insERRORrer" in ch:
        ch=ch.replace("PriERRORre d'insERRORrer","Prière d'insérer")
    if "AERRORm" in ch:
        ch=ch.replace("AERRORm","Aïm")
    if "LittERRORraire" in ch:
        ch=ch.replace("LittERRORraire","Littéraire")
    if "littERRORrature" in ch:
        ch=ch.replace("littERRORrature","littérature")
    if "TrERRORlisabeth" in ch:
        ch=ch.replace("TrERRORlisabeth","Trélisabeth")
    if "RanciERRORre" in ch:
        ch=ch.replace("RanciERRORre","Rancière")
    if "ClichERRORs" in ch:
        ch=ch.replace("ClichERRORs","Clichés")
    if "Contre-allERRORe" in ch:
        ch=ch.replace("Contre-allERRORe","Contre-allée")
    if "MERRORller" in ch:
        ch=ch.replace("MERRORller","Müller")
    if "GalilERRORe" in ch:
        ch=ch.replace("GalilERRORe","Gallilée")
    if "Livre ERROR venir" in ch:
        ch=ch.replace("Livre ERROR venir","Livre à venir")
    if "MichaERRORl" in ch:
        ch=ch.replace("MichaERRORl","Michaël")
    if "TolERRORrance" in ch:
        ch=ch.replace("TolERRORrance","Tolérance")
    if "CERRORcile" in ch:
        ch=ch.replace("CERRORcile","Cécile")
    if "CroisERRORes" in ch:
        ch=ch.replace("CroisERRORes","Croisée")
    if "mERRORme" in ch:
        ch=ch.replace("mERRORme","même")
    if "ProcERRORs" in ch:
        ch=ch.replace("ProcERRORs","Procès")
    if "invitERRORs" in ch:
        ch=ch.replace("invitERRORs","invités")
    if "AthERRORnes" in ch:
        ch=ch.replace("AthERRORnes","Athènes")
    if "J'ERRORcris" in ch:
        ch=ch.replace("J'ERRORcris","J'écris")
    if "pitalitERROR" in ch:
        ch=ch.replace("pitalitERROR","pitalité")
    if "dERRORcembre" in ch:
        ch=ch.replace("dERRORcembre","décembre")
    if "secrERRORtar" in ch:
        ch=ch.replace("secrERRORtar","secrétar")
    if "SecrERRORtar" in ch:
        ch=ch.replace("SecrERRORtar","Secrétari")
    if "LuminositERROR" in ch:
        ch=ch.replace("LuminositERROR","Luminosité")
    if "AmitiERROR" in ch:
        ch=ch.replace("AmitiERROR","Amitié")
    if "huitiERRORme" in ch:
        ch=ch.replace("huitiERRORme","huitième")
    if "SeptiERRORme" in ch:
        ch=ch.replace("SeptiERRORme","Septième")
    if "CaractERRORres" in ch:
        ch=ch.replace("CaractERRORres","Caractères")
    if "RERRORpondeur" in ch:
        ch=ch.replace("RERRORpondeur","Répondeur")
    if "MonDERRORbat" in ch:
        ch=ch.replace("MonDERRORbat","MonDébat")
    if "JERRORrusalem" in ch:
        ch=ch.replace("JERRORrusalem","Jérusalem")
    if "tERRORlecom" in ch:
        ch=ch.replace("tERRORlecom","télecom")
    if "ERROR soie" in ch:
        ch=ch.replace("ERROR soie","à soie")
    if "HumanitERRORs" in ch:
        ch=ch.replace("HumanitERRORs","Humanités")
    if "Driver d2ERROR" in ch:
        ch=ch.replace("Driver d2ERROR","Driver d2")
    if "ParERROR 97-98" in ch:
        ch=ch.replace("ParERROR 97-98","Par 97-98")
    #if "PrERRORfs. d'impression" in ch:
        #ch=ch.replace("PrERRORfs. d'impression","")
    if "Driver d2ERROR 4.5.4" in ch:
        ch=ch.replace("Driver d2ERROR 4.5.4","Driver d2")
    if "QuickTimeERROR" in ch:
        ch=ch.replace("QuickTimeERROR","QuickTime")
    if "FormatterOneERROR" in ch:
        ch=ch.replace("FormatterOneERROR","FormatterOne")
    if "HantaERROR" in ch:
        ch=ch.replace("HantaERROR","Hantaï")
    if "KERRORchihian" in ch:
        ch=ch.replace("KERRORchihian","Kéchihian")
    if "EHESSERRORlect" in ch:
        ch=ch.replace("EHESSERRORlect","EHESSélect")
    if "oudERRORe" in ch:
        ch=ch.replace("oudERRORe","oudée")
    if "SchERRORl" in ch:
        ch=ch.replace("SchERRORl","Schül")
    if "TrERRORzise" in ch:
        ch=ch.replace("TrERRORzise","Trézise")
    if "HampERROR" in ch:
        ch=ch.replace("HampERROR","Hampé")
    if "GaschERROR" in ch:
        ch=ch.replace("GaschERROR","Gasché")
    if "VERRORlissaris" in ch:
        ch=ch.replace("VERRORlissaris","Vélissaris")
    if "modif.antERRORr:relig." in ch:
        ch=ch.replace("modif.antERRORr:relig.","modif.antér:relig.")
    if "ADF 4ERRORdeC" in ch:
        ch=ch.replace("ADF 4ERRORdeC","ADF 4édeC")
    if "ADd'ERRORme" in ch:
        ch=ch.replace("ADd'ERRORme","ADd'âme")
    if "SAMERROR Intercept" in ch:
        ch=ch.replace("SAMERROR Intercept","SAMª Intercept")
    if "TrueTypeERROR" in ch:
        ch=ch.replace("TrueTypeERROR","TrueType")
    if "ServiERRORre" in ch:
        ch=ch.replace("ServiERRORre","Servière")
    if "RERRORpar" in ch:
        ch=ch.replace("RERRORpar","Répar")
    if "ElERRORv." in ch:
        ch=ch.replace("ElERRORv.","Elèv.")
    if "SignERROR" in ch:
        ch=ch.replace("SignERROR","Signé")
    #/media/veracrypt1/Images_Clones/IMG/scsi_b03b/ERRORERRORERROR*
    return ch

def comp_remplace(ch):
    #particuliers :
    #OpenFolderListDFï , doit être avant le ç plus loin car contient le caractère changée en ç si seul
    if "OpenFolderListDï" in ch:
        ch=ch.replace("OpenFolderListDï","OpenFolderListDF_")
    #Monde Diplï©, sans doute censé être Diplo mais fichiers avec lesquels on va comparer ont pour nom Monde Dipl donc on va juste supprimer
    if "Monde Diplï©" in ch:
        ch=ch.replace("Monde Diplï©","Monde Dipl")
    if "Driver d2â¢" in ch:
        ch=ch.replace("Driver d2â¢","Driver d2")
    if "QuickTimeâ¢" in ch:
        ch=ch.replace("QuickTimeâ¢","QuickTime")
    if "FormatterOneâ¢" in ch:
        ch=ch.replace("FormatterOneâ¢","FormatterOne")
    if "NAVâ¢ 7.0 QuickScan" in ch:
        ch=ch.replace("NAVâ¢ 7.0 QuickScan","Nav 7.0 QuickScan")
    #normalement devrait être transformé en "Bête" mais les fichiers avec lesquels la comparaison se fera sont appelés "Bte et Souverain," pas "Bête et Souverain"
    if "BÃªte" in ch: 
        ch=ch.replace("BÃªte","Bte")
    if "BÂte" in ch:
        ch=ch.replace("BÂte","Bte")
    if "Bte" in ch: #connor_files\root\BAS\Bte et Souverain (11)
        ch=ch.replace("Bte","Bte")
    ## connor_files\root\BAS\._La bte et le (4)(2
    if "bte" in ch: # à vérifier, possible que pour ceux-ci bête soit bien écrit
        ch=ch.replace("bte","bte")
    #les trois ont des char de contrôle on va juste les enlever
    if "ParÃ" in ch:
        ch=ch.replace("ParÃ","Par ")
    if "ParÑ " in ch:
        ch=ch.replace("ParÑ ","Par ")
    if "ParÃ " in ch:
        ch=ch.replace("ParÃ ","Par ")
    #les deux sont chelous mais il faut uniformiser : on choisi celui avec le moins de caractères
    if ".__SAMÂª" in ch:
        ch=ch.replace(".__SAMÂª",".__SAMª")
    #Réserve2000,
    if "RƒSERVE2000" in ch:
        ch=ch.replace("RƒSERVE2000","RESERVE2000")
    if "RÆSERVE2000" in ch:
        ch=ch.replace("RÆSERVE2000","RESERVE2000")
    #HyperCard Player, C:\french_data\syquest2\root\HyperCard¨ Player
    if "HyperCard¨ Player" in ch:
        ch=ch.replace("HyperCard¨ Player","HyperCard Player")
    if "HyperCardÂ¨ Player" in ch:
        ch=ch.replace("HyperCardÂ¨ Player","HyperCard Player")
    #Boîtes, \syquest2\LostDir_1c0\Bo”tes
    if "Bo”tes" in ch:
        ch=ch.replace("Bo”tes","Boîtes")
    if "BoÃ®tes" in ch:
        ch=ch.replace("BoÃ®tes","Boîtes")
    if "Boâtes" in ch:
        ch=ch.replace("Boâtes","Boites")
    #Bib IIIF-livr. sï¢JD
    if "Bib IIIF-livr. sï¢JD" in ch:
        ch=ch.replace("Bib IIIF-livr. sï¢JD","Bib IIIF-livr. s_JD")
    #complet2000ï¥
    if "complet2000ï¥" in ch:
        ch=ch.replace("complet2000ï¥","complet2000_")
    if "complet2000?" in ch:
        ch=ch.replace("complet2000?","complet2000_")
    #caractères
    #à
    if "Ã " in ch:
        ch=ch.replace("Ã ","à")
    if "Ë" in ch: #A:\Fichiers\syquest2_2018\root\RÅ½serve (deux)\Livre Ë venir
        ch=ch.replace("Ë","à")
    #ä  : connor_files\root\B2Seuil\recommandations\._SchŠl-
    if "Š" in ch:
        ch=ch.replace("Š","ä")
    #â : C:\french_data\syquest1\ADd'‰me
    if "‰" in ch:
        ch=ch.replace("‰","â")
    if "â°" in ch:
        ch=ch.replace("â°","â")
    #é : AnimalÃ©vilac
    if "Ž" in ch:
        ch=ch.replace("Ž","é")
    if "Ã©" in ch:
        ch=ch.replace("Ã©","é")
    if "Ã" in ch: #pas espace, caractère de contrôle "HTJ"
        ch=ch.replace("Ã","É")
    if "Å½" in ch:
        ch=ch.replace("Å½","é")
    #ê
    if "Ãª" in ch:
        ch=ch.replace("Ãª","ê")
    if "" in ch:
        ch=ch.replace("","ê")
    if "Â" in ch:
        ch=ch.replace("Â","ê")
    #è
    if "Â" in ch:
        ch=ch.replace("Â","è")
    if "" in ch:
        ch=ch.replace("","è")
    if "Ã©" in ch:
        ch=ch.replace("Ã©","é")
    if "Ã¨" in ch:
        ch=ch.replace("Ã¨","è")
    #ë
    if "â" in ch: #A:\Fichiers\syquest2_2018\root\RÅ½serve (deux)\._Michaâl L
        ch=ch.replace("â","ë")
    #ï
    if "Ã¯" in ch:
        ch=ch.replace("Ã¯","ï")
    if "â¢" in ch:
        ch=ch.replace("â¢","ï")
    if "•" in ch:
        ch=ch.replace("•","ï")
    #î
    if "â" in ch: #A:\Fichiers\syquest2_2018\root\Dossier SystÂme\Tableaux de bord\After Dark Files\After Dark 3.0\Fondu EnchaânÅ½"
        ch=ch.replace("â","î")
    #ç
    if "" in ch:
        ch=ch.replace("","ç")
    if "•" in ch: #connor_files\root\B2Seuil\recommandations\._A•m
        ch=ch.replace("•","ï")
    #Heiï¢foe, DERRIDAï¢CAVADA, Quiï¢Quoi, Derridaï¢ITV, UCIï¢
    if "ï¢" in ch:
        ch=ch.replace("ï¢","&")
    #ü
    if "Ã¼" in ch:
        ch=ch.replace("Ã¼","ü")
    if "Ÿ" in ch:
        ch=ch.replace("Ÿ","ü")
    if "Å¸" in ch:
        ch=ch.replace("Å¸","ü")
    if "Ã¤" in ch:
        ch=ch.replace("Ã¤","ü")
    #û
    if "Ã»" in ch:
        ch=ch.replace("Ã»","û")
    #ï¨
    if "#ï¨" in ch:
        ch=ch.replace("#ï¨","")
    #ï©
    if "ï©" in ch:
        ch=ch.replace("ï©","")
    #_ : ï + ï¥
    #ï¥
    if "ï¥" in ch:
        ch=ch.replace("ï¥","_")
        #ï
    if "ï" in ch:
        ch=ch.replace("ï","_")
    #Âª
    if "Âª" in ch:
        ch=ch.replace("Âª","")
        

    #inconnus
       
    #Ã¨, ElÃ¨v. RTF
    #inutile de remplacer pour le moment, pas présent dans d'autres fichiers
    
    #Bibliographie âï¤ L'Herne, Bibliographie â_ L'Herne, Textes 2 â_JD
    #inutile de remplacer pour le moment, pas présent dans d'autres fichiers
    
    #â¦, DERRIDA UNE TRAâ¦N RELEV - copie
    #inutile de remplacer pour le moment, pas présent dans d'autres fichiers

    #d2Âª, A:\Fichiers\syquest2_2018\root\Driver d2Âª 4.5.4\Driver d2Âª
    #inutile de remplacer, mêmes caractères partout
    
    return ch

def slashreplace(ch): #pour avoir les mêmes slash lors de la comparaison
    if "/" in ch:
        ch=ch.replace("/","\\")
    return(ch)

#####ouverture des fichiers et récupération des info dans dictionnaires

#fichier avec tous les files
allfiles=open("D:/stage_derrida/csv_derrida_files2.csv","r",encoding="utf-8")
#"id","path","name","date_modif","dir_id","key_MD5"

#fichiers de contrôle
syq1_ctrl=open("D:/stage_derrida/fichiers_ctrl/syquest1_files_14.csv","r",encoding="ansi")
#"index","stat","size","full filename","filename","signature","extension","flags","verfy","frags","start_sect","incr_sect","dir sect","parent dir sect","dir offset","track","sector error","filter","create","modify","access","attribute","log time","stat_1","stat_2","MD5 hash","SHA 256 hash"
#prendre 3, 4, 18, 19, 25 : full filename, filename, create, modify, md5 hash
syq2_ctrl=open("D:/stage_derrida/fichiers_ctrl/syquest2_files_16.csv","r",encoding="ansi")
#"index","stat","size","full filename","filename","signature","extension","flags","verfy","frags","start_sect","incr_sect","dir sect","parent dir sect","dir offset","track","sector error","filter","create","modify","access","attribute","log time","stat_1","stat_2","MD5 hash","SHA 256 hash"
#prendre 3, 4, 18, 19, 25 : full filename, filename, create, modify, md5 hash
conner_ctrl=open("D:/stage_derrida/fichiers_ctrl/conner_files_9.csv","r",encoding="ansi")
#"index","stat","size","full filename","filename","signature","extension","flags","verfy","frags","start_sect","incr_sect","dir sect","parent dir sect","dir offset","track","sector error","filter","create","modify","access","attribute","log time","stat_1","stat_2","MD5 hash","SHA 256 hash"
#prendre 3, 4, 18, 19, 25 : full filename, filename, create, modify, md5 hash

allctrl={} #dico dans lequel on va mettre toutes les infos qu'on veut des fichiers de contrôle
listctrl=[conner_ctrl,syq2_ctrl,syq1_ctrl]
for elem in listctrl:
    #print(elem)
    line=elem.readline()
    while line:
        row=line.split('","')
        allctrl[slashreplace(row[3])]=[slashreplace(row[4]),slashreplace(row[18]),slashreplace(row[19]),slashreplace(row[25])] #full filename: filename, create, modify, md5 hash, 
        line=elem.readline()

#fichiers image disque
macderrida_dirs_img=open("D:/stage_derrida/infos_img_disque/img_mac_derrida_dirs.csv","r",encoding="utf-8")
#"path","name","date modif"
macderrida_files_img=open("D:/stage_derrida/infos_img_disque/img_mac_derrida_files.csv","r",encoding="utf-8")
#"path","name","date modif"
syq1_dirs_img=open("D:/stage_derrida/infos_img_disque/img_syquest1_dirs.csv","r",encoding="utf-8")
#"path","name","date modif"
syq1_files_img=open("D:/stage_derrida/infos_img_disque/img_syquest1_files.csv","r",encoding="utf-8")
#"path","name","date modif"
syq2_dirs_img=open("D:/stage_derrida/infos_img_disque/img_syquest2_dirs.csv","r",encoding="utf-8")
#"path","name","date modif"
syq2_files_img=open("D:/stage_derrida/infos_img_disque/img_syquest2_files.csv","r",encoding="utf-8")
#"path","name","date modif"
scsi_files_img=open("D:/stage_derrida/infos_img_disque/img_scsi_b03b_files.csv","r",encoding="utf-8")
#"path","name","date modif"

allimg={} #dico dans lequel on va mettre toutes les infos des fichiers images
listimg=[macderrida_dirs_img,macderrida_files_img,syq1_dirs_img,syq1_files_img,syq2_dirs_img,syq2_files_img,scsi_files_img]
for elem in listimg:
    #print(elem)
    line=elem.readline()
    i=0
    while line:
        i+=1
        row=line.split('","')
        try:
            allimg[slashreplace(row[0][1:])]=[slashreplace(row[1]),slashreplace(row[2][:-2])] #path: name, date modif, sans le premier " et le \n et le dernier "
        except IndexError:
            print(i)
        line=elem.readline()

######initiation et ouverture du fichier de compilation

with open("all_info_compile.csv","w",encoding="utf-8") as compfile:
    compfile.write('"csv_derrida_files2.csv","","","","","","fichier_contrôle","","","","","fichier_image_disque","",""\n')
    #6,5,3
    compfile.write('"id","path","name","date_modif","dir_id","key_MD5","full_filename","filename","create","modify","md5_hash","path","name","datemodif"\n')

compfile=open("all_info_compile.csv","a",encoding="utf-8")

######comparaison des chemins

#on va prendre allfiles comme base, càd les fichiers que l'on a sur le disque dur et dont on sait qu'ils sont bien là
#va poser problème si certaines des autres références ne recensent pas les mêmes fichiers : soit pas de trace du fichier examiné, soit trace de
#fichier que nous n'avons pas dans le disque dur. ceux-là seront compilés à la suite.
#+ problème des fichiers qui sont bien recensés mais pas dans le même dossier
line_all_files=allfiles.readline()
i=0
while line_all_files:
    i+=1
    print(i)
    if i==1:
        line_all_files=allfiles.readline()
    else:
        #on écrit les 6 premières colonnes de référence des fichiers qu'on a sur le DD : id, chemin, nom, date modif, dir id, clé hash md5
        compfile.write(line_all_files[:-1]+",") #on enlève le \n et on ajoute une virgule à la fin
        #on prépare pour la comparaison en splittant
        row=line_all_files[1:-2] #on enlève les " de début et fin + le \n
        row=row.split('","') #id, path, name, date_modif, dir_id, key_MD5"
        
        written="no" #variable pour vérifier s'il y a bien eu un élément trouvé ou non dans comp de fichiers de contrôle
        written2="no" #même chose dans comp de fichiers d'image
        

        #comparer chemin ctrl à chemin allfiles
        for elem1 in allctrl:  #structure de allctrl -> full filename: filename, create, modify, md5 hash
            elem1comp=elem1[15:] #on enlève C:\french_data\
            #print("elem1comp=",elem1comp)
            rowcomp=row[1][12:] #on enlève A:\Fichiers\
            #print("rowcomp=",rowcomp)
            #print("row1=",row[1])
            
            #comparer : si commencent avec syquest1_2018 & syquest1 puis réduire et comparer chemins
            if elem1comp.startswith("syquest1") and rowcomp.startswith("syquest1_2018"):
                elem1comp=elem1comp.replace("syquest1","")
                rowcomp=rowcomp.replace("syquest1_2018","")
            #comparer : si commencent avec syquest2_2018 & syquest2 puis réduire et comparer chemins
            elif elem1comp.startswith("syquest2") and rowcomp.startswith("syquest2_2018"):
                elem1comp=elem1comp.replace("syquest2","")
                rowcomp=rowcomp.replace("syquest2_2018","")
            #comparer: si commencent avec Conner_2018 et connor_files puis réduire et comparer chemin (fichier ctrl de conner 2018 est contrôle de fonnor files)
            elif elem1comp.startswith("connor_file") and rowcomp.startswith("Conner_2018"):
                elem1comp=elem1comp.replace("connor_files","")
                rowcomp=rowcomp.replace("Conner_2018","")
            #si aucun n'est vrai : on compare quand même au cas où mais en principe, pas d'équivalence. on continue :
            
            #comparaison des chemins : on va utiliser la fonction définie précédemment pour remplacer les possibles caractères spéciaux pour la comparaison
            if comp_remplace(rowcomp)==comp_remplace(elem1comp):
                written="yes" #on signale qu'un élément a bien été trouvé
                compfile.write('"'+elem1+'","'+allctrl[elem1][0]+'","'+allctrl[elem1][1]+'","'+allctrl[elem1][2]+'","'+allctrl[elem1][3]+'",')
                #print(elem1)
                #marquer l'élément comme pris en compte
                elem1bis="DONE"+elem1
                allctrl[elem1bis]=allctrl[elem1]
                del allctrl[elem1]
        
        if written=="no": #si aucun élément n'a été trouvé à la fin du for
            compfile.write('"","","","","",')

        
        #comparer chemin img à chemin allfiles
        #problème de syquest2 : root et LostDir pas dans l'image -> possible que ce soit une image des fichiers et dossiers dans root, donc pas une
        #image du disque complète ? essayer comparaison avec syquest2 entier et comparaison avec juste root
        #même chose pour syquest1
        for elem2 in allimg: #structure de allimg -> path: name, date modif
            elem2comp=elem2[36:] # on enlève /media/veracrypt1/Images_Clones/IMG/
            rowcomp=row[1][12:] #on enlève A:\Fichiers\
            #traiter les ERROR
            if "ERROR" in elem2comp:
                #print(elem2comp)
                elem2comp=err_remplace(elem2comp)
            #comparer : si commencent avec syquest1_2018 & syquest1 puis réduire puis comparer chemin
            if elem2comp.startswith("syquest1") and rowcomp.startswith(r"syquest1_2018\root"):
                elem2comp=elem2comp.replace("syquest1","")
                rowcomp=rowcomp.replace(r"syquest1_2018\root","")
                #print(rowcomp,"\n",elem2comp)
            #comparer : si commencent avec syquest2_2018 & syquest2 puis réduire puis comparer chemins
            elif elem2comp.startswith("syquest2") and rowcomp.startswith(r"syquest2_2018\root"):
                elem2comp=elem2comp.replace("syquest2","")
                rowcomp=rowcomp.replace(r"syquest2_2018\root","")
            #comparer : si commencent avec mac_derrida_1_2010 et M_conner puis réduire et comparer chemin (img appelée m_conner est img de mac_derrida)
            elif elem2comp.startswith("M_conner") and rowcomp.startswith("mac_derrida_1_2010"):
                elem2comp=elem2comp.replace("M_conner","")
                rowcomp=rowcomp.replace("mac_derrida_1_2010","")
            #comparaison des chemins
            if comp_remplace(rowcomp)==comp_remplace(elem2comp):
                written2="yes"
                compfile.write('"'+elem2+'","'+allimg[elem2][0]+'","'+allimg[elem2][1]+'"\n')
                #marquer l'élément comme pris en compte
                elem2bis="DONE"+elem2
                allimg[elem2bis]=allimg[elem2]
                del allimg[elem2]
        if written2=="no":
            compfile.write('"","",""\n')
    
        line_all_files=allfiles.readline() #on passe à la ligne suivante dans le fichiers allfiles

#une fois qu'on a fini de parcourir allfiles, on peut ajouter les éléments qu'il reste dans les dictionnaires
for elem1rem in allctrl:
    if elem1rem.startswith("DONE")==False:
        compfile.write('"","","","","","","'+elem1rem+'","'+allctrl[elem1rem][0]+'","'+allctrl[elem1rem][1]+'","'+allctrl[elem1rem][2]+'","'+allctrl[elem1rem][3]+'","","",""\n')

for elem2rem in allimg:
    if elem2rem.startswith("DONE")==False:
        compfile.write('"","","","","","","","","","","","'+elem2rem+'","'+allimg[elem2rem][0]+'","'+allimg[elem2rem][1]+'"\n')

compfile.close()
#une fois qu'on a fini de compiler : comparer les dates de modif/création lorsqu'il y en a plusieurs -> autre script