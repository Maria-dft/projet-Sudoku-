grille = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def chiffreDansLigne(grille, ligne, valeur):
    for colonne in range(0, 9):
        if grille[ligne][colonne] == valeur:
            return True
    return False


def chiffreDansColonne(grille, colonne, valeur):
    for ligne in range(0, 9):
        if grille[ligne][colonne] == valeur:
            return True
    return False


def chiffreDansZone(grille, ligne, colonne, valeur):
    debutZoneLigne = (ligne // 3) * 3
    debutZoneColonne = (colonne // 3) * 3
    for i in range(debutZoneLigne, debutZoneLigne + 3):
        for j in range(debutZoneColonne, debutZoneColonne + 3):
            if grille[i][j] == valeur:
                return True
    return False


def placementValide(grille, ligne, colonne, valeur):
    if chiffreDansLigne(grille, ligne, valeur):
        return False
    if chiffreDansColonne(grille, colonne, valeur):
        return False
    if chiffreDansZone(grille, ligne, colonne, valeur):
        return False
    return True


def resoudreGrille(grille, position):
    if position >= 81:
        return True

    ligne = position // 9
    colonne = position % 9

    if grille[ligne][colonne] != 0:
        return resoudreGrille(grille, position + 1)

    for valeur in range(1, 10):
        if placementValide(grille, ligne, colonne, valeur):
            grille[ligne][colonne] = valeur
            if resoudreGrille(grille, position + 1):
                return True

    grille[ligne][colonne] = 0
    return False


if resoudreGrille(grille, 0):
    for ligne in grille:
        print(ligne)
else:
    print("Aucune solution")