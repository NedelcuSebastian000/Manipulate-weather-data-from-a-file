def temp():
    print("The average temperature is:")
    total = 0.0
    c = 0
    alltemp=[]
    with open("text.txt", 'r') as f:
        for line in f:
            if "Temperature" not in line: continue
            temp = line.split(" ")[1]
            total =total+ float(temp)
            c =c+ 1
            alltemp.append(total / c)
    print(total / c)
    return alltemp

def pressure():
    print("The average pressure is:")
    total = 0.0
    c = 0
    with open("text.txt", 'r') as f:
        for line in f:
            if "Pressure" not in line: continue
            presiune = line.split(" ")[4]
            total =total+ float(presiune)
            c =c+ 1
    print(total / c)

def altitude():
    print("The average altitude is:")
    total = 0.0
    c = 0
    with open("text.txt", 'r') as f:
        for line in f:
            if "Altitude" not in line: continue
            altitudine = line.split(" ")[4]
            total =total+ float(altitudine)
            c =c+ 1
    print(total / c)
temp()
pressure()
altitude()