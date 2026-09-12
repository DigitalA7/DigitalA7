def target(pc, offset, aligned=4):
    candidate=pc+offset
    return candidate if candidate%aligned==0 else None

if __name__=="__main__":
    assert target(100,8)==108 and target(100,3) is None
