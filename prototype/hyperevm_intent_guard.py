"""Garde-fou pour une intention HyperEVM."""

def accept(intent, network, now):
    required={"network","sender","nonce","asset","amount","deadline"}
    return isinstance(intent,dict) and required <= intent.keys() and intent["network"]==network and intent["amount"]>0 and intent["deadline"]>=now

if __name__ == "__main__":
    i={"network":"hyperevm","sender":"a","nonce":2,"asset":"USDC","amount":10,"deadline":100}
    assert accept(i,"hyperevm",99)
    assert not accept(i,"other",99)
