

x = []
y = 0
for i in range(5):
    x.append(input("Enter the number to print the pattern"))
    if i ==5:
        break
for i in range(5):
    y = x[i]
    for i in range(int(y)):
        print(y , end = ' ',)
    print(" ")

input("Press any key to exit")


