#print multiplication table of a number
num = int(input("Enter a number: "))

i=1
print("Multiplication table of",num)
while(i<=10):
    print(f'{num} x {i} = {num*i}')
    i+=1
