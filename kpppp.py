# binary tree time

def ll(list,k):
    oo = 0
    end = len(list) - 1
    mid = 0
    p = 0

    while oo <= end:

        mid  = end + oo //2
        if list[mid] <k :
            oo = mid+1
            p = p+1
        elif list[mid] >k:
            end = mid-1
            p = p+1

        else :
            return p
    
    print(p)
    return -1

pppp = ll([1,2,3,4,5,6,7,8,9,12,44,58,698,7823],44)   

print(pppp)

