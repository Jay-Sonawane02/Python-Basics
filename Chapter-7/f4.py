def check_for_line():
    word = "learning"
    data = True
    with open("p1.txt","r") as f:
        line_no =1
        while data:
            data = f.readline()
            if(word in data):
                return line_no
            line_no+=1
    
    return -1

print(check_for_line())