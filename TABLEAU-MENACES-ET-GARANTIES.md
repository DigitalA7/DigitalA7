# Tableau des menaces et garanties

| Actif ou propriété | Menace | Garantie recherchée | Limite à vérifier |
| --- | --- | --- | --- |
| Donnée privée | Lecture par un tiers | Chiffrement ou preuve sans divulgation | Métadonnées et résultat révélé |
| Calcul correct | Entrée ou contrainte incorrecte | Relation vérifiée | Propriété réellement exprimée |
| Clé d’autorisation | Vol ou délégation excessive | ACL, rotation, séparation des rôles | Gouvernance et récupération |
| Message inter-chaînes | Rejeu ou mauvaise destination | Nonce, attestation, validation | Finalité et reprise après erreur |
| Transaction utilisateur | Paramètre manipulé | Prévisualisation et approbation | Interface et agent hors chaîne |

## Lecture

Ce tableau sépare la promesse, le mécanisme et la limite. Il ne constitue pas un audit : chaque ligne doit être reliée au code et au modèle de menace du système étudié.
