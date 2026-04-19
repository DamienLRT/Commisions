import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Synthèse des travaux sur les commissions",
    layout="wide"
)

st.title("Synthèse des travaux sur les commissions")

# -------------------------
# SIDEBAR MENU
# -------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Aller vers :",
    [
        "À propos du projet",
        "Introduction",
        "Réel vs Théorique",
        "Standard vs Sur Mesure",
        "Inspecteurs",
        "Rals vs Non Rals",
        "Segmentation",
        "Conclusion"
    ]
)
# À PROPOS DU PROJET
# À PROPOS DU PROJET
if page == "À propos du projet":
    st.header("À propos du projet")

    st.markdown("""
    ## Contexte

    Ce projet s’inscrit dans une démarche d’analyse des commissions dans un environnement de gestion déléguée.  
    L’objectif est de comprendre la structure des commissions et d’identifier les principaux leviers d’analyse et de pilotage tarifaire.

 Les données ont été anonymisées et partiellement randomisées afin de garantir la confidentialité des informations sensibles tout en préservant leur structure statistique.

Ce projet respecte les principes du RGPD :
- Suppression des données directement identifiantes
- Traitement strictement analytique des données

    ---

    ## Objectifs

    - Analyser les écarts entre théorie et réalité des commissions  
    - Étudier l’impact des inspecteurs et des DG  
    - Comparer les contrats standards et sur mesure  
    - Analyser la répartition RALS / non RALS  
    - Étudier l’effet de la segmentation  

    ---

    ## Données utilisées

    Les données utilisées proviennent de sources multiples :
    - Fichiers plats (CSV, exports internes)
    - Bases de données en ligne

    Un travail d’unification des sources a été réalisé afin de garantir la cohérence des analyses.

    Les données ont également été **anonymisées et partiellement randomisées** afin de préserver la confidentialité des informations sensibles tout en conservant leur structure statistique.

    Un travail de standardisation des noms et référentiels a été effectué afin d’assurer l’homogénéité entre les différentes sources.

    ---

    ## Méthodologie

    - Analyse exploratoire des données (EDA)
    - Nettoyage et préparation des données
    - Uniformisation des référentiels multi-sources
    - Construction de visualisations analytiques
    - Interprétation des résultats selon plusieurs axes métier

    ---

    ## Outils utilisés

    - Python (pandas, numpy)
    - Streamlit (dashboard interactif)
    - Plotly (visualisation de données)
    - HTML intégré pour certains graphiques avancés
    - Gestion de données multi-sources (fichiers plats + bases en ligne)

    ---

    ## Périmètre d’analyse

    - Commissions santé et prévoyance  
    - Contrats standards et sur mesure  
    - RALS / non RALS  
    - Inspecteurs et DG  
    - Segmentation des portefeuilles  

    ---

    ## Objectif final

    Fournir une analyse structurée permettant de mieux comprendre les mécanismes de commissions et d’identifier des pistes d’amélioration pour la construction d’une politique tarifaire cohérente.

    ---

    ## Limites

    Malgré la richesse des analyses, les données disponibles ne permettent pas d’établir des relations causales fortes entre les différentes variables étudiées.
    """)


# -------------------------
# PAGES
# -------------------------

# INTRODUCTION
if page == "Introduction":
    st.header("Introduction")

    st.write("""
    Le but de cette étude est d’identifier les actes à déléguer ainsi que la rémunération associée. Nous
allons analyser l’impact du standard sur les commissions versées, puis étudier la répartition RALS /
non RALS dans les commissions versées. Enfin, la segmentation sera également examinée.
L’ensemble de ces analyses de données vise à définir un schéma permettant d’élaborer une politique
tarifaire adaptée.
Malheureusement, les données dont nous disposons actuellement ne nous permettent pas de parvenir à
une conclusion pleinement satisfaisante.
    """)

# NON RALS
elif page == "Réel vs Théorique":
    st.header("Comparatifs Réel vs Théorique – Non Rals")

    st.subheader("Règles & hypothèses")
    st.markdown("""
    - Contrats en gestion déléguée  
    - Santé & Prévoyance  
    - Contrats actifs  
    - Non RALS  
    """)

    st.image("images/reel_vs_mandat_sante.png", caption="Taux standards vs taux mandat")
    st.image("images/reel_vs_mandat_prev.png", caption="Taux prev standards vs taux mandats")

    st.markdown("""
    On constate que plusieurs DG bénéficient d’un taux de commission supérieur à leur taux mandat.  

    Suite à cette première observation, il est essentiel :
    - d’identifier les contrats concernés  
    - de calculer les montants de commissions versées  
    """)

    st.image("images/Comparatif total vs théorique.png", caption="Taux prev standards vs taux mandats")
    st.markdown("""
**Lecture du graphique**

- Les barres **violettes** représentent les commissions théoriques  
- Les barres **grises** représentent les commissions réellement versées  
- La différence entre ces deux barres correspond à l’écart entre théorie et réalité  

**Conclusion**

Les écarts observés restent limités et ne justifient pas d’action corrective de la part de GGVie.
""")

# STANDARD VS SUR MESURE
elif page == "Standard vs Sur Mesure":
    st.header("Comparatif Standard vs Sur Mesure")

    st.write("""Nous allons nous concentrer sur le portefeuille des huit premiers DG (en pourcentage de notre chiffre
d’affaires). Nous examinerons la répartition des contrats (standard et sur mesure) de chaque DG par
rapport à son taux mandat et au taux de référence.""")

    st.image("images/tableau.png", caption="Taux prev standards vs taux mandats")

    st.write("""Sur le tableau ci-dessus, on remarque que dans le domaine santé, les contrats sur mesure sont moins
commissionnés que les contrats standards alors que dans le domaine de la prévoyance c’est le constat
inverse.""")

    st.image("images/STD vs SM_sante.png", caption="Standard vs Surmesure sante")
    st.image("images/STD vs SM_prevoyance.png", caption="Standard vs Surmesure prev")

    st.markdown("""
    <p>
    Les graphiques ci-dessus, on constate que les montants de commissions versés sur les contrats
    standards sont négligeables par rapport à ceux des contrats sur mesure.
    </p>
    Pour la suite de l’étude, nous retiendrons l’hypothèse suivante :
    <p style="text-align: center;">
    <b>Commissions totales ~ Commissions sur mesures</b>
    </p>
    """, unsafe_allow_html=True)
# INSPECTEURS

elif page == "Inspecteurs":
    st.header("📊 Impact des inspecteurs")

    # ===================== SANTE =====================
    st.markdown("## 🩺 Santé")

    # Graphique 1
    with open("images/Taux_sante_vs_insp.html", "r", encoding="utf-8") as f:
        html1 = f.read()

    st.subheader("Taux santé vs Inspecteur")
    components.html(html1, height=750)


    st.markdown("---")

    # ===================== PREVOYANCE =====================
    st.markdown("## 🛡️ Prévoyance")

    # Graphique 3
    with open("images/Taux_prevoyance_vs_insp.html", "r", encoding="utf-8") as f:
        html3 = f.read()

    st.subheader("Taux prévoyance vs Inspecteur")
    components.html(html3, height=750)



    # ===================== CONCLUSION =====================
    st.markdown("---")

    st.markdown("## Conclusion")

    st.markdown("""
    • Les taux de commission présentent une forte variabilité, y compris au sein d’un même DG  
    • Aucun inspecteur n’applique une politique homogène  
    • Aucune corrélation claire entre inspecteur, DG et segmentation  

    Les taux semblent principalement déterminés par les négociations contractuelles.
    """)

# RALS VS NON RALS
elif page == "Rals vs Non Rals":
    st.header("Comparaison Rals / Non Rals")

    # Graphique global
    st.image("images/Rals_vs_nonrals.png")

    # Analyse
    st.markdown("""
    En prévoyance, les montants issus des commissions Rals sont globalement équivalents 
    à ceux des commissions non Rals.

    En santé, les commissions non Rals sont majoritaires. Toutefois, les commissions Rals 
    représentent également une part significative des montants versés.
    """)

    st.markdown("---")

    # Détail par catégorie
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Santé")
        st.image("images/rals_nonral_sante.png")

    with col2:
        st.subheader("Prévoyance")
        st.image("images/rals_vs_nonrals_prev.png")

    st.markdown("---")

    # Conclusion
    st.markdown("""
    ### Conclusion

    • En prévoyance : répartition équilibrée entre Rals et non Rals  
    • En santé : prédominance des non Rals, avec une contribution notable des Rals  

    Les commissions Rals constituent un levier significatif dans les deux segments.
    """)

# SEGMENTATION
elif page == "Segmentation":
    st.header("Segmentation")

    # ===================== SANTE =====================
    st.markdown("## Santé")

    with open("images/Taux_Sante_vs_Seg.html", "r", encoding="utf-8") as f:
        html2 = f.read()

    st.subheader("Taux santé vs Segmentation")
    components.html(html2, height=750)

    # ===================== PREVOYANCE =====================
    st.markdown("## Prévoyance")

    with open("images/Taux_Prevoyance_vs_Seg.html", "r", encoding="utf-8") as f:
        html4 = f.read()

    st.subheader("Taux prévoyance vs Segmentation")
    components.html(html4, height=750)

    st.markdown("---")

    # ===================== ANALYSE =====================
    st.markdown("## Analyse")

    st.markdown("""
    L’analyse des graphiques ne met pas en évidence de relation claire entre la segmentation 
    et les taux de commission.

    Cette absence de pattern s’explique principalement par une forte disparité des taux 
    entre les différents DG.

    Toutefois, certains DG semblent privilégier des segments spécifiques sur lesquels 
    les taux appliqués sont significativement supérieurs aux taux de référence.
    """)

# CONCLUSION

elif page == "Conclusion":
    st.header("Conclusion")

    st.markdown("""
    Cette étude a permis de mettre en évidence les points suivants :

    • Les commissions issues des contrats standards restent marginales par rapport au volume global  
    • Les commissions RALS sont plus significatives que celles versées directement aux DG  
    • Il n’existe pas de corrélation entre le segment délégué et le taux de commission  
    • Les mandats constituent une première base d’analyse, mais restent insuffisants pour définir une politique tarifaire robuste  

    ### Limites de l’analyse

    Avec les données disponibles, il n’a pas été possible de définir une politique tarifaire fiable.

    Une étude complémentaire sur le terrain, en collaboration avec les équipes de gestion et d’inspection, 
    serait nécessaire afin d’estimer précisément le coût de certaines opérations déléguées.""")
