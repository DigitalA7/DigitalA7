def accepted(data, schema):
    return isinstance(data,dict) and set(schema)<=data.keys() and all(data[k] is not None for k in schema)

if __name__=="__main__":
    assert accepted({"amount":1,"user":"a"},{"amount","user"})
    assert not accepted({"amount":1},{"amount","user"})
