# Digital A7

## Recherche, prototypage et documentation blockchain

Digital A7 étudie les protocoles open source en partant du code : architectures de preuve, invariants, frontières de confiance et intégrations EVM. Les parcours techniques sont publiés en français et distinguent explicitement analyse documentaire, tests et audit.

### Axes de recherche

- ZK-rollups, zkVM, STARK, SNARK et langages de circuits
- FHE et calcul confidentiel
- Base L2, comptes intelligents, paiements et agents
- Hyperliquid, HyperEVM et systèmes de données
- Smart contracts, interopérabilité et protocoles DeFi

### ZK et preuves

- [StarkWare Proving](https://github.com/DigitalA7/proving) — pipeline Cairo, AIR, Circle STARK, FRI, sérialisation et récursion.
- [Plonky3](https://github.com/DigitalA7/Plonky3) — AIR, traces, engagements, FRI et Fiat–Shamir.
- [Bellman](https://github.com/DigitalA7/bellman) — circuits R1CS, paramètres Groth16, témoins et vérification.
- [Noir](https://github.com/DigitalA7/noir) — HIR/SSA, ACIR, ACVM, Brillig et backends de preuve.
- [Arkworks R1CS Tutorial](https://github.com/DigitalA7/r1cs-tutorial) — signatures, arbres de Merkle et transition d’état d’un mini-rollup.

### FHE, Base et HyperEVM

- [HElib](https://github.com/DigitalA7/HElib) — BGV, CKKS, packing SIMD, bruit et bootstrapping.
- [Base Skills](https://github.com/DigitalA7/skills) — réseau, comptes, paiements, paymasters, ERC-8021 et agents.
- [Hyperliquid Stats](https://github.com/DigitalA7/hyperliquid-stats) — ingestion, idempotence, métriques, fraîcheur et frontière HyperCore/HyperEVM.

### Autres travaux

[L2 Basic](https://github.com/DigitalA7/L2-Basic), [OpenZeppelin Contracts](https://github.com/DigitalA7/openzeppelin-contracts), [Study Bridge](https://github.com/DigitalA7/study-bridge), [x402](https://github.com/DigitalA7/x402) et [Uniswap v4 by Example](https://github.com/DigitalA7/v4-by-example).

### Méthode et collaboration

Chaque parcours relie un mécanisme aux composants du dépôt dans `docs/fr/`, avec un commit par chapitre. Digital A7 est ouvert aux analyses reproductibles, à la documentation de sécurité et aux améliorations ciblées dans les écosystèmes ZK, FHE, Base et HyperEVM.
