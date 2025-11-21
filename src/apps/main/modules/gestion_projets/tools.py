import os

from django.conf import settings


def get_user_path(obj):
    return os.path.join(settings.WORKING_REPERTORY, str(obj.created_by))

def get_color_list():
    return {
        # Couleurs brutes (vives, bien reconnaissables)
        "#000000": {"fr": "Noir", "en": "Black"},
        "#FF4136": {"fr": "Rouge", "en": "Red"},
        "#0074D9": {"fr": "Bleu", "en": "Blue"},
        "#2ECC40": {"fr": "Vert", "en": "Green"},
        "#B10DC9": {"fr": "Violet", "en": "Violet"},
        "#FF851B": {"fr": "Orange", "en": "Orange"},
        "#FFDC00": {"fr": "Jaune", "en": "Yellow"},
        "#de00bc": {"fr": "Rose", "en": "Pink"},
        "#8B4513": {"fr": "Marron", "en": "Brown"},
        "#7F8C8D": {"fr": "Gris", "en": "Grey"},
        "#850000": {"fr": "Rouge foncé", "en": "DarkRed"},
        "#ff5d5d": {"fr": "Rouge clair", "en": "LightRed"},
        "#ff7400": {"fr": "Rouge orangé", "en": "OrangeRed"},
        "#0011b2": {"fr": "Bleu foncé", "en": "DarkBlue"},
        "#002eff": {"fr": "Bleu royal", "en": "RoyalBlue"},
        "#29b6f6": {"fr": "Bleu clair", "en": "LightBlue"},
        "#71ff7c": {"fr": "Vert clair", "en": "LightGreen"},
        "#007509": {"fr": "Vert foncé", "en": "DarkGreen"},
    }

def get_color_name_from_code(color_code, lang="fr"):
    color_dict = get_color_list()
    return color_dict.get(color_code, {}).get(lang)


def get_color_code_from_name(color_name_fr):
    for code, names in get_color_list().items():
        if names.get("fr") == color_name_fr:
            return code
    return None

def get_color_en_from_fr_name(color_name_fr):
    color_code = get_color_code_from_name(color_name_fr)
    if color_code:
        return get_color_name_from_code(color_code, lang="en")
    return None


def get_symbol_list():
    return {
        "circle": {
            "fr": "Cercle ●",
            "value": "circle",
            "symbol": "●",
            "mpl": "o"           # cercle
        },
        "square": {
            "fr": "Carré ■",
            "value": "square",
            "symbol": "■",
            "mpl": "s"           # carré
        },
        "triangle": {
            "fr": "Triangle Haut ▲",
            "value": "triangle",
            "symbol": "▲",
            "mpl": "^"           # triangle vers le haut
        },
        "inverted_triangle": {
            "fr": "Triangle Bas ▼",
            "value": "inverted_triangle",
            "symbol": "▼",
            "mpl": "v"           # triangle vers le bas
        },
        "x": {
            "fr": "Croix ✕",
            "value": "x",
            "symbol": "✕",
            "mpl": "x"           # croix diagonale
        },
        "cross": {
            "fr": "Plus ✚",
            "value": "cross",
            "symbol": "✚",
            "mpl": "+"           # croix classique
        },
        "asterisk": {
            "fr": "Étoile ✱",
            "value": "asterisk",
            "symbol": "✱",
            "mpl": "*"           # étoile
        },
        "hex": {
            "fr": "Hexagone ⬡",
            "value": "hex",
            "symbol": "⬡",
            "mpl": "h"           # hexagone
        }
    }



def get_symbol_name_from_code(symbol_code):
    symbol_dict = get_symbol_list()
    return symbol_dict.get(symbol_code, {}).get("symbol")