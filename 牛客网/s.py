import dis

def fu():
    a = 3
    b = a
    print(b)

dis.dis(fu)
