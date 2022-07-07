
def prime(num):

    trueprime = False
    for i in range(2,num):
        if num%i==0:
            trueprime = True
        else:
            continue
    if trueprime:
        print("no")
    else:
        (print("pr"))            
           

b = prime(31)