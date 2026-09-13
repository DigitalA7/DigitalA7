"""Prototype documentaire de validation d'un scalaire de frais Base."""

from dataclasses import dataclass


@dataclass(frozen=True)
class FeeScalar:
    value: int
    bits: int = 256


def decode_fee_scalar(raw: bytes, *, bits: int = 256) -> FeeScalar:
    if bits <= 0 or bits % 8:
        raise ValueError("largeur invalide")
    if len(raw) != bits // 8:
        raise ValueError("taille inattendue")
    value = int.from_bytes(raw, "big")
    if value == 0:
        raise ValueError("scalaire nul")
    return FeeScalar(value, bits)


if __name__ == "__main__":
    print(decode_fee_scalar((1).to_bytes(32, "big")))
