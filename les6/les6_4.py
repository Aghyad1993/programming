def rng(lijst):
    res = max(lijst)-min(lijst)
    return(res)

lijst = [4,0,1,-2]
maxverschil = rng(lijst)
print(maxverschil)
lijst2 = [8,10,21,-2]
maxverschil2 = rng(lijst2)
print(maxverschil2)