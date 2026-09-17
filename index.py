import random 
import string
import datetime

Bank = []
Account = []
Customer = []
Transaction = []

def GenAccountNo():
    accountNo =''.join(random.choices(string.digits, k=10))
    return accountNo

def GenCustomerId():
    CustomerId = ''.join(random.choices(string.digits, k = 12 ))
    return CustomerId

def TransId():

    while True:

        tranId = ''.join(
            random.choices(string.digits, k=10)
        )

        if not any(
            transaction["transactionId"] == tranId
            for transaction in Transaction
        ):
            return tranId


def CreateAcc():

    UserName = input("Enter Your Full-Name : ")
    UserDob = input("Enter Your Date of Birth (00-00-0000) : ")
    userPhone = int(input("Enter Your Phone-no. : "))
    UserEmail = input("Enter Your E-mail : ")
    UserAddress = input("Enter Your Address : ")
    UserPin = input("Enter Account Pin (4 digits) : ")

    if len(UserPin) !=4 or not UserPin.isdigit():

        print("Account Pin must contain 4 digit!")
        return

    while True:
        accountNum = GenAccountNo()
        if not any(Acc["accountNum"] == accountNum for Acc in Account):
            break

    UserInitDeposite = int(input("Enter Initial Deposite Amount : "))

    if UserInitDeposite < 300 :
        print(f"Minimum Initial Deposite Must be greater than (300rs)")
        return

    # accountNum = GenAccountNo()
    accountCreateDate = datetime.datetime.now().strftime("%d-%m-%y")
    accountStatus = "Active"
    accountBalance = UserInitDeposite
    accountTransactionHistory = []

    Acc = {
        'userName':UserName,
        'userDob':UserDob,
        'userPhone':userPhone,
        'userEmail':UserEmail,
        'userAddress':UserAddress,
        'userPin':UserPin,
        'userInitDeposite':UserInitDeposite,
        'accountNum':accountNum,
        'accountCreateDate':accountCreateDate,
        'accountStatus':accountStatus,
        'accountBalance':accountBalance,
        'accountTransactionHistory':accountTransactionHistory
    }
    
    Account.append(Acc)
    print(Acc)
    print("Account Created Succesfully!!")


def AddCutomer():

    customerName = input("Enter Your Full Name : ")
    customerAge = input("Enter your age : ")
    customerPhoneNum = input("Enter Your Phone.No : ")
    customerAddress = input("Enter your Address : ")

    while True:
        customerId = GenCustomerId()

        if not any(
            existingUser["customerId"] == customerId
            for existingUser in Customer
        ):
            break

    customerJoinDate = datetime.datetime.now().strftime("%d-%m-%y")

    user = {

        "customerId": customerId,
        "customerName": customerName,
        "customerAge": customerAge,
        "customerPhoneNum": customerPhoneNum,
        "customerAddress": customerAddress,
        "customerJoinDate": customerJoinDate
    }

    Customer.append(user)

    print(f"\nCustomer Added To The DataBase : {user}")

    print("=" * 30)

    print(f"{user['customerName']} Welcome to CLI Bank Services!")
    return


def DepositMoney():

    depositeAccountNo = input("Enter Your Account.no : ")

    for item in Account:

        if depositeAccountNo == item["accountNum"]:

            print(f"Account {item['accountNum']} found!!")

            askPin = input("Enter Pin For Your Account : ")

            if askPin == item["userPin"]:

                print("Pin Matched Successfully!")
            else:

                print("Incorrect Pin!")
                return

            depositAmmount = float(input("Enter The Deposit Ammount : "))

            if depositAmmount <= 0:
                print("Deposit amount must be greater than ₹0!")
                return
            
            item["accountBalance"] += depositAmmount

            depositDate = datetime.datetime.now().strftime("%d-%m-%y")

            Tran = {

                "depositAccountNo": depositeAccountNo,
                "transactionId": TransId(),
                "depositDate": depositDate,
                "depositAmount": depositAmmount,
                "transactionType": "Deposit",
                "balanceAfter": item["accountBalance"]
            }

            item["accountTransactionHistory"].append(Tran)
            Transaction.append(Tran)

            print(f"\nAccount No : {item['accountNum']}")
            print(f"₹{depositAmmount} Deposit Successful!")
            print(f"Current Balance : ₹{item['accountBalance']}")
            return

    print(f"Account No {depositeAccountNo} does not exist!")

def WithdrawMoney():

    WithdrawAccountNo = input("Enter Your Account Number!")

    for item in Account:

        WithdrawAmmount = float(input("Enter The Withdraw Ammount : "))

        if WithdrawAccountNo == item['accountNum']:
        
            if WithdrawAmmount <= 0:

                print("Withdraw amount must be greater than ₹0!")

                return

            if WithdrawAmmount > item["accountBalance"]:

                print("Insufficient Balance!!")

                return

            askPin = input("Enter Your PIN : ")

            if askPin != item["userPin"]:

                print("Incorrect Pin!")

                return

            print("Pin Matched Successfully!")
            
            item["accountBalance"] -= WithdrawAmmount

            withdrawDate = datetime.datetime.now().strftime("%d-%m-%y")
            Tran = {

                "WithdrawAccountNo": WithdrawAccountNo,
                "transactionId": TransId(),
                "withdrawDate": withdrawDate,
                "WithdrawAmmount": WithdrawAmmount,
                "transactionType": "Withdraw",
                "balanceAfter": item["accountBalance"]
            }

            item["accountTransactionHistory"].append(Tran)
            Transaction.append(Tran)

            print(f"\nAccount No : {item['accountNum']}")
            print(f"₹{WithdrawAmmount} Withdraw Successful!")
            print(f"Current Balance : ₹{item['accountBalance']}")
            return

    print(f"Account No {WithdrawAccountNo} does not exist!")


def TransferMoney():

    SenderAccountNo = input("Enter Your Account Number : ")

    for Sender in Account:

        if SenderAccountNo == Sender['accountNum']:

            print("Account Found Succesfully!")

            askPin = input("Enter Pin for Your Accout : ")

            if askPin != Sender['userPin']:
                print("Incorrect pin!")
                return
            print("Pin Matched Succesfully!")

            ReceiverAccountNo = input("Enter Receiver Account Number : ")

            if SenderAccountNo == ReceiverAccountNo:
                print("Sender and Receiver Account can not be same !!")
                return

            Receiver = None

            for item in Account:
            
                if ReceiverAccountNo == item['accountNum']:
                    Receiver = item
                    break
                
            if Receiver is None:
                print(
                    f"Receiver Account No {ReceiverAccountNo} does not exist!"
                )
                return

            print("Receiver Account Found Successfully!")

            TransferAmmount = float(input("Enter Transfer Ammount : "))

            if TransferAmmount <= 0 :
                print("Transfer Ammount Must be Greater Than 0!")
                return
            elif TransferAmmount > Sender['accountBalance']:
                print("Insuffucient Balance in Your Account ")
                print(f"Current Balance :{Sender['accountBalance']}")
                return

            Sender['accountBalance'] -= TransferAmmount
            Receiver['accountBalance'] += TransferAmmount

            TranferDate = datetime.datetime.now().strftime("%d-%m-%y")

            transactionId = TransId()
            
            SenderTransaction = {
                    
                 "SenderAccountNo": SenderAccountNo,
                 "ReceiverAccountNo": ReceiverAccountNo,
                 "transactionId": transactionId,
                 "TranferDate": TranferDate,
                 "TransferAmmount": TransferAmmount,
                 "transactionType": "Transfer",
                 "balanceAfter": Sender["accountBalance"]
            }
            ReceiverTransaction = {
                    
                 "SenderAccountNo": SenderAccountNo,
                 "ReceiverAccountNo": ReceiverAccountNo,
                 "transactionId": transactionId,
                 "TranferDate": TranferDate,
                 "TransferAmmount": TransferAmmount,
                 "transactionType": "Transfer",
                 "balanceAfter": Receiver["accountBalance"]
            }

            Sender['accountTransactionHistory'].append(SenderTransaction)
            Receiver['accountTransactionHistory'].append(ReceiverTransaction)

            Transaction.append(SenderTransaction)
            Transaction.append(ReceiverTransaction)

            print("\nTransfer Successful!")
            print(f"From Account : {SenderAccountNo}")
            print(f"To Account   : {ReceiverAccountNo}")
            print(f"Amount       : ₹{TransferAmmount}")
            print(f"Your Balance : ₹{Sender['accountBalance']}")

            return

    print(
            f"Account No {SenderAccountNo} does not Exists!!"
        )

def CheckBalance():
     
     Check = input("Enter Your Account Number : ")

     for item in Account:

         if Check == item['accountNum']:
             print("Account Match Found Succesdully!")

             askPin = input("Enter Your Pin :")

             if askPin != item['userPin']:
                 print("Incorrect pin!")
                 return
             print("Pin Matched Succesfully!")
             print("-"*30)
             print(f"Current Account Balance : ${item['accountBalance']}")
             print("-"*30)
             return
     print(f"Account No {Check} does not exist!")

def ViewTransactionHistory():
    pass

def CloseAccount():
    pass

while True:


    print("="*30)
    print("="*8 + "Choose Action" + "="*8)
    print("="*30)
    print("1. Create Account")
    print("2. Add Customer")
    print("3. Deposite Money")
    print("4. Withdraw Money")
    print("5. Transfer Monay")
    print("6. Check Balance")
    print("7. View Transactions")
    print("8. Close Account")
    print("9. Exit Bank Cli")
    print("="*30)


    selectAction = input("Enter Choice Action.No (1.2.3.4.5.6.7.8.9) : ")

    if selectAction == "1":
        CreateAcc()

    elif selectAction == "2":
        AddCutomer()

    elif selectAction == "3":
        DepositMoney()

    elif selectAction == "4":
        WithdrawMoney()

    elif selectAction == "5":
        TransferMoney()

    elif selectAction == "6":
        CheckBalance()

    elif selectAction == "7":
        ViewTransactionHistory()

    elif selectAction == "8":
        CloseAccount()

    elif selectAction == "9":
        print("Thank Your Dear Customer For Trusting Us!!")
        print("Goodbye , Visiting The Bank Again!!")
        break

    else :
        print("invalid choice!!")
