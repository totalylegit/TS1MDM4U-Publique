from math import comb

#paramètres
n = 11 # rangée numéro n
pascal = [[comb(r,c) for c in range(r+1)] for r in range(n+1)] #construire le triangle de Pascal
valeurs_bloqué = {20,35,56,126,252} #valeurs bloquées

#idnetifie les pegs qui sont bloquées par (rangée, colonne)
bloqué = {(r,c) for r in range(n+1) for c in range(r+1) if pascal[r][c] in valeurs_bloqué}

#compute le nombre de façons d'atteindre chaque peg
façons = [[0]*(r+1) for r in range(n+1)]
façons[0][0] = 1 #commence à la sommet
for r in range(n):
    for c in range(r+1):
        if façons[r][c] == 0 or (r,c) in bloqué: 
            continue
        #côté gauche
        if (r+1,c) not in bloqué:
            façons[r+1][c] += façons[r][c]
        #côté droit
        if (r+1,c+1) not in bloqué:
            façons[r+1][c+1] += façons[r][c]

#résultats à la fond du triangle
fond = façons[n]
chemin_total = sum(fond)

récompenses = [1000 / comb(n, k) for k in range(n+1)]
probs = [b / chemin_total for b in fond]
contribs = [p * r for p, r in zip(probs, récompenses)]
E = sum(contribs)

print("Chemins Totals::", chemin_total)
for k in range(n+1):
    print(k, comb(n,k), fond[k], probs[k], récompenses[k], contribs[k])
print("Paiement Expecté:", E)