def eligible(request, now, delay):
    return isinstance(request,dict) and request.get("status")=="finalized" and request.get("amount",0)>0 and now>=request.get("created_at",now)+delay

if __name__=="__main__":
    r={"status":"finalized","amount":1,"created_at":10}
    assert eligible(r,20,5) and not eligible(r,12,5)
