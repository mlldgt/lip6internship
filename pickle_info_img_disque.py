# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:33:30 2019

@author: malou
"""

import pickle

pickle_f=open("dicos_img_disque/files.pickle","rb")

pickle_d=open("dicos_img_disque/dirs.pickle","rb")

files=pickle.load(pickle_f,encoding="utf-8")
dirs=pickle.load(pickle_d,encoding="utf-8")

#print(list(files['/media/veracrypt1/Images_Clones/IMG/M_conner/Word 5/Dictionnaire fran\udc8dais'][0]))

"""test=files['/media/veracrypt1/Images_Clones/IMG/M_conner/Word 5/Dictionnaire fran\udc8dais'][0]
if 	u'\udc8d' in test:
    print("x")
    test.replace(u'\udc8d',"FUCK")
    f=open("test.txt","w")
    f.write(test)
    f.close()"""
    
with open("infos_img_disque/img_mac_derrida_files.csv","w",encoding="utf-8") as file:
    file.write('"path","name","date modif"\n')
    for entry in files:
        try:
            file.write('"'+entry+'","'+files[entry][0]+'","'+files[entry][1]+'"\n')
        except UnicodeEncodeError:
            path=list(entry)
            name=list(files[entry][0])
            date=files[entry][1]
            file.write('"')
            for char in path:
                try:
                    file.write(char)
                except UnicodeEncodeError:
                    file.write("ERROR")
            file.write('","')
            for char in name:
                try:
                    file.write(char)
                except UnicodeEncodeError:
                    file.write("ERROR")
            file.write('","'+date+'"\n"')

with open("infos_img_disque/img_mac_derrida_dirs.csv","w",encoding="utf-8") as file2:
    file2.write('"path","name","date modif"\n')
    for entry in dirs:
        #print(entry)
        try:
            file2.write('"'+entry+'","'+dirs[entry][0]+'","'+dirs[entry][1]+'"\n')
        except UnicodeEncodeError:
            path=list(entry)
            name=list(dirs[entry][0])
            date=dirs[entry][1]
            file2.write('"')
            for char in path:
                try:
                    file2.write(char)
                except UnicodeEncodeError:
                    file2.write("ERROR")
            file2.write('","')
            for char in name:
                try:
                    file2.write(char)
                except UnicodeEncodeError:
                    file2.write("ERROR")
            file2.write('","'+date+'"\n"')