class Nullifiers:
    def __init__(self): self.used=set()
    def consume(self,n):
        if not n or n in self.used:return False
        self.used.add(n);return True

if __name__=="__main__":
    s=Nullifiers(); assert s.consume("n1") and not s.consume("n1")
