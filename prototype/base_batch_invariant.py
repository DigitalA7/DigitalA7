"""Invariant pédagogique d un lot Base."""

def valid_batch(batch, chain_id=8453):
    required={"chain_id","number","transactions","data_commitment"}
    return isinstance(batch,dict) and required <= batch.keys() and batch["chain_id"]==chain_id and batch["number"]>=0 and isinstance(batch["transactions"],list) and bool(batch["data_commitment"])

if __name__ == "__main__":
    assert valid_batch({"chain_id":8453,"number":1,"transactions":[],"data_commitment":"c"})
    assert not valid_batch({"chain_id":1,"number":1,"transactions":[],"data_commitment":"c"})
