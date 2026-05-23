import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Charger les donnees depuis le fichier JSON
with open("lignes_ddd.json", "r") as f:
    lignes = json.load(f)

@app.route("/")
def accueil():
    return jsonify({
        "message": "Bienvenue sur l'API SenTransport !",
        "endpoints": ["/lignes", "/lignes/<id>", "/arrets", "/stats", "/lignes/recherche"]
    })

@app.route("/lignes")
def get_lignes():
    return jsonify(lignes)

@app.route("/lignes/<int:ligne_id>")
def get_ligne(ligne_id):
    ligne = next(
        (l for l in lignes if l["id"] == ligne_id),
        None
    )
    if ligne is None:
        return jsonify({"erreur": "Ligne non trouvee"}), 404
    return jsonify(ligne)

# Exercice 1
@app.route("/arrets")
def get_arrets():
    arrets_uniques = set(arret for ligne in lignes for arret in ligne["listeArrets"])
    
    liste_arrets = list(arrets_uniques)
    
    return jsonify(liste_arrets)

# Exercice 2
@app.route("/stats")
def get_stats():
    total_lignes = len(lignes)
    
    total_arrets = len(set(arret for ligne in lignes for arret in ligne["listeArrets"]))
    
    ligne_max = max(lignes, key=lambda l: l["arrets"])
    numero_ligne_max = ligne_max["numero"]
    
    return jsonify({
        "nbre total de lignes": total_lignes,
        "nbre total d'arrets": total_arrets,
        "ligne ayant le plus d'arrets": numero_ligne_max
    })

# Exercice 3
from flask import request

@app.route("/lignes/recherche")
def recherche_lignes():
    q = request.args.get("q", "").lower()
    
    lignes_filtrees = [
        l for l in lignes 
        if q in l["depart"].lower() or q in l["arrivee"].lower()
    ]
    
    return jsonify(lignes_filtrees)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

