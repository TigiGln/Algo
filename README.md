# Projet d'Algorithmique

Réalisé par Thierry Galliano

M1 DLAD 2020-2021

################################################

## Dependances

################################################

Bibliothèque Tkinter

sudo apt-get install python3-tk

bibliothèque "re" pour les regex

pip install regex


###############################################

## LANCEMENT DU PROJET

###############################################

Pour lancer l'interface du projet et accéder au logiciel:

### python3 Interface_project.py

Dans l'interface, vous pouvez utiliser n'importe quelle lettre de l'alphabet français sans espace

#############################################################################################
Vous pouvez tester aussi de façon indépendante les parties BWT et HUFFMAN avec comme séquence choisie par défaut celle du pdf du projet mais vous pouvez changer cela à votre guise.

Pour la transformée de Burrows Weeler:

#### python3 subparts/BWT.py ACTTGATC


Pour l'Algorithme d'Huffman:

#### python3 subparts/huffman.py NNTNACTTNGNNGTTNCCTATACCT


Attention ces deux option ne sont là que pour tester le code en arrière plan de l'interface pas pour enregistrer des fichiers ou faire votre analyse complète. Pour cela il y a l'interface du projet qui se suffit à elle seule.


#############################################

## FONCTIONNEMENT

#############################################

Utilisation du logiciel:

Commencer par le haut de l'interface en choisissant si vous souhaitez le résultat sans visualisation des étapes avec le bouton radio "no step" ou avec les différentes étapes, matrice ou développement Huffman, avec le second bouton radio "with step".

Vous avez ensuite le choix pour entrer votre séquence d'intérêt, soit directement dans le cadre prévu à cette effet pour de petites séquences, soit avec le bouton "Open file" pour choisir un fichier fasta ou txt.

Une fois votre séquence donnée au logiciel, vous avez le choix entre 6 boutons pour votre analyse:
Encryption: Pour encrypter votre séquence
Compression: Pour la compresser 
Décompression: Pour la décompresser
Décryption: Pour la décrypter
Encryption/Compression: Pour crypter et compresser le cryptage directement
Decompression/Decryption: Pour décompresser et décrypter la séquence décompresser directement.

Attention vous ne pouvez décompresser ou décrypter qu'une séquence enregistrer compresser ou crypter respectivement dans un fichier. Cela fonctionne pareil pour le bouton Décompression/Décryptage avec un fichier encrypter et compresser.

Cependant une fois que vous avez enregistrer votre séquence avec les boutons Encryption, Compression et Encryption/Compression. Si vous souhaitez rester sur la même séquence vous pouvez utiliser les 6 boutons selon vos envies sans être obligé de recherger un fichier à chaque fois.

###########################################

## COMMENTAIRES 

###########################################

Certaines fonctions de l'interface se ressemblent fortement, je suis conscient que j'aurai pu les factoriser en une seule cependant j'ai préféré cette décomposition pour la flexibité de l'affichage avec "pack()" qui aurait été plus complexe pour moi selon les séquences à analyser.






