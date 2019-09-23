# lip6internship
Code that I developed during one of my internships. Mostly to gather, compare and sort data

All programs written for Python 3. Unless indicated otherwise, all should work under Windows, MacOS and Linux

*essai_traitement_fichiers*
  status: essential
  input: address of the directory containing all the files to examine
  output: csv_f_derrida.csv & csv_d_derrida.csv (all files and directories name, path, modification dates compiled in csv file); csv_derrida_files.csv & csv_derrida_dir.csv (same as previous files but with unique id associated to each files or directory); csv_derrida_files2.csv (same as before for files, but with am MD5 hash key created by the program)
  info: this program can only work as-is under Windows. It uses the Windows command CertUtil, as well as the software HashConsole, to create the MD5 keys.
  description: the program goes through the directory given as source and examines all files and directories contained in it, gathering information such as their name, their path, and their latest modification date. It also adds a uniaue id to each element and a MD5 hash key to all files. A MD5 key is a chain of letters and numbers that symbolizes the textual content of a file and allows quick comparisons between files to see if their content is identical or not.

*compteur_cle_md5*
  status: non essential
  input: csv_derrida_files2.csv
  output: resultats.txt (lists all distinct MD5 keys and associates to each a list of the files possessing this key, as well as the files properties); resultats_noms.txt (same as before but only with files names); cles_noms_fichiers_differents.txt (lists all distinct MD5 keys corresponding to at least 2 files with different names, as well as all the files each key is associated to); noms_fichiers_et_fichiers_correspondants.txt (lists all distinct file names and associates each names to a list of the properties of each file with that name); noms_fichiers_avec_plusieurs_cles.txt (lists all distinct file names that are linked to at least two different MD5 keys, and associates each name to a list of the properties of each file with that name)
  description: mostly gives organized overview of all the files and their properties so we can compare them and have a preliminary idea of what the database looks like
  
*comparaison_dossiers*
  status: non essential
  input: address of the directory containing all the files to examine
  output: sim_cont.txt (lists all distinct directory contents and associates to each singular content a list of the name of the directories with that content); sim_name.txt (lists all distinct directory names and associates to each name a list of the contents of directories with that name); meme_nom_contenu_different.txt (lists only directory names that are associated to at least two different contents, and lists those contents for each name); meme_nom_meme_contenu.txt (lists only directories that have both the same name and the same content, and associate to each name/content couple the paths of those directories)
  description: mostly gives organized overview od all the directories and their contents so we can compare them and have a preliminary idea of what the database will look like
  
*pickle_info_img_disque*
  status: auxiliary
  input: all dictionaries created as a result of examining disk images
  output: all of the information contained in the dictionaries, but in CSV file form
  info: this program is based on the information gathered by mounting disk images under linux and stocking this information in PICKLE files. The program that produces these PICKLE files will be added later.
  description: gathers information contained in PICKLE files and organizes it in CSV files
  
*comparaison_et_compilation_infos_fichiers*
  status: essential
  input: all CSV files containing information about file properties (csv_derrida_files2.csv, CSV file containing the disk images information...)
  output: all_info_compile.csv
  description: this program gathers all the information about files that we possess and groups them together in one file.
  
*problematic_names_detection*
  status: auxiliary
  input: all CSV files containing information about file properties
  output: all_problematic_names.csv
  description: this program gathers in one file all the file names with an encoding problem (or an ERROR in their name in the case of the file information coming from the disk images). The created file can then be used to find by hand all those symbols that aren't being correctly interpreted, and will be integrated in a correcting function in the dates comparing program.

*comparaison_dates*
  status: essential
  input: all_info_compile.csv
  output: all_info_w_good_dates.csv
  description: compares all available information to determine if the modification date for each file is plausible or exact. In this case, the date has to be comprised between 1985 and October 9th 2004. If there are dates with the same day but different hours, the default will be the date gathered from the files in our possession (written down in csv_derrida_files2.csv)
  
*etablissement_anteriorite*
  status: essential
  input: all_info_w_good_dates.csv
  output: all_info_w_chronology.csv; chronologie_correspondance.csv; md5_correspondance.csv
  description: from all the information gathered and cleaned, this program establishes chronological links between the files, recorded in chronologie_correspondance.csv in a format that allows the information to be transfered into the OrientDB database. It also establishes links based on file names and MD5 keys, recorded in md5_correspondance.csv in the same format. Finally, it also adds all this information to the file all_info_w_chronology, which is now the file gathering the most complete and accurate information about the files.
