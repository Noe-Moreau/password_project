import os
import json
import random

# Fichier de sauvegarde des données
FICHIER = "mots_de_passe.json"


# -------------------- UTILITAIRES --------------------

# Charge les données depuis le fichier JSON.
# Retourne une liste vide si le fichier n'existe pas ou est corrompu.
def charger_donnees():
    if not os.path.exists(FICHIER):
        return []
    try:
        with open(FICHIER, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Fichier corrompu, réinitialisation.")
        return []


# Sauvegarde les données dans le fichier JSON.
# Écrase le contenu existant de manière formatée.
def sauvegarder(donnees):
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=4)


# Affiche les données sous forme de tableau lisible en console.
# Aligne les colonnes pour une lecture claire.
def afficher_tableau(donnees):
    print("-" * 120)
    print(
        f"{'Site':20} | "
        f"{'Catégorie':15} | "
        f"{'Nom du compte':20} | "
        f"{'Adresse mail':30} | "
        f"{'Score':5} | "
        f"{'Créé le'}"
    )
    print("-" * 120)

    for d in donnees:
        print(
            f"{d['site']:20} | "
            f"{d['categorie']:15} | "
            f"{d['nom_compte']:20} | "
            f"{d['email']:30} | "
            f"{d['score']:5} | "
            f"{d['date_creation']}"
        )

    print("-" * 120)


# Demande une réponse O/N à l'utilisateur et retourne True pour O, False pour N
# Boucle jusqu'à obtenir une entrée valide
def _input_oui_non(message: str) -> bool:
    while True:
        choix = input(message).strip().upper()
        if choix in ("O", "N"):
            return choix == "O"
        print("Entrée invalide. Répondez par O ou N.")


# Demande une longueur de mot de passe comprise entre 8 et 64
# Vérifie que l'entrée est un entier valide
def _input_longueur() -> int:
    while True:
        try:
            valeur = int(input("Longueur du mot de passe (8 à 64) : "))
            if 8 <= valeur <= 64:
                return valeur
            print("La longueur doit être entre 8 et 64.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")


"""
 --------------------------------------------------
 1. Générer un mot de passe
 --------------------------------------------------
 Données saisies par l'utilisateur :
 - Longueur du mot de passe (entier entre 8 et 64)
 - Choix d'inclure :
     * lettres minuscules (oui/non)
     * lettres majuscules (oui/non)
     * chiffres (oui/non)
     * caractères spéciaux (oui/non)
 - Option pour exclure les caractères ambigus (0/O, l/1)

 Fonctionnement :
 - Vérifie la validité des entrées (longueur, au moins un type sélectionné)
 - Construit un ensemble de caractères autorisés
 - Génère un mot de passe aléatoire sécurisé
 - Retourne le mot de passe généré
"""


def generer_mdp() -> str:
    longueur = _input_longueur()

    minuscules = _input_oui_non("Inclure des minuscules ? (O/N) : ")
    majuscules = _input_oui_non("Inclure des majuscules ? (O/N) : ")
    chiffres = _input_oui_non("Inclure des chiffres ? (O/N) : ")
    speciaux = _input_oui_non("Inclure des caractères spéciaux ? (O/N) : ")
    exclure_ambigus = _input_oui_non("Exclure les caractères ambigus ? (O/N) : ")

    if not any([minuscules, majuscules, chiffres, speciaux]):
        raise ValueError("Au moins un type de caractères doit être sélectionné.")

    minuscules_liste = [chr(i) for i in range(97, 123)]
    majuscules_liste = [chr(i) for i in range(65, 91)]
    chiffres_liste = [chr(i) for i in range(48, 58)]
    speciaux_liste = list("!@#$%^&*()-_=+[]{};:,.<>?/")

    ambigus = {"0", "O", "o", "1", "l", "I"}

    autorises = []

    if minuscules:
        autorises.extend(minuscules_liste)
    if majuscules:
        autorises.extend(majuscules_liste)
    if chiffres:
        autorises.extend(chiffres_liste)
    if speciaux:
        autorises.extend(speciaux_liste)

    if exclure_ambigus:
        autorises = [c for c in autorises if c not in ambigus]

    if not autorises:
        raise ValueError("Aucun caractère autorisé après filtrage.")

    rng = random.SystemRandom()
    return "".join(rng.choice(autorises) for _ in range(longueur))

""" 
 --------------------------------------------------
 2. Analyser la force d'un mot de passe
 --------------------------------------------------
 Données saisies par l'utilisateur :
 - Mot de passe à analyser (chaîne de caractères)

 Fonctionnement :
 - Analyse la longueur du mot de passe
 - Vérifie la diversité des types de caractères utilisés
 - Calcule une entropie estimée
 - Vérifie si le mot de passe fait partie d'un dictionnaire commun
 - Attribue un score de 0 à 100
 - Retourne le score et un niveau (Faible, Moyen, Fort, Très fort)
"""


def analyser_force():
    pass


"""
 --------------------------------------------------
 3. Ajouter un compte
 --------------------------------------------------
 Données saisies par l'utilisateur :
 - Site ou service (ex : gmail.com)
 - Catégorie (choisie dans une liste prédéfinie)
 - Nom du compte
 - Adresse email (format valide)
 - Mot de passe (saisi ou généré)

 Fonctionnement :
 - Vérifie les formats (email, date, doublon de site)
 - Analyse automatiquement la force du mot de passe
 - Génère la date de création
 - Stocke toutes les informations dans un dictionnaire
 - Ajoute le dictionnaire à la liste des comptes
 - Sauvegarde les données dans un fichier JSON
"""


def ajouter_compte():
    pass


"""
 --------------------------------------------------
 4. Lister les comptes
 --------------------------------------------------
 Données saisies par l'utilisateur :
 - Aucune (ou optionnellement un filtre par catégorie)

 Fonctionnement :
 - Charge les comptes depuis le fichier de sauvegarde
 - Affiche les comptes sous forme de tableau formaté
 - Montre les informations essentielles (site, catégorie, score, date)
 """


def lister_comptes():
    pass


"""
 --------------------------------------------------
 5. Rechercher un compte
 --------------------------------------------------
 Données saisies par l'utilisateur :
 - Terme de recherche (nom du site ou catégorie)

 Fonctionnement :
 - Parcourt la liste des comptes sauvegardés
 - Compare le terme avec les noms de site et catégories
 - Affiche les comptes correspondants sous forme de tableau
 - Affiche un message si aucun résultat n'est trouvé
"""


def rechercher():
    pass


""" --------------------------------------------------
 6. Calculer et afficher les statistiques
 --------------------------------------------------
 Données saisies par l'utilisateur :
 - Aucune

 Fonctionnement :
 - Calcule le nombre total de comptes
 - Calcule la répartition par catégorie
 - Calcule le score moyen de sécurité
 - Identifie les mots de passe faibles
 - Identifie les mots de passe trop anciens (> 90 jours)
 - Affiche un résumé clair des statistiques
"""


def calculer_stats():
    pass


"""
 --------------------------------------------------
 7. Quitter le programme
 --------------------------------------------------
 Données saisies par l'utilisateur :
 - Confirmation éventuelle (oui/non)

 Fonctionnement :
 - Sauvegarde les données si nécessaire
 - Affiche un message de fermeture
 - Met fin proprement à l'exécution du programme
"""


def quitter():
    pass