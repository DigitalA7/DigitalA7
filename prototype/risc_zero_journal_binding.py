def bound(receipt, image_id, journal):
    return isinstance(receipt,dict) and receipt.get("image_id")==image_id and receipt.get("journal")==journal and bool(receipt.get("seal"))

if __name__=="__main__":
    r={"image_id":"i","journal":"j","seal":"s"}
    assert bound(r,"i","j") and not bound(r,"x","j")
