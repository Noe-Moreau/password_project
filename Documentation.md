# Documentation - Gestionnaire de Mots de Passe

## Table des matières


1. [Vue d'ensemble](#vue-densemble)
2. [Installation et lancement](#installation-et-lancement)
3. [Structure du projet](#structure-du-projet)
4. [Fonctionnalités](#fonctionnalités)
5. [Guide d'utilisation](#guide-dutilisation)
6. [Pseudo-code](#pseudo-code)
7. [Détails techniques](#détails-techniques)
8. [Sécurité](#sécurité)

---

## Vue d'ensemble

Le gestionnaire de mots de passe est une application console écrite en Python permettant de générer, stocker et analyser des mots de passe de manière sécurisée. L'application offre une interface en ligne de commande intuitive pour gérer tous vos comptes en ligne.

### Caractéristiques principales

- Génération de mots de passe sécurisés personnalisables
- Analyse de la force des mots de passe
- Stockage chiffré des informations de compte
- Recherche et filtrage des comptes
- Statistiques détaillées sur la sécurité
- Sauvegarde automatique au format JSON

---

## Installation et lancement

### Prérequis

- Python 3.10 ou supérieur
- Aucune dépendance externe (utilise uniquement la bibliothèque standard)

### Lancement

```bash
python gestionnaire_mdp.py
```

Le programme créera automatiquement un fichier `mots_de_passe.json` pour stocker les données.

---

## Structure du projet

### Fichiers

- `gestionnaire_mdp.py` : fichier principal contenant tout le code
- `mots_de_passe.json` : fichier de sauvegarde (créé automatiquement)

### Architecture du code

Le code est organisé en plusieurs sections :

1. **Constantes et configuration**
   - `FICHIER` : nom du fichier de sauvegarde
   - `DICTIONNAIRE_FAIBLE` : liste de mots de passe courants à éviter

2. **Fonctions utilitaires**
   - `charger_donnees()` : chargement des données JSON
   - `sauvegarder()` : sauvegarde des données JSON
   - `afficher_tableau()` : affichage formaté
   - `_input_oui_non()` : validation des entrées O/N
   - `_input_longueur()` : validation de longueur

3. **Fonctions métier**
   - `generer_mdp()` : génération de mots de passe
   - `analyser_force()` : analyse de sécurité
   - `ajouter_compte()` : ajout de nouveaux comptes
   - `lister_comptes()` : affichage des comptes
   - `rechercher()` : recherche de comptes
   - `calculer_stats()` : statistiques détaillées
   - `quitter()` : fermeture du programme

4. **Interface utilisateur**
   - `afficher_menu()` : affichage du menu
   - `menu_principal()` : boucle principale

---

## Fonctionnalités

### 1. Génération de mot de passe

Génère un mot de passe aléatoire sécurisé selon vos critères.

**Paramètres configurables :**

- Longueur : entre 8 et 64 caractères
- Types de caractères :
  - Lettres minuscules (a-z)
  - Lettres majuscules (A-Z)
  - Chiffres (0-9)
  - Caractères spéciaux (!@#$%^&*()...)
- Option d'exclusion des caractères ambigus (0/O, l/1, I)

**Sécurité :** Utilise `random.SystemRandom()` pour un générateur cryptographiquement sécurisé.

### 2. Analyse de la force

Évalue la robustesse d'un mot de passe selon 8 critères.

**Critères d'évaluation :**

1. Longueur minimale de 8 caractères
2. Longueur recommandée de 12+ caractères
3. Présence de majuscules
4. Présence de minuscules
5. Présence de chiffres
6. Présence de caractères spéciaux
7. Absence de caractères consécutifs identiques
8. Absence du mot de passe dans le dictionnaire commun

**Score :** De 0 à 100, avec classification :

- 0-25 : Très faible
- 26-50 : Faible
- 51-75 : Moyen
- 76-100 : Très fort

### 3. Ajout de compte

Enregistre un nouveau compte avec toutes ses informations.

**Informations collectées :**

- Site ou service (ex: gmail.com)
- Catégorie (8 options prédéfinies)
- Nom du compte
- Adresse email (avec validation de format)
- Mot de passe (saisi manuellement ou généré)

**Catégories disponibles :**

- Réseaux sociaux
- Email
- Banque
- Shopping
- Travail
- Divertissement
- Cloud
- Autre

**Validations :**

- Vérification du format email (@, domaine valide)
- Détection des doublons de site
- Alerte si le mot de passe est faible (score <= 50)
- Génération automatique de la date de création

### 4. Liste des comptes

Affiche tous les comptes enregistrés sous forme de tableau.

**Colonnes affichées :**

- Site
- Catégorie
- Nom du compte
- Adresse email
- Date de création

### 5. Recherche de compte

Recherche des comptes par site ou catégorie.

**Fonctionnement :**

- Recherche insensible à la casse
- Correspondance partielle dans le site ou la catégorie
- Affichage des résultats sous forme de tableau
- Nombre de résultats trouvés

### 6. Statistiques

Affiche des statistiques détaillées sur la sécurité.

**Métriques calculées :**

- Nombre total de comptes
- Répartition par catégorie (nombre et pourcentage)
- Score moyen de sécurité
- Comptes avec mots de passe faibles (score <= 50)
- Comptes avec mots de passe anciens (> 90 jours)
- État général de la sécurité

**Classification de l'état général :**

- Excellent : score moyen >= 75
- Bon : score moyen >= 60
- Moyen : score moyen >= 40
- Faible : score moyen < 40

### 7. Quitter

Ferme proprement le programme après confirmation.

---

## Guide d'utilisation

### Démarrage rapide

1. Lancez le programme
2. Choisissez une option du menu (1-7)
3. Suivez les instructions à l'écran

### Scénario : Créer un nouveau compte

```
1. Sélectionnez l'option 3 (Ajouter un compte)
2. Entrez le nom du site (ex: facebook.com)
3. Choisissez la catégorie (ex: 1 pour Réseaux sociaux)
4. Entrez le nom du compte (ex: john.doe)
5. Entrez l'adresse email (ex: john@example.com)
6. Choisissez de générer un mot de passe (O/N)
   - Si O : configurez les paramètres de génération
   - Si N : saisissez votre mot de passe
7. Validez l'ajout même si le score est faible (optionnel)
8. Le compte est enregistré automatiquement
```

### Scénario : Générer un mot de passe fort

```
1. Sélectionnez l'option 1 (Générer un mot de passe)
2. Entrez la longueur souhaitée (ex: 16)
3. Incluez tous les types de caractères (O pour chaque)
4. Excluez les caractères ambigus (O recommandé)
5. Le mot de passe est généré et affiché
```

### Scénario : Vérifier la sécurité

```
1. Sélectionnez l'option 6 (Afficher les statistiques)
2. Consultez le score moyen et les comptes à risque
3. Pour chaque compte faible, notez le site
4. Utilisez l'option 3 pour mettre à jour ces comptes
```

---

## Pseudo-code

```
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

```

---

## Détails techniques

### Format de stockage

Les données sont stockées au format JSON avec la structure suivante :

```json
[
  {
    "site": "gmail.com",
    "categorie": "Email",
    "nom_compte": "john.doe",
    "email": "john@example.com",
    "mot_de_passe": "Xy9#mK2$pL4@",
    "score": 87,
    "date_creation": "2026-01-19"
  }
]
```

### Validation des entrées

**Email :**
- Doit contenir un @
- Doit contenir un point après le @

**Longueur de mot de passe :**
- Minimum : 8 caractères
- Maximum : 64 caractères

**Dates :**
- Format : YYYY-MM-DD
- Générées automatiquement avec `datetime.now()`

### Gestion des erreurs

Le programme gère les erreurs suivantes :

- Fichier JSON corrompu : réinitialisation automatique
- Interruption clavier (Ctrl+C) : fermeture propre
- Entrées invalides : redemande avec message d'erreur
- Exceptions inattendues : message d'erreur et continuation

---

## Sécurité

### Points forts

1. **Générateur cryptographique** : Utilise `random.SystemRandom()` au lieu de `random.Random()`
2. **Validation stricte** : Vérification de tous les formats d'entrée
3. **Analyse multi-critères** : 8 critères pour évaluer la force
4. **Détection de mots faibles** : Dictionnaire de 30 mots de passe courants
5. **Alertes proactives** : Avertissement pour les mots de passe faibles et anciens

### Points d'attention

1. **Stockage non chiffré** : Les mots de passe sont stockés en clair dans le fichier JSON
2. **Pas d'authentification** : Aucun mot de passe maître pour protéger l'accès
3. **Pas de sauvegarde automatique** : Une seule copie des données
4. **Affichage en clair** : Les mots de passe sont visibles à l'écran