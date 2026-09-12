# Matrice des garanties

| Domaine | Invariant | Hypothèse | Rejet |
|---|---|---|---|
| Base | lot sur la bonne chaîne | données disponibles | chain ID ou engagement absent |
| EVM | appel dans son domaine | nonce et contrat fiables | cible ou chaîne incorrecte |
| HyperEVM | intention non expirée | horloge et réseau fiables | deadline dépassée |
| ZK | sortie liée au programme | verifier correct | preuve ou programme incorrect |
| FHE | accès finalisé | politique et clé valides | finalité non accordée |
| RISC Zero | receipt liée à l image | image et journal attendus | seal ou journal incohérent |
