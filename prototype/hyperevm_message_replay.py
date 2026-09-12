class Replay: 
    def __init__(self): self.seen=set()
    def accept(self,domain,sender,nonce):
        k=(domain,sender,nonce)
        if k in self.seen:return False
        self.seen.add(k);return True

if __name__=="__main__":
    r=Replay(); assert r.accept("hyperevm","a",1) and not r.accept("hyperevm","a",1)
