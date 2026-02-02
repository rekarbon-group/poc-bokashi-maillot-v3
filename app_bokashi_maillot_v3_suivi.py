#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
    BOKASHI MAÎTRE COMPOSTEUR × REKARBON - POC VITRINE PREMIUM V3
═══════════════════════════════════════════════════════════════════════════════
    Mr MAILLOT - Maître Composteur Professionnel
    La Réunion 🇷🇪 - Déploiement Multi-Sites + Suivi 100 Foyers Individuels
    
    © 2026 Rekarbon SAS - All Rights Reserved
    Triple Valorisation: Compost + Jus + Crédits Multi-Impact
═══════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import time
import json
import hashlib
import random

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Bokashi × Rekarbon MRV Platform",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════════════════════
# CSS PREMIUM DESIGN - BOKASHI GREEN THEME
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
/* BOKASHI BRAND COLORS */
:root {
    --bokashi-green: #2D5016;
    --bokashi-light: #4CAF50;
    --bokashi-dark: #1B3409;
    --earth-brown: #8B4513;
    --compost-gold: #DAA520;
    --water-blue: #0077B6;
    --bio-purple: #7B68EE;
    --energy-orange: #FF6600;
}

/* HIDE STREAMLIT DEFAULTS */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stDeployButton {display: none;}

/* CUSTOM SCROLLBAR */
::-webkit-scrollbar {width: 8px; height: 8px;}
::-webkit-scrollbar-track {background: #f1f1f1; border-radius: 4px;}
::-webkit-scrollbar-thumb {background: var(--bokashi-green); border-radius: 4px;}
::-webkit-scrollbar-thumb:hover {background: var(--bokashi-dark);}

/* HEADER PREMIUM */
.premium-header {
    background: linear-gradient(135deg, #2D5016 0%, #1B3409 50%, #0D1A04 100%);
    padding: 2.5rem 3rem;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 10px 40px rgba(45,80,22,0.3);
    position: relative;
    overflow: hidden;
}
.premium-header::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(76,175,80,0.15) 0%, transparent 60%);
    animation: shimmer 20s linear infinite;
}
@keyframes shimmer {
    0% {transform: rotate(0deg);}
    100% {transform: rotate(360deg);}
}

/* VALUE BOXES */
.value-box-green {
    background: linear-gradient(135deg, #2D5016 0%, #1B3409 100%);
    color: white;
    padding: 2rem;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 8px 32px rgba(45,80,22,0.3);
}
.value-box-light-green {
    background: linear-gradient(135deg, #4CAF50 0%, #388E3C 100%);
    color: white;
    padding: 2rem;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 8px 32px rgba(76,175,80,0.3);
}
.value-box-brown {
    background: linear-gradient(135deg, #8B4513 0%, #5D2E0C 100%);
    color: white;
    padding: 2rem;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 8px 32px rgba(139,69,19,0.3);
}
.value-box-gold {
    background: linear-gradient(135deg, #DAA520 0%, #B8860B 100%);
    color: #1a1a1a;
    padding: 2rem;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 8px 32px rgba(218,165,32,0.3);
}
.value-box-blue {
    background: linear-gradient(135deg, #0077B6 0%, #005F8C 100%);
    color: white;
    padding: 2rem;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 8px 32px rgba(0,119,182,0.3);
}
.value-box-purple {
    background: linear-gradient(135deg, #7B68EE 0%, #5B4ACE 100%);
    color: white;
    padding: 2rem;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 8px 32px rgba(123,104,238,0.3);
}
.value-box-orange {
    background: linear-gradient(135deg, #FF6600 0%, #CC5200 100%);
    color: white;
    padding: 2rem;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 8px 32px rgba(255,102,0,0.3);
}

/* METRIC CARDS */
.metric-premium {
    background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
    padding: 1.5rem;
    border-radius: 16px;
    border-left: 5px solid var(--bokashi-green);
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    margin: 0.5rem 0;
    transition: all 0.3s ease;
}
.metric-premium:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(45,80,22,0.15);
}

/* SITE CARDS */
.site-card {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    border: 2px solid #4CAF50;
    margin: 0.5rem 0;
    transition: all 0.3s ease;
    text-align: center;
}
.site-card:hover {
    border-color: #2D5016;
    transform: scale(1.02);
    box-shadow: 0 8px 25px rgba(45,80,22,0.15);
}

/* TRIPLE VALORISATION BOX */
.triple-box {
    background: linear-gradient(135deg, #2D5016 0%, #1B3409 50%, #8B4513 100%);
    color: white;
    padding: 2rem;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 8px 40px rgba(45,80,22,0.4);
    margin: 1.5rem 0;
    position: relative;
    overflow: hidden;
}
.triple-box::after {
    content: '♻️';
    position: absolute;
    top: 10px;
    right: 20px;
    font-size: 3rem;
    opacity: 0.3;
}

/* EM HIGHLIGHT BOX */
.em-box {
    background: linear-gradient(135deg, #DAA520 0%, #B8860B 50%, #8B4513 100%);
    color: white;
    padding: 2rem;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 8px 40px rgba(218,165,32,0.4);
    margin: 1.5rem 0;
}

/* BADGES */
.badge-fermentation {
    display: inline-block;
    background: linear-gradient(135deg, #FF6600, #CC5200);
    color: white;
    padding: 0.4rem 1rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    margin: 0.2rem;
}
.badge-ready {
    display: inline-block;
    background: linear-gradient(135deg, #4CAF50, #388E3C);
    color: white;
    padding: 0.4rem 1rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    margin: 0.2rem;
}
.badge-cert {
    display: inline-block;
    background: linear-gradient(135deg, #2D5016, #1B3409);
    color: white;
    padding: 0.4rem 1rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    margin: 0.2rem;
}

/* LIVE INDICATOR */
.live-indicator {
    display: inline-flex;
    align-items: center;
    background: #1a1a1a;
    color: #00ff00;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: bold;
}
.live-dot {
    width: 8px;
    height: 8px;
    background: #00ff00;
    border-radius: 50%;
    margin-right: 6px;
    animation: pulse 1.5s infinite;
}
@keyframes pulse {
    0%, 100% {opacity: 1; transform: scale(1);}
    50% {opacity: 0.5; transform: scale(1.2);}
}

/* TABS */
.stTabs [data-baseweb="tab-list"] {gap: 8px;}
.stTabs [data-baseweb="tab"] {background: #f0f2f6; border-radius: 8px 8px 0 0; padding: 10px 20px;}
.stTabs [aria-selected="true"] {background: #2D5016 !important; color: white !important;}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# BOKASHI DATA MODEL
# ═══════════════════════════════════════════════════════════════════════════════

MAITRE_COMPOSTEUR = {
    "name": "Mr MAILLOT",
    "title": "Maître Composteur Professionnel",
    "location": "La Réunion 🇷🇪",
    "certifications": ["Maître Composteur", "Formation EM", "Rekarbon Certified"],
    "experience_years": 5
}

SITES_CLIENTS = {
    "REST-001": {
        "name": "Restaurant Le Créole",
        "type": "restaurant",
        "address": "Saint-Denis, La Réunion",
        "containers": 2,
        "capacity_kg": 100,
        "daily_input_kg": 25,
        "monthly_fee": 150,
        "status": "active",
        "icon": "🍽️"
    },
    "CANT-002": {
        "name": "Cantine Lycée Bellepierre",
        "type": "ecole_cantine",
        "address": "Saint-Denis, La Réunion",
        "containers": 4,
        "capacity_kg": 200,
        "daily_input_kg": 75,
        "monthly_fee": 300,
        "status": "active",
        "icon": "🏫"
    },
    "SUPER-003": {
        "name": "Carrefour Saint-Pierre",
        "type": "supermarche",
        "address": "Saint-Pierre, La Réunion",
        "containers": 6,
        "capacity_kg": 500,
        "daily_input_kg": 150,
        "monthly_fee": 500,
        "status": "active",
        "icon": "🛒"
    },
    "MARCH-004": {
        "name": "Marché de Saint-Paul",
        "type": "marche",
        "address": "Saint-Paul, La Réunion",
        "containers": 8,
        "capacity_kg": 800,
        "daily_input_kg": 200,
        "monthly_fee": 600,
        "status": "active",
        "icon": "🏪"
    },
    "QUAR-005": {
        "name": "Quartier Les Camélias",
        "type": "quartier_residentiel",
        "address": "Saint-Denis, La Réunion",
        "containers": 10,
        "capacity_kg": 500,
        "daily_input_kg": 100,
        "monthly_fee": 400,
        "status": "active",
        "icon": "🏘️"
    }
}

BOKASHI_PROCESS = {
    "phases": {
        "chargement": {"duration_days": 0, "temp_range": "20-25°C", "color": "#FFD700"},
        "activation": {"duration_days": 2, "temp_range": "35-45°C", "color": "#FF6600"},
        "fermentation": {"duration_days": 14, "temp_range": "45-60°C", "color": "#E31E24"},
        "maturation": {"duration_days": 7, "temp_range": "40-50°C", "color": "#8B4513"},
        "pret": {"duration_days": 0, "temp_range": "25-35°C", "color": "#4CAF50"}
    },
    "optimal_conditions": {
        "temperature": "45-60°C",
        "humidity": "60-70%",
        "ph": "3.5-4.5",
        "duration": "21 jours"
    },
    "em_dosage": "5% du poids des déchets",
    "yield_pct": 70
}

EM_PRODUCTS = {
    "EM1": {"name": "EM1 Original", "price_l": 25, "usage": "Solution mère"},
    "EM2": {"name": "EM2 Activé", "price_l": 8, "usage": "Application terrain"},
    "EM3": {"name": "EM3 Bokashi", "price_l": 12, "usage": "Fermentation Bokashi"},
    "EM4": {"name": "EM4 Compost", "price_l": 10, "usage": "Maturation compost"}
}

MRV_CONSTANTS = {
    "carbon_price_eur": 45,  # €/tCO2
    "water_credit_eur_m3": 3,  # €/m³ économisé
    "biodiversity_credit_eur_ha": 500,  # €/ha amélioré
    "compost_price_eur_t": 120,  # €/tonne
    "juice_price_eur_l": 8,  # €/litre
    "rekarbon_share_pct": 30,  # Part Rekarbon sur crédits
    "sequestration_tco2_per_t": 0.7,  # tCO2 séquestré par tonne compost
    "avoided_tco2_per_t": 0.5  # tCO2 évité vs décharge
}

# ═══════════════════════════════════════════════════════════════════════════════
# BASE CLIENTS INDIVIDUELS BOKASHI - 100 FOYERS RÉUNIONNAIS
# Suivi uniquement - Pas de crédits environnementaux
# ═══════════════════════════════════════════════════════════════════════════════

def generate_clients_individuels():
    """Génère 100 clients individuels Bokashi avec noms réunionnais."""
    
    noms_reunion = [
        "HOARAU", "PAYET", "RIVIÈRE", "GRONDIN", "BOYER", "ROBERT", "MOREL",
        "FONTAINE", "HOAREAU", "LEBON", "DIJOUX", "NATIVEL", "LAURET", "MAILLOT",
        "VIDOT", "CADET", "BÈGUE", "TURPIN", "BARRET", "GONTHIER", "ETHÈVE",
        "PICARD", "TECHER", "DAMOUR", "GUICHARD", "COTTE", "VITRY", "LUCAS",
        "CLAIN", "FLORENT", "LOUISAR", "HIBON", "BARET", "SÉRAPHINE", "PITOU",
        "THAZAR", "CAROUPAYE", "SINAMA", "DALLEAU", "BUREL", "LALLEMAND",
        "DUPONT", "ARZUL", "BÉNARD", "CÉLIMÈNE", "DORSEUIL", "ÉTHÉMOND",
        "FÉRARD", "GAUVIN", "HÉMERY", "IVOULA", "JEANSON", "KICHENIN",
        "LÉPINAY", "MOUNIEN", "NIRLO", "OCTAVE", "PARNY", "QUINTRIC",
        "RAMSAMY", "SAUTRON", "TÉCHER", "ULYSSE", "VAVELIN", "WARO",
        "AIMÉE", "BOISVILLIERS", "COURTEAUD", "DESFORGES", "ÉLISABETH",
        "FOLIO", "GÉRARD", "HUBERT", "ISAUTIER", "JOSÉPHINE", "KERMABON",
        "LAPORTE", "MÉZINO", "NARASSIGUIN", "ORRÉ", "PAUSÉ", "RAMASSAMY",
        "SINAPIN", "TÉVANE", "VALLY", "ZITTE", "ABLEMONT", "BÉDIER",
        "CALICHIAMA", "DOUYÈRE", "ÉLOÏSE", "FOCK-YUEN", "GRONDIN-PAYET",
        "HAMON", "INSA", "JOURDAIN", "KORDJEE", "LEGROS"
    ]
    
    prenoms_reunion = [
        "Jean-Claude", "Marie-Claire", "Thierry", "José", "Jean-Pierre",
        "Christian", "Gérard", "Hervé", "Marcel", "Yannick", "Stéphane",
        "Frédéric", "David", "Éric", "Jean-Luc", "Joël", "Alain",
        "Marie-Thérèse", "Lucienne", "Simone", "Rose-Marie", "Jean-Marie",
        "Marie-Laure", "Jacqueline", "Monique", "Sylvie", "Nicole",
        "Marie-Josée", "Brigitte", "André", "René", "Georges", "Michel",
        "Dominique", "Jean-François", "Marie-Ange", "Marie-Line", "Isabelle",
        "Jean-Bernard", "Jean-Marc", "Philippe", "Daniel", "Jean-Yves",
        "Marie-Paule", "Thérèse", "Jean-Louis", "Marie-Rose", "Jocelyne",
        "Hubert", "Marie-Françoise", "Louis", "Paul", "Jean-René", "Sully",
        "Marie-Claude", "Yvette", "Émile", "Jean-Paul", "Bernadette",
        "Marie-Hélène", "Jean-Jacques", "Félix", "Graziella", "Élodie",
        "Marie-Noëlle", "Jean-Max", "Axel", "Ludovic", "Vanessa",
        "Marie-Alice", "Jean-Hugues", "Corinne", "Fabrice", "Véronique",
        "Marie-Pierre", "Jean-Régis", "Sandra", "Didier", "Nathalie",
        "Jean-Sébastien", "Marie-Louise", "Guillaume", "Sandrine", "Rémy",
        "Marie-Anne", "Jean-Noël", "Maryse", "Kévin", "Marie-Jeanne",
        "Jean-Robert", "Colette", "Laurent", "Marie-Céline", "Jean-Michel",
        "Cindy", "Richard", "Marie-Denise", "Jean-Patrick", "Nadège"
    ]
    
    communes_reunion = [
        "Saint-Denis", "Saint-Paul", "Saint-Pierre", "Le Tampon", "Saint-André",
        "Saint-Louis", "Le Port", "Saint-Benoît", "Sainte-Marie", "Sainte-Suzanne",
        "Saint-Joseph", "Saint-Leu", "La Possession", "L'Étang-Salé", "Petite-Île",
        "Bras-Panon", "Trois-Bassins", "Sainte-Rose", "Entre-Deux", "Les Avirons",
        "Cilaos", "Salazie", "La Plaine-des-Palmistes"
    ]
    
    quartiers = {
        "Saint-Denis": ["Le Chaudron", "Sainte-Clotilde", "Le Moufia", "La Bretagne", "La Montagne", "Les Camélias", "Bellepierre"],
        "Saint-Paul": ["La Saline", "Boucan Canot", "L'Hermitage", "Saint-Gilles", "Le Guillaume", "Bois-de-Nèfles"],
        "Saint-Pierre": ["Terre Sainte", "Ravine Blanche", "Bois d'Olives", "Pierrefonds", "Ligne Paradis"],
        "Le Tampon": ["Le 14ème", "Le 17ème", "Trois Mares", "Bras de Pontho", "La Plaine des Cafres"],
        "Saint-André": ["Cambuston", "Champ Borne", "Petit Bazar", "Rivière du Mât"],
        "Saint-Louis": ["La Rivière", "Les Makes", "Le Gol", "Bel Air"],
        "Le Port": ["Rivière des Galets", "La Zac", "Centre-ville"],
        "Saint-Benoît": ["Sainte-Anne", "Bras Fusil", "La Confiance"],
    }
    
    statuts = ["Actif", "Actif", "Actif", "Actif", "Actif", "Actif", "Actif",  # 70% actif
               "En pause", "En pause",  # 20% en pause
               "Nouveau"]  # 10% nouveau
    
    types_bokashi = ["Seau 20L", "Seau 20L", "Seau 20L",  # 50% seau 20L
                     "Bac 50L", "Bac 50L",  # 30% bac 50L
                     "Double seau 20L"]  # 20% double
    
    random.seed(974)  # Code postal Réunion pour reproductibilité
    
    clients = []
    for i in range(100):
        nom = noms_reunion[i % len(noms_reunion)]
        prenom = prenoms_reunion[i % len(prenoms_reunion)]
        commune = random.choice(communes_reunion)
        
        # Quartier si disponible
        quartier_list = quartiers.get(commune, [commune + " centre"])
        quartier = random.choice(quartier_list)
        
        statut = random.choice(statuts)
        type_bac = random.choice(types_bokashi)
        
        # Capacité selon type
        if "Double" in type_bac:
            capacite = 40
        elif "50L" in type_bac:
            capacite = 50
        else:
            capacite = 20
        
        # Production hebdo (kg) - entre 3 et 15 kg/semaine pour un foyer
        prod_hebdo = round(random.uniform(3, 15), 1)
        
        # Nombre de personnes au foyer
        nb_personnes = random.randint(1, 7)
        
        # Date inscription (dans les 12 derniers mois)
        jours_depuis = random.randint(7, 365)
        date_inscription = (datetime.now() - timedelta(days=jours_depuis)).strftime("%d/%m/%Y")
        
        # Dernière collecte EM
        jours_derniere_collecte = random.randint(1, 45)
        derniere_collecte = (datetime.now() - timedelta(days=jours_derniere_collecte)).strftime("%d/%m/%Y")
        
        # Score qualité (1-10)
        score_qualite = round(random.uniform(5.0, 10.0), 1)
        
        # Nombre de lots terminés
        lots_termines = max(0, (365 - jours_depuis) // 21) + random.randint(0, 5)
        if statut == "Nouveau":
            lots_termines = random.randint(0, 2)
            score_qualite = round(random.uniform(5.0, 7.5), 1)
        
        # Alerte si dernière collecte > 30 jours
        alerte = "⚠️" if jours_derniere_collecte > 30 else ""
        
        clients.append({
            "id": f"IND-{i+1:03d}",
            "nom": nom,
            "prenom": prenom,
            "nom_complet": f"{prenom} {nom}",
            "commune": commune,
            "quartier": quartier,
            "type_bac": type_bac,
            "capacite_l": capacite,
            "nb_personnes": nb_personnes,
            "prod_hebdo_kg": prod_hebdo,
            "statut": statut,
            "date_inscription": date_inscription,
            "derniere_collecte_em": derniere_collecte,
            "jours_depuis_collecte": jours_derniere_collecte,
            "score_qualite": score_qualite,
            "lots_termines": lots_termines,
            "alerte": alerte,
            "telephone": f"0692 {random.randint(10,99)} {random.randint(10,99)} {random.randint(10,99)}",
        })
    
    return clients

CLIENTS_INDIVIDUELS = generate_clients_individuels()

# ═══════════════════════════════════════════════════════════════════════════════
# MRV CALCULATION ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class BokashiMRVEngine:
    """Complete MRV calculation engine for Bokashi."""
    
    @staticmethod
    def calculate_site_credits(site_id: str, biomass_kg: float, application_area_m2: float = 100):
        """Calculate credits for a single site."""
        
        site = SITES_CLIENTS.get(site_id, {})
        compost_kg = biomass_kg * (BOKASHI_PROCESS["yield_pct"] / 100)
        
        # Carbon Credits
        carbon_seq = (compost_kg / 1000) * MRV_CONSTANTS["sequestration_tco2_per_t"]
        carbon_avoid = (biomass_kg / 1000) * MRV_CONSTANTS["avoided_tco2_per_t"]
        total_carbon = carbon_seq + carbon_avoid
        carbon_value = total_carbon * MRV_CONSTANTS["carbon_price_eur"]
        
        # Water Credits (jus Bokashi + économie irrigation)
        juice_l = biomass_kg * 0.15  # 15% du poids en jus
        water_saved_m3 = (application_area_m2 * 0.3) / 1000  # 0.3 L/m² économisé
        water_value = juice_l * MRV_CONSTANTS["juice_price_eur_l"] + water_saved_m3 * MRV_CONSTANTS["water_credit_eur_m3"]
        
        # Biodiversity Credits
        bio_area_ha = application_area_m2 / 10000
        bio_value = bio_area_ha * MRV_CONSTANTS["biodiversity_credit_eur_ha"] * 0.5
        
        # Total Credits
        total_credits = carbon_value + water_value + bio_value
        
        # Product Sales
        compost_sales = (compost_kg / 1000) * MRV_CONSTANTS["compost_price_eur_t"]
        juice_sales = juice_l * MRV_CONSTANTS["juice_price_eur_l"]
        
        return {
            "site_id": site_id,
            "site_name": site.get("name", "Unknown"),
            "biomass_kg": biomass_kg,
            "compost_kg": compost_kg,
            "juice_l": juice_l,
            "carbon_tco2": total_carbon,
            "carbon_value_eur": carbon_value,
            "water_value_eur": water_value,
            "bio_value_eur": bio_value,
            "total_credits_eur": total_credits,
            "compost_sales_eur": compost_sales,
            "juice_sales_eur": juice_sales,
            "total_revenue_eur": total_credits + compost_sales,
            "rekarbon_share_eur": total_credits * (MRV_CONSTANTS["rekarbon_share_pct"] / 100),
            "your_share_eur": total_credits * (1 - MRV_CONSTANTS["rekarbon_share_pct"] / 100)
        }
    
    @staticmethod
    def calculate_monthly_summary():
        """Calculate monthly summary for all sites."""
        
        total_biomass = sum(s["daily_input_kg"] * 30 for s in SITES_CLIENTS.values())
        total_compost = total_biomass * (BOKASHI_PROCESS["yield_pct"] / 100)
        total_juice = total_biomass * 0.15
        
        # Carbon
        carbon_seq = (total_compost / 1000) * MRV_CONSTANTS["sequestration_tco2_per_t"]
        carbon_avoid = (total_biomass / 1000) * MRV_CONSTANTS["avoided_tco2_per_t"]
        total_carbon = carbon_seq + carbon_avoid
        carbon_value = total_carbon * MRV_CONSTANTS["carbon_price_eur"]
        
        # Water
        water_value = total_juice * MRV_CONSTANTS["juice_price_eur_l"] * 0.3
        
        # Biodiversity
        bio_value = 500  # Estimation mensuelle
        
        # Products
        compost_sales = (total_compost / 1000) * MRV_CONSTANTS["compost_price_eur_t"]
        juice_sales = total_juice * MRV_CONSTANTS["juice_price_eur_l"]
        
        # Contracts
        contract_revenue = sum(s["monthly_fee"] for s in SITES_CLIENTS.values())
        
        # Total Credits
        total_credits = carbon_value + water_value + bio_value
        
        return {
            "total_biomass_kg": total_biomass,
            "total_compost_kg": total_compost,
            "total_juice_l": total_juice,
            "total_carbon_tco2": total_carbon,
            "carbon_value_eur": carbon_value,
            "water_value_eur": water_value,
            "bio_value_eur": bio_value,
            "total_credits_eur": total_credits,
            "compost_sales_eur": compost_sales,
            "juice_sales_eur": juice_sales,
            "contract_revenue_eur": contract_revenue,
            "rekarbon_share_eur": total_credits * (MRV_CONSTANTS["rekarbon_share_pct"] / 100),
            "your_credits_share_eur": total_credits * (1 - MRV_CONSTANTS["rekarbon_share_pct"] / 100),
            "total_your_revenue_eur": contract_revenue + compost_sales + juice_sales + total_credits * 0.7
        }

# ═══════════════════════════════════════════════════════════════════════════════
# BATCH SIMULATOR
# ═══════════════════════════════════════════════════════════════════════════════

class BatchSimulator:
    """Simulates Bokashi batch monitoring."""
    
    @staticmethod
    def generate_batch_status():
        """Generate current batch status for all sites."""
        batches = []
        
        for site_id, site in SITES_CLIENTS.items():
            for i in range(site["containers"]):
                phase_num = random.randint(0, 4)
                phases = list(BOKASHI_PROCESS["phases"].keys())
                phase = phases[phase_num]
                
                days_in_phase = random.randint(1, BOKASHI_PROCESS["phases"][phase]["duration_days"] + 1) if BOKASHI_PROCESS["phases"][phase]["duration_days"] > 0 else 0
                
                batches.append({
                    "Site": site["name"][:20],
                    "Container": f"C{i+1:02d}",
                    "Phase": phase.capitalize(),
                    "Jour": days_in_phase,
                    "Temp (°C)": round(random.uniform(40, 58), 1),
                    "pH": round(random.uniform(3.5, 4.5), 1),
                    "Humidité (%)": round(random.uniform(60, 70), 0),
                    "Masse (kg)": round(site["capacity_kg"] / site["containers"] * random.uniform(0.5, 1.0), 0),
                    "Status": "✅" if phase in ["fermentation", "maturation", "pret"] else "⏳"
                })
        
        return pd.DataFrame(batches[:15])  # Limit to 15 rows
    
    @staticmethod
    def generate_fermentation_curve(days=21):
        """Generate fermentation temperature curve."""
        
        temps = []
        for d in range(days):
            if d < 2:  # Activation
                temp = 25 + (d * 10)
            elif d < 14:  # Fermentation peak
                temp = 45 + np.sin((d - 2) * np.pi / 12) * 15
            else:  # Maturation
                temp = 55 - ((d - 14) * 2)
            temps.append(temp + random.uniform(-2, 2))
        
        return pd.DataFrame({
            "Jour": list(range(1, days + 1)),
            "Temperature": temps,
            "Optimal_Min": [45] * days,
            "Optimal_Max": [60] * days
        })

# ═══════════════════════════════════════════════════════════════════════════════
# CERBERE SECURITY
# ═══════════════════════════════════════════════════════════════════════════════

class CerbereSecurity:
    """Simplified CERBERE security for demo."""
    
    @staticmethod
    def sign_measurement(data: dict) -> dict:
        timestamp = datetime.utcnow().isoformat() + "Z"
        payload = json.dumps(data, sort_keys=True) + timestamp
        signature = hashlib.sha256(payload.encode()).hexdigest()[:32]
        
        return {
            **data,
            "timestamp": timestamp,
            "signature": f"ED25519:{signature}",
            "verified": True,
            "standard": "Bokashi MRV | ISO 14064-2"
        }
    
    @staticmethod
    def generate_certificate_id():
        return f"BOKASHI-{datetime.now().strftime('%Y%m%d')}-{hashlib.sha256(str(time.time()).encode()).hexdigest()[:8].upper()}"

# ═══════════════════════════════════════════════════════════════════════════════
# SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════

if "page" not in st.session_state:
    st.session_state.page = "home"
if "mrv_data" not in st.session_state:
    st.session_state.mrv_data = None

# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR NAVIGATION
# ═══════════════════════════════════════════════════════════════════════════════

with st.sidebar:
    st.markdown(f"### 👨‍🌾 {MAITRE_COMPOSTEUR['name']}")
    st.markdown(f"*{MAITRE_COMPOSTEUR['title']}*")
    st.markdown(f"📍 {MAITRE_COMPOSTEUR['location']}")
    
    st.markdown("---")
    st.markdown("### 🧭 Navigation")
    
    pages = [
        ("home", "🏠", "Accueil"),
        ("dashboard", "📊", "Dashboard Live"),
        ("sites", "📍", "Sites Clients"),
        ("suivi", "👥", "Suivi Individuels"),
        ("batches", "🧪", "Lots en Cours"),
        ("credits", "💎", "Crédits Multi-Impact"),
        ("business", "📈", "Business Case"),
        ("simulation", "🎮", "Simulation"),
        ("architecture", "🔧", "Architecture")
    ]
    
    for page_id, icon, label in pages:
        if st.button(f"{icon} {label}", key=f"nav_{page_id}", use_container_width=True):
            st.session_state.page = page_id
            st.rerun()
    
    st.markdown("---")
    st.markdown("### 📊 Résumé Réseau")
    st.metric("Sites Actifs", len(SITES_CLIENTS), "clients pro")
    st.metric("Containers", sum(s["containers"] for s in SITES_CLIENTS.values()), "déployés")
    total_daily = sum(s["daily_input_kg"] for s in SITES_CLIENTS.values())
    st.metric("Production/Jour", f"{total_daily} kg", "biomasse")
    
    st.markdown("---")
    st.markdown("### 👥 Bokashi Individuels")
    actifs_indiv = sum(1 for c in CLIENTS_INDIVIDUELS if c["statut"] == "Actif")
    st.metric("Foyers Inscrits", len(CLIENTS_INDIVIDUELS), f"{actifs_indiv} actifs")
    alertes = sum(1 for c in CLIENTS_INDIVIDUELS if c["alerte"])
    if alertes > 0:
        st.warning(f"⚠️ {alertes} foyer(s) sans collecte >30j")
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; font-size: 0.8rem; color: #666;'>
        <p>© 2026 Rekarbon SAS</p>
        <p>v3.0 Premium</p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: HOME
# ═══════════════════════════════════════════════════════════════════════════════

if st.session_state.page == "home":
    
    # Premium Header
    st.markdown(f"""
    <div class='premium-header'>
        <h1 style='font-size: 2.5rem; margin: 0;'>♻️ Bokashi × Rekarbon</h1>
        <p style='font-size: 1.3rem; margin: 1rem 0; opacity: 0.9;'>Plateforme MRV pour Maître Composteur</p>
        <p style='font-size: 1.1rem;'>👨‍🌾 {MAITRE_COMPOSTEUR['name']} - {MAITRE_COMPOSTEUR['location']}</p>
        <div style='margin-top: 1.5rem;'>
            <span class='badge-cert'>Maître Composteur</span>
            <span class='badge-cert'>EM Certified</span>
            <span class='badge-cert'>Rekarbon MRV</span>
            <span class='badge-cert'>ISO 14064-2</span>
        </div>
        <div style='margin-top: 1rem;'>
            <span class='live-indicator'><span class='live-dot'></span>MONITORING LIVE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Top Metrics
    total_daily = sum(s["daily_input_kg"] for s in SITES_CLIENTS.values())
    total_containers = sum(s["containers"] for s in SITES_CLIENTS.values())
    monthly_revenue = sum(s["monthly_fee"] for s in SITES_CLIENTS.values())
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Sites Clients", len(SITES_CLIENTS), "actifs")
    with col2:
        st.metric("Containers", total_containers, "déployés")
    with col3:
        st.metric("Traitement/Jour", f"{total_daily} kg", "biomasse")
    with col4:
        st.metric("Compost/Mois", f"{total_daily * 30 * 0.7 / 1000:.1f} t", "produit")
    with col5:
        st.metric("Contrats", f"€{monthly_revenue:,}", "/mois")
    
    st.markdown("---")
    
    # Triple Valorisation Box
    st.markdown("""
    <div class='triple-box'>
        <h2 style='margin: 0;'>💎 TRIPLE VALORISATION BOKASHI</h2>
        <p style='font-size: 1.2rem; margin: 1rem 0;'>3 Sources de Revenus Simultanées</p>
        <div style='display: flex; justify-content: space-around; margin: 2rem 0; flex-wrap: wrap;'>
            <div style='text-align: center; padding: 1rem;'>
                <h3>🌱 COMPOST</h3>
                <p>Enrichi aux EM</p>
                <h2>€120/t</h2>
            </div>
            <div style='text-align: center; padding: 1rem;'>
                <h3>💧 JUS BOKASHI</h3>
                <p>Engrais liquide premium</p>
                <h2>€8/L</h2>
            </div>
            <div style='text-align: center; padding: 1rem;'>
                <h3>💎 CRÉDITS</h3>
                <p>Carbone + Eau + Bio</p>
                <h2>€50-100/t</h2>
            </div>
        </div>
        <p style='font-size: 1.3rem; padding: 1rem; background: rgba(0,0,0,0.2); border-radius: 10px;'>
            <strong>🎯 Jusqu'à €250/tonne de biomasse traitée!</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # EM Products Box
    st.markdown("""
    <div class='em-box'>
        <h2 style='margin: 0;'>🦠 MICRO-ORGANISMES EFFICACES (EM)</h2>
        <p style='font-size: 1.2rem; margin: 1rem 0;'>La Clé de la Fermentation Bokashi</p>
        <div style='display: flex; justify-content: space-around; margin-top: 1.5rem; flex-wrap: wrap;'>
            <div><h3>EM1</h3><p>Solution mère - €25/L</p></div>
            <div><h3>EM2</h3><p>Activé terrain - €8/L</p></div>
            <div><h3>EM3</h3><p>Spécial Bokashi - €12/L</p></div>
            <div><h3>EM4</h3><p>Finition compost - €10/L</p></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Sites Clients
    st.markdown("### 📍 Réseau de Sites Clients")
    
    site_cols = st.columns(5)
    
    for i, (site_id, site) in enumerate(SITES_CLIENTS.items()):
        with site_cols[i]:
            st.markdown(f"""
            <div class='site-card'>
                <h2>{site['icon']}</h2>
                <h4 style='color: #2D5016;'>{site['name'][:18]}</h4>
                <hr>
                <p>📦 {site['containers']} containers</p>
                <p>⚖️ {site['daily_input_kg']} kg/jour</p>
                <p>💰 €{site['monthly_fee']}/mois</p>
                <span class='badge-ready'>✅ Actif</span>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Calculate Button
    if st.button("🚀 Calculer Valorisation Mensuelle", type="primary", use_container_width=True):
        with st.spinner("Calcul en cours..."):
            time.sleep(1)
            st.session_state.mrv_data = BokashiMRVEngine.calculate_monthly_summary()
            st.balloons()
            st.success("✅ Calcul terminé!")
    
    # Display Results
    if st.session_state.mrv_data:
        mrv = st.session_state.mrv_data
        
        st.markdown("---")
        st.markdown("### 💰 Valorisation Mensuelle")
        
        val_cols = st.columns(4)
        
        with val_cols[0]:
            st.markdown(f"""
            <div class='value-box-green'>
                <h4>♻️ Crédits Carbone</h4>
                <h2>€{mrv['carbon_value_eur']:,.0f}</h2>
                <p>{mrv['total_carbon_tco2']:.1f} tCO2</p>
            </div>
            """, unsafe_allow_html=True)
        
        with val_cols[1]:
            st.markdown(f"""
            <div class='value-box-blue'>
                <h4>💧 Crédits Eau</h4>
                <h2>€{mrv['water_value_eur']:,.0f}</h2>
                <p>{mrv['total_juice_l']:,.0f} L jus</p>
            </div>
            """, unsafe_allow_html=True)
        
        with val_cols[2]:
            st.markdown(f"""
            <div class='value-box-purple'>
                <h4>🦋 Biodiversité</h4>
                <h2>€{mrv['bio_value_eur']:,.0f}</h2>
                <p>Amélioration sols</p>
            </div>
            """, unsafe_allow_html=True)
        
        with val_cols[3]:
            st.markdown(f"""
            <div class='value-box-gold'>
                <h4>🎯 TOTAL CRÉDITS</h4>
                <h2>€{mrv['total_credits_eur']:,.0f}</h2>
                <p>Multi-impact</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Revenue Summary
        rev_cols = st.columns(4)
        
        with rev_cols[0]:
            st.markdown(f"""
            <div class='value-box-brown'>
                <h4>📦 Vente Compost</h4>
                <h2>€{mrv['compost_sales_eur']:,.0f}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with rev_cols[1]:
            st.markdown(f"""
            <div class='value-box-light-green'>
                <h4>📋 Contrats</h4>
                <h2>€{mrv['contract_revenue_eur']:,.0f}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with rev_cols[2]:
            st.markdown(f"""
            <div class='value-box-orange'>
                <h4>🏷️ Part Rekarbon (30%)</h4>
                <h2>€{mrv['rekarbon_share_eur']:,.0f}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with rev_cols[3]:
            st.markdown(f"""
            <div class='value-box-green'>
                <h4>💰 VOTRE REVENU</h4>
                <h2>€{mrv['total_your_revenue_eur']:,.0f}</h2>
                <p>/mois</p>
            </div>
            """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: DASHBOARD
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.page == "dashboard":
    
    st.markdown("""
    <div class='premium-header'>
        <h1>📊 Dashboard Live</h1>
        <p>Monitoring temps réel de tous les sites</p>
        <span class='live-indicator'><span class='live-dot'></span>LIVE DATA</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Real-time metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Batches Actifs", f"{random.randint(25, 30)}", "en fermentation")
    with col2:
        st.metric("Temp Moyenne", f"{random.uniform(48, 55):.1f}°C", "optimal")
    with col3:
        st.metric("pH Moyen", f"{random.uniform(3.8, 4.2):.1f}", "cible")
    with col4:
        st.metric("Alertes", f"{random.randint(0, 2)}", "en cours")
    
    st.markdown("---")
    
    # Batch Status Table
    st.markdown("### 🧪 Status des Lots")
    
    batch_df = BatchSimulator.generate_batch_status()
    st.dataframe(batch_df, use_container_width=True, height=400)
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🌡️ Courbe de Fermentation Type")
        
        ferm_df = BatchSimulator.generate_fermentation_curve(21)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=ferm_df["Jour"], y=ferm_df["Temperature"],
            name="Température", line=dict(color="#E31E24", width=3),
            fill="tozeroy", fillcolor="rgba(227,30,36,0.1)"
        ))
        fig.add_trace(go.Scatter(
            x=ferm_df["Jour"], y=ferm_df["Optimal_Min"],
            name="Min Optimal", line=dict(color="#4CAF50", dash="dash")
        ))
        fig.add_trace(go.Scatter(
            x=ferm_df["Jour"], y=ferm_df["Optimal_Max"],
            name="Max Optimal", line=dict(color="#4CAF50", dash="dash")
        ))
        fig.update_layout(
            height=350,
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis_title="Température (°C)",
            xaxis_title="Jour"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 📦 Production par Site")
        
        site_names = [s["name"][:15] for s in SITES_CLIENTS.values()]
        daily_inputs = [s["daily_input_kg"] for s in SITES_CLIENTS.values()]
        
        fig = go.Figure(data=[go.Bar(
            x=site_names, y=daily_inputs,
            marker_color=["#2D5016", "#4CAF50", "#8B4513", "#DAA520", "#0077B6"],
            text=[f"{d} kg" for d in daily_inputs],
            textposition="outside"
        )])
        fig.update_layout(
            height=350,
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis_title="kg/jour"
        )
        st.plotly_chart(fig, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: SITES CLIENTS
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.page == "sites":
    
    st.markdown("""
    <div class='premium-header'>
        <h1>📍 Sites Clients</h1>
        <p>Réseau de déploiement Bokashi</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sites table
    st.markdown("### 📋 Détail des Sites")
    
    sites_data = []
    for site_id, site in SITES_CLIENTS.items():
        sites_data.append({
            "ID": site_id,
            "Site": f"{site['icon']} {site['name']}",
            "Type": site["type"].replace("_", " ").title(),
            "Adresse": site["address"],
            "Containers": site["containers"],
            "Capacité (kg)": site["capacity_kg"],
            "Production (kg/j)": site["daily_input_kg"],
            "Contrat (€/mois)": f"€{site['monthly_fee']}",
            "Status": "✅ Actif"
        })
    
    st.dataframe(pd.DataFrame(sites_data), use_container_width=True)
    
    st.markdown("---")
    
    # Revenue by type
    st.markdown("### 📊 Répartition par Type de Site")
    
    col1, col2 = st.columns(2)
    
    with col1:
        type_production = {}
        for site in SITES_CLIENTS.values():
            t = site["type"]
            type_production[t] = type_production.get(t, 0) + site["daily_input_kg"]
        
        fig = go.Figure(data=[go.Pie(
            labels=[t.replace("_", " ").title() for t in type_production.keys()],
            values=list(type_production.values()),
            hole=0.4,
            marker_colors=["#2D5016", "#4CAF50", "#8B4513", "#DAA520", "#0077B6"]
        )])
        fig.update_layout(title="Production par Type (kg/jour)", height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        type_revenue = {}
        for site in SITES_CLIENTS.values():
            t = site["type"]
            type_revenue[t] = type_revenue.get(t, 0) + site["monthly_fee"]
        
        fig = go.Figure(data=[go.Pie(
            labels=[t.replace("_", " ").title() for t in type_revenue.keys()],
            values=list(type_revenue.values()),
            hole=0.4,
            marker_colors=["#2D5016", "#4CAF50", "#8B4513", "#DAA520", "#0077B6"]
        )])
        fig.update_layout(title="Revenus Contrats par Type (€/mois)", height=350)
        st.plotly_chart(fig, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: SUIVI INDIVIDUELS (100 foyers Bokashi - pas de crédits)
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.page == "suivi":
    
    st.markdown("""
    <div class='premium-header'>
        <h1>👥 Suivi Bokashi Individuels</h1>
        <p>100 Foyers Réunionnais - Compostage de Proximité</p>
        <div style='margin-top: 1rem;'>
            <span class='badge-cert'>🏠 Particuliers</span>
            <span class='badge-cert'>♻️ Suivi uniquement</span>
            <span class='badge-fermentation'>Pas de crédits</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # ── KPIs globaux ──
    actifs = [c for c in CLIENTS_INDIVIDUELS if c["statut"] == "Actif"]
    en_pause = [c for c in CLIENTS_INDIVIDUELS if c["statut"] == "En pause"]
    nouveaux = [c for c in CLIENTS_INDIVIDUELS if c["statut"] == "Nouveau"]
    alertes = [c for c in CLIENTS_INDIVIDUELS if c["alerte"]]
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Total Foyers", len(CLIENTS_INDIVIDUELS), "inscrits")
    with col2:
        st.metric("Actifs", len(actifs), f"{len(actifs)/len(CLIENTS_INDIVIDUELS)*100:.0f}%")
    with col3:
        st.metric("En Pause", len(en_pause), "⏸️")
    with col4:
        st.metric("Nouveaux", len(nouveaux), "🆕")
    with col5:
        st.metric("Alertes", len(alertes), "⚠️ >30j")
    
    st.markdown("---")
    
    # ── Production globale ──
    total_prod_hebdo = sum(c["prod_hebdo_kg"] for c in actifs)
    total_prod_mensuel = total_prod_hebdo * 4.33
    total_lots = sum(c["lots_termines"] for c in CLIENTS_INDIVIDUELS)
    score_moyen = np.mean([c["score_qualite"] for c in CLIENTS_INDIVIDUELS])
    
    kpi_cols = st.columns(4)
    with kpi_cols[0]:
        st.markdown(f"""
        <div class='value-box-green'>
            <h4>⚖️ Production Hebdo</h4>
            <h2>{total_prod_hebdo:.0f} kg</h2>
            <p>{total_prod_mensuel:.0f} kg/mois</p>
        </div>
        """, unsafe_allow_html=True)
    with kpi_cols[1]:
        st.markdown(f"""
        <div class='value-box-brown'>
            <h4>🧪 Lots Terminés</h4>
            <h2>{total_lots}</h2>
            <p>total réseau</p>
        </div>
        """, unsafe_allow_html=True)
    with kpi_cols[2]:
        st.markdown(f"""
        <div class='value-box-light-green'>
            <h4>⭐ Score Qualité Moyen</h4>
            <h2>{score_moyen:.1f}/10</h2>
            <p>fermentation</p>
        </div>
        """, unsafe_allow_html=True)
    with kpi_cols[3]:
        st.markdown(f"""
        <div class='value-box-gold'>
            <h4>👨‍👩‍👧‍👦 Personnes Touchées</h4>
            <h2>{sum(c['nb_personnes'] for c in CLIENTS_INDIVIDUELS)}</h2>
            <p>habitants sensibilisés</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # ── Filtres ──
    st.markdown("### 🔍 Filtres de Recherche")
    
    filt_col1, filt_col2, filt_col3, filt_col4 = st.columns(4)
    
    with filt_col1:
        filtre_statut = st.selectbox("Statut", ["Tous", "Actif", "En pause", "Nouveau"])
    with filt_col2:
        communes_list = sorted(set(c["commune"] for c in CLIENTS_INDIVIDUELS))
        filtre_commune = st.selectbox("Commune", ["Toutes"] + communes_list)
    with filt_col3:
        filtre_type = st.selectbox("Type Bac", ["Tous", "Seau 20L", "Bac 50L", "Double seau 20L"])
    with filt_col4:
        filtre_alerte = st.checkbox("⚠️ Alertes uniquement", value=False)
    
    # Appliquer filtres
    clients_filtres = CLIENTS_INDIVIDUELS.copy()
    if filtre_statut != "Tous":
        clients_filtres = [c for c in clients_filtres if c["statut"] == filtre_statut]
    if filtre_commune != "Toutes":
        clients_filtres = [c for c in clients_filtres if c["commune"] == filtre_commune]
    if filtre_type != "Tous":
        clients_filtres = [c for c in clients_filtres if c["type_bac"] == filtre_type]
    if filtre_alerte:
        clients_filtres = [c for c in clients_filtres if c["alerte"]]
    
    st.info(f"📋 **{len(clients_filtres)}** foyer(s) affiché(s) sur {len(CLIENTS_INDIVIDUELS)}")
    
    st.markdown("---")
    
    # ── Tableau principal ──
    st.markdown("### 📋 Liste des Foyers Bokashi")
    
    df_display = pd.DataFrame([{
        "ID": c["id"],
        "Nom": c["nom_complet"],
        "Commune": c["commune"],
        "Quartier": c["quartier"],
        "Bac": c["type_bac"],
        "Foyer": f"{c['nb_personnes']} pers.",
        "Prod/sem (kg)": c["prod_hebdo_kg"],
        "Lots terminés": c["lots_termines"],
        "Score": f"{c['score_qualite']}/10",
        "Dernière collecte EM": c["derniere_collecte_em"],
        "Statut": "✅ " + c["statut"] if c["statut"] == "Actif" else ("⏸️ " + c["statut"] if c["statut"] == "En pause" else "🆕 " + c["statut"]),
        "Alerte": c["alerte"]
    } for c in clients_filtres])
    
    st.dataframe(df_display, use_container_width=True, height=500)
    
    st.markdown("---")
    
    # ── Graphiques d'analyse ──
    st.markdown("### 📊 Analyse du Réseau Individuels")
    
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        # Répartition par commune
        commune_counts = {}
        for c in CLIENTS_INDIVIDUELS:
            commune_counts[c["commune"]] = commune_counts.get(c["commune"], 0) + 1
        
        commune_sorted = sorted(commune_counts.items(), key=lambda x: -x[1])
        
        fig = go.Figure(data=[go.Bar(
            x=[c[0] for c in commune_sorted[:12]],
            y=[c[1] for c in commune_sorted[:12]],
            marker_color="#4CAF50",
            text=[str(c[1]) for c in commune_sorted[:12]],
            textposition="outside"
        )])
        fig.update_layout(
            title="Foyers par Commune (top 12)",
            height=400,
            margin=dict(l=20, r=20, t=40, b=80),
            xaxis_tickangle=-45,
            yaxis_title="Nombre de foyers"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with chart_col2:
        # Répartition par statut
        statut_counts = {}
        for c in CLIENTS_INDIVIDUELS:
            statut_counts[c["statut"]] = statut_counts.get(c["statut"], 0) + 1
        
        colors_statut = {"Actif": "#4CAF50", "En pause": "#FFB300", "Nouveau": "#42A5F5"}
        
        fig = go.Figure(data=[go.Pie(
            labels=list(statut_counts.keys()),
            values=list(statut_counts.values()),
            hole=0.45,
            marker_colors=[colors_statut.get(s, "#999") for s in statut_counts.keys()]
        )])
        fig.update_layout(title="Répartition par Statut", height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    chart_col3, chart_col4 = st.columns(2)
    
    with chart_col3:
        # Distribution des scores qualité
        scores = [c["score_qualite"] for c in CLIENTS_INDIVIDUELS]
        
        fig = go.Figure(data=[go.Histogram(
            x=scores,
            nbinsx=10,
            marker_color="#2D5016",
            opacity=0.85
        )])
        fig.update_layout(
            title="Distribution des Scores Qualité",
            height=350,
            margin=dict(l=20, r=20, t=40, b=40),
            xaxis_title="Score Qualité (/10)",
            yaxis_title="Nombre de foyers"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with chart_col4:
        # Répartition par type de bac
        type_counts = {}
        for c in CLIENTS_INDIVIDUELS:
            type_counts[c["type_bac"]] = type_counts.get(c["type_bac"], 0) + 1
        
        fig = go.Figure(data=[go.Pie(
            labels=list(type_counts.keys()),
            values=list(type_counts.values()),
            hole=0.45,
            marker_colors=["#8B4513", "#DAA520", "#2D5016"]
        )])
        fig.update_layout(title="Répartition par Type de Bac", height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # ── Top 10 producteurs ──
    st.markdown("### 🏆 Top 10 Foyers les Plus Actifs")
    
    top_producteurs = sorted(CLIENTS_INDIVIDUELS, key=lambda x: -x["prod_hebdo_kg"])[:10]
    
    top_cols = st.columns(5)
    for i, client in enumerate(top_producteurs[:5]):
        with top_cols[i]:
            medal = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"][i]
            st.markdown(f"""
            <div class='site-card'>
                <h2>{medal}</h2>
                <h4 style='color: #2D5016; font-size: 0.9rem;'>{client['nom_complet']}</h4>
                <p style='font-size: 0.8rem;'>{client['quartier']}, {client['commune']}</p>
                <hr>
                <p><strong>{client['prod_hebdo_kg']} kg/sem</strong></p>
                <p>⭐ {client['score_qualite']}/10</p>
                <p>🧪 {client['lots_termines']} lots</p>
            </div>
            """, unsafe_allow_html=True)
    
    top_cols2 = st.columns(5)
    for i, client in enumerate(top_producteurs[5:10]):
        with top_cols2[i]:
            rank = ["6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"][i]
            st.markdown(f"""
            <div class='site-card'>
                <h2>{rank}</h2>
                <h4 style='color: #2D5016; font-size: 0.9rem;'>{client['nom_complet']}</h4>
                <p style='font-size: 0.8rem;'>{client['quartier']}, {client['commune']}</p>
                <hr>
                <p><strong>{client['prod_hebdo_kg']} kg/sem</strong></p>
                <p>⭐ {client['score_qualite']}/10</p>
                <p>🧪 {client['lots_termines']} lots</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # ── Note importante : Pas de crédits ──
    st.markdown(f"""
    <div class='em-box'>
        <h3>ℹ️ NOTE IMPORTANTE - SUIVI UNIQUEMENT</h3>
        <hr style='border-color: rgba(255,255,255,0.3);'>
        <p style='font-size: 1.1rem;'>Les foyers individuels Bokashi bénéficient d'un <strong>suivi gratuit</strong> 
        par le maître composteur {MAITRE_COMPOSTEUR['name']}.</p>
        <p style='font-size: 1rem; margin-top: 1rem;'>
            ✅ <strong>Inclus :</strong> Formation initiale, fourniture EM, suivi qualité, conseils personnalisés<br>
            ❌ <strong>Non inclus :</strong> Génération de crédits environnementaux (réservé aux sites professionnels)<br>
            🎯 <strong>Objectif :</strong> Réduction des déchets à la source, sensibilisation, maillage territorial
        </p>
        <p style='font-size: 1rem; margin-top: 1rem; padding: 1rem; background: rgba(0,0,0,0.2); border-radius: 10px;'>
            👥 <strong>{len(CLIENTS_INDIVIDUELS)} foyers</strong> | 
            👨‍👩‍👧‍👦 <strong>{sum(c['nb_personnes'] for c in CLIENTS_INDIVIDUELS)} personnes</strong> | 
            ⚖️ <strong>{total_prod_mensuel:.0f} kg/mois</strong> détournés de la poubelle
        </p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: BATCHES
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.page == "batches":
    
    st.markdown("""
    <div class='premium-header'>
        <h1>🧪 Lots en Fermentation</h1>
        <p>Suivi des batches Bokashi</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Process overview
    st.markdown("### 📋 Processus Bokashi - 21 Jours")
    
    phase_cols = st.columns(5)
    phases = [
        ("Chargement", "📥", "0-1j", "#FFD700"),
        ("Activation", "🔥", "1-2j", "#FF6600"),
        ("Fermentation", "🦠", "2-14j", "#E31E24"),
        ("Maturation", "🌱", "14-21j", "#8B4513"),
        ("Prêt", "✅", "21j+", "#4CAF50")
    ]
    
    for i, (name, icon, duration, color) in enumerate(phases):
        with phase_cols[i]:
            st.markdown(f"""
            <div class='metric-premium' style='text-align: center; border-color: {color};'>
                <h2>{icon}</h2>
                <h4>{name}</h4>
                <p>{duration}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Optimal conditions
    st.markdown("### ⚙️ Conditions Optimales")
    
    cond_cols = st.columns(4)
    conditions = [
        ("🌡️ Température", "45-60°C"),
        ("💧 Humidité", "60-70%"),
        ("⚗️ pH", "3.5-4.5"),
        ("⏱️ Durée", "21 jours")
    ]
    
    for i, (name, value) in enumerate(conditions):
        with cond_cols[i]:
            st.markdown(f"""
            <div class='value-box-light-green'>
                <h4>{name}</h4>
                <h2>{value}</h2>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Batch table
    st.markdown("### 📊 Lots Actifs")
    batch_df = BatchSimulator.generate_batch_status()
    st.dataframe(batch_df, use_container_width=True, height=400)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: CREDITS
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.page == "credits":
    
    st.markdown("""
    <div class='premium-header'>
        <h1>💎 Crédits Multi-Impact</h1>
        <p>Carbone + Eau + Biodiversité</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Credit types
    st.markdown("### 🏷️ Types de Crédits Générés")
    
    credit_cols = st.columns(3)
    
    with credit_cols[0]:
        st.markdown(f"""
        <div class='value-box-green'>
            <h3>♻️ CARBONE</h3>
            <h1>€45/tCO2</h1>
            <hr style='border-color: rgba(255,255,255,0.3);'>
            <p>Séquestration: 0.7 tCO2/t compost</p>
            <p>Évitement: 0.5 tCO2/t déchets</p>
            <p>Standards: VCS, Gold Standard</p>
        </div>
        """, unsafe_allow_html=True)
    
    with credit_cols[1]:
        st.markdown(f"""
        <div class='value-box-blue'>
            <h3>💧 EAU</h3>
            <h1>€3/m³</h1>
            <hr style='border-color: rgba(255,255,255,0.3);'>
            <p>Jus Bokashi: 15% du poids</p>
            <p>Économie irrigation: 30%</p>
            <p>Rétention sols améliorée</p>
        </div>
        """, unsafe_allow_html=True)
    
    with credit_cols[2]:
        st.markdown(f"""
        <div class='value-box-purple'>
            <h3>🦋 BIODIVERSITÉ</h3>
            <h1>€500/ha</h1>
            <hr style='border-color: rgba(255,255,255,0.3);'>
            <p>Microbiome sol enrichi</p>
            <p>Matière organique +50%</p>
            <p>Faune auxiliaire stimulée</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Revenue share
    st.markdown("### 💰 Partage des Revenus Crédits")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = go.Figure(data=[go.Pie(
            labels=["Votre Part (70%)", "Rekarbon (30%)"],
            values=[70, 30],
            hole=0.5,
            marker_colors=["#4CAF50", "#FF6600"]
        )])
        fig.update_layout(title="Répartition Crédits", height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(f"""
        <div class='triple-box'>
            <h3>🤝 PARTENARIAT REKARBON</h3>
            <hr style='border-color: rgba(255,255,255,0.3);'>
            <p>✅ <strong>Vous:</strong> Production + Collecte + EM</p>
            <p>✅ <strong>Rekarbon:</strong> MRV + Certification + Marchés</p>
            <hr style='border-color: rgba(255,255,255,0.3);'>
            <p>💰 <strong>70%</strong> des crédits pour vous</p>
            <p>💰 <strong>30%</strong> pour Rekarbon (certification)</p>
            <hr style='border-color: rgba(255,255,255,0.3);'>
            <p>✅ Vente compost: <strong>100%</strong> pour vous</p>
            <p>✅ Jus Bokashi: <strong>100%</strong> pour vous</p>
            <p>✅ Contrats: <strong>100%</strong> pour vous</p>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: BUSINESS CASE
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.page == "business":
    
    st.markdown("""
    <div class='premium-header'>
        <h1>📈 Business Case</h1>
        <p>Analyse Financière Complète</p>
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.mrv_data:
        st.session_state.mrv_data = BokashiMRVEngine.calculate_monthly_summary()
    
    mrv = st.session_state.mrv_data
    
    # Monthly summary
    st.markdown("### 💰 Revenus Mensuels")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class='value-box-light-green'>
            <h4>📋 Contrats</h4>
            <h2>€{mrv['contract_revenue_eur']:,.0f}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='value-box-brown'>
            <h4>🌱 Vente Compost</h4>
            <h2>€{mrv['compost_sales_eur']:,.0f}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='value-box-gold'>
            <h4>💎 Crédits (70%)</h4>
            <h2>€{mrv['your_credits_share_eur']:,.0f}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class='value-box-green'>
            <h4>🎯 TOTAL MENSUEL</h4>
            <h2>€{mrv['total_your_revenue_eur']:,.0f}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Annual projection
    st.markdown("### 📈 Projection Annuelle")
    
    months = list(range(1, 13))
    base_monthly = mrv['total_your_revenue_eur']
    growth = [base_monthly * (1 + 0.05 * m) for m in range(12)]  # 5% growth/month
    cumulative = [sum(growth[:i+1]) for i in range(12)]
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(go.Bar(
        x=months, y=growth,
        name="Revenu Mensuel (€)",
        marker_color="#4CAF50"
    ), secondary_y=False)
    
    fig.add_trace(go.Scatter(
        x=months, y=cumulative,
        name="Cumulé (€)",
        line=dict(color="#FF6600", width=3),
        mode="lines+markers"
    ), secondary_y=True)
    
    fig.update_layout(
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
        xaxis_title="Mois"
    )
    fig.update_yaxes(title_text="Mensuel (€)", secondary_y=False)
    fig.update_yaxes(title_text="Cumulé (€)", secondary_y=True)
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Annual summary
    annual_revenue = sum(growth)
    
    st.markdown(f"""
    <div class='value-box-green' style='margin-top: 2rem;'>
        <h3>🎯 PROJECTION ANNUELLE</h3>
        <h1 style='font-size: 3rem;'>€{annual_revenue:,.0f}</h1>
        <p>Revenu total année 1</p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: SIMULATION
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.page == "simulation":
    
    st.markdown("""
    <div class='premium-header'>
        <h1>🎮 Simulation MRV</h1>
        <p>Démonstration collecte et certification</p>
        <span class='live-indicator'><span class='live-dot'></span>SIMULATION</span>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        site_id = st.selectbox("Site", list(SITES_CLIENTS.keys()))
    with col2:
        biomass = st.slider("Biomasse (kg)", 50, 500, 150)
    with col3:
        area = st.slider("Surface application (m²)", 50, 500, 100)
    
    if st.button("▶️ Lancer Simulation Batch", type="primary", use_container_width=True):
        
        metrics_placeholder = st.empty()
        chart_placeholder = st.empty()
        data_placeholder = st.empty()
        cert_placeholder = st.empty()
        
        data_points = []
        
        for day in range(1, 11):
            # Simulate fermentation day
            if day <= 2:
                phase = "Activation"
                temp = 25 + day * 10
            elif day <= 7:
                phase = "Fermentation"
                temp = 45 + (day - 2) * 2
            else:
                phase = "Maturation"
                temp = 55 - (day - 7) * 1.5
            
            measurement = {
                "site": SITES_CLIENTS[site_id]["name"],
                "day": day,
                "phase": phase,
                "temperature": round(temp + random.uniform(-2, 2), 1),
                "ph": round(4.0 + random.uniform(-0.3, 0.3), 2),
                "humidity": round(65 + random.uniform(-5, 5), 0),
                "co2_produced_kg": round(biomass * 0.002 * day, 2)
            }
            
            signed = CerbereSecurity.sign_measurement(measurement)
            data_points.append(signed)
            
            with metrics_placeholder.container():
                m_col1, m_col2, m_col3, m_col4 = st.columns(4)
                with m_col1:
                    st.metric("Jour", f"{day}/21", phase)
                with m_col2:
                    st.metric("Température", f"{measurement['temperature']}°C")
                with m_col3:
                    st.metric("pH", f"{measurement['ph']}")
                with m_col4:
                    st.metric("Humidité", f"{measurement['humidity']}%")
            
            with chart_placeholder.container():
                if len(data_points) > 1:
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(
                        x=[d["day"] for d in data_points],
                        y=[d["temperature"] for d in data_points],
                        mode="lines+markers",
                        line=dict(color="#E31E24", width=2)
                    ))
                    fig.update_layout(height=250, margin=dict(l=20, r=20, t=20, b=20), yaxis_title="Temp (°C)")
                    st.plotly_chart(fig, use_container_width=True)
            
            with data_placeholder.container():
                st.markdown("### 📄 Mesures Signées (CERBERE)")
                display_df = pd.DataFrame(data_points[-5:])
                st.dataframe(display_df[["day", "phase", "temperature", "ph", "signature"]], use_container_width=True)
            
            time.sleep(0.6)
        
        # Calculate credits
        credits = BokashiMRVEngine.calculate_site_credits(site_id, biomass, area)
        cert_id = CerbereSecurity.generate_certificate_id()
        
        with cert_placeholder.container():
            st.markdown(f"""
            <div class='value-box-green' style='margin-top: 2rem;'>
                <h3>✅ CERTIFICAT MRV GÉNÉRÉ</h3>
                <p><strong>ID:</strong> {cert_id}</p>
                <p><strong>Site:</strong> {credits['site_name']}</p>
                <p><strong>Biomasse:</strong> {biomass} kg</p>
                <p><strong>Compost:</strong> {credits['compost_kg']:.0f} kg</p>
                <hr style='border-color: rgba(255,255,255,0.3);'>
                <p>♻️ <strong>Carbone:</strong> €{credits['carbon_value_eur']:.2f}</p>
                <p>💧 <strong>Eau:</strong> €{credits['water_value_eur']:.2f}</p>
                <p>🦋 <strong>Biodiversité:</strong> €{credits['bio_value_eur']:.2f}</p>
                <hr style='border-color: rgba(255,255,255,0.3);'>
                <h3>💰 TOTAL: €{credits['total_credits_eur']:.2f}</h3>
                <p>Votre part (70%): €{credits['your_share_eur']:.2f}</p>
                <p><strong>Standard:</strong> Bokashi MRV | ISO 14064-2</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.balloons()

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: ARCHITECTURE
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.page == "architecture":
    
    st.markdown("""
    <div class='premium-header'>
        <h1>🔧 Architecture Technique</h1>
        <p>Système MRV Edge-Native Bokashi</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ```
    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                    BOKASHI × REKARBON ARCHITECTURE                           │
    ├─────────────────────────────────────────────────────────────────────────────┤
    │                                                                             │
    │  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐         │
    │  │  SITE BOKASHI   │    │  SITE BOKASHI   │    │  SITE BOKASHI   │  ×N     │
    │  │  Raspberry Pi5  │    │  Raspberry Pi5  │    │  Raspberry Pi5  │  sites  │
    │  │  + Capteurs IoT │    │  + Capteurs IoT │    │  + Capteurs IoT │         │
    │  │  + CERBERE Lite │    │  + CERBERE Lite │    │  + CERBERE Lite │         │
    │  └────────┬────────┘    └────────┬────────┘    └────────┬────────┘         │
    │           │                      │                      │                   │
    │           └──────────────────────┼──────────────────────┘                   │
    │                                  │                                          │
    │                         ┌────────▼────────┐                                 │
    │                         │   4G / WiFi     │                                 │
    │                         │  Data Link      │                                 │
    │                         └────────┬────────┘                                 │
    │                                  │                                          │
    │  ┌───────────────────────────────┼───────────────────────────────┐         │
    │  │                          CLOUD REKARBON                       │         │
    │  │  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐       │         │
    │  │  │  DT-REC     │    │  DT-SEQ     │    │  DASHBOARD  │       │         │
    │  │  │ MRV Engine  │───▶│Token Engine │───▶│   Maître    │       │         │
    │  │  │  Bokashi    │    │ ERC-3643    │    │ Composteur  │       │         │
    │  │  └─────────────┘    └─────────────┘    └─────────────┘       │         │
    │  └───────────────────────────────────────────────────────────────┘         │
    │                                  │                                          │
    │                         ┌────────▼────────┐                                 │
    │                         │  CARBON MARKETS │                                 │
    │                         │  VCS | GS | Bio │                                 │
    │                         │ + Water Credits │                                 │
    │                         └─────────────────┘                                 │
    └─────────────────────────────────────────────────────────────────────────────┘
    ```
    """)
    
    st.markdown("---")
    
    # Technical specs
    st.markdown("### ⚙️ Spécifications Techniques")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 📡 Capteurs Site
        - **Température:** DS18B20 (-55 à +125°C)
        - **Humidité:** SHT31 (±2% RH)
        - **pH:** Sonde industrielle
        - **Gaz:** CO2, NH3, CH4
        - **Poids:** Cellule de charge
        
        **Hardware:**
        - Raspberry Pi 5 (8GB)
        - SSD NVMe 256GB
        - Boîtier IP65
        """)
    
    with col2:
        st.markdown("""
        #### 🔐 Sécurité (CERBERE)
        - **Signatures:** Ed25519
        - **Hashing:** SHA-256
        - **Chain:** Hash-chain locale
        - **Protocole:** TLS 1.3
        
        **Standards:**
        - ISO 14064-2:2019
        - VCS Bokashi
        - Gold Standard
        """)
    
    with col3:
        st.markdown("""
        #### ☁️ Cloud Platform
        - **API:** FastAPI + GraphQL
        - **Database:** TimescaleDB
        - **Tokens:** ERC-3643
        - **Uptime:** 99.9% SLA
        
        **Outputs:**
        - Crédits Carbone
        - Crédits Eau
        - Crédits Biodiversité
        - Certificats PDF
        """)

# ═══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown(f"""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p><strong>♻️ Bokashi × Rekarbon MRV Platform</strong></p>
    <p>Triple Valorisation: Compost + Jus + Crédits Multi-Impact</p>
    <p>👨‍🌾 {MAITRE_COMPOSTEUR['name']} - {MAITRE_COMPOSTEUR['location']}</p>
    <p>© 2026 Rekarbon SAS - All Rights Reserved</p>
    <p style='font-size: 0.8rem;'>v3.0 Premium + Suivi Individuels | Built with Streamlit & Plotly</p>
</div>
""", unsafe_allow_html=True)
