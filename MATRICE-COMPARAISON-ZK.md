# Matrice de comparaison des systèmes ZK

## STARK

Les STARK s’appuient généralement sur une trace, une représentation AIR, des engagements et une vérification FRI. Ils évitent certaines configurations de confiance mais peuvent produire des preuves plus volumineuses.

## SNARK

Les SNARK privilégient souvent des preuves compactes et une vérification efficace. L’analyse doit préciser le système de contraintes, les clés, la SRS éventuelle et les hypothèses cryptographiques.

## zkVM

Une zkVM déplace une partie du travail vers la preuve de l’exécution d’un programme. Il faut vérifier le jeu d’instructions, les précompilés, les limites de mémoire et la correspondance avec le programme source.

## Critères

Comparer sécurité, taille de preuve, coût du prover, coût du vérificateur, récursion, transparence et ergonomie. Aucun axe unique ne suffit pour choisir une architecture.
