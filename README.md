# SIRENE Monitoring

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![INSEE API](https://img.shields.io/badge/INSEE-SIRENE_API-003B6C)
![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-26A5E4?logo=telegram&logoColor=white)

Surveillance automatisée des nouvelles micro-entreprises en Moselle via l'API INSEE SIRENE avec notifications Telegram.

## Fonctionnalités

- **Surveillance en temps réel** des créations de micro-entreprises
- **Filtrage géographique** par codes postaux de Moselle
- **Classification automatique** par codes NAF (activités)
- **Notifications Telegram** instantanées avec formatage HTML
- **Configuration flexible** via variables d'environnement

## Prérequis

- Python 3.9+
- Clé API INSEE SIRENE ([obtenir une clé](https://api.insee.fr/))
- Bot Telegram (optionnel, via [@BotFather](https://t.me/botfather))

## Installation

```bash
# Cloner le repository
git clone https://github.com/votre-username/SIRENE-Monitoring.git
cd SIRENE-Monitoring

# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt
```

## Configuration

### 1. Créer le fichier de configuration local

```bash
cp .env .env.local
```

### 2. Éditer `.env.local` avec vos paramètres

```ini
# API INSEE SIRENE
INSEE_API_KEY=votre_cle_api_insee_ici

# Codes postaux de Moselle à surveiller
PREFIXES_CP=576,578,574,572,575

# Période de recherche (en jours)
DAYS_LOOKBACK=1

# Configuration Telegram (optionnel)
TELEGRAM_TOKEN=votre_token_bot_telegram
TELEGRAM_CHAT_ID=votre_chat_id
```

## Utilisation

### Exécution manuelle

```bash
# Avec l'environnement activé
python main.py

# Ou directement
venv/bin/python main.py
```

## Structure du projet

```
SIRENE-Monitoring/
├── main.py           # Script principal
├── naf_codes.py      # Classification des codes NAF
├── .env              # Template de configuration
├── .env.local        # Configuration locale (ignoré par git)
├── requirements.txt  # Dépendances Python
└── .gitignore        # Fichiers à ignorer
```

## Variables d'environnement

| Variable | Description | Exemple |
|----------|-------------|---------|
| `INSEE_API_KEY` | Clé API INSEE SIRENE | `a7cd3b9d-902e...` |
| `PREFIXES_CP` | Codes postaux à surveiller | `576,578,574` |
| `DAYS_LOOKBACK` | Jours de recherche rétroactive | `1` |
| `TELEGRAM_TOKEN` | Token du bot Telegram | `8748945427:AAH...` |
| `TELEGRAM_CHAT_ID` | ID du chat Telegram | `7126227902` |

## Codes NAF supportés

Le fichier `naf_codes.py` contient la classification des activités :
- Commerce de détail
- Restauration
- Coiffure / Esthétique
- Construction
- Informatique
- Santé
- Et plus encore...

## Contribution

Les contributions sont bienvenues ! N'hésitez pas à :
- Ajouter de nouveaux codes NAF dans `naf_codes.py`
- Reporter des bugs
- Proposer des améliorations