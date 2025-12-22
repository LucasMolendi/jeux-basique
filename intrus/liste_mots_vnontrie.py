#création d'une base de données contenant la liste de nom
liste_mots = [
    "forêt", "arbre", "fleur", "pluie", "vent", "orage", "feu", "eau", "air", "terre",
    "roche", "sable", "rivière", "lac", "océan", "mer", "colline", "montagne", "vallée", "prairie",
    "désert", "glacier", "caverne", "grottes", "falaise", "île", "archipel", "plaine", "jungle", "savane",
    "brouillard", "rosée", "givre", "neige", "tempête", "éclair", "lumière", "ombre", "soleil", "lune",
    "étoile", "galaxie", "univers", "cosmos", "astéroïde", "comète", "cratère", "volcan", "ciel", "horizon",
    "table", "chaise", "lampe", "livre", "plume", "papier", "stylo", "verre", "assiette", "fourchette",
    "épée", "bouclier", "arc", "flèche", "corde", "cloche", "clé", "porte", "fenêtre", "maison",
    "toit", "mur", "château", "tour", "pont", "barque", "voile", "navire", "roue", "chariot",
    "moulin", "forge", "marteau", "enclume", "pioche", "lanterne", "seau", "miroir", "peigne", "anneau",
    "chat", "chien", "cheval", "loup", "ours", "renard", "aigle", "corbeau", "hibou", "serpent",
    "grenouille", "poisson", "requin", "baleine", "dauphin", "poule", "coq", "lion", "tigre", "panthère",
    "éléphant", "girafe", "zèbre", "rhinocéros", "hippopotame", "singe", "papillon", "abeille", "fourmi", "araignée",
    "escargot", "lézard", "dragon", "licorne", "griffon", "hydre", "phénix", "sirène", "kraken", "chimère",
    "amour", "haine", "colère", "joie", "peur", "tristesse", "espoir", "désespoir", "courage", "force",
    "faiblesse", "sagesse", "folie", "rêve", "cauchemar", "souvenir", "destin", "avenir", "passé", "présent",
    "mémoire", "oubli", "silence", "murmure", "cri", "chant", "musique", "harmonie", "désordre", "paix",
    "guerre", "victoire", "défaite", "justice", "injustice", "vérité", "mensonge", "mystère", "secret", "légende",
    "courir", "marcher", "sauter", "nager", "voler", "glisser", "ramper", "grimper", "tomber", "danser",
    "chanter", "rire", "pleurer", "parler", "écouter", "voir", "sentir", "toucher", "penser", "imaginer",
    "créer", "détruire", "construire", "briser", "allumer", "éteindre", "ouvrir", "fermer", "donner", "prendre",
    "perdre", "trouver", "chercher", "attendre", "espérer", "croire", "savoir", "ignorer", "oser", "vaincre"
]
# Dico contenant des listes pour différents thèmes
themes_jeu = {
    "nature": ["forêt", "arbre", "fleur", "pluie", "vent", "orage", "feu", "eau", "air", "terre"],
    "paysage": ["océan", "montagne", "vallée", "désert", "glacier", "caverne", "falaise", "île", "jungle", "savane"],
    "cosmos": ["soleil", "lune", "étoile", "galaxie", "univers", "comète", "volcan", "ciel", "horizon", "aurore"],
    "animal": ["loup", "ours", "renard", "cheval", "lion", "tigre", "éléphant", "singe", "serpent", "cerf"],
    "mythologie": ["dragon", "licorne", "griffon", "phénix", "sirène", "kraken", "chimère", "hydre", "golem", "pégase"]
}