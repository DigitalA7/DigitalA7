# Parcours ZK : étude de cas

## 1. Formuler la propriété

Commencer par une phrase vérifiable : quelle relation doit être prouvée, quelles données sont publiques et quelles données restent dans le witness ? Cette étape fixe le périmètre de toute la suite.

## 2. Construire le circuit

Relier la propriété aux signaux, contraintes, bornes et opérations arithmétiques. Rechercher les valeurs libres, les conversions implicites et les branches qui ne participent pas réellement à la preuve.

## 3. Produire et vérifier

Documenter génération du witness, création de la preuve, transcript, paramètres et vérification. En cas de vérification on-chain, préciser l’encodage et l’action déclenchée.

## 4. Évaluer

Comparer coût du prover, taille de preuve, coût du vérificateur et hypothèses de confiance. Une preuve valide ne garantit que la relation effectivement encodée.
