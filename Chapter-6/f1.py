#WAP to print length of a list

l=[1,2,3,4,5,6,7,8,9,10]

def myLength(lt):
    count=0
    for i in lt:
        count+=1
    print(count)
    return count

myLength(l)