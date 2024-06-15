def myFunc():
    with open("numbers.txt","r") as f:
        data = f.read()
        nums = data.split(",")

    print(nums)
    count=0
    for i in nums:
        if(int(i)%2==0):
            count+=1

    print("No of Even Numbers:",count)
myFunc()