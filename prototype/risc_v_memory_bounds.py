def load(memory, address, width):
    if address<0 or width<=0 or address+width>len(memory): raise IndexError("out of bounds")
    return memory[address:address+width]

if __name__=="__main__":
    assert load(b"abcd",1,2)==b"bc"
    try: load(b"ab",1,2); raise AssertionError
    except IndexError: pass
