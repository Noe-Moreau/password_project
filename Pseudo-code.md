# GESTIONNAIRE DE MOTS DE PASSE — PSEUDO-CODE
# Phase : JOUR 1 — CONCEPTION
# DÉMARRAGE DU PROGRAMME

DÉBUT PROGRAMME

    Charger les comptes depuis le fichier de sauvegarde (JSON)
    SI le fichier n’existe pas OU est invalide
        Initialiser une liste vide de comptes
    FIN SI


# BOUCLE PRINCIPALE

    TANT QUE l’utilisateur ne choisit pas "Quitter"

        Afficher le menu principal :
            1. Générer un mot de passe
            2. Analyser la force d’un mot de passe
            3. Ajouter un compte
            4. Lister les comptes
            5. Rechercher un compte
            6. Afficher les statistiques
            7. Quitter le programme

        Lire le choix de l’utilisateur

        SELON le choix
            CAS 1 :
                Appeler la fonction de génération de mot de passe
            CAS 2 :
                Appeler la fonction d’analyse de mot de passe
            CAS 3 :
                Appeler la fonction d’ajout de compte
            CAS 4 :
                Appeler la fonction de listing des comptes
            CAS 5 :
                Appeler la fonction de recherche de compte
            CAS 6 :
                Appeler la fonction de calcul et d’affichage des statistiques
            CAS 7 :
                Demander confirmation à l’utilisateur
                SI confirmation
                    Sauvegarder les données
                    Quitter la boucle
                FIN SI
            CAS PAR DÉFAUT :
                Afficher "Choix invalide"
        FIN SELON

    FIN TANT QUE


# 1. GÉNÉRER UN MOT DE PASSE

FONCTION generer_mdp

    Demander la longueur du mot de passe (entier entre 8 et 64)
    Vérifier que la valeur est valide

    Demander si l’utilisateur souhaite inclure :
        - lettres minuscules
        - lettres majuscules
        - chiffres
        - caractères spéciaux

    Vérifier qu’au moins un type de caractères est sélectionné

    Demander si les caractères ambigus (0/O, l/1) doivent être exclus

    Construire l’ensemble de caractères autorisés

    Générer un mot de passe aléatoire sécurisé

    Afficher le mot de passe généré

FIN FONCTION


# 2. ANALYSER LA FORCE D’UN MOT DE PASSE

FONCTION analyser_force

    Demander le mot de passe à analyser

    Analyser :
        - la longueur du mot de passe
        - la présence de lettres minuscules
        - la présence de lettres majuscules
        - la présence de chiffres
        - la présence de caractères spéciaux

    Estimer l’entropie du mot de passe

    Vérifier si le mot de passe appartient à un dictionnaire commun

    Calculer un score de sécurité entre 0 et 100

    Déterminer le niveau de sécurité :
        - Faible
        - Moyen
        - Fort
        - Très fort

    Afficher le score et le niveau

    Retourner le score

FIN FONCTION


# 3. AJOUTER UN COMPTE

FONCTION ajouter_compte

    Demander le site ou service
    Vérifier qu’il n’existe pas déjà dans les comptes enregistrés

    Afficher la liste des catégories disponibles
    Demander la catégorie du site

    Demander le nom du compte

    Demander l’adresse email
    Vérifier le format de l’email

    Demander si le mot de passe doit être généré ou saisi manuellement
        SI généré
            Appeler la fonction generer_mdp
        SINON
            Lire le mot de passe saisi
        FIN SI

    Analyser automatiquement la force du mot de passe

    Générer la date de création (date du jour)

    Créer un dictionnaire contenant :
        - site
        - catégorie
        - nom du compte
        - email
        - mot de passe
        - date de création
        - score de sécurité

    Ajouter le dictionnaire à la liste des comptes

    Sauvegarder la liste des comptes dans le fichier JSON

    Afficher un message de confirmation

FIN FONCTION


# 4. LISTER LES COMPTES

FONCTION lister_comptes

    Charger les comptes depuis le fichier de sauvegarde

    SI aucun compte n’existe
        Afficher "Aucun compte enregistré"
    SINON
        Afficher les comptes sous forme de tableau formaté :
            - site
            - catégorie
            - score
            - date de création
    FIN SI

FIN FONCTION


# 5. RECHERCHER UN COMPTE

FONCTION rechercher_compte

    Demander le terme de recherche

    Parcourir la liste des comptes

    Sélectionner les comptes dont :
        - le site contient le terme
        OU
        - la catégorie contient le terme

    SI aucun résultat trouvé
        Afficher "Aucun compte trouvé"
    SINON
        Afficher les résultats sous forme de tableau
    FIN SI

FIN FONCTION


# 6. CALCULER ET AFFICHER LES STATISTIQUES

FONCTION calculer_stats

    Calculer :
        - le nombre total de comptes
        - la répartition des comptes par catégorie
        - le score moyen de sécurité
        - le nombre de mots de passe faibles
        - le nombre de mots de passe de plus de 90 jours

    Afficher un résumé clair des statistiques

FIN FONCTION


# 7. QUITTER LE PROGRAMME

FONCTION quitter_programme

    Sauvegarder les données si nécessaire

    Afficher un message de fermeture

    Terminer proprement l’exécution du programme

FIN FONCTION


# FIN DU PROGRAMME

FIN PROGRAMME
