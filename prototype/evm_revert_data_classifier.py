"""Prototype documentaire de classification des retours d'erreur EVM."""

ERROR = bytes.fromhex("08c379a0")
PANIC = bytes.fromhex("4e487b71")


def classify_revert(data: bytes) -> str:
    if not data:
        return "empty"
    if data[:4] == ERROR:
        return "error(string)"
    if data[:4] == PANIC:
        return "panic(uint256)"
    if len(data) >= 4:
        return "custom-or-unknown"
    return "truncated-selector"


if __name__ == "__main__":
    print(classify_revert(PANIC + b"\x00" * 32))
