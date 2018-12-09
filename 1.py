print("This is the assignment for December 1st")

file = open("1.txt", "r")

total = 0

for line in file:
    if line[0] == "+":
        total += int(line[1:])
    else:
        total -= int(line[1:])

print("Result part a:")
print(total)

total2 = 0
history = {0}
count = 0

while True:
    #print("Restarting......")
    #count+=1
    #print (count)
    file = open("1.txt", "r")

    for line in file:
        if line[0] == "+":
            total2 += int(line[1:])
        else:
            total2 -= int(line[1:])
        if total2 in history: 
            #print ("In history:")
            #print (total2)
            break
        history.add(int(total2))
    else:
        continue
    break

print ("Result part b:")
print(total2)