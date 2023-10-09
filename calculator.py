def claculator(n=0):
    print("-----------------------------------------")
    print("For getting ansawer press '='")
    print("-----------------------------------------")
    operation=input("What operation do you want to perform? + - / * ")
    if operation is "=":
        ansawer=n
        print(ansawer)
        return ansawer
    user_input=int(input("Enter number"))
    if operation is "+":
        print("works")
        user_input= user_input+int(input("Enter number"))
        claculator(n=user_input)
    elif operation is "-":
        user_input=user_input-int(input("Enter number"))
        claculator(n=user_input)
    elif operation is "*":
        user_input=user_input*int(input("Enter Number"))
        claculator(n=user_input)
    elif operation is "/":
        user_input=user_input//int(input("Enter number"))
        claculator(n=user_input)
    else:
        print("Enter following * + - /")
        claculator(n=user_input)
claculator()