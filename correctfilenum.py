import os
pref="" #add prefix here
cdir=os.getcwd()
for r, d, fs in os.walk(cdir):
    for f in fs:
        af=cdir+'\\'+f
        s=f.split('.')
        so=s[0][len(pref):]
        k=len(so)
        if(k<2):
            print(af)
            os.rename(af,cdir+'\\'+pref+'0'+so+'.'+s[1])