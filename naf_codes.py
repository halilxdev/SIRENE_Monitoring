"""
Correspondance entre codes NAF et libellés d'activités
Source: INSEE - Nomenclature d'activités française
"""

NAF_LABELS = {
    # Commerce
    "47": "Commerce de détail",
    "45": "Commerce / Réparation automobiles",

    # Restauration et hébergement
    "56": "Restauration",

    # Services aux particuliers
    "96.02": "Coiffure / Esthétique",
    "96.04": "Bien-être / Spa",

    # Construction
    "41": "Construction",
    "43": "Travaux de construction spécialisés",

    # Santé et action sociale
    "86": "Santé humaine",
    "88": "Action sociale",

    # Conseil et services aux entreprises
    "70": "Conseil / Management",
    "74": "Activités spécialisées",

    # Sport, loisirs et enseignement
    "93": "Sport / Loisirs",
    "85.51": "Enseignement sportif / Loisirs",

    # Transport et logistique
    "53": "Distribution postale / Livraison",

    # Informatique et télécommunications
    "62": "Informatique",
    "63": "Services d'information",
}

def get_naf_label(code):
    """
    Retourne le libellé d'activité correspondant au code NAF

    Args:
        code (str): Code NAF (ex: "47.11A", "62.01Z")

    Returns:
        str: Libellé de l'activité ou le code NAF si non trouvé
    """
    if not code:
        return "Activité inconnue"

    # Recherche par préfixe (ex: "47.11A" match "47")
    for prefix, label in NAF_LABELS.items():
        if code.startswith(prefix):
            return label

    # Si aucune correspondance, retourne le code tel quel
    return code