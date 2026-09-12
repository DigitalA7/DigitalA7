"""Contrôle d une sortie publique de preuve ZK."""

def consistent(output, expected_program, expected_public):
    required={"program_id","public_output","proof"}
    return isinstance(output,dict) and required <= output.keys() and output["program_id"]==expected_program and output["public_output"]==expected_public and bool(output["proof"])

if __name__ == "__main__":
    o={"program_id":"p1","public_output":"ok","proof":"opaque"}
    assert consistent(o,"p1","ok")
    assert not consistent(o,"p2","ok")
