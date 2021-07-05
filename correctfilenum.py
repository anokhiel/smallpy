import os
pref="" #add prefix here
 
def getmax(fs):
    n=0
    for f in fs:
        s=f.split('.')
        so=s[0][len(pref):]
        if(len(so)>n):
            n=len(so)
    return n

cdir=os.getcwd()
for r, d, fs in os.walk(cdir):
    m=getmax(fs)
    for f in fs:
        af=cdir+'\\'+f
        s=f.split('.')
        so=s[0][len(pref):]
        k=len(so)
        m=getmax 
        if(k<2 and s[1]!='py'):
            print(af)
            os.rename(af,cdir+'\\'+pref+'0'*m+so+'.'+s[1])