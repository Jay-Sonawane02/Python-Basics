#search for a number x in tuple

tup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter a number: "))

index=0
while(index < len(tup)):
    if(tup[index] == x):
        print("found")
        break
    index+=1

if(index == len(tup)):
    print("Not Found")