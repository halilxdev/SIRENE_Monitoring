import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
from naf_codes import get_naf_label

load_dotenv()
load_dotenv('.env.local', override=True)

API_KEY = os.getenv('INSEE_API_KEY')
if not API_KEY:
    raise ValueError("INSEE_API_KEY n'est pas défini dans les variables d'environnement")

prefixes_str = os.getenv('PREFIXES_CP', '576,578,574,572,575')
PREFIXES_CP = [p.strip() for p in prefixes_str.split(',')]

days_lookback = int(os.getenv('DAYS_LOOKBACK', '1'))
date_debut = (datetime.now() - timedelta(days=days_lookback)).strftime("%Y-%m-%d")
date_fin = datetime.now().strftime("%Y-%m-%d")

def get_nouvelles_entreprises():

    cp_query = " OR ".join([f"codePostalEtablissement:{p}*" for p in PREFIXES_CP])
    
    url = "https://api.insee.fr/api-sirene/3.11/siret"
    headers = {
        "X-INSEE-Api-Key-Integration": API_KEY,
        "Accept": "application/json"
    }
    params = {
        "q": f"dateCreationEtablissement:[{date_debut} TO {date_fin}] AND ({cp_query}) AND categorieJuridiqueUniteLegale:1000",
        "nombre": 50,
        "champs": "siret,denominationUniteLegale,nomUniteLegale,prenomUsuelUniteLegale,activitePrincipaleEtablissement,codePostalEtablissement,libelleCommuneEtablissement,dateCreationEtablissement"
    }

    response = requests.get(url, headers=headers, params=params)
    print("Status:", response.status_code)
    print("Réponse:", response.text[:500])
    return response.json()

def main():
    print("Recherche des nouvelles micro-entreprises...")
    data = get_nouvelles_entreprises()

    if "etablissements" not in data:
        print("Aucun résultat ou erreur:", data)
        return

    etablissements = data["etablissements"]
    print(f"\n{len(etablissements)} nouvelles micro-entreprises en Moselle hier :\n")

    for e in etablissements:
        ul = e.get("uniteLegale", {})
        nom = ul.get("denominationUniteLegale") or f"{ul.get('prenomUsuelUniteLegale', '')} {ul.get('nomUniteLegale', '')}"
        
        adresse = e.get("adresseEtablissement", {})
        ville = adresse.get("libelleCommuneEtablissement", "")
        cp = adresse.get("codePostalEtablissement", "")
        
        periodes = e.get("periodesEtablissement", [])
        code_naf = periodes[0].get("activitePrincipaleEtablissement", "") if periodes else ""
        activite = get_naf_label(code_naf)
        date_creation = e.get("dateCreationEtablissement", "")

        print(f"- {nom.strip()} | {activite} | {cp} {ville} | créé le {date_creation}")

if __name__ == "__main__":
    main()
