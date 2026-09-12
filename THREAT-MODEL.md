# Modèle de menaces Digital A7

- Base : séquenceur indisponible, données L1 indisponibles, dérivation incohérente, clés admin compromises.
- EVM/HyperEVM : mauvais chain ID, rejeu, nonce réutilisé, domaine de signature absent.
- ZK/RISC Zero : mauvais programme, statement ou journal, receipt liée au mauvais contexte.
- FHE : finalité non autorisée, clé révoquée, fuite de métadonnées.

```mermaid
graph TD
 A[Entrée] --> B{Contexte}
 B --> C[Base/EVM: chaîne + nonce]
 B --> D[ZK/RISC Zero: programme + journal]
 B --> E[FHE: sujet + finalité + clé]
 C --> F[Décision]
 D --> F
 E --> F
```
