def within_budget(receipt, limit):
    return isinstance(receipt,dict) and 0<=receipt.get("cycles",-1)<=limit and bool(receipt.get("seal"))

if __name__=="__main__":
    assert within_budget({"cycles":10,"seal":"s"},20)
    assert not within_budget({"cycles":21,"seal":"s"},20)
