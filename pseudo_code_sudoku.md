Variable grille : tableau[9][9] d'entiers

Fonction ChiffreDansLigne(grille : tableau[9][9] d'entiers, ligne, valeur : entier) : booléen
    Pour colonne allant de 0 à 8 par pas de 1 faire
        Si grille[ligne][colonne] = valeur alors
            retourner vrai
        Fin Si
    Fin Pour
    retourner faux
Fin Fonction

Fonction ChiffreDansColonne(grille : tableau[9][9] d'entiers, colonne, valeur : entier) : booléen
    Pour ligne allant de 0 à 8 par pas de 1 faire
        Si grille[ligne][colonne] = valeur alors
            retourner vrai
        Fin Si
    Fin Pour
    retourner faux
Fin Fonction

Fonction ChiffreDansZone(grille : tableau[9][9] d'entiers, ligne, colonne, valeur : entier) : booléen
    debutZoneLigne <- (ligne div 3) * 3
    debutZoneColonne <- (colonne div 3) * 3
    Pour i allant de debutZoneLigne à debutZoneLigne + 2 par pas de 1 faire
        Pour j allant de debutZoneColonne à debutZoneColonne + 2 par pas de 1 faire
            Si grille[i][j] = valeur alors
                retourner vrai
            Fin Si
        Fin Pour
    Fin Pour
    retourner faux
Fin Fonction

Fonction PlacementValide(grille : tableau[9][9] d'entiers, ligne, colonne, valeur : entier) : booléen
    Si ChiffreDansLigne(grille, ligne, valeur) alors
        retourner faux
    Fin Si
    Si ChiffreDansColonne(grille, colonne, valeur) alors
        retourner faux
    Fin Si
    Si ChiffreDansZone(grille, ligne, colonne, valeur) alors
        retourner faux
    Fin Si
    retourner vrai
Fin Fonction

Fonction ResoudreGrille(grille : tableau[9][9] d'entiers, position : entier) : booléen
    Si position ≥ 81 alors
        retourner vrai
    Fin Si

    ligne <- position div 9
    colonne <- position modulo 9

    Si grille[ligne][colonne] ≠ 0 alors
        retourner ResoudreGrille(grille, position + 1)
    Fin Si

    Pour valeur allant de 1 à 9 par pas de 1 faire
        Si PlacementValide(grille, ligne, colonne, valeur) alors
            grille[ligne][colonne] <- valeur
            Si ResoudreGrille(grille, position + 1) alors
                retourner vrai
            Fin Si
        Fin Si
    Fin Pour

    grille[ligne][colonne] <- 0
    retourner faux
Fin Fonction

Début
    Si ResoudreGrille(grille, 0) alors
        Afficher(grille)
    Sinon
        Afficher("Aucune solution")
    Fin Si
Fin
