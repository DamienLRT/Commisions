# Analyse des commissions – Dashboard Streamlit

## Présentation du projet

Ce projet est un dashboard interactif développé avec **Streamlit** permettant d’analyser les mécanismes de commissions dans un environnement de gestion déléguée.

L’objectif est de comprendre la structure des commissions, d’identifier les facteurs explicatifs des écarts observés et de fournir une base d’aide à la décision pour la définition d’une politique tarifaire.

---

## Problématique métier

Dans un contexte de gestion déléguée, les commissions versées présentent des variations importantes selon les contrats, les inspecteurs, les segments et les typologies de produits.

Ce projet vise à répondre aux questions suivantes :
- Les commissions sont-elles alignées avec les règles théoriques ?
- Quel est l’impact des inspecteurs et des DG sur les taux appliqués ?
- Existe-t-il une structure cohérente entre segmentation et niveaux de commission ?
- Quelle est la part des contrats standards vs sur mesure dans les volumes de commissions ?
- Quel est le rôle des RALS dans la structure globale des rémunérations ?

---

## Données utilisées

Les données utilisées proviennent de sources hétérogènes :
- Fichiers plats (exports internes, CSV)
- Bases de données en ligne

Un travail de **consolidation multi-sources** a été réalisé afin d’assurer la cohérence des analyses.

### Traitements appliqués :
- Anonymisation des données sensibles
- Randomisation partielle des variables pour préserver la structure statistique
- Uniformisation des référentiels et des nomenclatures
- Nettoyage et standardisation des variables métiers

### Conformité :
Ce projet respecte les principes du **RGPD** :
- Suppression des données identifiantes
- Traitement strictement analytique des données
- Absence d’exploitation de données personnelles réelles

---

## Méthodologie

L’approche adoptée repose sur une démarche analytique structurée :

1. **Exploration des données (EDA)**
2. **Nettoyage et préparation des données**
3. **Harmonisation des sources multi-systèmes**
4. **Analyse comparative multi-axes**
   - Inspecteurs
   - DG
   - Segmentation
   - Type de contrat
   - RALS / non RALS
5. **Visualisation des résultats**
6. **Interprétation métier des tendances observées**

---

## Outils et technologies

- Python (pandas, numpy)
- Streamlit (dashboard interactif)
- Plotly (visualisation de données)
- HTML intégré pour visualisations avancées
- Gestion de données multi-sources

---

## Résultats clés

- Forte variabilité des taux de commission au sein des mêmes structures
- Absence de corrélation claire entre inspecteurs, DG et segmentation
- Poids limité des contrats standards dans les volumes de commissions
- Importance significative des commissions RALS dans certains segments
- Structure globale fortement influencée par les négociations contractuelles

---

## Limites de l’analyse

- Absence de causalité directe entre les variables étudiées
- Données partiellement agrégées limitant certaines analyses fines
- Besoin d’informations terrain complémentaires pour affiner les conclusions

---

## Perspectives

Pour approfondir l’analyse, les axes suivants pourraient être explorés :
- Intégration de données terrain (gestion / inspection)
- Modélisation prédictive des commissions
- Construction d’un modèle de politique tarifaire automatisée
- Analyse du coût réel des actes délégués

---

## Structure du projet
