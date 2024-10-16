Etudiant 1 : Rim Kais
Etudiant 2 : Nadira Houch

Le but du TP est de comparer un ensemble d'echantillons de séquence d'ADN entre eux deux à deux en utilisant l'indice Jaccard

### Resultats obtenus
Le fichier kmers.py 

![resultats](resultat.png)

Ces valeurs nous donne une idée sur la similitude entre les différente séquences étudiée par exemple ici GCA_000008865.2 et GCA_000005845.2 sont les deux sequences avec le meilleur score de 0.436 c'est à dire les plus similaire 

## Scripts

### kmer
 
Le fichier kmers.py contient les fonction necessaire pour calculer lire les sequences et les diviser en kmer

kmer2str : transforme les kmer de entiers en chaine de caratére 

encode_nucl : retrourne la valeur en chiffre d'acide nucléique

strem_kmer : calcul tout les kmer d'une seqence d'ADN 

filter_smallest : permet de faire un sketch sur tout les kmer de chaque sequence on ne gradant qu'un nombre de kmer choisi de taille s en utilisant la methode bottom minhash on ne garde que les s plus petites valeurs de kmer apres la fonction Hach (xorshift64)

create_index : cree un dictionnaire a partir contenant les kmer choisi ansi que la frequence de leur présence dans la liste 



### main

Dans le main la fonction Jaccard compare les deux sequence en calculant l'intersection et l'union de l'ensemble des kmers qui se trouve dans les deux sequences 
