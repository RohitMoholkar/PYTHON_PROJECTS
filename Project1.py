# ATM MANAGEMENT SYSTEM USING PYTHON.  

def option_screen2():

    print() 
    print( " please select one of the option below : " )

    print() 
    print( " 4. Back to Options " ) 
    print( " 5. EXIT " ) 

def option_screen1():

    print() 
    print( " please select one of the option below : " ) 
    
    print() 
    print( " 1. CHECK ACCOUNT BALANCE " ) 
    print( " 2. DEPOSIT MONEY " )
    print( " 3. WITHDRAW MONEY " ) 

def welcome_screen():

    id = "batman_account" 
    password = 123456789
 
    print() 
    print( " ********** HELLO AND WELCOME TO BANK OF IRELAND ********** " ) 
    print() 
    print( " to move forward please enter your id and password " ) 
    
    print()
    id_check = input(" Please enter your bank id : ") 
    password_check = int(input(" Please enter your bank password : ")) 

    if id==id_check and password==password_check: 

        return True
    
    else:

        return False

check = True 
bank_balance = 500000

if welcome_screen():

    print() 
    print( " ^ your id and password is correct you can move forward now ^ " )  

else:

    check = False 
    val = 0 

while check==True: 

    option_screen1()  

    print() 
    option1 = int(input(" Enter option : ")) 

    if option1==1:

        print() 
        print( " Account Balance is :", bank_balance, "Rs" )  

    elif option1==2:

        print() 
        amount1 = int(input( " please enter the amount you want to deposite in your account : " ))

        bank_balance = bank_balance + amount1
    
    elif option1==3:

        print()
        amount2 = int(input(" please enter the amount you want to withdraw from your bank account : " ))

        if amount2<=bank_balance:

            bank_balance = bank_balance - amount2 
        
        else:

            print()
            print( " you dont have sufficent balance in your bank account ! " ) 

    option_screen2() 

    print() 
    option2 = int(input(" Enter option : "))

    if option2==4:

        continue

    elif option2==5:

        val = 1  

        break 

if val==0:

    print() 
    print( " either your id or password is incorrect ! " )
    print( " Please Try Again " ) 
    print()  

else:
 
    print() 
    print( " ********** THANK YOU FOR USING BANK OF IRELAND ********** " )

    print() 
    print( " ********** HAVE A NICE DAY ********** " )
    print() 