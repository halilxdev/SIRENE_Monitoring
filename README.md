# SIRENE Monitoring - Veille Nouvelles Entreprises

Script de surveillance des nouvelles micro-entreprises en Moselle via l'API INSEE SIRENE.

## Installation

```bash
# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement
source venv/bin/activate  # macOS/Linux
# ou venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt
```

## Configuration

1. Copier `.env` vers `.env.local`
2. Modifier `INSEE_API_KEY` dans `.env.local` avec votre vraie clé API
3. Ajuster les codes postaux `PREFIXES_CP` si nécessaire

## Utilisation

```bash
source venv/bin/activate
python veille.py
```

## Variables d'environnement

- `INSEE_API_KEY` : Clé API INSEE SIRENE
- `PREFIXES_CP` : Codes postaux à surveiller (séparés par virgules)
- `DAYS_LOOKBACK` : Nombre de jours en arrière pour la recherche