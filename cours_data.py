# cours_data.py
# -*- coding: utf-8 -*-

"""
Base de connaissances complète pour le cours d'Hydrologie de surface,
Gestion des eaux pluviales urbaines, Risques et Modélisation.
Niveau : Master Génie Civil / Sciences de l'Eau (Univ. Lille).
"""

SEANCES = {
    1: {
        "titre": "Cycle de l'eau, bilan hydrique & Morphométrie du bassin versant",
        "description": "Bilan hydrologique global (P = ETR + Q + ΔS), temps de résidence, compacité de Gravelius (Kc), rectangle équivalent et caractéristiques de relief (hypsométrie, pente Ig).",
        "cm": """
        <h4>1. Le cycle hydrologique et le bilan hydrique</h4>
        <p>L'hydrologie de surface étudie la composante précipitée qui s'écoule à la surface des sols jusqu'à l'exutoire. Sur un pas de temps donné (généralement annuel), l'équation de conservation de la masse s'écrit :</p>
        <div class="alert alert-primary text-center fs-5">
            $$P = ETR + Q + \\Delta S$$
        </div>
        <ul>
            <li>$P$ : Précipitations moyennes spatialisées sur le bassin ($\text{mm}$).</li>
            <li>$ETR$ : Évapotranspiration réelle ($\text{mm}$), intégrant l'évaporation directe et la transpiration végétale.</li>
            <li>$Q$ : Lame d'eau totale écoulée mesurée à l'exutoire ($\text{mm}$).</li>
            <li>$\\Delta S$ : Variation nette des réserves (sol, aquifères, neige, retenues). Sur une base interannuelle, $\\Delta S \\approx 0$, d'où $Q \\approx P - ETR$.</li>
        </ul>
        <p>Le <strong>coefficient d'écoulement moyen</strong> s'exprime par :</p>
        <div class="alert alert-secondary text-center">
            $$K_e = \\frac{Q}{P} \\quad (\\text{sans dimension})$$
        </div>
        <p><strong>Conversions hydrologiques essentielles :</strong></p>
        <div class="alert alert-light border">
            $$\\boxed{1\\text{ mm sur } 1\\text{ ha} = 10\\text{ m}^3} \\qquad \\boxed{1\\text{ mm sur } 1\\text{ km}^2 = 1\\,000\\text{ m}^3}$$
            $$V = H \\times A \\times 1\\,000 \\quad (V\\text{ en m}^3, H\\text{ en mm}, A\\text{ en km}^2) \\qquad \\overline{Q} = \\frac{V}{\\text{durée}}$$
        </div>

        <h4>2. Morphométrie et géométrie du bassin versant</h4>
        <p>Le bassin versant est la surface topographique interceptant les eaux ruisselant vers un exutoire commun. En milieu urbain, il est souvent modifié et délimité par les collecteurs d'assainissement.</p>
        
        <p><strong>Indice de compacité de Gravelius ($K_c$) :</strong><br>
        Rapport du périmètre du bassin à celui d'un cercle de même superficie :</p>
        <div class="alert alert-secondary text-center">
            $$K_c = \\frac{P}{2\\sqrt{\\pi A}} \\approx 0{,}28 \\cdot \\frac{P}{\\sqrt{A}} \\quad (P\\text{ en km, } A\\text{ en km}^2)$$
        </div>
        <ul>
            <li>$K_c = 1{,}0$ : Bassin parfaitement circulaire (isochronisme élevé, pointe de crue aiguë et violente).</li>
            <li>$K_c > 1{,}3$ : Bassin allongé (transfert désynchronisé, crue étalée dans le temps, débit de pointe amorti).</li>
        </ul>

        <p><strong>Rectangle équivalent (valable pour $K_c \\ge 1{,}12$) :</strong><br>
        Assimile le bassin à un rectangle de même surface $A$, même périmètre $P$ et même hypsométrie :</p>
        <div class="alert alert-secondary text-center">
            $$L = \\frac{K_c \\sqrt{A}}{1{,}12} \\left[ 1 + \\sqrt{1 - \\left(\\frac{1{,}12}{K_c}\\right)^2} \\right]$$
            $$l = \\frac{K_c \\sqrt{A}}{1{,}12} \\left[ 1 - \\sqrt{1 - \\left(\\frac{1{,}12}{K_c}\\right)^2} \\right]$$
        </div>

        <h4>3. Caractéristiques de relief et réseau hydrographique</h4>
        <ul>
            <li><strong>Pente moyenne du cours d'eau :</strong> $S = \\frac{\\Delta H}{L}$ ($\text{m/m}$).</li>
            <li><strong>Indice de pente global :</strong> $I_g = \\frac{D}{L}$, où $D$ représente la dénivelée utile séparant les altitudes contenant 5 % et 95 % de la courbe hypsométrique.</li>
            <li><strong>Densité de drainage :</strong> $D_d = \\frac{\\sum L_i}{A}$ ($\text{km/km}^2$). Plus $D_d$ est grande, plus la réponse hydrologique est rapide.</li>
        </ul>
        """,
        "td": """
        <h5>Exercice 1 : Bilan hydrique annuel et débit moyen</h5>
        <p>Un bassin versant naturel d'une superficie $A = 100\\text{ km}^2$ reçoit un apport pluviométrique moyen interannuel de $P = 800\\text{ mm/an}$. L'évapotranspiration réelle annuelle est estimée à $ETR = 500\\text{ mm/an}$. Les variations de stock sont considérées nulles sur l'année ($\\Delta S = 0$).</p>
        <ol>
            <li>Calculer la lame d'eau totale écoulée à l'exutoire $Q$ ($\text{mm/an}$) ainsi que le coefficient d'écoulement interannuel $K_e$.</li>
            <li>Déterminer le volume total annuel écoulé $V$ ($\text{m}^3$) et en déduire le débit moyen continu annuel $\\overline{Q}$ ($\text{m}^3/\\text{s}$).</li>
        </ol>

        <h5>Exercice 2 : Morphométrie, compacité et rectangle équivalent</h5>
        <p>Un bassin versant présente une surface $A = 25\\text{ km}^2$ et un périmètre mesuré de $P = 24\\text{ km}$.</p>
        <ol>
            <li>Calculer l'indice de compacité de Gravelius $K_c$. Quelle conclusion en tirer sur la dynamique de montée de crue ?</li>
            <li>Vérifier la condition d'application du rectangle équivalent et calculer sa longueur $L$ et sa largeur $l$. Vérifier que $L \\times l = A$.</li>
        </ol>
        """,
        "corrige": """
        <h5>Corrigé de l'Exercice 1 :</h5>
        <ol>
            <li><strong>Lame d'eau écoulée et coefficient d'écoulement :</strong><br>
            D'après l'équation du bilan :
            $$Q = P - ETR - \\Delta S = 800 - 500 - 0 = 300\\text{ mm/an}$$
            $$K_e = \\frac{Q}{P} = \\frac{300}{800} = 0{,}375 \\quad (37{,}5\\,\\%)$$
            </li>
            <li><strong>Volume et débit moyen :</strong><br>
            Application de la relation de conversion :
            $$V = Q \\times A \\times 1\\,000 = 300\\text{ mm} \\times 100\\text{ km}^2 \\times 1\\,000 = 30 \\times 10^6\\text{ m}^3$$
            Le débit moyen sur une année civile ($365\\text{ jours} \\times 86\\,400\\text{ s/jour} = 31\\,536\\,000\\text{ s}$) :
            $$\\overline{Q} = \\frac{30 \\times 10^6}{31\\,536\\,000} \\approx 0{,}951\\text{ m}^3/\\text{s}$$
            </li>
        </ol>

        <h5>Corrigé de l'Exercice 2 :</h5>
        <ol>
            <li><strong>Indice de Gravelius :</strong><br>
            $$K_c = 0{,}28 \\cdot \\frac{24}{\\sqrt{25}} = 0{,}28 \\cdot \\frac{24}{5} = 1{,}344$$
            Puisque $K_c = 1{,}344 > 1{,}30$, le bassin est nettement allongé. L'onde de crue sera étalée dans le temps, avec une désynchronisation des apports des différents affluents et un débit de pointe inférieur à celui d'un bassin compact de même surface.
            </li>
            <li><strong>Rectangle équivalent :</strong><br>
            $K_c = 1{,}344 \\ge 1{,}12$ : la méthode est valide.<br>
            Calculons les termes intermédiaires :
            $$\\frac{1{,}12}{K_c} = \\frac{1{,}12}{1{,}344} \\approx 0{,}8333 \\implies \\left(\\frac{1{,}12}{K_c}\\right)^2 \\approx 0{,}6944$$
            $$\\sqrt{1 - 0{,}6944} = \\sqrt{0{,}3056} \\approx 0{,}5528$$
            $$\\frac{K_c \\sqrt{A}}{1{,}12} = \\frac{1{,}344 \\times 5}{1{,}12} = 6{,}0\\text{ km}$$
            D'où :
            $$L = 6{,}0 \\times (1 + 0{,}5528) = 6{,}0 \\times 1{,}5528 \\approx 9{,}32\\text{ km}$$
            $$l = 6{,}0 \\times (1 - 0{,}5528) = 6{,}0 \\times 0{,}4472 \\approx 2{,}68\\text{ km}$$
            <strong>Vérification :</strong> $L \\times l = 9{,}32 \\times 2{,}68 = 24{,}98 \\approx 25\\text{ km}^2$. Le périmètre vaut $2 \\times (9{,}32 + 2{,}68) = 24\\text{ km}$.
            </li>
        </ol>
        """
    },
    2: {
        "titre": "Temps de concentration et cinématique des écoulements",
        "description": "Temps de concentration (tc), formules empiriques (Kirpich, Passini, Ventura), méthode de la vitesse par tronçon et temps d'entrée en assainissement.",
        "cm": """
        <h4>1. Notion de temps de concentration ($t_c$)</h4>
        <p>Le temps de concentration $t_c$ représente la durée nécessaire pour qu'une particule d'eau tombée sur le point hydrologiquement le plus éloigné atteigne l'exutoire du bassin versant. C'est à $t = t_c$ que la totalité du bassin contribue simultanément au ruissellement (débit de pointe maximal pour une intensité uniforme).</p>

        <h4>2. Formules empiriques usuelles</h4>
        <p>Chaque formule possède un domaine de validité propre :</p>
        
        <p><strong>Formule de Kirpich (bassins ruraux, pentes moyennes à fortes) :</strong></p>
        <div class="alert alert-primary text-center">
            $$t_c\\text{ (min)} = 0{,}0195 \\cdot L^{0{,}77} \\cdot S^{-0{,}385}$$
            <small>$L$ : Longueur du talweg principal ($\text{m}$), $S$ : Pente moyenne du thalweg ($\text{m/m}$).</small>
        </div>

        <p><strong>Formule de Passini (bassins naturels de surface moyenne) :</strong></p>
        <div class="alert alert-secondary text-center">
            $$t_c\\text{ (h)} = 0{,}108 \\cdot \\frac{(A \\cdot L)^{1/3}}{\\sqrt{S}}$$
            <small>$A$ en $\\text{km}^2$, $L$ en $\\text{km}$, $S$ en $\\text{m/m}$.</small>
        </div>

        <p><strong>Formule de Ventura :</strong></p>
        <div class="alert alert-secondary text-center">
            $$t_c\\text{ (h)} = 0{,}127 \\cdot \\sqrt{\\frac{A}{S}} \\quad (A\\text{ en km}^2, S\\text{ en m/m})$$
        </div>

        <h4>3. Méthode cinématique de la vitesse par tronçons</h4>
        <p>Sur un bassin subdivisé ou en milieu urbain, le temps global est la somme des temps de transit sur chaque bief géométrique :</p>
        <div class="alert alert-secondary text-center">
            $$t_c = t_e + \\sum_{i=1}^m \\frac{L_i}{V_i}$$
        </div>
        <ul>
            <li>$t_e$ : Temps d'humectation et d'entrée superficielle (ruissellement sur toitures, chaussées : 3 à 10 min).</li>
            <li>$L_i, V_i$ : Longueur et vitesse moyenne d'écoulement dans le collecteur ou le fossé $i$.</li>
        </ul>
        """,
        "td": """
        <h5>Exercice 1 : Calcul de Kirpich sur bassin versant rural</h5>
        <p>Un bassin rural possède un thalweg principal de longueur $L = 3\\,000\\text{ m}$ avec une dénivelée totale $\\Delta H = 60\\text{ m}$.</p>
        <ol>
            <li>Calculer la pente moyenne $S$ du cours d'eau en $\\text{m/m}$ et en pourcentage.</li>
            <li>Calculer le temps de concentration $t_c$ en minutes à l'aide de la formule de Kirpich.</li>
        </ol>

        <h5>Exercice 2 : Comparaison Kirpich vs Passini</h5>
        <p>Considérons le bassin ci-dessus avec une surface réceptrice $A = 4\\text{ km}^2$.</p>
        <ol>
            <li>Calculer $t_c$ avec la formule de Passini.</li>
            <li>Comparer et justifier les écarts observés entre les deux approches empiriques.</li>
        </ol>
        """,
        "corrige": """
        <h5>Corrigé de l'Exercice 1 :</h5>
        <ol>
            <li><strong>Pente moyenne :</strong><br>
            $$S = \\frac{\\Delta H}{L} = \\frac{60}{3\\,000} = 0{,}02\\text{ m/m} \\quad (2\\,\\%)$$
            </li>
            <li><strong>Temps de Kirpich :</strong><br>
            Calculons les termes exponentiels :
            $$L^{0{,}77} = 3\\,000^{0{,}77} = \\exp(0{,}77 \\times \\ln(3\\,000)) = \\exp(0{,}77 \\times 8{,}0064) = \\exp(6{,}1649) \\approx 475{,}77$$
            $$S^{-0{,}385} = 0{,}02^{-0{,}385} = \\exp(-0{,}385 \\times \\ln(0{,}02)) = \\exp(-0{,}385 \\times (-3{,}9120)) = \\exp(1{,}5061) \\approx 4{,}509$$
            $$t_c = 0{,}0195 \\times 475{,}77 \\times 4{,}509 \\approx 41{,}8\\text{ min} \\approx 42\\text{ min}$$
            </li>
        </ol>

        <h5>Corrigé de l'Exercice 2 :</h5>
        <ol>
            <li><strong>Formule de Passini :</strong><br>
            Données : $A = 4\\text{ km}^2$, $L = 3\\text{ km}$, $S = 0{,}02\\text{ m/m}$.
            $$(A \\cdot L)^{1/3} = (4 \\times 3)^{1/3} = 12^{1/3} \\approx 2{,}289$$
            $$\\sqrt{S} = \\sqrt{0{,}02} \\approx 0{,}1414$$
            $$t_c\\text{ (h)} = 0{,}108 \\cdot \\frac{2{,}289}{0{,}1414} \\approx 1{,}748\\text{ h} = 1{,}748 \\times 60 \\approx 105\\text{ min}$$
            </li>
            <li><strong>Analyse critique :</strong><br>
            Kirpich donne environ $42\\text{ min}$ tandis que Passini donne $105\\text{ min}$. Passini a été étalonnée en Italie sur des bassins plus grands et montagneux en intégrant l'amortissement superficiel, alors que Kirpich s'applique aux écoulements concentrés rapides en petits bassins agricoles aux États-Unis. En ingénierie, on retiendra la formule la plus représentative de la topographie locale.
            </li>
        </ol>
        """
    },
    3: {
        "titre": "Précipitations, analyse fréquentielle et courbes IDF",
        "description": "Statistique des extrêmes, période de retour T, risque cumulé P(n), loi de Gumbel, formule de Montana et construction des pluies de projet.",
        "cm": """
        <h4>1. Période de retour ($T$) et risque cumulé</h4>
        <p>La période de retour $T$ (en années) définit l'intervalle moyen séparant deux dépassements d'un événement hydrométéorologique donné. Chaque année, la probabilité de dépassement est $p = 1/T$.</p>
        <p>La probabilité d'observer <strong>au moins un dépassement</strong> de la crue de période de retour $T$ sur une période contractuelle ou une durée de vie de $n$ années s'écrit :</p>
        <div class="alert alert-primary text-center">
            $$P(n) = 1 - \\left(1 - \\frac{1}{T}\\right)^n$$
        </div>
        <p><em>Exemple frappant :</em> Une pluie cinquantennale ($T = 50$) a une probabilité de survenue de $1 - (0{,}98)^{50} \\approx 63{,}6\\,\\%$ sur 50 ans !</p>

        <h4>2. Ajustement statistique de Gumbel</h4>
        <p>Pour les séries de maxima annuels de précipitation, la fonction de répartition de Gumbel s'exprime par :</p>
        <div class="alert alert-secondary text-center">
            $$F(x) = \\exp\\left(-\\exp\\left(-\\frac{x - x_0}{u}\\right)\\right)$$
        </div>
        <p>Le quantile de précipitation $x(T)$ associé à la période de retour $T$ est :</p>
        <div class="alert alert-secondary text-center">
            $$x(T) = x_0 - u \\cdot \\ln\\left(-\\ln\\left(1 - \\frac{1}{T}\\right)\\right)$$
        </div>

        <h4>3. Courbes IDF et loi de Montana</h4>
        <p>Les courbes Intensité-Durée-Fréquence (IDF) relient l'intensité moyenne maximale $i$ à la durée de l'averse $t$. En France, Météo-France formalise ces courbes sous la <strong>loi de Montana</strong> :</p>
        <div class="alert alert-primary text-center">
            $$i(t) = a \\cdot t^{-b} \\quad (i\\text{ en mm/h, } t\\text{ en min})$$
            $$H(t) = \\frac{a \\cdot t^{1-b}}{60} \\quad (H\\text{ en mm})$$
        </div>
        <p>Plus la durée $t$ augmente, plus l'intensité moyenne diminue. Plus la période de retour $T$ augmente, plus le paramètre $a$ est grand.</p>
        """,
        "td": """
        <h5>Exercice 1 : Calculs de risque de dépassement</h5>
        <ol>
            <li>Quelle est la probabilité d'observer au moins une crue centennale ($T = 100$ ans) pendant la durée de vie nominale d'un ouvrage fixée à $n = 30$ ans ?</li>
            <li>Quelle période de retour de dimensionnement $T$ faut-il choisir pour que le risque cumulé de défaillance sur une période de 50 ans ne dépasse pas $10\\,\\%$ ?</li>
        </ol>

        <h5>Exercice 2 : Quantile décennal et loi de Montana</h5>
        <p>On adopte les coefficients pédagogiques de Montana pour une pluie décennale ($T = 10$ ans) : $a = 300$ et $b = 0{,}70$.</p>
        <ol>
            <li>Calculer l'intensité moyenne $i$ en $\\text{mm/h}$ pour des averses de durées $t = 5\\text{ min}$, $t = 25\\text{ min}$ et $t = 180\\text{ min}$.</li>
            <li>Calculer les hauteurs cumulées correspondantes $H(t)$ en $\\text{mm}$.</li>
        </ol>
        """,
        "corrige": """
        <h5>Corrigé de l'Exercice 1 :</h5>
        <ol>
            <li><strong>Probabilité sur 30 ans ($T = 100$) :</strong><br>
            $$P(30) = 1 - \\left(1 - \\frac{1}{100}\\right)^{30} = 1 - (0{,}99)^{30} = 1 - 0{,}7397 \\approx 0{,}2603 \\quad (26\\,\\%)$$
            </li>
            <li><strong>Période de retour pour un risque limité à 10 % sur 50 ans :</strong><br>
            $$1 - \\left(1 - \\frac{1}{T}\\right)^{50} = 0{,}10 \\iff \\left(1 - \\frac{1}{T}\\right)^{50} = 0{,}90$$
            $$1 - \\frac{1}{T} = 0{,}90^{1/50} = \\exp\\left(\\frac{\\ln(0{,}90)}{50}\\right) = \\exp(-0{,}002107) \\approx 0{,}997895$$
            $$\\frac{1}{T} = 1 - 0{,}997895 = 0{,}002105 \\implies T = \\frac{1}{0{,}002105} \\approx 475\\text{ ans}$$
            Pour garantir une sécurité à 90 % sur 50 ans, il faut dimensionner l'ouvrage pour la crue d'occurrence 475 ans.
            </li>
        </ol>

        <h5>Corrigé de l'Exercice 2 :</h5>
        <ol>
            <li><strong>Intensités de Montana :</strong><br>
            Loi : $i(t) = 300 \\cdot t^{-0{,}70}$.
            <ul>
                <li>Pour $t = 5\\text{ min}$ : $5^{-0{,}70} \\approx 0{,}3243 \\implies i(5) = 300 \\times 0{,}3243 \\approx 97{,}3\\text{ mm/h}$.</li>
                <li>Pour $t = 25\\text{ min}$ : $25^{-0{,}70} = (5^2)^{-0{,}70} = 5^{-1{,}40} \\approx 0{,}10515 \\implies i(25) = 300 \\times 0{,}10515 \\approx 31{,}54\\text{ mm/h}$.</li>
                <li>Pour $t = 180\\text{ min}$ : $180^{-0{,}70} \\approx 0{,}02629 \\implies i(180) = 300 \\times 0{,}02629 \\approx 7{,}89\\text{ mm/h} \\approx 8{,}0\\text{ mm/h}$.</li>
            </ul>
            </li>
            <li><strong>Hauteurs cumulées :</strong><br>
            $H(t) = \\frac{i(t) \\times t}{60}$.
            <ul>
                <li>$H(5) = \\frac{97{,}3 \\times 5}{60} \\approx 8{,}1\\text{ mm}$.</li>
                <li>$H(25) = \\frac{31{,}54 \\times 25}{60} \\approx 13{,}1\\text{ mm}$.</li>
                <li>$H(180) = \\frac{7{,}89 \\times 180}{60} \\approx 23{,}7\\text{ mm}$.</li>
            </ul>
            </li>
        </ol>
        """
    },
    4: {
        "titre": "Pertes au ruissellement, infiltration & méthode SCS-CN",
        "description": "Mécanismes hortoniens vs par saturation (Dunne), coefficient de ruissellement pondéré, surface active et modèle américain SCS-CN (Curve Number).",
        "cm": """
        <h4>1. Processus de formation du ruissellement</h4>
        <ul>
            <li><strong>Ruissellement hortonien (à capacité d'infiltration dépassée) :</strong> survient dès que l'intensité de précipitation $i(t)$ excède la capacité d'infiltration $f(t)$ du sol (fréquent sur sols imperméabilisés, battants ou arides).</li>
            <li><strong>Ruissellement par saturation (Dunne) :</strong> survient quand la nappe ou le profil de sol est intégralement saturé d'eau (bas de versants, zones alluviales humides).</li>
        </ul>

        <h4>2. Coefficient de ruissellement $C$ et surface active</h4>
        <p>Le coefficient volumétrique $C$ représente la part de la pluie brute transformée en pluie nette ruisselée ($0 \\le C \\le 1$) :</p>
        <div class="alert alert-secondary text-center">
            $$C_{\\text{pond}} = \\frac{\\sum (C_i \\cdot A_i)}{\\sum A_i} \\qquad S_a = C_{\\text{pond}} \\cdot A$$
        </div>
        <p><em>Valeurs courantes :</em> Toitures & voiries : $0{,}90$ à $0{,}95$ ; Parkings bitumés : $0{,}80$ à $0{,}90$ ; Pavillonnaire : $0{,}30$ à $0{,}50$ ; Jardins/Parcs : $0{,}10$ à $0{,}20$.</p>

        <h4>3. Modèle SCS-CN (Soil Conservation Service)</h4>
        <p>Utilisé mondialement sur bassins périurbains et ruraux. La lame d'eau nette ruisselée $Q$ ($\text{mm}$) pour une averse brute $P$ ($\text{mm}$) s'écrit :</p>
        <div class="alert alert-primary text-center">
            $$S = \\frac{25\\,400}{CN} - 254 \\quad (S\\text{ en mm})$$
            $$I_a = 0{,}2 \\cdot S \\quad (\\text{pertes initiales : interception, dépressions})$$
            $$Q = \\frac{(P - I_a)^2}{P - I_a + S} = \\frac{(P - 0{,}2S)^2}{P + 0{,}8S} \\quad \\text{si } P > I_a \\text{, sinon } Q = 0$$
        </div>
        <p>$CN$ (0 à 100) dépend du groupe hydrologique de sol (A : perméable à D : argile imperméable), de l'occupation du sol et des conditions hydriques préalables (AMC I, II, III).</p>
        """,
        "td": """
        <h5>Exercice 1 : Application de la méthode SCS-CN</h5>
        <p>Une pluie d'orage de hauteur cumulée $P = 80\\text{ mm}$ tombe sur un bassin périurbain de superficie $A = 5\\text{ km}^2$, dont le Curve Number est estimé à $CN = 80$.</p>
        <ol>
            <li>Calculer la rétention potentielle maximale $S$ en mm, puis les pertes initiales $I_a$.</li>
            <li>Calculer la lame d'eau ruisselée nette $Q$ en mm.</li>
            <li>En déduire le coefficient de ruissellement moyen équivalent et le volume total ruisselé à l'exutoire en $\\text{m}^3$.</li>
        </ol>

        <h5>Exercice 2 : Coefficient pondéré d'un aménagement mixte</h5>
        <p>Un projet urbain de $15\\text{ ha}$ est composé de : $6\\text{ ha}$ de voiries/toitures ($C = 0{,}90$), $4\\text{ ha}$ d'habitats collectifs ($C = 0{,}65$) et $5\\text{ ha}$ d'espaces verts aménagés ($C = 0{,}15$).</p>
        <ol>
            <li>Calculer le coefficient de ruissellement pondéré $C$ et la surface active correspondante $S_a$.</li>
        </ol>
        """,
        "corrige": """
        <h5>Corrigé de l'Exercice 1 :</h5>
        <ol>
            <li><strong>Calcul de $S$ et $I_a$ :</strong><br>
            $$S = \\frac{25\\,400}{80} - 254 = 317{,}5 - 254 = 63{,}5\\text{ mm}$$
            $$I_a = 0{,}2 \\times 63{,}5 = 12{,}7\\text{ mm}$$
            </li>
            <li><strong>Lame d'eau ruisselée nette $Q$ :</strong><br>
            Puisque $P = 80\\text{ mm} > I_a = 12{,}7\\text{ mm}$, le ruissellement s'amorce :
            $$P - I_a = 80 - 12{,}7 = 67{,}3\\text{ mm}$$
            $$P - I_a + S = 67{,}3 + 63{,}5 = 130{,}8\\text{ mm}$$
            $$Q = \\frac{67{,}3^2}{130{,}8} = \\frac{4\\,529{,}29}{130{,}8} \\approx 34{,}63\\text{ mm} \\approx 34{,}6\\text{ mm}$$
            </li>
            <li><strong>Coefficient d'écoulement et volume ruisselé :</strong><br>
            $$C_{\\text{éq}} = \\frac{Q}{P} = \\frac{34{,}63}{80} \\approx 0{,}433 \\quad (43{,}3\\,\\%)$$
            $$V = Q \\times A \\times 1\\,000 = 34{,}63\\text{ mm} \\times 5\\text{ km}^2 \\times 1\\,000 = 173\\,150\\text{ m}^3 \\approx 173\\,000\\text{ m}^3$$
            </li>
        </ol>

        <h5>Corrigé de l'Exercice 2 :</h5>
        <ol>
            <li><strong>Coefficient de ruissellement pondéré :</strong><br>
            $$C = \\frac{6 \\times 0{,}90 + 4 \\times 0{,}65 + 5 \\times 0{,}15}{15} = \\frac{5{,}40 + 2{,}60 + 0{,}75}{15} = \\frac{8{,}75}{15} \\approx 0{,}583$$
            $$S_a = 0{,}583 \\times 15\\text{ ha} = 8{,}75\\text{ ha} = 87\\,500\\text{ m}^2$$
            </li>
        </ol>
        """
    },
    5: {
        "titre": "Transformation pluie-débit & Débits de pointe",
        "description": "Méthode rationnelle, formule superficielle de Caquot (IT 1977), hydrogramme unitaire triangulaire (SCS) et formule régionale Crupédix.",
        "cm": """
        <h4>1. La méthode rationnelle</h4>
        <p>Valable pour les bassins versants homogènes de surface modérée ($A < 100$ à $200\\text{ ha}$). L'hypothèse fondamentale pose que le débit de pointe maximal se produit pour une pluie d'intensité constante $i$ dont la durée égale exactement le temps de concentration $t_c$ :</p>
        <div class="alert alert-primary text-center">
            $$Q_p = \\frac{C \\cdot i(t_c) \\cdot A}{360} \\quad (Q_p\\text{ en m}^3/\\text{s}, i\\text{ en mm/h}, A\\text{ en ha})$$
            $$Q_p = \\frac{C \\cdot i(t_c) \\cdot A}{3{,}6} \\quad (Q_p\\text{ en m}^3/\\text{s}, i\\text{ en mm/h}, A\\text{ en km}^2)$$
        </div>

        <h4>2. Formule superficielle de Caquot (Circulaire de 1977)</h4>
        <p>Spécifique à l'assainissement urbain français, elle intègre l'effet de stockage du réseau et la forme non uniforme de la pluie :</p>
        <div class="alert alert-secondary text-center">
            $$Q_p = k \\cdot I^\\alpha \\cdot C^\\beta \\cdot A^\\gamma$$
            <small>$I$ : pente moyenne ($\text{m/m}$), $C$ : coefficient de ruissellement, $A$ : surface ($\text{ha}$). Pour la Région 1 et $T = 10$ ans : $k \\approx 1{,}43$ ; $\\alpha \\approx 0{,}29$ ; $\\beta \\approx 1{,}20$ ; $\\gamma \\approx 0{,}78$.</small>
        </div>

        <h4>3. Hydrogramme unitaire triangulaire du SCS</h4>
        <p>Réponse du bassin versant à une pluie nette unitaire de hauteur $P_n$ et de durée $D$ :</p>
        <div class="alert alert-secondary text-center">
            $$T_p = \\frac{D}{2} + 0{,}6 \\cdot t_c \\quad (\\text{temps de montée en heures})$$
            $$Q_p = \\frac{0{,}208 \\cdot A \\cdot P_n}{T_p} \\quad (Q_p\\text{ en m}^3/\\text{s}, A\\text{ en km}^2, P_n\\text{ en mm}, T_p\\text{ en h})$$
        </div>

        <h4>4. Méthode régionale Crupédix</h4>
        <p>Estimation du débit de crue décennale $Q_{10}$ sur bassins versants naturels :</p>
        <div class="alert alert-secondary text-center">
            $$Q_{10} = S^{0{,}8} \\cdot \\left(\\frac{P_{10}}{80}\\right)^2 \\cdot R \\quad (S\\text{ en km}^2, P_{10}\\text{ en mm/jour}, R\\text{ coefficient régional})$$
        </div>
        """,
        "td": """
        <h5>Exercice 1 : Méthode rationnelle et impact de l'imperméabilisation</h5>
        <p>Un bassin versant de $12\\text{ ha}$ présente dans sa configuration rurale initiale un coefficient $C_1 = 0{,}45$ et un temps de concentration mesuré $t_c = 25\\text{ min}$. On adopte la formule de Montana décennale : $i(t) = 300 \\cdot t^{-0{,}70}$ ($\text{mm/h}$).</p>
        <ol>
            <li>Calculer l'intensité décennale $i(t_c)$ et le débit de pointe décennal $Q_1$ en $\\text{m}^3/\\text{s}$ et en $\\text{L/s}$.</li>
            <li>Par suite de l'urbanisation, le coefficient passe à $C_2 = 0{,}80$ (en supposant $t_c$ maintenu à 25 min). Calculer le nouveau débit de pointe $Q_2$ et déterminer l'augmentation en pourcentage.</li>
        </ol>

        <h5>Exercice 2 : Hydrogramme unitaire triangulaire</h5>
        <p>Soit un bassin versant naturel de $A = 10\\text{ km}^2$ avec $t_c = 2{,}5\\text{ h}$. Une averse nette unitaire de $P_n = 20\\text{ mm}$ tombe pendant une durée $D = 1\\text{ h}$.</p>
        <ol>
            <li>Calculer le temps de montée $T_p$ de l'hydrogramme.</li>
            <li>Calculer le débit maximal de pointe $Q_p$.</li>
        </ol>
        """,
        "corrige": """
        <h5>Corrigé de l'Exercice 1 :</h5>
        <ol>
            <li><strong>Intensité et débit de pointe initial :</strong><br>
            $$i(25) = 300 \\times 25^{-0{,}70} \\approx 31{,}54\\text{ mm/h}$$
            $$Q_1 = \\frac{C_1 \\cdot i \\cdot A}{360} = \\frac{0{,}45 \\times 31{,}54 \\times 12}{360} = \\frac{170{,}32}{360} \\approx 0{,}473\\text{ m}^3/\\text{s} = 473\\text{ L/s}$$
            </li>
            <li><strong>Après urbanisation :</strong><br>
            $$Q_2 = \\frac{0{,}80 \\times 31{,}54 \\times 12}{360} \\approx 0{,}841\\text{ m}^3/\\text{s} = 841\\text{ L/s}$$
            $$+ \\Delta \\% = \\left(\\frac{0{,}841}{0{,}473} - 1\\right) \\times 100 = \\left(\\frac{0{,}80}{0{,}45} - 1\\right) \\times 100 \\approx +77{,}8\\,\\% \\approx +78\\,\\%$$
            <em>Remarque pratique :</em> Dans la réalité, l'imperméabilisation réduit également le temps de concentration $t_c$, ce qui fait croître $i(t_c)$ et aggrave encore davantage le pic d'écoulement.
            </li>
        </ol>

        <h5>Corrigé de l'Exercice 2 :</h5>
        <ol>
            <li><strong>Temps de montée :</strong><br>
            $$T_p = \\frac{D}{2} + 0{,}6 \\cdot t_c = \\frac{1}{2} + 0{,}6 \\times 2{,}5 = 0{,}5 + 1{,}5 = 2{,}0\\text{ h}$$
            </li>
            <li><strong>Débit de pointe de l'HU :</strong><br>
            $$Q_p = \\frac{0{,}208 \\cdot A \\cdot P_n}{T_p} = \\frac{0{,}208 \\times 10 \\times 20}{2{,}0} = 20{,}8\\text{ m}^3/\\text{s}$$
            </li>
        </ol>
        """
    },
    6: {
        "titre": "Hydraulique à surface libre : Canaux et cours d'eau",
        "description": "Écoulement uniforme (Manning-Strickler), géométrie hydraulique (section, périmètre, rayon hydraulique), régimes fluvial/torrentiel (Froude) et courbe de tarage.",
        "cm": """
        <h4>1. Géométrie hydraulique et formule de Manning-Strickler</h4>
        <p>Pour un écoulement à surface libre uniforme dans un canal de section $A$ et de périmètre mouillé $P_m$ :</p>
        <div class="alert alert-primary text-center">
            $$R_h = \\frac{A}{P_m} \\quad (\\text{Rayon hydraulique en m})$$
            $$V = K \\cdot R_h^{2/3} \\cdot I^{1/2} \\qquad Q = K \\cdot A \\cdot R_h^{2/3} \\cdot I^{1/2}$$
            <small>$K$ : Coefficient de Strickler ($\text{m}^{1/3}/\text{s}$), $I$ : Pente longitudinale du fond ($\text{m/m}$).</small>
        </div>
        <p><em>Valeurs indicatives de $K$ :</em> PVC/PEHD : 100 ; Béton lisse : 70-80 ; Canaux maçonnés : 50-60 ; Fossés enherbés : 25-35 ; Lits naturels de rivière : 20-35.</p>

        <h4>2. Canal trapézoïdal</h4>
        <p>Pour un canal de largeur au radier $b$, de profondeur d'eau $h$ et de fruit de berge $m$ ($1\\text{V} / m\\text{H}$) :</p>
        <div class="alert alert-secondary text-center">
            $$A = (b + m \\cdot h) \\cdot h \\qquad P_m = b + 2h\\sqrt{1 + m^2} \\qquad B = b + 2mh$$
        </div>

        <h4>3. Régimes d'écoulement et nombre de Froude</h4>
        <p>Rapport adimensionnel entre forces d'inertie et de gravité :</p>
        <div class="alert alert-primary text-center">
            $$Fr = \\frac{V}{\\sqrt{g \\cdot h_m}} \\quad \\text{avec } h_m = \\frac{A}{B}$$
        </div>
        <ul>
            <li>$Fr < 1$ : Régime <strong>fluvial</strong> (subcritique). La vitesse est modérée, toute perturbation se propage vers l'amont (contrôle aval).</li>
            <li>$Fr = 1$ : Régime <strong>critique</strong>. L'énergie spécifique $H_s = h + \\frac{V^2}{2g}$ est minimale.</li>
            <li>$Fr > 1$ : Régime <strong>torrentiel</strong> (supercritique). L'onde d'information ne peut remonter vers l'amont (contrôle amont).</li>
        </ul>
        """,
        "td": """
        <h5>Exercice : Dimensionnement d'un canal trapézoïdal</h5>
        <p>Un canal d'évacuation trapézoïdal en terre enherbée ($K = 30\\text{ m}^{1/3}/\\text{s}$) possède une largeur au radier $b = 6{,}0\\text{ m}$, un fruit de talus $m = 1{,}0$ ($45^\\circ$), une pente de fond longitudinale $I = 0{,}1\\,\\%$ ($0{,}001\\text{ m/m}$) et transporte une hauteur d'eau normale $h = 1{,}50\\text{ m}$. Prendre $g = 9{,}81\\text{ m/s}^2$.</p>
        <ol>
            <li>Calculer la section mouillée $A$, le périmètre mouillé $P_m$ et le rayon hydraulique $R_h$.</li>
            <li>Déterminer la vitesse moyenne découlement $V$ et le débit transporté $Q$.</li>
            <li>Calculer la largeur au miroir $B$, la profondeur hydraulique moyenne $h_m$, le nombre de Froude $Fr$ et caractériser le régime découlement.</li>
        </ol>
        """,
        "corrige": """
        <h5>Corrigé de l'Exercice :</h5>
        <ol>
            <li><strong>Grandeurs géométriques :</strong><br>
            $$A = (b + m \\cdot h) \\cdot h = (6{,}0 + 1{,}0 \\times 1{,}50) \\times 1{,}50 = 7{,}50 \\times 1{,}50 = 11{,}25\\text{ m}^2$$
            $$P_m = b + 2h\\sqrt{1 + m^2} = 6{,}0 + 2 \\times 1{,}50 \\times \\sqrt{1 + 1^2} = 6{,}0 + 3{,}0\\sqrt{2} \\approx 6{,}0 + 4{,}243 = 10{,}243\\text{ m}$$
            $$R_h = \\frac{A}{P_m} = \\frac{11{,}25}{10{,}243} \\approx 1{,}098\\text{ m} \\approx 1{,}10\\text{ m}$$
            </li>
            <li><strong>Hydraulique de l'écoulement :</strong><br>
            $$R_h^{2/3} = 1{,}098^{2/3} \\approx 1{,}0645$$
            $$\\sqrt{I} = \\sqrt{0{,}001} \\approx 0{,}03162$$
            $$V = K \\cdot R_h^{2/3} \\cdot \\sqrt{I} = 30 \\times 1{,}0645 \\times 0{,}03162 \\approx 1{,}010\\text{ m/s}$$
            $$Q = A \\cdot V = 11{,}25 \\times 1{,}010 \\approx 11{,}36\\text{ m}^3/\\text{s} \\approx 11{,}4\\text{ m}^3/\\text{s}$$
            </li>
            <li><strong>Nombre de Froude et régime :</strong><br>
            $$B = b + 2mh = 6{,}0 + 2 \\times 1{,}0 \\times 1{,}50 = 9{,}0\\text{ m}$$
            $$h_m = \\frac{A}{B} = \\frac{11{,}25}{9{,}0} = 1{,}25\\text{ m}$$
            $$\\sqrt{g \\cdot h_m} = \\sqrt{9{,}81 \\times 1{,}25} = \\sqrt{12{,}2625} \\approx 3{,}502\\text{ m/s}$$
            $$Fr = \\frac{V}{\\sqrt{g \\cdot h_m}} = \\frac{1{,}010}{3{,}502} \\approx 0{,}288 \\approx 0{,}29$$
            Puisque $Fr = 0{,}29 < 1$, l'écoulement s'effectue en régime <strong>fluvial</strong> (subcritique), avec une ligne d'eau gouvernée par les conditions hydrauliques d'aval.
            </li>
        </ol>
        """
    },
    7: {
        "titre": "Hydraulique des conduites & Organes de régulation",
        "description": "Dimensionnement des collecteurs fermés à pleine section, vitesse d'autocurage, vidange par orifice sous charge et déversoirs d'orage.",
        "cm": """
        <h4>1. Collecteurs fermés à section circulaire</h4>
        <p>À pleine section ($h = D$), on a $A = \\frac{\\pi D^2}{4}$ et $P_m = \\pi D$, soit un rayon hydraulique $R_h = \\frac{D}{4}$. La formule de Manning-Strickler devient :</p>
        <div class="alert alert-primary text-center">
            $$Q_{ps} = K \\cdot \\frac{\\pi D^2}{4} \\cdot \\left(\\frac{D}{4}\\right)^{2/3} \\cdot I^{1/2} = K \\cdot \\frac{\\pi}{4 \\cdot 4^{2/3}} \\cdot D^{8/3} \\cdot I^{1/2}$$
            $$D_{\\text{théo}} = \\left[ \\frac{Q}{K \\cdot \\frac{\\pi}{4 \\cdot 4^{2/3}} \\cdot I^{1/2}} \\right]^{3/8}$$
        </div>
        <p><strong>Critères réglementaires d'exploitation :</strong></p>
        <ul>
            <li><strong>Autocurage :</strong> $V \\ge 0{,}6\\text{ m/s}$ pour les pluies courantes (évite la sédimentation des sables).</li>
            <li><strong>Vitesse limite d'abrasion :</strong> $V \\le 4{,}0$ à $5{,}0\\text{ m/s}$ (évite l'usure prématurée des parois).</li>
            <li>Le diamètre théorique calculé doit toujours être arrondi au diamètre nominal commercial supérieur (DN 400, 500, 600, 700, 800 mm, etc.).</li>
        </ul>

        <h4>2. Orifices de fuite sous charge</h4>
        <p>Pour vidanger un réservoir de rétention avec un débit régulé :</p>
        <div class="alert alert-secondary text-center">
            $$Q = \\mu \\cdot S_0 \\cdot \\sqrt{2gh} \\qquad S_0 = \\frac{\\pi d^2}{4}$$
            <small>$\\mu \\approx 0{,}60$ à $0{,}62$ (orifice à paroi mince), $h$ : charge hydraulique au-dessus de l'axe de l'orifice ($\text{m}$).</small>
        </div>

        <h4>3. Déversoirs de surverse (seuil dénoyé)</h4>
        <div class="alert alert-secondary text-center">
            $$Q = m_d \\cdot L_d \\cdot \\sqrt{2g} \\cdot h_d^{3/2}$$
            <small>$m_d \\approx 0{,}40$ (seuil mince), $L_d$ : largeur déversante, $h_d$ : lame d'eau au-dessus de la crête.</small>
        </div>
        """,
        "td": """
        <h5>Exercice 1 : Dimensionnement d'un collecteur d'eaux pluviales</h5>
        <p>On doit transiter un débit de pointe décennal $Q_p = 0{,}473\\text{ m}^3/\\text{s}$ dans une conduite circulaire en béton armé ($K = 70\\text{ m}^{1/3}/\\text{s}$) posée avec une pente constante $I = 0{,}5\\,\\%$ ($0{,}005\\text{ m/m}$).</p>
        <ol>
            <li>Calculer le diamètre théorique à pleine section $D_{\\text{théo}}$ en mètres.</li>
            <li>Choisir le diamètre commercial supérieur dans la série standard (DN 500, 600, 700, 800 mm).</li>
            <li>Calculer la capacité à pleine section $Q_{ps}$ et la vitesse à pleine section $V_{ps}$ du DN retenu. L'autocurage est-il assuré ?</li>
        </ol>

        <h5>Exercice 2 : Orifice de vidange calibré</h5>
        <p>Un bassin de rétention doit évacuer un débit de fuite maximal de $36\\text{ L/s}$ ($0{,}036\\text{ m}^3/\\text{s}$) sous une charge d'eau $h = 1{,}50\\text{ m}$ à l'axe. Le coefficient de contraction de l'orifice vaut $\\mu = 0{,}60$. Prendre $g = 9{,}81\\text{ m/s}^2$.</p>
        <ol>
            <li>Calculer la section requise $S_0$ de l'orifice en $\\text{m}^2$.</li>
            <li>En déduire le diamètre calibré de l'orifice $d$ en millimètres.</li>
        </ol>
        """,
        "corrige": """
        <h5>Corrigé de l'Exercice 1 :</h5>
        <ol>
            <li><strong>Diamètre théorique :</strong><br>
            Constante géométrique de la conduite circulaire :
            $$\\frac{\\pi}{4 \\cdot 4^{2/3}} = \\frac{\\pi}{4 \\cdot 2{,}5198} \\approx 0{,}3117$$
            $$K \\cdot 0{,}3117 \\cdot \\sqrt{I} = 70 \\times 0{,}3117 \\times \\sqrt{0{,}005} = 21{,}819 \\times 0{,}07071 \\approx 1{,}543$$
            $$D^{8/3} = \\frac{Q}{1{,}543} = \\frac{0{,}473}{1{,}543} \\approx 0{,}3065$$
            $$D_{\\text{théo}} = 0{,}3065^{3/8} = 0{,}3065^{0{,}375} \\approx 0{,}641\\text{ m} = 641\\text{ mm}$$
            </li>
            <li><strong>Diamètre commercial :</strong><br>
            On retient le diamètre standard supérieur immédiatement disponible : <strong>DN 700 mm</strong> ($D = 0{,}70\\text{ m}$).
            </li>
            <li><strong>Contrôle à pleine section :</strong><br>
            $$D^{8/3} = 0{,}70^{8/3} \\approx 0{,}3879$$
            $$Q_{ps} = 1{,}543 \\times 0{,}3879 \\approx 0{,}598\\text{ m}^3/\\text{s} \\approx 0{,}60\\text{ m}^3/\\text{s}$$
            Section mouillée : $A_{ps} = \\frac{\\pi \\times 0{,}70^2}{4} \\approx 0{,}3848\\text{ m}^2$.
            $$V_{ps} = \\frac{Q_{ps}}{A_{ps}} = \\frac{0{,}598}{0{,}3848} \\approx 1{,}55\\text{ m/s}$$
            Pour le débit de projet : $\\frac{Q}{Q_{ps}} = \\frac{0{,}473}{0{,}598} \\approx 0{,}79$. La vitesse réelle d'écoulement est d'environ $1{,}60\\text{ m/s}$, largement supérieure au seuil d'autocurage ($0{,}6\\text{ m/s}$) et inférieure à la vitesse critique d'usure ($4\\text{ m/s}$). Le collecteur est parfaitement dimensionné.
            </li>
        </ol>

        <h5>Corrigé de l'Exercice 2 :</h5>
        <ol>
            <li><strong>Section de l'orifice :</strong><br>
            Vitesse d'éjection théorique : $\\sqrt{2gh} = \\sqrt{2 \\times 9{,}81 \\times 1{,}50} = \\sqrt{29{,}43} \\approx 5{,}425\\text{ m/s}$.
            $$Q = \\mu \\cdot S_0 \\cdot \\sqrt{2gh} \\implies S_0 = \\frac{Q}{\\mu \\sqrt{2gh}} = \\frac{0{,}036}{0{,}60 \\times 5{,}425} = \\frac{0{,}036}{3{,}255} \\approx 0{,}01106\\text{ m}^2$$
            </li>
            <li><strong>Diamètre de l'orifice :</strong><br>
            $$d = \\sqrt{\\frac{4 S_0}{\\pi}} = \\sqrt{\\frac{4 \\times 0{,}01106}{\\pi}} = \\sqrt{0{,}01408} \\approx 0{,}1187\\text{ m} \\approx 119\\text{ mm}$$
            On choisit un orifice calibré de diamètre <strong>$d = 120\\text{ mm}$</strong>.
            </li>
        </ol>
        """
    },
    8: {
        "titre": "Dimensionnement du stockage & Bassins de rétention",
        "description": "Méthode des pluies, recherche de la durée critique t*, dimensionnement analytique du volume de stockage Vs et prise en compte de la revanche.",
        "cm": """
        <h4>1. Principe de la méthode des pluies</h4>
        <p>Le bassin de rétention compense l'écart entre le volume ruisselé généré par une pluie de projet et le volume évacué par le régulateur ou l'orifice de fuite vers l'exutoire à débit bridé $q_s$.</p>
        <p>Pour chaque durée d'averse candidate $t$, la hauteur nette à stocker par unité de surface active $S_a$ vaut :</p>
        <div class="alert alert-primary text-center">
            $$H_s(t) = H_{\\text{pluie}}(t) - H_{\\text{évac}}(t) \\quad (\\text{en mm})$$
            $$H_{\\text{pluie}}(t) = \\frac{a \\cdot t^{1-b}}{60} \\qquad H_{\\text{évac}}(t) = \\frac{q_s \\cdot t \\cdot 60}{S_a} \\cdot 1\\,000 = \\alpha_e \\cdot t$$
            <small>$t$ en minutes, $q_s$ en $\\text{m}^3/\\text{s}$, $S_a$ en $\\text{m}^2$.</small>
        </div>

        <h4>2. Durée critique $t^*$ et volume maximal</h4>
        <p>Le maximum de stockage s'obtient à l'annulation de la dérivée : $\\frac{dH_s(t)}{dt} = 0$, ce qui correspond à l'instant où <em>l'intensité de pluie devient égale au débit de fuite ramené à la surface active</em> :</p>
        <div class="alert alert-secondary text-center">
            $$t^* = \\left[ \\frac{60 \\cdot \\alpha_e}{a \\cdot (1 - b)} \\right]^{-1/b}$$
            $$V_{\\text{rétention}} = \\max_t [H_s(t)] \\times \\frac{S_a}{1\\,000} \\quad (V\\text{ en m}^3, H_s\\text{ en mm}, S_a\\text{ en m}^2)$$
        </div>
        <p><em>Règles de bonne pratique :</em> Ajouter une revanche de sécurité de 20 à 50 cm, un déversoir de surverse d'urgence (dimensionné pour $T = 100$ ans) et une pente de fond $\\ge 0{,}5\\,\\%$ vers la fosse d'aspiration/vidange.</p>
        """,
        "td": """
        <h5>Exercice : Dimensionnement complet d'un bassin de rétention</h5>
        <p>Un lotissement périurbain de $12\\text{ ha}$ est aménagé avec un coefficient de ruissellement post-développement $C = 0{,}80$. Le règlement du PLU impose un débit de fuite spécifique strict de $q_{\\text{spéc}} = 3\\text{ L/s/ha}$ pour une période de retour de dimensionnement $T = 10$ ans. On adopte la formule de Montana décennale : $a = 300$, $b = 0{,}70$.</p>
        <ol>
            <li>Calculer la surface active $S_a$ en $\\text{ha}$ et $\\text{m}^2$, puis le débit de fuite total autorisé $q_s$ en $\\text{L/s}$ et $\\text{m}^3/\\text{s}$.</li>
            <li>Exprimer les fonctions $H(t)$ et $H_{\\text{évac}}(t)$ en millimètres en fonction de la durée $t$ en minutes.</li>
            <li>Établir l'expression de la hauteur à stocker $H_s(t)$. Déterminer analytiquement la durée critique d'averse $t^*$ (en minutes et en heures).</li>
            <li>Calculer la hauteur maximale à retenir $H_s(t^*)$ et en déduire le volume de stockage utile $V$. Appliquer une marge de sécurité de 10 %.</li>
        </ol>
        """,
        "corrige": """
        <h5>Corrigé de l'Exercice :</h5>
        <ol>
            <li><strong>Surface active et débit de fuite :</strong><br>
            $$S_a = C \\cdot A = 0{,}80 \\times 12\\text{ ha} = 9{,}6\\text{ ha} = 96\\,000\\text{ m}^2$$
            $$q_s = q_{\\text{spéc}} \\times A = 3\\text{ L/s/ha} \\times 12\\text{ ha} = 36\\text{ L/s} = 0{,}036\\text{ m}^3/\\text{s}$$
            </li>
            <li><strong>Formulations analytiques :</strong><br>
            Pluie cumulée :
            $$H(t) = \\frac{a \\cdot t^{1-b}}{60} = \\frac{300 \\cdot t^{0{,}30}}{60} = 5 \\cdot t^{0{,}30} \\quad (\\text{mm})$$
            Débit de fuite en $\\text{m}^3/\\text{min}$ : $q_s = 0{,}036 \\times 60 = 2{,}16\\text{ m}^3/\\text{min}$.
            Hauteur équivalente évacuée :
            $$H_{\\text{évac}}(t) = \\frac{2{,}16 \\times t}{96\\,000} \\times 1\\,000 = 0{,}0225 \\cdot t \\quad (\\text{mm})$$
            </li>
            <li><strong>Durée critique $t^*$ :</strong><br>
            $$H_s(t) = 5 \\cdot t^{0{,}30} - 0{,}0225 \\cdot t$$
            $$\\frac{dH_s}{dt} = 5 \\times 0{,}30 \\cdot t^{-0{,}70} - 0{,}0225 = 1{,}5 \\cdot t^{-0{,}70} - 0{,}0225 = 0$$
            $$t^{-0{,}70} = \\frac{0{,}0225}{1{,}5} = 0{,}015 \\implies t^{0{,}70} = \\frac{1}{0{,}015} \\approx 66{,}67$$
            $$t^* = 66{,}67^{1/0{,}70} = 66{,}67^{1{,}4286} \\approx 403\\text{ min} \\approx 6{,}72\\text{ heures}$$
            </li>
            <li><strong>Volume de stockage :</strong><br>
            $$403^{0{,}30} = \\exp(0{,}30 \\times \\ln(403)) = \\exp(0{,}30 \\times 5{,}9989) \\approx 6{,}048$$
            $$H_s(t^*) = 5 \\times 6{,}048 - 0{,}0225 \\times 403 = 30{,}24 - 9{,}07 = 21{,}17\\text{ mm}$$
            $$V = 21{,}17\\text{ mm} \\times \\frac{96\\,000\\text{ m}^2}{1\\,000} \\approx 2\\,032\\text{ m}^3 \\approx 2\\,030\\text{ m}^3$$
            Avec une marge de sécurité classique de $+10\\,\\%$ pour prendre en compte le volume mort et les dépôts :
            $$V_{\\text{retenu}} = 2\\,030 \\times 1{,}10 \\approx 2\\,230\\text{ m}^3$$
            </li>
        </ol>
        """
    },
    9: {
        "titre": "Gestion intégrée des eaux pluviales & Solutions fondées sur la Nature",
        "description": "Techniques alternatives (noues, tranchées, toitures végétalisées, chaussées réservoirs), infiltration selon Darcy et cadre réglementaire (rubrique IOTA 2.1.5.0).",
        "cm": """
        <h4>1. De l'assainissement tout-tuyau à la gestion à la source</h4>
        <p>L'assainissement traditionnel accélère l'évacuation vers l'aval, augmentant les débits de pointe et le risque d'inondation. La gestion intégrée moderne prône :</p>
        <ol>
            <li><strong>Infiltrer</strong> au plus près du point d'impact de la goutte pour recharger les nappes.</li>
            <li><strong>Stocker et retarder</strong> par des aménagements paysagers aériens multifonctionnels.</li>
            <li><strong>Dépolluer</strong> par filtration naturelle végétale (décantation, phytoremédiation).</li>
        </ol>

        <h4>2. Solutions Fondées sur la Nature (SfN)</h4>
        <ul>
            <li><strong>Toitures végétalisées :</strong> abattement d'évapotranspiration (jusqu'à 50 à 70 % du volume annuel).</li>
            <li><strong>Noues et fossés enherbés :</strong> stockage temporaire, décantation des matières en suspension (MES) et infiltration lente.</li>
            <li><strong>Chaussées à structure réservoir :</strong> granulats poreux sous voirie absorbant l'eau avant infiltration ou rejet régulé.</li>
        </ul>

        <h4>3. Infiltration et dimensionnement (Loi de Darcy)</h4>
        <div class="alert alert-secondary text-center">
            $$Q_{\\text{inf}} = K_s \\cdot S_{\\text{inf}} \\cdot i_h \\approx K_s \\cdot S_{\\text{inf}}$$
            <small>$K_s$ : Perméabilité à saturation mesurée in situ ($\text{m/s}$), $S_{\\text{inf}}$ : Surface d'infiltration, $i_h \\approx 1$ : gradient hydraulique.</small>
        </div>
        <p><em>Règle d'or :</em> Une structure d'infiltration doit se vidanger entièrement en moins de <strong>24 à 48 heures</strong> pour être opérationnelle lors d'un second épisode orageux rapproché.</p>

        <h4>4. Cadre réglementaire français (Loi sur l'eau)</h4>
        <p><strong>Rubrique 2.1.5.0 de la nomenclature IOTA :</strong></p>
        <ul>
            <li>Surface interceptée $< 1\\text{ ha}$ : Non soumis.</li>
            <li>De $1\\text{ ha}$ à $20\\text{ ha}$ : Régime de <strong>Déclaration</strong> avec dossier d'incidence.</li>
            <li>$\\ge 20\\text{ ha}$ : Régime d'<strong>Autorisation</strong> environnementale.</li>
        </ul>
        """,
        "td": """
        <h5>Exercice 1 : Faisabilité d'une tranchée d'infiltration</h5>
        <p>On conçoit une tranchée d'infiltration pour recueillir le volume d'eau d'une pluie décennale de $V = 120\\text{ m}^3$. La surface de fond disponible au sol est $S_{\\text{inf}} = 150\\text{ m}^2$. Les essais de sol Porchet ont déterminé une perméabilité $K_s = 5 \\times 10^{-5}\\text{ m/s}$. On adopte un coefficient de sécurité de colmatage de 2 (soit $K_{\\text{utile}} = K_s / 2$).</p>
        <ol>
            <li>Calculer le débit d'infiltration permanent à travers le fond $Q_{\\text{inf}}$ en $\\text{m}^3/\\text{s}$ et en $\\text{L/s}$.</li>
            <li>Calculer le temps théorique de vidange complète $t_{\\text{vidange}}$ en heures. L'ouvrage respecte-t-il la règle des 48 heures ?</li>
        </ol>

        <h5>Exercice 2 : Analyse multicritères de terrain</h5>
        <p>Un aménageur souhaite infiltrer les eaux d'un parking de centre commercial. L'étude de sol montre un sol argilo-limoneux peu perméable ($K_s = 10^{-7}\\text{ m/s}$) et un toit de nappe phréatique affleurant à $0{,}80\\text{ m}$ sous le terrain naturel. Que préconisez-vous ?</p>
        """,
        "corrige": """
        <h5>Corrigé de l'Exercice 1 :</h5>
        <ol>
            <li><strong>Débit d'infiltration :</strong><br>
            $$K_{\\text{utile}} = \\frac{5 \\times 10^{-5}}{2} = 2{,}5 \\times 10^{-5}\\text{ m/s}$$
            $$Q_{\\text{inf}} = K_{\\text{utile}} \\times S_{\\text{inf}} = 2{,}5 \\times 10^{-5} \\times 150 = 3{,}75 \\times 10^{-3}\\text{ m}^3/\\text{s} = 3{,}75\\text{ L/s}$$
            </li>
            <li><strong>Temps de vidange :</strong><br>
            $$t_{\\text{vidange}} = \\frac{V}{Q_{\\text{inf}}} = \\frac{120}{3{,}75 \\times 10^{-3}} = 32\\,000\\text{ secondes}$$
            $$t_{\\text{vidange}} = \\frac{32\\,000}{3\\,600} \\approx 8{,}89\\text{ heures}$$
            Puisque $8{,}9\\text{ h} \\ll 48\\text{ heures}$, le critère de vidange rapide est parfaitement validé.
            </li>
        </ol>

        <h5>Corrigé de l'Exercice 2 :</h5>
        <p>L'infiltration directe dans le sous-sol est <strong>strictement à proscrire</strong> pour deux raisons techniques majeures :</p>
        <ul>
            <li>La perméabilité est bien trop faible ($K_s = 10^{-7}\\text{ m/s} < 10^{-5}\\text{ m/s}$), ce qui entraînerait une stagnation prolongée des eaux et un risque d'asphyxie des ouvrages.</li>
            <li>La nappe superficielle ($< 1\\text{ m}$) serait immédiatement polluée par les hydrocarbures et métaux lourds issus du parking, et la sous-pression empêcherait toute infiltration.</li>
        </ul>
        <p><strong>Solution préconisée :</strong> Traitement des eaux par débourbeur-déshuileur, stockage étanche sous forme de noue plantée avec géomembrane ou chaussée réservoir étanchée, et régulation des rejets vers le réseau d'eaux pluviales au débit autorisé par le règlement local.</p>
        """
    },
    10: {
        "titre": "Risques d'inondation, crues extrêmes & Protection des biens",
        "description": "Le triptyque Aléa / Enjeu / Vulnérabilité, typologie des inondations, cartographie PPRI, aménagements structurels (digues, ZEC) et impacts du changement climatique.",
        "cm": """
        <h4>1. Le triptyque du Risque d'inondation</h4>
        <div class="alert alert-primary text-center fs-5">
            $$\\text{Risque} = \\text{Aléa} \\times \\text{Enjeux} \\times \\text{Vulnérabilité}$$
        </div>
        <ul>
            <li><strong>Aléa :</strong> Probabilité d'occurrence d'un phénomène hydraulique d'intensité donnée (hauteur d'eau submersion, vitesse de courant, durée de crue). Caractérisé par la crue centennale ($Q_{100}$).</li>
            <li><strong>Enjeux :</strong> Personnes, habitations, activités économiques et infrastructures publiques situées en zone inondable.</li>
            <li><strong>Vulnérabilité :</strong> Fragilité intrinsèque ou prédisposition des enjeux à subir des dommages réversibles ou irréversibles.</li>
        </ul>

        <h4>2. Typologie des inondations</h4>
        <ul>
            <li><strong>Crue lente de plaine :</strong> montée progressive (jours/semaines) par débordement du lit mineur (Seine, Somme).</li>
            <li><strong>Crues rapides et torrentielles :</strong> orages intenses sur petits bassins versants pentus (réponse en quelques heures, transport sédimentaire violent).</li>
            <li><strong>Ruissellement pluvial urbain :</strong> saturation des réseaux due à l'imperméabilité des sols sous averses orageuses.</li>
            <li><strong>Remontée de nappe phréatique :</strong> émergence prolongée des eaux souterraines inondant les sous-sols et rez-de-chaussée.</li>
        </ul>

        <h4>3. Aménagements de protection : Réduire l'aléa ou la vulnérabilité</h4>
        <ul>
            <li><strong>Zones d'Expansion de Crue (ZEC) :</strong> zones naturelles ou agricoles inondées volontairement en amont pour abaisser la ligne d'eau à l'aval.</li>
            <li><strong>Digues et levées :</strong> protègent localement, mais créent un <em>risque résiduel majeur</em> (surverse, rupture brutale) et reportent la crue vers l'aval.</li>
            <li><strong>Mesures non structurelles :</strong> PPRI (interdiction de construire en zone rouge), batardeaux, zones refuges au-dessus des plus hautes eaux connues (PHEC).</li>
        </ul>
        <p><strong>Impact climatique (Loi de Clausius-Clapeyron) :</strong> L'augmentation de la température atmosphérique accroît la teneur maximale en vapeur d'eau d'environ <strong>$7\\,\\%$ par degré Celsius de réchauffement</strong>, intensifiant la violence des pluies orageuses extrêmes.</p>
        """,
        "td": """
        <h5>Exercice 1 : Distinction conceptuelle du risque</h5>
        <p>Un camping et une zone industrielle sont situés sur une plaine alluviale inondable par la crue centennale du cours d'eau local.</p>
        <ol>
            <li>Identifier clairement l'aléa, les enjeux et la vulnérabilité dans cette situation.</li>
            <li>Proposer deux mesures de prévention pour réduire la vulnérabilité sans modifier l'aléa hydraulique.</li>
        </ol>

        <h5>Exercice 2 : Effets pervers du recalibrage d'une rivière</h5>
        <p>Pour éviter les inondations dans un village amont, une collectivité a élargi, approfondi et bétonné le lit de la rivière sur 2 km.</p>
        <ol>
            <li>Quels sont les trois effets pervers majeurs subis par les communes riveraines situées en aval ?</li>
        </ol>
        """,
        "corrige": """
        <h5>Corrigé de l'Exercice 1 :</h5>
        <ol>
            <li><strong>Identification :</strong><br>
            <ul>
                <li><strong>Aléa :</strong> Submersion par une lame d'eau de hauteur $h$ et de vitesse $V$ générée par la crue centennale ($T = 100$ ans).</li>
                <li><strong>Enjeux :</strong> Les vacanciers du camping, les ouvriers, les machines de production, les bâtiments industriels et les réseaux routiers.</li>
                <li><strong>Vulnérabilité :</strong> Les toiles de tente et mobile-homes sont extrêmement vulnérables (emportement immédiat) ; les armoires électriques d'usines au niveau du sol subissent des dommages irréversibles.</li>
            </ul>
            </li>
            <li><strong>Réduction de la vulnérabilité :</strong><br>
            Fermeture et évacuation préventive du camping lors du déclenchement de la vigilance crue ; surélévation des postes électriques au-dessus de la cote centennale ; pose de batardeaux amovibles à l'entrée des ateliers.
            </li>
        </ol>

        <h5>Corrigé de l'Exercice 2 :</h5>
        <p>Les trois impacts négatifs en aval sont :</p>
        <ol>
            <li><strong>Aggravation du débit de pointe en aval :</strong> La suppression du lit majeur naturel en amont élimine la zone tampon d'écrêtement naturel.</li>
            <li><strong>Accélération brutale de l'onde de crue :</strong> L'augmentation de la pente et le lissage hydraulique raccourcissent le temps de transfert, générant une pointe de crue plus abrupte et difficile à anticiper.</li>
            <li><strong>Érosion régressive et dégradation biologique :</strong> L'augmentation des vitesses arrache le fond et les berges à l'aval immédiat tout en détruisant les habitats piscicoles.</li>
        </ol>
        """
    },
    11: {
        "titre": "Modélisation hydrologique, hydraulique 1D/2D & Muskingum",
        "description": "Typologie des modèles (conceptuels GR, physiques distribués), équations de Saint-Venant 1D/2D, propagation de crue par Muskingum et script Python de réservoir linéaire.",
        "cm": """
        <h4>1. Typologie des modèles hydrologiques</h4>
        <ul>
            <li><strong>Modèles globaux conceptuels :</strong> représentent le bassin sous forme de réservoirs interconnectés (GR4J, HBV). Très performants pour la prévision de débit continu avec peu de paramètres.</li>
            <li><strong>Modèles physiques distribués :</strong> maillent le territoire et résolvent les équations locales de conservation de masse et d'énergie (MIKE SHE, SWMM, ParFlow).</li>
        </ul>

        <h4>2. Hydraulique numérique : Équations de Saint-Venant 1D</h4>
        <p>Régissent les écoulements instationnaires à surface libre dans les rivières et canaux :</p>
        <div class="alert alert-primary">
            $$\\text{Masse : } \\quad \\frac{\\partial A}{\\partial t} + \\frac{\\partial Q}{\\partial x} = q_L$$
            $$\\text{Quantité de mouvement : } \\quad \\frac{\\partial Q}{\\partial t} + \\frac{\\partial}{\\partial x}\\left(\\frac{Q^2}{A}\\right) + gA \\frac{\\partial h}{\\partial x} = gA (S_0 - S_f)$$
            <small>$q_L$ : débit d'apport latéral, $S_0$ : pente du fond, $S_f$ : pente de frottement (Manning-Strickler $S_f = \\frac{Q^2}{K^2 A^2 R_h^{4/3}}$).</small>
        </div>

        <h4>3. Propagation de crue : Méthode de Muskingum</h4>
        <p>Pour propager un hydrogramme dans un tronçon fluvial de stockage $S$ avec un temps de transfert $K$ et un facteur de pondération $X$ ($0 \\le X \\le 0{,}5$) :</p>
        <div class="alert alert-secondary text-center">
            $$S = K \\cdot [X \\cdot I + (1 - X) \\cdot Q]$$
            $$Q_{j+1} = C_0 \\cdot I_{j+1} + C_1 \\cdot I_j + C_2 \\cdot Q_j \\quad \\text{avec } C_0 + C_1 + C_2 = 1$$
        </div>
        """,
        "td": """
        <h5>Exercice : Propagation d'hydrogramme avec Muskingum</h5>
        <p>Un tronçon de rivière possède les paramètres Muskingum suivants : $K = 12\\text{ h}$, $X = 0{,}20$. On adopte un pas de temps de calcul $\\Delta t = 6\\text{ h}$.</p>
        <ol>
            <li>Calculer les trois coefficients de routage $C_0$, $C_1$, et $C_2$. Vérifier que leur somme est égale à 1.</li>
            <li>À l'instant $t = 0\\text{ h}$, le débit amont est $I_0 = 50\\text{ m}^3/\\text{s}$ et le débit aval est stabilisé à $Q_0 = 50\\text{ m}^3/\\text{s}$. À $t = 6\\text{ h}$, l'onde amont atteint $I_1 = 140\\text{ m}^3/\\text{s}$. Calculer le débit de sortie $Q_1$ à $t = 6\\text{ h}$.</li>
        </ol>
        """,
        "corrige": """
        <h5>Corrigé de l'Exercice :</h5>
        <ol>
            <li><strong>Coefficients Muskingum :</strong><br>
            Les relations théoriques sont :
            $$D = 2K(1 - X) + \\Delta t = 2 \\times 12 \\times (1 - 0{,}20) + 6 = 24 \\times 0{,}80 + 6 = 19{,}2 + 6 = 25{,}2\\text{ h}$$
            $$C_0 = \\frac{\\Delta t - 2KX}{D} = \\frac{6 - 2 \\times 12 \\times 0{,}20}{25{,}2} = \\frac{6 - 4{,}8}{25{,}2} = \\frac{1{,}2}{25{,}2} \\approx 0{,}0476$$
            $$C_1 = \\frac{\\Delta t + 2KX}{D} = \\frac{6 + 4{,}8}{25{,}2} = \\frac{10{,}8}{25{,}2} \\approx 0{,}4286$$
            $$C_2 = \\frac{2K(1 - X) - \\Delta t}{D} = \\frac{19{,}2 - 6}{25{,}2} = \\frac{13{,}2}{25{,}2} \\approx 0{,}5238$$
            <strong>Vérification :</strong> $C_0 + C_1 + C_2 = 0{,}0476 + 0{,}4286 + 0{,}5238 = 1{,}000$.
            </li>
            <li><strong>Débit de sortie à $t = 6\\text{ h}$ :</strong><br>
            $$Q_1 = C_0 \\cdot I_1 + C_1 \\cdot I_0 + C_2 \\cdot Q_0$$
            $$Q_1 = 0{,}0476 \\times 140 + 0{,}4286 \\times 50 + 0{,}5238 \\times 50$$
            $$Q_1 = 6{,}664 + 21{,}43 + 26{,}19 = 54{,}28\\text{ m}^3/\\text{s} \\approx 54{,}3\\text{ m}^3/\\text{s}$$
            L'effet de stockage dans le tronçon amortit considérablement le pic initial qui passe de $140\\text{ m}^3/\\text{s}$ à l'entrée à seulement $54{,}3\\text{ m}^3/\\text{s}$ à la sortie au pas $6\\text{ h}$.
            </li>
        </ol>
        """
    },
    12: {
        "titre": "Calage, validation, critère de Nash-Sutcliffe & Incertitudes",
        "description": "Protocole d'étalonnage, critère de performance NSE, équifinalité, biais sur le volume et détection des sur-paramétrages.",
        "cm": """
        <h4>1. Protocole de calage / validation</h4>
        <p>Un modèle hydrologique ou hydraulique ne peut être utilisé pour la décision sans une phase de validation stricte :</p>
        <ol>
            <li><strong>Calage (optimisation) :</strong> Ajustement des paramètres libres (rugosités, perméabilités, capacités de réservoirs) pour minimiser l'écart aux chroniques observées.</li>
            <li><strong>Validation croisée (split-sample test) :</strong> Évaluation de la performance sur une période temporelle ou des averses totalement indépendantes de celles du calage.</li>
        </ol>

        <h4>2. Critère de Nash-Sutcliffe (NSE)</h4>
        <p>Le critère adimensionnel NSE compare la variance résiduelle du modèle à la variance des observations :</p>
        <div class="alert alert-primary text-center">
            $$NSE = 1 - \\frac{\\sum_{i=1}^N (Q_{\\text{obs},i} - Q_{\\text{sim},i})^2}{\\sum_{i=1}^N (Q_{\\text{obs},i} - \\overline{Q_{\\text{obs}}})^2}$$
        </div>
        <ul>
            <li>$NSE = 1{,}0$ : Modélisation parfaite.</li>
            <li>$NSE > 0{,}75$ : Modèle d'excellente qualité prédictive.</li>
            <li>$0{,}50 < NSE \\le 0{,}75$ : Performance satisfaisante.</li>
            <li>$NSE \\le 0$ : Le modèle simule moins bien que la simple moyenne constante des débits observés.</li>
        </ul>

        <h4>3. Notion d'équifinalité (Beven)</h4>
        <p>Dans les modèles environnementaux complexes, plusieurs jeux de paramètres totalement distincts peuvent aboutir à des résultats de performance statistique identiques. Ne jamais sur-paramétrer un modèle sans mesures physiques directes.</p>
        """,
        "td": """
        <h5>Exercice : Calcul complet du critère de Nash-Sutcliffe</h5>
        <p>Au cours d'un épisode de crue, on a relevé 5 débits observés à l'exutoire : $[10, 25, 40, 30, 15]\\text{ m}^3/\\text{s}$.<br>
        Le modèle hydrologique simulé fournit sur les mêmes pas de temps : $[12, 22, 38, 33, 14]\\text{ m}^3/\\text{s}$.</p>
        <ol>
            <li>Calculer la moyenne arithmétique des débits observés $\\overline{Q_{\\text{obs}}}$.</li>
            <li>Calculer la somme des carrés des écarts du modèle $\\sum (Q_{\\text{obs}} - Q_{\\text{sim}})^2$.</li>
            <li>Calculer la variance totale des observations $\\sum (Q_{\\text{obs}} - \\overline{Q_{\\text{obs}}})^2$.</li>
            <li>En déduire le critère $NSE$. Conclure sur la qualité du calage.</li>
            <li>Pourquoi un bon score $NSE$ sur seulement 5 pas de temps est-il insuffisant pour certifier le modèle ?</li>
        </ol>
        """,
        "corrige": """
        <h5>Corrigé de l'Exercice :</h5>
        <ol>
            <li><strong>Moyenne observée :</strong><br>
            $$\\overline{Q_{\\text{obs}}} = \\frac{10 + 25 + 40 + 30 + 15}{5} = \\frac{120}{5} = 24{,}0\\text{ m}^3/\\text{s}$$
            </li>
            <li><strong>Somme des carrés des résidus (numérateur) :</strong><br>
            Écarts $(Q_{\\text{obs}} - Q_{\\text{sim}})$ :
            <ul>
                <li>Pas 1 : $10 - 12 = -2 \\implies (-2)^2 = 4$</li>
                <li>Pas 2 : $25 - 22 = +3 \\implies (+3)^2 = 9$</li>
                <li>Pas 3 : $40 - 38 = +2 \\implies (+2)^2 = 4$</li>
                <li>Pas 4 : $30 - 33 = -3 \\implies (-3)^2 = 9$</li>
                <li>Pas 5 : $15 - 14 = +1 \\implies (+1)^2 = 1$</li>
            </ul>
            $$\\sum_{i=1}^5 (Q_{\\text{obs},i} - Q_{\\text{sim},i})^2 = 4 + 9 + 4 + 9 + 1 = 27$$
            </li>
            <li><strong>Dispersion des observations (dénominateur) :</strong><br>
            Écarts $(Q_{\\text{obs}} - \\overline{Q_{\\text{obs}}})$ :
            <ul>
                <li>Pas 1 : $10 - 24 = -14 \\implies (-14)^2 = 196$</li>
                <li>Pas 2 : $25 - 24 = +1 \\implies (+1)^2 = 1$</li>
                <li>Pas 3 : $40 - 24 = +16 \\implies (+16)^2 = 256$</li>
                <li>Pas 4 : $30 - 24 = +6 \\implies (+6)^2 = 36$</li>
                <li>Pas 5 : $15 - 24 = -9 \\implies (-9)^2 = 81$</li>
            </ul>
            $$\\sum_{i=1}^5 (Q_{\\text{obs},i} - \\overline{Q_{\\text{obs}}})^2 = 196 + 1 + 256 + 36 + 81 = 570$$
            </li>
            <li><strong>Valeur du critère $NSE$ :</strong><br>
            $$NSE = 1 - \\frac{27}{570} = 1 - 0{,}04737 \\approx 0{,}953 \\approx 0{,}95$$
            Le score $NSE = 0{,}95$ est très proche de 1, indiquant une reproduction quasi-parfaite de la forme de l'hydrogramme sur cet événement précis.
            </li>
            <li><strong>Mise en garde méthodologique :</strong><br>
            Un échantillon de 5 valeurs est statistiquement trop faible pour valider un modèle. Le modèle pourrait être calé sur des erreurs qui se compensent mutuellement (sur-apprentissage). Une validation crédible exige une chronique de longue durée (plusieurs dizaines d'épisodes de crue), un test sur des conditions extrêmes hors calage, et une vérification conjointe du bilan en volume et de l'erreur sur le débit de pointe.
            </li>
        </ol>
        """
    }
}