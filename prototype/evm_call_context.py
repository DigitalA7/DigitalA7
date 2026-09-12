"""Validation minimale d un contexte d appel EVM."""

def safe_call(call, expected_chain, expected_contract):
    fields={"chain_id","sender","target","value","data","nonce"}
    return isinstance(call,dict) and fields <= call.keys() and call["chain_id"]==expected_chain and call["target"]==expected_contract and call["value"]>=0 and call["nonce"]>=0

if __name__ == "__main__":
    c={"chain_id":8453,"sender":"a","target":"0xapp","value":0,"data":"0x","nonce":1}
    assert safe_call(c,8453,"0xapp")
    assert not safe_call(c,1,"0xapp")
