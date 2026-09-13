import random 
import string
import datetime

Bank = []
Account = []
Customer = []

def GenAccountNo():

    accountNo =''.join(random.choices(string.digits, k=10))
    return accountNo

def GenCustomerId():

    CustomerId = ''.join(random.choices(string.digits, k = 12 ))
    return CustomerId

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
        'UserEmail':UserEmail,
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
