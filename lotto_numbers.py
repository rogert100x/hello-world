# create a list of number 1..52
#randomly select a number and remove it from the listdo this 6 times
#Use list.append(item) to add items to the list
#Use random.choice(list name) to randomly select an item in the list
#Use list.append(item) to add an item to a list
#list.remove(item) to remove an item from a list
# create a list of number 1..52
#outputs lotto_numbers.txt

import random
import numpy as np
repeats=int(input(' How many repeats? \n'))
print('\n Here are ',repeats,' lists of randomly generated Lotto \n number between 1 ..52')
f = open("lotto_numbers.txt", "a")
f.write('\nList of lotto numbers...')
f.write('\n')
f.close()    
listoflist=[]
#repeat repeats times
for h in range(repeats):
    numlist=[]
    lottolist=[]
    #generate a str list 1..52
    for f in range (1,53): 
        numlist.append(str(f))
    #end of f
    #randomly select a number and remove it from the list * 6 times
    for t in range(6):
        temp=random.choice(numlist)
        lottolist.append(temp)
        numlist.remove(temp)
    #end of t - lottolist complete
    listoflist.append(lottolist)
    #write lotolist to file
    f = open("lotto_numbers.txt", "a")
    f.write('-'.join(lottolist))
    f.write('\n')
    f.close()    

#end of h

#create listoflist as an ndarray using numpy
arr=np.array(listoflist)
print(arr)

print('Read generated lotto_numbers.txt file')
filename='lotto_numbers.txt'
f=open(filename,'r')
print(f.read())
f.close()
