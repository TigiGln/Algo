# Projet d'Algorithmique

#########################

## LANCEMENT DU PROJET

#########################

Pour lancer l'interface du projet et accéder au logiciel:

<font color = "red">python3 Interface_project.py</font>

Vous pouvez tester aussi de façon indépendante les parties BWT et HUFFMAN avec comme séquences choisies celle de votre pdf de projet.

Pour la transformée de Burrows Weeler:

python3 subparts/BWT.py


Pour l'Algorithme d'Huffman:

python3 subparts/huffman.py



#########################

## FONCTIONNEMENT

#########################

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

Attention vous ne pouvez décompresser ou décrypter qu'une séquence enregistrer compresser ou crypter respectivement dans un fichier. Comme pour le bouton Décompression/Décryptage.

Cependant une fois que vous avez enregistrer votre séquence avec les boutons Encryption, Compression et Encryption/Compression. Si vous souhaitez rester sur la même séquence vous pouvez utiliser les 6 boutons selon vos envies.

########################

## COMMENTAIRES 

########################

Certaines fonctions de l'interface se ressemblent fortement, je suis conscient que j'aurai pu les factoriser en une seule cependant j'ai préféré cette décomposition pour la flexibité de l'affichage avec "pack()" qui aurait été plus complexe pour moi selon les séquences à analyser.






