print('This is your name backwards with no spaces:- ',end='')
revname=''
for f in reversed("roger thomas jenkins"):
    if f!=' ':
        revname=revname+f
print(revname,' and \n is ',len(revname),'characters long')
