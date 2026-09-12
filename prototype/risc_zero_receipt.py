"""Cohérence pédagogique d une receipt RISC Zero."""

def valid(receipt, image_id, journal):
    required={"image_id","journal","seal"}
    return isinstance(receipt,dict) and required <= receipt.keys() and receipt["image_id"]==image_id and receipt["journal"]==journal and bool(receipt["seal"])

if __name__ == "__main__":
    r={"image_id":"img","journal":"j","seal":"opaque"}
    assert valid(r,"img","j")
    assert not valid(r,"other","j")
