import random
import math


with open('badandboujee.txt', 'r') as f:
    wordlist = []
    count = 0
    for line in f:
        for word in line.split():
            wordlist.append(word)
    
    #for word in wordlist:
        #count = count + 1
        
        
def no_duplicates(wordlist):
    new_set = set()
    new_set_add = new_set.add
    return [x for x in wordlist if x not in new_set and not new_set_add(x)]

sd = no_duplicates(wordlist)



for word in sd:
    count = count + 1
    
   
print ("Welcome to the Lyrical Name Game")
while True:
    print ("")
    answer = input("Enter a Letter or type Quit: ")
    ds = answer.strip()
    dl = ds.lower() or ds.upper()
    if dl == ('quit'):
        quit()
    try:
        newlist = [ word for word in sd if word[0] == (dl) ]
        print (random.choice(newlist))
        continue
        
    except:
        print ('{} Not Found. Try Again.'.format(dl))
        continue
                







        
        
        
        


#while rndword > 0:
    #rndword -= 1
    #print (random.choice(newlist))
   # break
    



    
        

                       
