#sum of first n natural numbers

n = int(input("Enter n: "))

sum=0
i=1

while(i<=n):
    sum+=i
    i+=1

print(sum)