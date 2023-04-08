# Passwords
# Raushan - 4045, Zeeshan - 2654, Kashish - 2185
# Account Number
# Raushan - 12345, Zeeshan - 65412, Kashish - 98745

import pwinput
def sum(x,y):
    z = x + y
    return(z)
def sub(x,y):
    z = x - y
    return(z)
print("\nWelcome to Row Bank\n")
users = {'Raushan': '4045', 'Zeeshan': '2654', 'Kashish': '2185'}
while True:
    username = input("Enter username: ")
    if username not in users:
        print("Invalid Username\nPlease Try again")
        continue
    password = users[username]
    a = pwinput.pwinput(prompt='Enter Password: ', mask='*')
    break
for i in range (1, 3, 1):
    if a != password:
        print("Incorrect Password\nAttempt Left:",3-i)
        a = pwinput.pwinput("\nEnter Password again: ")
        if a == password:
            print("Access Granted")
            break
    else:
        print("Access Granted")
        break
if a != password:
    print("Access Blocked")
    
if a == password:
    print("\nHello!",username)
    while a==password:
        ub = {'Raushan': 10000, 'Zeeshan': 5210, 'Kashish': 50000}
        Balance = ub[username]
        while True:
            try:
                print("\n1. Check Balance\n2. Withdraw Money\n3. Deposit Money\n4. Transfer\n5. My Profile\n6. Logout")
                choice = int(input("Enter Your Choice: "))
                break
            except ValueError:
                print("Enter Choice Only in Numbers")
        if choice == 1:
            print("Your Account Balance is $",Balance)
        elif choice == 2:
            while True:
                try:
                    withdraw = int(input("Enter Amount: "))
                    break
                except ValueError:
                    print("Enter Values in Numbers")
            if withdraw > Balance:
                print("\nInsufficient Balance in your Account\nTry again")
            else:
                print("You withdraw $",withdraw)
                print("The New Balance in your account is $",sub(Balance,withdraw))
                break
        elif choice == 3:
            while True:
                try:
                    deposit = int(input("Enter Amount: "))
                    break
                except ValueError:
                    print("Enter Values in Numbers")
            print("You Deposited $",deposit)
            print("The New Balance in your account is $",sum(Balance,deposit))
            break
        elif choice == 4:
            while True:
                try:
                    Transfer = int(input("Enter Amount: "))
                    break
                except ValueError:
                    print("Enter Values in Number")
            if Transfer >= Balance:
                print("Insufficient Balance in your Account")
                break
            while True:
                try:
                    Account = int(input("Enter Account Number: "))
                    break
                except ValueError:
                    print("Enter Values in Numbers")
            Acc = {12345: 'Raushan', 65412: 'Zeeshan', 98745: 'Kashish'}
            if Account not in Acc.keys():
                print("Account",Account,"not found in our Database")
            else:
                Name = Acc[Account]
                print("Amount",Transfer,"Transferred to Account Number",Account,"belongs to",Name)
                print("The New Balance in your account is $",sub(Balance,Transfer))
                break
        elif choice == 5:
            nm = {'Raushan': 'Raushan Kumar', 'Zeeshan': 'Zeeshan Ahmad', 'Kashish': 'Kashish Balhara'}
            nme = nm[username]
            do = {'Raushan': "25-04-2003", 'Zeeshan': '05-06-2003', 'Kashish': '29-03-2004'}
            dob = do[username]
            ac = {'Raushan': '02-04-2020', 'Zeeshan': '04-05-2021', 'Kashish': '15-05-2022'}
            acr = ac[username]
            print("\nName\t\t:",nme,"\nD.O.B\t\t:",dob,'\nAcc. Opened on\t:',acr)
        elif choice == 6:
            print("Thanks for visiting.")
            break
        elif choice != 1:
            print("\nYour Entered Choice",choice,"not found\nEnter Choice Only in between 1-4")