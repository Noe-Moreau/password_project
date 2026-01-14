# Gestionnaire de Mots de Passe Sécurisé

## Description du projet

Ce projet consiste à développer un **gestionnaire complet de mots de passe** en ligne de commande python.  
Il permet de **générer**, **stocker**, **analyser** et **gérer** des mots de passe de manière sécurisée, tout en offrant des **statistiques globales** et des **alertes de sécurité**.

L'objectif est de sensibiliser aux bonnes pratiques de cybersécurité tout en mettant en œuvre des concepts clés de programmation : structures de données, fonctions, gestion des erreurs, fichiers JSON et analyse algorithmique.

---

## Fonctionnalités principales

### Menu principal (7 options)
1. Générer un mot de passe
2. Analyser la force d’un mot de passe
3. Ajouter un compte
4. Lister les comptes
5. Rechercher un compte
6. Afficher les statistiques
7. Quitter le programme

---

## Génération avancée de mots de passe

- Longueur configurable : **8 à 64 caractères**
- Choix des types de caractères :
  - Lettres minuscules
  - Lettres majuscules
  - Chiffres
  - Caractères spéciaux
- Option d’exclusion des caractères ambigus :
  - `0 / O`
  - `l / 1`

---

## Analyse de la force des mots de passe

Chaque mot de passe reçoit un **score de 0 à 100**, basé sur :
- Longueur
- Diversité des types de caractères
- Entropie estimée
- Présence dans un dictionnaire de mots de passe courants

### Interprétation du score :
- `0 – 39` :  Faible
- `40 – 69` :  Moyen
- `70 – 84` :  Fort
- `85 – 100` :  Très fort

---

## Gestion des comptes

Chaque compte contient :
- Site / service (ex : `gmail.com`)
- Catégorie :
  - Réseaux sociaux
  - Banque
  - Email
  - Travail
  - Autre
- Nom du compte
- Adresse email associée
- Mot de passe
- Date de création
- Score de sécurité

**Structure des données :**
```python
{
  "site": "gmail.com",
  "categorie": "Email",
  "nom_compte": "Nomdecompte",
  "email": "exemplemail1@mail.com",
  "mdp": "MotDePasse123!",
  "date_creation": "2025-01-10",
  "score": 87
}