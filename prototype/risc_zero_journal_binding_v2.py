def bound(receipt, image_id, journal):
    return receipt.get("image_id")==image_id and receipt.get("journal")==journal and bool(receipt.get("seal"))
