# app.py
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from groq import Groq
from cours_data import SEANCES

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'default_secret_lille')

# Initialisation du client Groq
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html', seances=SEANCES)

@app.route('/seance/<int:seance_id>')
def seance(seance_id):
    data = SEANCES.get(seance_id)
    if not data:
        return "Séance introuvable", 404
    return render_template('seance.html', seance_id=seance_id, data=data, total_seances=len(SEANCES))

@app.route('/api/chat', methods=['POST'])
def chat():
    payload = request.get_json() or {}
    user_message = payload.get('message', '').strip()
    seance_id = payload.get('seance_id', 1)

    if not user_message:
        return jsonify({'error': 'Message vide'}), 400

    data = SEANCES.get(int(seance_id), {})
    contexte_cours = f"""
    SEANCE ACTUELLE DU COURS : Séance {seance_id} - {data.get('titre', '')}
    DESCRIPTION : {data.get('description', '')}
    CONTENU DU COURS : {data.get('cm', '')}
    EXERCICES DE LA SÉANCE : {data.get('td', '')}
    CORRIGÉS OFFICIELS : {data.get('corrige', '')}
    """
    system_prompt = f"""
        Tu es un Enseignant-Chercheur et Tuteur Pédagogique expert en Hydrologie de surface et Gestion des eaux pluviales à l'Université de Lille pour des étudiants de Master.

        CONSIGNE STRICTE POUR LES FORMULES MATHÉMATIQUES :
        1. Pour TOUTE formule centrée ou mise en évidence, utilise TOUJOURS la syntaxe avec doubles dollars :
        $$ formule $$
        Exemple : $$ \\boxed{{1\\text{{ mm sur }} 1\\text{{ ha}} = 10\\text{{ m}}^3}} $$
        2. Pour les formules ou variables dans le texte, utilise TOUJOURS les simples dollars :
        $ formule $
        Exemple : Soit une surface de $A = 100\\text{{ km}}^2$ et un débit $Q$.
        3. N'utilise JAMAIS de simples crochets [ ] ou parenthèses ( ) pour entourer des formules LaTeX.
        4. N'ajoute pas de points-virgules inutiles dans les formules mathématiques.

        Aide l'étudiant avec pédagogie, rigueur et bienveillance.
        
        CONTEXTE DU COURS :
        {contexte_cours}
    """


    try:
        completion = groq_client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.3,
            max_tokens=5000
        )
        reponse_ia = completion.choices[0].message.content
        return jsonify({'response': reponse_ia})
    except Exception as e:
        return jsonify({'error': f"Erreur avec l'API Groq : {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)