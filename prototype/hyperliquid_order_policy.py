def accepted(order, now):
    return isinstance(order,dict) and order.get("side") in {"buy","sell"} and order.get("size",0)>0 and order.get("deadline",0)>=now and bool(order.get("client_id"))

if __name__=="__main__":
    o={"side":"buy","size":2,"deadline":10,"client_id":"c"}
    assert accepted(o,9) and not accepted(o,11)
