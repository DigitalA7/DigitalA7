# Modèle de menaces FHE

## Ce que le chiffrement protège

FHE protège la lisibilité de certaines données pendant le calcul, selon le schéma et les paramètres utilisés. Elle ne masque pas nécessairement tailles, timings, fréquence des requêtes ou résultats publiés.

## Clés et autorisations

La génération, la conservation, la rotation et la délégation des clés forment une frontière de confiance distincte. Une politique d’accès mal conçue peut annuler le bénéfice du chiffrement.

## Intégrité

La confidentialité ne prouve pas que les entrées sont correctes ni que le calcul correspond à l’intention métier. Il faut traiter séparément authentification, validation, replay et disponibilité.

## Analyse

Pour chaque scénario, identifier adversaire, actif, observation possible, opération protégée et condition de déchiffrement. Les garanties doivent rester limitées au modèle étudié.
