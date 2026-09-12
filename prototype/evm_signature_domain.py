def matches(message, chain_id, contract):
    return isinstance(message,dict) and message.get("chain_id")==chain_id and message.get("contract")==contract and bool(message.get("nonce")) and bool(message.get("payload"))

if __name__=="__main__":
    m={"chain_id":8453,"contract":"app","nonce":1,"payload":"call"}
    assert matches(m,8453,"app") and not matches(m,1,"app")
