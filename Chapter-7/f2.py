with open("p1.txt","r") as f:
    data = f.read()

new_data = data.replace("Java","Python")

with open("p1.txt","w") as f:
    f.write(new_data)