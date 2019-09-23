# -*- coding: utf-8 -*-

##################### IMPORT

import pickle

##################### FUNCTION

def pickle_open(source_file,cible_nom):
    source_loaded=open(source_file,"rb")
    source=pickle.load(source_loaded,encoding="utf-8")
    with open(cible_nom,"w",encoding="utf-8") as cible:
        cible.write('"path","name","date modif"\n')
        for entry in source:
            try:
                cible.write('"'+entry+'","'+source[entry][0]+'","'+source[entry][1]+'"\n')
            except UnicodeEncodeError:
                path=list(entry)
                name=list(source[entry][0])
                date=source[entry][1]
                cible.write('"')
                for char in path:
                    try:
                        cible.write(char)
                    except UnicodeEncodeError:
                        cible.write("ERROR")
                cible.write('","')
                for char in name:
                    try:
                        cible.write(char)
                    except UnicodeEncodeError:
                        cible.write("ERROR")
                cible.write('","'+date+'"\n"')

##################### PROGRAM                

pickle_open("./dicos_img_disque/files.pickle","./infos_img_disque/img_mac_derrida_files.csv")
pickle_open("./dicos_img_disque/dirs.pickle","./infos_img_disque/img_mac_derrida_dirs.csv")
pickle_open("./dicos_img_disque/files_syquest1.pickle","./infos_img_disque/img_syquest1_files.csv")
pickle_open("./dicos_img_disque/dirs_syquest1.pickle","./infos_img_disque/img_syquest1_dirs.csv")
pickle_open("./dicos_img_disque/files_syquest2.pickle","./infos_img_disque/img_syquest2_files.csv")
pickle_open("./dicos_img_disque/dirs_syquest2.pickle","./infos_img_disque/img_syquest2_dirs.csv")
pickle_open("./dicos_img_disque/files_scsi_b03b.pickle","./infos_img_disque/img_scsi_b03b_files.csv")