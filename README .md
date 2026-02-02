# ♻️ POC Bokashi × Rekarbon — Maître Composteur MRV Platform

**v3.0 Premium — Suivi 100 Foyers Individuels**

> Plateforme MRV (Monitoring, Reporting, Verification) pour maître composteur professionnel Bokashi à La Réunion 🇷🇪

---

## 🎯 Présentation

POC vitrine développé pour **Mr MAILLOT**, maître composteur professionnel, démontrant la capacité de la technologie **Rekarbon** à piloter un réseau Bokashi multi-sites avec certification environnementale.

### Deux volets complémentaires

| Volet | Cible | Crédits | Objectif |
|-------|-------|---------|----------|
| **Sites Professionnels** | Restaurants, cantines, supermarchés, marchés, quartiers | ✅ Carbone + Eau + Biodiversité | Génération de revenus via crédits certifiés |
| **Suivi Individuels** | 100 foyers particuliers réunionnais | ❌ Pas de crédits | Suivi de proximité, sensibilisation, maillage territorial |

---

## 🚀 Démarrage Rapide

### Prérequis

- Python 3.9+

### Installation

```bash
git clone https://github.com/VOTRE-USERNAME/poc-bokashi-maillot-v3.git
cd poc-bokashi-maillot-v3
pip install -r requirements.txt
```

### Lancement

```bash
streamlit run app_bokashi_maillot_v3_suivi.py
```

L'application s'ouvre automatiquement dans le navigateur sur `http://localhost:8501`

---

## 📱 Pages de l'Application

| Page | Description |
|------|-------------|
| 🏠 **Accueil** | Vue d'ensemble, triple valorisation (Compost + Jus + Crédits), produits EM |
| 📊 **Dashboard Live** | Monitoring temps réel, courbes fermentation, production par site |
| 📍 **Sites Clients** | 5 sites professionnels déployés, détail contrats et capacités |
| 👥 **Suivi Individuels** | **NOUVEAU** — 100 foyers Bokashi, filtres, graphiques, top producteurs |
| 🧪 **Lots en Cours** | Suivi des batches par phase (activation → fermentation → maturation) |
| 💎 **Crédits Multi-Impact** | Carbone (€45/tCO2) + Eau (€3/m³) + Biodiversité (€500/ha) |
| 📈 **Business Case** | Projection financière annuelle avec croissance mensuelle |
| 🎮 **Simulation** | Démonstration collecte MRV avec signatures CERBERE |
| 🔧 **Architecture** | Schéma technique Edge-Native (Raspberry Pi 5 → Cloud → Marchés) |

---

## 👥 Onglet Suivi Individuels — Détail

L'onglet **Suivi Individuels** gère 100 foyers particuliers réunionnais pour le compostage Bokashi de proximité.

### Fonctionnalités

- **KPIs globaux** : foyers actifs, en pause, nouveaux, alertes (>30 jours sans collecte EM)
- **Tableau de suivi** : nom, commune, quartier, type de bac, production hebdo, score qualité, statut
- **Filtres** : par statut, commune, type de bac, alertes
- **Graphiques** : répartition géographique, statuts, scores qualité, types de bacs
- **Top 10** des foyers les plus productifs
- **100 noms à consonance réunionnaise** : Hoarau, Payet, Rivière, Grondin, Boyer, Dijoux, Nativel, Lauret, Séraphine, Caroupaye, Gonthier, Ethève...
- **23 communes** de La Réunion avec quartiers réels

### Données simulées par foyer

| Champ | Description |
|-------|-------------|
| ID | IND-001 à IND-100 |
| Nom / Prénom | Noms réunionnais authentiques |
| Commune / Quartier | Géolocalisation réelle La Réunion |
| Type de bac | Seau 20L, Bac 50L, Double seau 20L |
| Foyer | 1 à 7 personnes |
| Production | 3 à 15 kg/semaine |
| Score qualité | /10 (qualité fermentation) |
| Lots terminés | Historique de production |
| Statut | Actif / En pause / Nouveau |
| Alerte | ⚠️ si >30 jours sans collecte EM |

---

## 💎 Modèle Économique (Sites Pro)

```
Triple Valorisation Bokashi:
├── 🌱 Compost enrichi EM ─────── €120/tonne
├── 💧 Jus Bokashi (engrais) ──── €8/litre
└── 💎 Crédits Multi-Impact ───── €50-100/tonne
    ├── Carbone: 0.7 tCO2 séquestré + 0.5 tCO2 évité par tonne
    ├── Eau: économie irrigation 30%
    └── Biodiversité: microbiome sol enrichi

Partage crédits:
├── 70% Maître Composteur (génère les crédits)
└── 30% Rekarbon (certification MRV + marchés)
```

---

## 🔐 Sécurité — CERBERE

- **Signatures** : Ed25519
- **Hashing** : SHA-256
- **Chaîne** : Hash-chain locale
- **Standards** : ISO 14064-2, VCS Bokashi, Gold Standard

---

## 🛠️ Stack Technique

| Composant | Technologie |
|-----------|-------------|
| Frontend | Streamlit |
| Graphiques | Plotly |
| Data | Pandas, NumPy |
| Edge Computing | Raspberry Pi 5 (8GB) + SSD NVMe |
| Capteurs | DS18B20, SHT31, pH, CO2/NH3/CH4 |
| Sécurité | CERBERE (Ed25519 + SHA-256) |
| Certification | ISO 14064-2 / VCS / Gold Standard |

---

## 📂 Structure

```
poc-bokashi-maillot-v3/
├── app_bokashi_maillot_v3_suivi.py   # Application principale (1 885 lignes)
├── requirements.txt                   # Dépendances Python
└── README.md                          # Documentation
```

---

## 📈 Résultats Attendus

| Métrique | 5 sites pro | + 100 foyers individuels |
|----------|-------------|--------------------------|
| Biomasse traitée | 550 kg/jour | + ~250 kg/semaine |
| Compost produit | 11.6 t/mois | — |
| Crédits/mois | ~€1 950 | Pas de crédits (suivi) |
| Contrats/mois | €1 950 | — |
| Personnes touchées | ~500 | + ~350 habitants |

---

## 🇷🇪 Contexte La Réunion

Ce POC s'inscrit dans la dynamique de réduction des déchets organiques à La Réunion, où le compostage Bokashi offre une alternative rapide (21 jours vs 3-6 mois) et compacte au compostage aérobie classique, tout en acceptant viandes et poissons.

---

**© 2026 Rekarbon SAS** — Zero AI, Pure Math — Edge-Native MRV Infrastructure

*Développé avec ❤️ à La Réunion*
