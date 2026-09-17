import random 
import string
import datetime
import json

Bank = []
Account = []
Customer = []
Transaction = []

def SaveData():

    accData = {
        "accounts" : Account,
        "customers": Customer,
        "trnsaction":Transaction
    }

    with open("data/bank_data.json", "w") as file:
        json.dump(accData,file, indent=4)
        
    print("data saved succesfully!!")

def LoadData():

    global Account
    global Customer
    global Transaction

    try:
        with open("data/bank_data.json","r") as file:
            data =  json.load(file)
    
        Account = data.get("Account",[])
        Customer = data.get("Customer", [])
        Transaction = data.get("Transaction", [])

        print("Data Loaded Successfully")

    except FileNotFoundError:
        print("No Previous Data Found. Starting fresh !!")


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

    UserInitDeposit = int(input("Enter Initial Deposit Amount : "))

    if UserInitDeposit < 300 :
        print(f"Minimum Initial Deposit Must be greater than (300rs)")
        return

    # accountNum = GenAccountNo()
    accountCreateDate = datetime.datetime.now().strftime("%d-%m-%y")
    accountStatus = "Active"
    accountBalance = UserInitDeposit
    accountTransactionHistory = []

    Acc = {
        'userName':UserName,
        'userDob':UserDob,
        'userPhone':userPhone,
        'userEmail':UserEmail,
        'userAddress':UserAddress,
        'userPin':UserPin,
        'UserInitDeposit':UserInitDeposit,
        'accountNum':accountNum,
        'accountCreateDate':accountCreateDate,
        'accountStatus':accountStatus,
        'accountBalance':accountBalance,
        'accountTransactionHistory':accountTransactionHistory
    }
    
    Account.append(Acc)
    print(Acc)
    print("Account Created Successfully!!")


def AddCustomer():

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

    DepositAccountNo = input("Enter Your Account.no : ")

    for item in Account:

        if DepositAccountNo == item["accountNum"]:

            print(f"Account {item['accountNum']} found!!")

            askPin = input("Enter Pin For Your Account : ")

            if askPin == item["userPin"]:

                print("Pin Matched Successfully!")
            else:

                print("Incorrect Pin!")
                return

            depositAmount = float(input("Enter The Deposit Amount : "))

            if depositAmount <= 0:
                print("Deposit amount must be greater than ₹0!")
                return
            
            item["accountBalance"] += depositAmount

            depositDate = datetime.datetime.now().strftime("%d-%m-%y")

            Tran = {

            "accountNumber": DepositAccountNo,
            "transactionId": TransId(),
            "date": depositDate,
            "amount": depositAmount,
            "transactionType": "Deposit",
            "balanceAfter": item["accountBalance"]

            }

            item["accountTransactionHistory"].append(Tran)
            Transaction.append(Tran)

            print(f"\nAccount No : {item['accountNum']}")
            print(f"₹{depositAmount} Deposit Successful!")
            print(f"Current Balance : ₹{item['accountBalance']}")
            return

    print(f"Account No {DepositAccountNo} does not exist!")

def WithdrawMoney():

    WithdrawAccountNo = input("Enter Your Account Number!")

    for item in Account:

        WithdrawAmount = float(input("Enter The Withdraw Amount : "))

        if WithdrawAccountNo == item['accountNum']:
        
            if WithdrawAmount <= 0:

                print("Withdraw amount must be greater than ₹0!")

                return

            if WithdrawAmount > item["accountBalance"]:

                print("Insufficient Balance!!")

                return

            askPin = input("Enter Your PIN : ")

            if askPin != item["userPin"]:

                print("Incorrect Pin!")

                return

            print("Pin Matched Successfully!")
            
            item["accountBalance"] -= WithdrawAmount

            withdrawDate = datetime.datetime.now().strftime("%d-%m-%y")
            Tran = {
                
                "accountNumber": WithdrawAccountNo,
                "transactionId": TransId(),
                "date": withdrawDate,
                "amount": WithdrawAmount,
                "transactionType": "Withdraw",
                "balanceAfter": item["accountBalance"]

            }

            item["accountTransactionHistory"].append(Tran)
            Transaction.append(Tran)

            print(f"\nAccount No : {item['accountNum']}")
            print(f"₹{WithdrawAmount} Withdraw Successful!")
            print(f"Current Balance : ₹{item['accountBalance']}")
            return

    print(f"Account No {WithdrawAccountNo} does not exist!")


def TransferMoney():

    SenderAccountNo = input("Enter Your Account Number : ")

    for Sender in Account:

        if SenderAccountNo == Sender['accountNum']:

            print("Account Found Successfully!")

            askPin = input("Enter Pin for Your Account : ")

            if askPin != Sender['userPin']:
                print("Incorrect pin!")
                return
            print("Pin Matched Successfully!")

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

            TransferAmount = float(input("Enter Transfer Amount : "))

            if TransferAmount <= 0 :
                print("Transfer Amount Must be Greater Than 0!")
                return
            elif TransferAmount > Sender['accountBalance']:
                print("Insufficient Balance in Your Account ")
                print(f"Current Balance :{Sender['accountBalance']}")
                return

            Sender['accountBalance'] -= TransferAmount
            Receiver['accountBalance'] += TransferAmount

            TransferDate = datetime.datetime.now().strftime("%d-%m-%y")

            transactionId = TransId()
            
            SenderTransaction = {

                "SenderAccountNo": SenderAccountNo,
                "ReceiverAccountNo": ReceiverAccountNo,
                "transactionId": transactionId,
                "date": TransferDate,
                "amount": TransferAmount,
                "transactionType": "Transfer",
                "balanceAfter": Sender["accountBalance"]

            }
            ReceiverTransaction = {
                    
                "SenderAccountNo": SenderAccountNo,
                "ReceiverAccountNo": ReceiverAccountNo,
                "transactionId": transactionId,
                "date": TransferDate,
                "amount": TransferAmount,
                "transactionType": "Transfer",
                "balanceAfter": Receiver["accountBalance"]
            }

            Sender['accountTransactionHistory'].append(SenderTransaction)
            Receiver['accountTransactionHistory'].append(ReceiverTransaction)

            Transaction.append(SenderTransaction)
            Transaction.append(ReceiverTransaction)

            print("\nTransfer Successful!")
            print(f"form Account : {SenderAccountNo}")
            print(f"To Account   : {ReceiverAccountNo}")
            print(f"Amount       : ₹{TransferAmount}")
            print(f"Your Balance : ₹{Sender['accountBalance']}")

            return

    print(
            f"Account No {SenderAccountNo} does not exist!!"
        )

def CheckBalance():
     
     Check = input("Enter Your Account Number : ")

     for item in Account:

         if Check == item['accountNum']:
             print("Account Match Found Successfully!")

             askPin = input("Enter Your Pin :")

             if askPin != item['userPin']:
                 print("Incorrect pin!")
                 return
             
             print("Pin Matched Successfully!")

             print("-"*30)
             print(f"Current Account Balance : ₹{item['accountBalance']}")
             print("-"*30)

             return
         
     print(f"Account Number {Check} does not exist!")

def ViewTransactionHistory():

    view = input("Enter Your Account Number : ")

    for item in Account:

        if view == item['accountNum']:

            print("Account Match Found Successfully!")

            askPin = input("Enter Account Pin  ")

            if askPin != item['userPin']:
                print("Pin Incorrect !")
                return
            print("Pin Matched Successfully !")

            print("-" * 30)
            print(f"Your Transaction History for Account : {item['accountNum']}")
            print("-" * 30)
            print(f"Transaction History")

            # print(f"- > {item['accountTransactionHistory']}")
            for transaction in item['accountTransactionHistory']:

                print(f"Transaction ID     : " f"{transaction['transactionId']}")

                print(f"Transaction Type   : "f"{transaction['transactionType']}")

                print(f"Transaction Amount : "f"₹{transaction['amount']}")

                print(f"Transaction Date   : "f"{transaction['date']}")

                print(f"Balance After      : "f"₹{transaction['balanceAfter']}")
                print("-" * 30)

            return

    print(f"Account Number {view} does not exist!")

def CloseAccount():

    close = input("Enter Your Account Number : ")

    for item in Account:

        if close != item['accountNum']:

            print(f"No Account Found with Account.No {close}")

            return

        print("Account Match Found!")

        check = input("DO YOU WANT TO CLOSE THIS ACCOUNT ? (y/n)")

        if check == "y":

            item['accountBalance'] >= 0

            print("Can't close Account Yet, Make Sure Your Account Balance is Zero")

            print(f"Current Account Balance = {item['accountBalance']}")

            return

        item['accountStatus'] == "closed"

        for acc in Account:

            print(f"Account Holder Name   : {acc['userName']}")
            print(f"Account Number        : {acc['accountNum']}")
            print(f"Account Creation-Date : {acc['accountCreateDate']}")
            print(f"Account Status        : {acc['accountStatus']}")

            return

    print(f"Account Number {close} Does Not Exist!")

LoadData()

while True:


    print("="*30)
    print("="*8 + "Choose Action" + "="*8)
    print("="*30)
    print("1. Create Account")
    print("2. Add Customer")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Transfer money")
    print("6. Check Balance")
    print("7. View Transactions")
    print("8. Close Account")
    print("9. Save Data")
    print("10. Exit Bank CLI")
    print("="*30)


    selectAction = input("Enter Choice Action.No (1.2.3.4.5.6.7.8.9.10) : ")

    if selectAction == "1":
        CreateAcc()

    elif selectAction == "2":
        AddCustomer()

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
        SaveData()
    
    elif selectAction == "10":
        SaveData()
        print("Thank Your Dear Customer For Trusting Us!!")
        print("Goodbye , Visiting The Bank Again!!")
        break

    else :
        print("invalid choice!!")
