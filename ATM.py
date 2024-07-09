print("------------ ATM ------------")
print("Welcome to SBI ")
print("\n 1=check balance","\n 2=widrow money", "\n 3=deposite money", "\n 4=check deposite")
choice = int(input("Please eneter the choice"))
ab = 1000
if choice == 1:
    print("your account balance is ", ab)
elif choice == 2:
    b  = int(input("please amount you want to widrow"))
    amount = ab - b
    print(f"you have succesfully widrow {b}", "Now your balance is", amount)
    print("thank you for SBI banking")
elif choice == 3:
    d = int(input("please enter the amount you want to deposite"))
    c = ab + d
    print("Now your account balance is ", c)
elif choice == 4:
    c = input("please enter the bank name to deposite check")
    print(f"your check has been deposite in {c} bank")
else:
    print("you have eneter the invalid input,  please try again")