"""Prototype documentaire de résolution sûre des tags de bloc."""

FINAL_TAGS = {"safe", "finalized"}


def validate_block_reference(tag: str, explicit_height: int | None = None) -> None:
    if tag in {"latest", "pending"} and explicit_height is not None:
        raise ValueError("tag et hauteur explicite ne doivent pas être mélangés")
    if tag in FINAL_TAGS and explicit_height is not None:
        raise ValueError("tag final et hauteur explicite ambigus")
    if tag not in {"latest", "pending", "safe", "finalized", "number"}:
        raise ValueError("tag inconnu")
    if tag == "number" and (explicit_height is None or explicit_height < 0):
        raise ValueError("hauteur explicite invalide")


if __name__ == "__main__":
    validate_block_reference("number", 123)
    print("block reference accepted")
