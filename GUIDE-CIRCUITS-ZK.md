# Circuits et contraintes ZK

## Propriété cible

Commencer par la relation que le circuit doit prouver, puis distinguer entrées publiques, witness privé et sorties consommées par le vérificateur.

## Sous-contrainte

Toute valeur non reliée par une contrainte peut devenir une liberté inattendue. Les signaux inutilisés, conversions implicites et branches non couvertes méritent une lecture spécifique.

## Témoins et encodage

Documenter la construction du witness, les domaines numériques, les bornes et les sérialisations. Une incohérence entre prover et verifier peut invalider l’intégration sans invalider la primitive.

## Limites

La preuve garantit seulement la relation réellement exprimée par le circuit, avec les hypothèses du système de preuve.
