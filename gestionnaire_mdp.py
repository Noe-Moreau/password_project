import os
import json
import random
from datetime import datetime

# Fichier de sauvegarde des données
FICHIER = "mots_de_passe.json"

DICTIONNAIRE_FAIBLE = [
    "password", "123456", "123456789", "qwerty", "abc123", "football",
    "monkey", "letmein", "dragon", "111111", "baseball", "iloveyou",
    "trustno1", "123123", "sunshine", "master", "welcome", "shadow",
    "ashley", "jesus", "ninja", "1234", "12345", "admin", "login",
    "princess", "solo", "passw0rd", "starwars"
]

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

def analyser_force(mdp: str) -> tuple[int, str]:

    score_points = 0
    max_points = 8  # 8 critères

    # Critère 1 : longueur ≥ 8
    if len(mdp) >= 8:
        score_points += 1

    # Critère 2 : longueur ≥ 12 (bonus)
    if len(mdp) >= 12:
        score_points += 1

    # Critère 3 : contient au moins une majuscule
    if any(c.isupper() for c in mdp):
        score_points += 1

    # Critère 4 : contient au moins une minuscule
    if any(c.islower() for c in mdp):
        score_points += 1

    # Critère 5 : contient au moins un chiffre
    if any(c.isdigit() for c in mdp):
        score_points += 1

    # Critère 6 : contient au moins un caractère spécial
    speciaux = "!@#$%^&*()-_=+[]{};:,.<>?/"
    if any(c in speciaux for c in mdp):
        score_points += 1
    # Critère 7 : pas de caractères répétés consécutifs
    if all(mdp[i] != mdp[i+1] for i in range(len(mdp)-1)):
        score_points += 1

    # Critère 8 : mot de passe pas dans le dictionnaire
    if mdp.lower() not in DICTIONNAIRE_FAIBLE:
        score_points += 1

    # Conversion en pourcentage sur 0-100
    score = int((score_points / max_points) * 100)

    # Définition du niveau selon le score
    if score <= 25:       # 0-2 points → Très faible
        niveau = "Très faible"
    elif score <= 50:     # 3-4 points → Faible
        niveau = "Faible"
    elif score <= 75:     # 5-6 points → Moyen
        niveau = "Moyen"
    else:                 # 7-8 points → Très fort
        niveau = "Très fort"

    return score, niveau


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
    # Charger les données existantes
    donnees = charger_donnees()

    # Catégories prédéfinies
    categories = [
        "Réseaux sociaux",
        "Email",
        "Banque",
        "Shopping",
        "Travail",
        "Divertissement",
        "Cloud",
        "Autre"
    ]

    # 1. Saisir le site
    while True:
        site = input("Site ou service (ex: gmail.com) : ").strip()
        if not site:
            print("Le nom du site ne peut pas être vide.")
            continue

        # Vérifier si le site existe déjà
        if any(d['site'].lower() == site.lower() for d in donnees):
            print(f"Attention : Un compte pour '{site}' existe déjà.")
            if not _input_oui_non("Voulez-vous continuer quand même ? (O/N) : "):
                print("Ajout annulé.")
                return
        break

    # 2. Choisir la catégorie
    print("\nCatégories disponibles :")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")

    while True:
        try:
            choix = int(input(f"Choisissez une catégorie (1-{len(categories)}) : "))
            if 1 <= choix <= len(categories):
                categorie = categories[choix - 1]
                break
            print(f"Veuillez entrer un nombre entre 1 et {len(categories)}.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    # 3. Saisir le nom du compte
    while True:
        nom_compte = input("Nom du compte : ").strip()
        if nom_compte:
            break
        print("Le nom du compte ne peut pas être vide.")

    # 4. Saisir l'email avec validation basique
    while True:
        email = input("Adresse email : ").strip()
        if email and "@" in email and "." in email.split("@")[-1]:
            break
        print("Format d'email invalide. Veuillez réessayer.")

    # 5. Mot de passe (saisir ou générer)
    generer = _input_oui_non("Générer un mot de passe automatiquement ? (O/N) : ")

    if generer:
        try:
            mot_de_passe = generer_mdp()
            print(f"\nMot de passe généré : {mot_de_passe}")
        except ValueError as e:
            print(f"Erreur : {e}")
            return
    else:
        while True:
            mot_de_passe = input("Entrez le mot de passe : ").strip()
            if mot_de_passe:
                break
            print("Le mot de passe ne peut pas être vide.")

    # 6. Analyser la force du mot de passe
    score, niveau = analyser_force(mot_de_passe)

    print(f"\nScore de sécurité du mot de passe : {score}/100 ({niveau})")

    if score <= 50:
        print("Attention : Ce mot de passe est faible !")
        if not _input_oui_non("Voulez-vous continuer quand même ? (O/N) : "):
            print("Ajout annulé.")
            return

    # 7. Générer la date de création
    date_creation = datetime.now().strftime("%Y-%m-%d")

    # 8. Créer le dictionnaire du compte
    nouveau_compte = {
        "site": site,
        "categorie": categorie,
        "nom_compte": nom_compte,
        "email": email,
        "mot_de_passe": mot_de_passe,
        "score": score,
        "date_creation": date_creation
    }

    # 9. Ajouter à la liste et sauvegarder
    donnees.append(nouveau_compte)
    sauvegarder(donnees)

    print(f"\n✓ Compte ajouté avec succès pour {site} !")
    print(f"  Catégorie : {categorie}")
    print(f"  Email : {email}")
    print(f"  Sécurité : {score}/100")


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
    # 1. Charger les données
    comptes = charger_donnees()

    # vérifier s'il y a des comptes
    if not comptes:
        print("Aucun compte enregistré.")
        return

    # 2. Affichage du tableau, 1ere ligne
    print("-" * 100)
    print(
        f"{'Site':20} | "
        f"{'Genre du site':15} | "
        f"{'Compte':20} | "
        f"{'Mail':30} | "
        f"{'Date de création'}"
    )
    print("-" * 100)

    # 3. Affichage du tableau, 2ere ligne à dernière ligne
    for c in comptes:
        print(
            f"{c['site']:20} | "
            f"{c['categorie']:15} | "
            f"{c['nom_compte']:20} | "
            f"{c['email']:30} | "
            f"{c['date_creation']}"
        )



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
    """
    Recherche des comptes par site ou catégorie.
    Affiche les résultats correspondants sous forme de tableau.
    """
    # Charger les données
    donnees = charger_donnees()

    if not donnees:
        print("\nAucun compte enregistré pour le moment.")
        return

    # Demander le terme de recherche
    terme = input("\nEntrez le terme de recherche (site ou catégorie) : ").strip()

    if not terme:
        print("Le terme de recherche ne peut pas être vide.")
        return

    # Rechercher les comptes correspondants (insensible à la casse)
    resultats = []
    terme_lower = terme.lower()

    for compte in donnees:
        site_lower = compte['site'].lower()
        categorie_lower = compte['categorie'].lower()

        # Vérifier si le terme est dans le site ou la catégorie
        if terme_lower in site_lower or terme_lower in categorie_lower:
            resultats.append(compte)

    # Afficher les résultats
    if resultats:
        print(f"\n{len(resultats)} résultat(s) trouvé(s) pour '{terme}' :\n")
        afficher_tableau(resultats)
    else:
        print(f"\nAucun compte trouvé pour le terme '{terme}'.")
        print("Essayez avec un autre terme de recherche.")



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
    # Charger les données
    donnees = charger_donnees()

    if not donnees:
        print("\nAucune donnée disponible pour les statistiques.")
        return

    print("\n" + "=" * 60)
    print("STATISTIQUES DU GESTIONNAIRE DE MOTS DE PASSE")
    print("=" * 60)

    # 1. Nombre total de comptes
    total_comptes = len(donnees)
    print(f"\nNombre total de comptes : {total_comptes}")

    # 2. Répartition par catégorie
    print("\nRépartition par catégorie :")
    categories_count = {}
    for d in donnees:
        cat = d.get('categorie', 'Non définie')
        categories_count[cat] = categories_count.get(cat, 0) + 1

    for cat, count in sorted(categories_count.items(), key=lambda x: x[1], reverse=True):
        pourcentage = (count / total_comptes) * 100
        print(f"   - {cat:20} : {count:3} compte(s) ({pourcentage:.1f}%)")

    # 3. Score moyen de sécurité
    scores = [d.get('score', 0) for d in donnees]
    score_moyen = sum(scores) / len(scores) if scores else 0
    print(f"\nScore moyen de sécurité : {score_moyen:.1f}/100")

    # 4. Identifier les mots de passe faibles (score <= 50)
    comptes_faibles = [d for d in donnees if d.get('score', 0) <= 50]
    print(f"\nMots de passe faibles (score <= 50) : {len(comptes_faibles)}")
    if comptes_faibles:
        print("   Sites concernés :")
        for d in comptes_faibles:
            print(f"   - {d['site']:20} - Score : {d.get('score', 0)}/100")

    # 5. Identifier les mots de passe trop anciens (> 90 jours)
    from datetime import datetime, timedelta

    date_limite = datetime.now() - timedelta(days=90)
    comptes_anciens = []

    for d in donnees:
        date_str = d.get('date_creation', '')
        try:
            date_creation = datetime.strptime(date_str, "%Y-%m-%d")
            if date_creation < date_limite:
                jours_anciennete = (datetime.now() - date_creation).days
                comptes_anciens.append((d, jours_anciennete))
        except ValueError:
            continue

    print(f"\nMots de passe anciens (> 90 jours) : {len(comptes_anciens)}")
    if comptes_anciens:
        print("   Sites concernés :")
        for d, jours in sorted(comptes_anciens, key=lambda x: x[1], reverse=True):
            print(f"   - {d['site']:20} - {jours} jour(s)")

    # Résumé final
    print("\n" + "-" * 60)
    print("RÉSUMÉ")
    print("-" * 60)

    if score_moyen >= 75:
        etat = "Excellent"
    elif score_moyen >= 60:
        etat = "Bon"
    elif score_moyen >= 40:
        etat = "Moyen"
    else:
        etat = "Faible"

    print(f"État général de la sécurité : {etat}")
    print(f"Comptes à renforcer : {len(comptes_faibles)}")
    print(f"Comptes à renouveler : {len(comptes_anciens)}")
    print("=" * 60 + "\n")

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

    confirmation = _input_oui_non("Voulez-vous vraiment quitter ? (O/N) : ")

    if confirmation:
        print("\n" + "=" * 50)
        print("Merci d'avoir utilisé le gestionnaire de mots de passe.")
        print("À bientôt !")
        print("=" * 50)
        exit()
    else:
        print("\nRetour au menu principal...\n")


"""
 MENU PRINCIPAL
 
 Affiche le menu principal et gère le choix de l'utilisateur.
 Appelle les fonctions correspondantes selon l'option choisie.
"""


def afficher_menu():
    """
    Affiche le menu principal avec toutes les options disponibles.
    """
    print("\n" + "=" * 60)
    print("       GESTIONNAIRE DE MOTS DE PASSE")
    print("=" * 60)
    print("\n1. Générer un mot de passe")
    print("2. Analyser la force d'un mot de passe")
    print("3. Ajouter un compte")
    print("4. Lister les comptes")
    print("5. Rechercher un compte")
    print("6. Afficher les statistiques")
    print("7. Quitter")
    print("\n" + "-" * 60)

"""
    Boucle principale du programme.
    Affiche le menu et traite les choix de l'utilisateur.
"""
def menu_principal():

    while True:
        afficher_menu()

        try:
            choix = input("\nChoisissez une option (1-7) : ").strip()

            if choix == "1":
                print("\n--- Génération de mot de passe ---")
                try:
                    mdp = generer_mdp()
                    print(f"\nMot de passe généré : {mdp}")
                    print(f"Longueur : {len(mdp)} caractères")
                except ValueError as e:
                    print(f"Erreur : {e}")

            elif choix == "2":
                print("\n--- Analyse de la force du mot de passe ---")
                mdp = input("Entrez le mot de passe à analyser : ").strip()
                if mdp:
                    score, niveau = analyser_force(mdp)
                    print(f"\nRésultat de l'analyse :")
                    print(f"  Score : {score}/100")
                    print(f"  Niveau : {niveau}")
                else:
                    print("Le mot de passe ne peut pas être vide.")

            elif choix == "3":
                print("\n--- Ajout d'un nouveau compte ---")
                ajouter_compte()

            elif choix == "4":
                print("\n--- Liste des comptes ---")
                lister_comptes()

            elif choix == "5":
                print("\n--- Recherche de compte ---")
                rechercher()

            elif choix == "6":
                print("\n--- Statistiques ---")
                calculer_stats()

            elif choix == "7":
                quitter()

            else:
                print("\nChoix invalide. Veuillez entrer un nombre entre 1 et 7.")

            # Pour éviter d'afficher le menu sans action
            input("...")

        except KeyboardInterrupt:
            print("\n\nInterruption détectée. Fermeture du programme...")
            break
        except Exception as e:
            print(f"\nErreur inattendue : {e}")
            print("Veuillez réessayer.")


# Point d'entrée du programme
if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\nProgramme interrompu. Au revoir !")
    except Exception as e:
        print(f"\nErreur fatale : {e}")