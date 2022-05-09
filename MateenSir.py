# unlimited Multiplication Table, if you want..
while True:
    n=int(input("Enter a number: "))
    for i in range(1,11):
        print(n,"X",i,"=",i*n)
    x=input("Do you want to exit??(Y/N): ")
    if x=="Y":
        continue
    elif x=="N":
        print("Bye Bye...")
        break
    else:
        print("error")
        print("Please run the code again & type correct number...")
        break
