#WAP to check if list is palindromic or not

list1 = [1,2,1]
copy = list1.copy()
copy.reverse()

print(list1)
print(copy)

if(list1 == copy):
    print("Palindrome")
else:
    print("Not Palindromic")