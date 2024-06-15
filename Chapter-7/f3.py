with open("p1.txt","r") as f:
    data=f.read()

if(data.find("learning") != -1):
    print("Found")
else:
    print("Not Found")
