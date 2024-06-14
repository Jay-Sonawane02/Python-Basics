#recursively print all elements of a list

def myPrint(l,index=0):
    if(index == len(l)):
        return

    print(l[index])
    myPrint(l,index+1)

myPrint([1,2,3,4,5])