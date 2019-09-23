# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:45:40 2019

@author: malou
"""

import re

#détection des titres avec caractères problématiques
filesutf8=["D:/stage_derrida/csv_derrida_files2.csv",
       "D:/stage_derrida/infos_img_disque/img_mac_derrida_dirs.csv",
       "D:/stage_derrida/infos_img_disque/img_mac_derrida_files.csv",
       "D:/stage_derrida/infos_img_disque/img_syquest1_dirs.csv",
       "D:/stage_derrida/infos_img_disque/img_syquest1_files.csv",
       "D:/stage_derrida/infos_img_disque/img_syquest2_dirs.csv",
       "D:/stage_derrida/infos_img_disque/img_syquest2_files.csv",
       "D:/stage_derrida/infos_img_disque/img_scsi_b03b_files.csv"]

filesansi=["D:/stage_derrida/fichiers_ctrl/syquest1_files_14.csv",
       "D:/stage_derrida/fichiers_ctrl/syquest2_files_16.csv",
       "D:/stage_derrida/fichiers_ctrl/conner_files_9.csv"]


with open("D:/stage_derrida/all_problematic_names.csv","w",encoding="utf-8") as out:
    out.write('"file","fileinfos"\n')
    

out=open("D:/stage_derrida/all_problematic_names.csv","a",encoding="utf-8")


nonalphnum=re.compile('[^a-zA-Z0-9\s\:\\\_\(\)\,\+\.\'-]') #on cherche ce qui n'est pas dans la regex

"""exp ="A:\Fichiers\Zip_100_983A_2017\Zip 100\HERNE\Textes L'Herne 3\HAMACHER"

if re.search(nonalphnum, exp) == None:
    pass
else:
    print(re.search(nonalphnum, exp))
    print(exp)"""

def prob_comp(listfiles,encode):
    for file in listfiles:
        #print(file)
        f=open(file,"r",encoding=encode)
        line=f.readline()
        while line:
            row=line.split('","')
            comp=""
            if encode=="utf-8":
                comp=row[1]
                #print(comp)
            elif encode=="ansi":
                comp=row[3]
               # print(comp)
            if re.search(nonalphnum, comp) == None:
                pass
            else:
                out.write('"'+file+'","'+line)
            line=f.readline()

prob_comp(filesutf8,"utf-8")
prob_comp(filesansi,"ansi")