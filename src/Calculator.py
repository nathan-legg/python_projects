'''
Created on Aug 15, 2016

@author: Nathan
'''

running = True

while running:
    print("\nSelect an operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiple")
    print("4.Divide")
    print("5.Exit program")
    
    cmd = int(input("Enter choice(1/2/3/4/5): "))
    
    if cmd == 1:
        print("\nAdd")
        fnum = int(input("Enter first number: "))
        snum = int(input("Enter second number: "))
        result = fnum + snum
        print("\nResult: " + str(fnum) + " + " + str(snum) + " = " + str(result))
    if cmd == 2:
        print("\nSubtract")
        fnum = int(input("Enter first number: "))
        snum = int(input("Enter second number: "))
        result = fnum - snum
        print("\nResult: " + str(fnum) + " - " + str(snum) + " = " + str(result))
    if cmd == 3:
        print("\nMultiply")
        fnum = int(input("Enter first number: "))
        snum = int(input("Enter second number: "))
        result = fnum * snum
        print("\nResult: " + str(fnum) + " * " + str(snum) + " = " + str(result))
    if cmd == 4:
        print("\nDivide")
        fnum = int(input("Enter first number: "))
        snum = int(input("Enter second number: "))
        result = fnum / snum
        print("\nResult: " + str(fnum) + " / " + str(snum) + " = " + str(result))
    if cmd == 5:
        print("\nExiting!")
        running = False