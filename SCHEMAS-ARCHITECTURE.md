# Schémas d’architecture

## Pipeline ZK

```mermaid
flowchart LR
  I[Entrées publiques] --> C[Circuit ou programme]
  W[Witness privé] --> C
  C --> P[Prover]
  P --> Z[Preuve]
  Z --> V[Verifier]
  V --> A[Action acceptée]
```

## Frontière FHE

```mermaid
flowchart LR
  U[Utilisateur] --> E[Chiffrement]
  E --> S[Service de calcul]
  S --> R[Résultat chiffré]
  R --> D[Déchiffrement autorisé]
  S -. métadonnées .-> M[Observateur]
```

## Lecture

Ces schémas sont conceptuels. Ils rendent visibles les acteurs, les flux et les frontières ; ils ne remplacent pas la vérification des composants réels.
