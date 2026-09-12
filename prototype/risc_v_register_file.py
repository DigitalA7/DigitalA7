def write(regs, name, value):
    if name=="x0": return dict(regs)
    out=dict(regs); out[name]=value; return out

if __name__=="__main__":
    r=write({"x0":0,"x1":1},"x2",3); assert r["x2"]==3 and write(r,"x0",9)["x0"]==0
