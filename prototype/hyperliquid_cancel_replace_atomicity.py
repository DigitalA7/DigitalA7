"""Prototype documentaire d'une séquence annulation/remplacement d'ordre."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    client_id: str
    status: str


def can_replace(current: Order, replacement: Order) -> bool:
    if current.status != "open":
        return False
    if not replacement.client_id or replacement.client_id == current.client_id:
        return False
    return replacement.status == "new"


def transition(current: Order, replacement: Order) -> tuple[str, str]:
    if not can_replace(current, replacement):
        raise ValueError("remplacement non atomique ou état interdit")
    return ("cancel_requested", "replacement_submitted")


if __name__ == "__main__":
    print(transition(Order("old", "open"), Order("new", "new")))
