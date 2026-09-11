# Architecture d’un pipeline ZK

## De la propriété au circuit

Toute expérience commence par une propriété précise : ce qui est public, ce qui reste dans le witness et ce que le vérificateur doit accepter. Une formulation ambiguë produit une preuve difficile à interpréter.

## Du witness à la preuve

Le pipeline relie génération du witness, contraintes, arithmétisation, engagements, transcript et preuve finale. Chaque transformation doit préserver la relation cible et son domaine numérique.

## Vérification et intégration

La vérification peut être locale ou exécutée par un contrat. Il faut documenter l’encodage, les erreurs, les paramètres publics et l’action déclenchée après acceptation.

## Point de vigilance

Une preuve valide démontre uniquement la relation encodée. Elle ne garantit ni la qualité des entrées, ni l’interface, ni la gouvernance du système.
