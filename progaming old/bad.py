def get_dict(x):
    x = x.lower()
    N = len(x)-1
    d = {"smallest":1/N}
    for i in range(len(x)-1):
        try:
            d[x[i:i+2]] +=1/N
        except:
            d[x[i:i+2]] = 1/N
    
    return d

def H(x,d):
    ent = 0
    for i in range(len(x)-1):
        try:
            p = d[x[i:i+2]]*1
            ent-= p*np.log(p)
        except:
            p = d["smallest"]
            ent-=p*np.log(p)
    return ent/(len(x)-1)


D = get_dict(training)

def probably_human_written(x):
    entropy = H(x,D)
    if entropy>0.015:
        return True
    else:
        return False



print(probably_human_written("qwert yui oasdfsaf asfasf jlkjxz lcjkv pasd fghjklzxc vbnm"))
print(probably_human_written("hallo ik ben leander post en ik woon in utrecht"))
