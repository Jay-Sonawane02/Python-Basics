light = input("Enter color of light: ").lower()
if(light == "red"):
    print("STOP!")
elif(light == "yellow"):
    print("STEADY!")
elif(light == "green"):
    print("GO")
else:
    print("light is broken")