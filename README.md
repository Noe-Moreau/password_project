# Gestionnaire de Mots de Passe Sécurisé

## Présentation

Ce projet est un **gestionnaire de mots de passe en ligne de commande**, développé en **Python**, permettant de **générer**, **analyser**, **stocker** et **gérer** des mots de passe de manière sécurisée.

L'application vise à sensibiliser aux bonnes pratiques de cybersécurité tout en mettant en œuvre des concepts fondamentaux de programmation : gestion de fichiers JSON, validation des entrées, analyse algorithmique, structures de données et modularité du code.

---

## Fonctionnalités clés

* Génération de mots de passe forts et personnalisables
* Analyse avancée de la sécurité des mots de passe
* Gestion complète de comptes (ajout, liste, recherche)
* Statistiques détaillées sur la sécurité globale
* Sauvegarde automatique des données au format JSON
* Interface utilisateur claire en ligne de commande

---

## Prérequis

* Python **3.10** ou supérieur
* Aucune bibliothèque externe requise (bibliothèque standard uniquement)

---

## Installation et lancement

1. Clonez ou téléchargez le projet
2. Placez-vous dans le dossier du projet
3. Lancez le programme :

```bash
python gestionnaire_mdp.py
```

Au premier lancement, le fichier `mots_de_passe.json` est créé automatiquement.

---

## Structure du projet

```
.
├── gestionnaire_mdp.py   # Programme principal
├── mots_de_passe.json   # Données sauvegardées (auto-généré)
├── README.md
└── documentation.md
```

Le code est organisé en sections claires :

* constantes et configuration
* fonctions utilitaires
* logique métier
* interface utilisateur

---

## Menu principal

L'application propose **7 options** :

1. Générer un mot de passe
2. Analyser la force d’un mot de passe
3. Ajouter un compte
4. Lister les comptes
5. Rechercher un compte
6. Afficher les statistiques
7. Quitter le programme

---

## Génération de mots de passe

Les mots de passe peuvent être générés selon vos critères :

* Longueur configurable : **8 à 64 caractères**
* Types de caractères au choix :

  * Lettres minuscules
  * Lettres majuscules
  * Chiffres
  * Caractères spéciaux
* Option pour exclure les caractères ambigus (`0/O`, `l/1`, `I`)

 Le générateur utilise `random.SystemRandom()` pour une génération cryptographiquement sécurisée.

---

## Analyse de la force

Chaque mot de passe est évalué selon **8 critères de sécurité**, incluant :

* Longueur
* Diversité des caractères
* Présence de caractères spéciaux
* Entropie estimée
* Vérification contre un dictionnaire de mots de passe courants

### Score de sécurité

* **0 – 25** : Très faible
* **26 – 50** : Faible
* **51 – 75** : Moyen
* **76 – 100** : Très fort

---

## Gestion des comptes

Chaque compte enregistré contient :

* Site ou service
* Catégorie
* Nom du compte
* Adresse email
* Mot de passe
* Score de sécurité
* Date de création

### Catégories disponibles

* Réseaux sociaux
* Email
* Banque
* Shopping
* Travail
* Divertissement
* Cloud
* Autre

Des validations automatiques sont appliquées (format email, doublons, alertes de sécurité).

---

## Recherche et affichage

* **Liste des comptes** : affichage sous forme de tableau
* **Recherche** : par site ou catégorie

  * Insensible à la casse
  * Correspondance partielle

---

## Statistiques de sécurité

L'application calcule et affiche :

* Nombre total de comptes
* Répartition par catégorie
* Score moyen de sécurité
* Comptes avec mots de passe faibles (score ≤ 50)
* Comptes avec mots de passe anciens (> 90 jours)
* État général de la sécurité
o
### État global

* Excellent : ≥ 75
* Bon : ≥ 60
* Moyen : ≥ 40
* Faible : < 40

---

## Format de stockage

Les données sont stockées localement au format **JSON** :

```json
{
  "site": "gmail.com",
  "categorie": "Email",
  "nom_compte": "john.doe",
  "email": "john@example.com",
  "mot_de_passe": "Xy9#mK2$pL4@",
  "score": 87,
  "date_creation": "2026-01-19"
}
```

---

## Sécurité


* Génération cryptographiquement sécurisée
* Validation stricte des entrées utilisateur
* Analyse multi-critères des mots de passe
* Alertes pour mots de passe faibles ou anciens

---

## Auteurs

- Ayman Tisguini
- Enzo Graveline
- Noé Moreau