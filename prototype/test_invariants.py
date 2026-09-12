"""Tests sans dépendance pour les invariants publiés."""
from base_batch_invariant import valid_batch
from evm_call_context import safe_call
from hyperevm_intent_guard import accept
from zk_public_output_check import consistent

def run():
    assert valid_batch({"chain_id":8453,"number":1,"transactions":[],"data_commitment":"c"})
    assert safe_call({"chain_id":8453,"sender":"a","target":"0xapp","value":0,"data":"0x","nonce":1},8453,"0xapp")
    assert accept({"network":"hyperevm","sender":"a","nonce":1,"asset":"USDC","amount":1,"deadline":10},"hyperevm",9)
    assert consistent({"program_id":"p","public_output":"ok","proof":"x"},"p","ok")

if __name__ == "__main__": run(); print("invariants: ok")
