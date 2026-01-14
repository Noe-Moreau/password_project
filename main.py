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
def generer_mdp():
    pass


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
