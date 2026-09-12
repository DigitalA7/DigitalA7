def shaped(claim):
    return isinstance(claim,dict) and bool(claim.get("root")) and bool(claim.get("leaf")) and isinstance(claim.get("path"),list) and claim.get("index",-1)>=0

if __name__=="__main__":
    assert shaped({"root":"r","leaf":"l","path":[],"index":0}) and not shaped({"root":"","leaf":"l","path":[],"index":0})
