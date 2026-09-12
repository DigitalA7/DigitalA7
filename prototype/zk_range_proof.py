def valid_range(claim, low, high):
    return isinstance(claim,dict) and claim.get("statement")=="range" and low<=claim.get("value",low-1)<=high and bool(claim.get("proof"))

if __name__=="__main__":
    assert valid_range({"statement":"range","value":4,"proof":"p"},0,10) and not valid_range({"statement":"range","value":11,"proof":"p"},0,10)
