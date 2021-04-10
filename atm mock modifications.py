#database ={accountNumber: firstname, lastname, email, dob, gender, transaction pin,account balance}

import random
import sys
import datetime
import time

database= {}

def calculateAge(dOB):
    birthdate=datetime.datetime.strptime(dOB,'%d/%m/%y').date()
    today= datetime.date.today()
    age = today.year - birthdate.year -((today.month, today.day)<(birthdate.month, birthdate.day))
    return age


def welcomePage():
    print('\t======== WELCOME TO EFFs-BANK ========')
    while True:
        try:
            available_option= int(input('''
1. Existing User
2. New User (Create account) \n'''))
            if(available_option == 1):
                login()
                break
            elif(available_option== 2):
                register()
                break
            else:
                print('Invalid Option')
                continue
        except ValueError:
            print('Invalid Input')


def register():
    print('\t=====CREATE ACCOUNT=====')
    firstname = input('firstname:\n')
    lastname = input('Lastname: \n')
    dOB = input('Date Of Birth(DD/MM/YY)  e.g(04/06/02):\n')
    ageResult=calculateAge(dOB)
    email = input('Email: \n')
    accountBalance= 0.00
    pin=int(input('Create Transaction pin: \n'))
    gender= input('''
Male (M)
Female(F)
Others (O) \n''')
    gender.lower

    while True:
        createPassword= input('create password: \n')
        confirmPassword= input('confirm password: \n')
        if len(createPassword) < 6:
            print('Password must contain atleast 6 characters')
            continue
        else:
            
            if((len(firstname) < 3) or (len(lastname) < 3) or (pin not in range(1000,10000 )) or (len(email) < 8 ) or (len(gender) != 1 or('@'  and '.' and 'com' not in email))and (gender.lower != 'm' or gender.lower !='f' or gender.lower != 'o' )):
                time.sleep(3)
                print('\n fill all required field, pin must be 4 characters, user must provide a valid email address')
                register()
                break
            else:
                if(confirmPassword == createPassword):
                    if ageResult >= 16:
                        acct_number = str(generateAcctID())
                        time.sleep(2)
                        print("Account Created")
                        print(f'Account number: {acct_number}')
                        database[acct_number]=[firstname, lastname, dOB, email, pin, gender, createPassword, accountBalance]
                        print('Proceed to login>>>')

                        login()
                        break
                            
                    else:
                        print('user must be up to age 16 to use app')
                        sys.exit()
                                    
                else:
                    print('passwords do not match')
                    continue

    
    

def login():
    print('\n ===== LOGIN =====')
    for item in range(1,3):
        account_number = input('Account number: \n')
        loginPassword = input('Password: \n')
        if ((account_number in database )):
            if (loginPassword == database[account_number][6]):
                print("\nloading...")
                time.sleep(2)
                
                now = datetime.datetime.now()
                print('\n you are logged in at :')
                print(now.strftime("%d/%m/%Y %H:%M:%S")) 

                bankOperation(account_number)
                break
            else:
                print("UserID provided doesn't match")
                continue
        else:
            print('Invalid account number')
            forgottenID= input('forgotten userID? (press 1), tap enter to skip \n')
            if(forgottenID =='1' ):
                forgotID()  
            elif(len(forgottenID)== 0 ):
                welcomePage()
            else:
                print('invalid input')
                sys.exit()
    login()


def forgotID():
    print('\t \n===== FORGOTTEN ID ========')
    forgottenAcct_No= input('account number: \n ')
    forgottenDateOfBirth= input ('D.O.B(DD/MM/YY): \n')
    if forgottenAcct_No in database:
        if(forgottenDateOfBirth == database[forgottenAcct_No][2]):
            print('account password: ', database[forgottenAcct_No][6])
            time.sleep(3)
            login()
        else:
            print("Invalid user details")
            welcomePage()
    else:
        print("account doesn't exist")
        welcomePage()


def generateAcctID():
    print('Generating Account Number...')
    return random.randrange(0000000000,9999999999)


def bankOperation(user):
    f_name = database[user][0]
    l_name = database[user][1]
    
    print(f'\nWelcome,{f_name} {l_name}') #I'll correct this by using a dictionary to store the values of first_name & last_name
    print('''
    select option
    1. Withdraw
    2. deposit
    3. Transfer
    4. Account Balance
    5. log out
    6. Exit''')
    select_option= int(input('select option=> '))
    if select_option == 1:
        withdraw(user)
    if select_option == 2:
        deposit(user)
    if select_option == 3:
        print('===== TRANSFER CASH =====')
        print('Processing...')
        time.sleep(2)
        print('''service unavalaible at the moment,
                 please try again later, THANK YOU!''')
        return_to_bankOperation(user)
        
    
    if select_option == 4:
        account_balance(user)
    if select_option == 5:
        print('are you sure you want to log out?')
        logOut= input("1.(yes) 2(no) \n")
        if logOut == '1' :
            time.sleep(4)
            login()
        elif logOut == '2':
            bankOperation(user)
        else:
            print('Invalid option')
            bankOperation(user)
            
    if select_option == 6:
        exit()
        

def deposit(user):
    print('====== DEPOSIT CASH ======')
    depositCash= int(input('amount to be deposited: \n #'))
    time.sleep(2)
    depositPin= int(input('Input tranasaction pin => \n'))
    if depositPin == database[user][4]:
        print('\n Processing...')
        time.sleep(3)
        if depositCash <= 1000000000:
            print('\n Transaction successful')
            database[user][7]= database[user][7] + depositCash
            return_to_bankOperation(user)
        else:
            print('\n Processing...')
            time.sleep(3)
            print('Transaction failed, user exceeded deposit limit')
            return_to_bankOperation(user)
           
    else:
        time.sleep(2)
        print('Invalid pin, Transaction Failed')
        time.sleep(2)
        bankOperation(user)        
    

def withdraw(user):
    print('=' * 5, 'WITHDRAW CASH','=' * 5)
    withdrawAmount = int(input('input amount to withdraw => \n #'))
    if withdrawAmount <= database[user][7]:
        withdrawPin = int(input(' Enter Transaction pin => \n'))
        if withdrawPin == database[user][4]:
            print('\n Processing...')
            time.sleep(3)
            print('\n Transaction successful')
            database[user][7]= database[user][7] - withdrawAmount
            return_to_bankOperation(user)
             
        else:
            time.sleep(2)
            print('Invalid pin, Transaction Failed')
            time.sleep(2)
            bankOperation(user)

    else:
        print('processing...')
        time.sleep(2)
        print('Insufficient Funds')
        time.sleep(2)
        return_to_bankOperation(user)
    

def account_balance(user):
    print('===== ACCOUNT BALANCE =====')
    print('\n Processing...')
    time.sleep(2)
    print('#',database[user][7])
    return_to_bankOperation(user)
    
        
def return_to_bankOperation(user):
    while True:
        transaction_two = input('''\n would you like to make another action?
1(yes to proceed)
2 (No to exit)\n''')
        if transaction_two == '1':
            time.sleep(3)
            bankOperation(user)
            break
        if transaction_two == '2':
            exit()
        else:
            print('invalid Option')
            continue
    
        

welcomePage()

