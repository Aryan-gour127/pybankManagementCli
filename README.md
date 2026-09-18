# 🏦 PyBank Management CLI

<p align="center">

### 💰 A simple banking system built with Python 🐍

**Create accounts • Manage customers • Deposit • Withdraw • Transfer • Track transactions • Save data**

</p>

---

## 🌷 About The Project

**PyBank Management CLI** is a beginner-friendly command-line banking application built with **Python**.

The project simulates basic banking operations through a simple terminal interface. It was created to practice Python programming fundamentals while building something that feels like a small real-world application.

The application allows users to create accounts, manage customers, perform banking transactions, check balances, view transaction history, close accounts, and save banking data using JSON.

> 🐍 Built with Python, curiosity, and a lot of `print()` statements. 💖

---

## ✨ Features

### 👤 Account Management

* 🏦 Create a new bank account
* 🔢 Automatically generate a unique account number
* 🔐 Set a 4-digit account PIN
* 💰 Set an initial deposit
* 📅 Store account creation date
* 💵 Track current account balance
* 🟢 Maintain account status

### 🧑 Customer Management

* 👤 Add customers
* 🆔 Generate unique customer IDs
* 📱 Store customer phone number
* 🏠 Store customer address
* 📅 Store customer joining date

### 💸 Banking Operations

* 💰 Deposit money
* 💳 Withdraw money
* 🔄 Transfer money between accounts
* 💵 Check account balance
* 📜 View transaction history
* 🔒 Close an account

### 💾 Data Persistence

Banking information can be stored locally using **JSON**.

```text
                 🏦 PyBank
                    │
                    ▼
             ┌──────────────┐
             │   Account    │
             │   Customer   │
             │ Transactions │
             └──────┬───────┘
                    │
                    ▼
              💾 JSON Data
```

This means the project can be extended from a temporary in-memory CLI into a persistent application.

---

## 🖥️ Application Menu

```text
==============================
========Choose Action========
==============================
1. Create Account
2. Add Customer
3. Deposit Money
4. Withdraw Money
5. Transfer Money
6. Check Balance
7. View Transactions
8. Close Account
9. Save Data
10. Exit Bank CLI
==============================
```

---

## 🔄 How The Application Works

```text
        🚀 Start Program
              │
              ▼
        📂 Load Data
              │
              ▼
       🏦 Choose Action
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
   Account  Customer  Transaction
      │       │        │
      └───────┼────────┘
              ▼
          💾 Save Data
              │
              ▼
           👋 Exit
```

---

## 💳 Banking Flow

### 🏦 Create Account

A user can create an account by providing:

```text
👤 Full Name
🎂 Date of Birth
📱 Phone Number
📧 Email
🏠 Address
🔐 4-Digit PIN
💰 Initial Deposit
```

The application then generates a unique account number.

---

### 💰 Deposit

```text
Enter Account Number
        ↓
Verify PIN
        ↓
Enter Deposit Amount
        ↓
Update Balance
        ↓
Create Transaction
```

---

### 💸 Withdraw

```text
Enter Account Number
        ↓
Enter Withdrawal Amount
        ↓
Check Balance
        ↓
Verify PIN
        ↓
Update Balance
        ↓
Create Transaction
```

---

### 🔄 Transfer

Money can be transferred from one account to another.

```text
Sender Account
      │
      ▼
 Verify PIN
      │
      ▼
Receiver Account
      │
      ▼
Check Balance
      │
      ▼
Transfer Amount
      │
      ▼
Update Both Accounts
      │
      ▼
Create Transactions
```

---

## 📜 Transaction History

The application maintains transaction information such as:

```text
Transaction ID
Transaction Type
Transaction Amount
Transaction Date
Balance After Transaction
```

This makes it possible to review an account's previous banking activity.

---

## 💾 JSON Data Storage

The project uses Python's built-in `json` module for local data storage.

A simple project structure can look like:

```text
PyBankManagementCli/
│
├── index.py
├── data/
│   └── bank_data.json
│
└── README.md
```

The JSON file can contain information for:

```text
👤 Customers
🏦 Accounts
💸 Transactions
```

---

## 🛠️ Tech Stack

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| 🐍 Python     | Main programming language |
| 🎲 `random`   | Generate unique IDs       |
| 🔤 `string`   | Generate numeric IDs      |
| 📅 `datetime` | Handle dates              |
| 💾 `json`     | Store and load data       |
| 🖥️ CLI       | User interaction          |

---

## 🧠 Python Concepts Practiced

This project was created to practice core Python concepts including:

* Variables
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* `for` loops
* `while` loops
* `if / elif / else`
* Functions and return statements
* String formatting
* User input
* Data validation
* Random ID generation
* File handling
* JSON serialization
* Basic application flow

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Aryan-gour127/pybankManagementCli.git
```

### 2. Open the Project

```bash
cd pybankManagementCli
```

### 3. Run the Application

```bash
python index.py
```

That's it! 🎉

---

## 📁 Project Structure

```text
📦 pybankManagementCli
│
├── 🐍 index.py
│
├── 💾 data/
│   └── bank_data.json
│
└── 📖 README.md
```

---

## 🎯 Learning Goals

This project is part of my journey toward becoming a better **Python developer**.

While building it, I focused on understanding how individual Python concepts can come together to create a complete command-line application.

```text
🐣 Python Basics
      ↓
🧠 Programming Logic
      ↓
🧩 Functions & Data Structures
      ↓
🏦 Banking Operations
      ↓
💾 Persistent Data
      ↓
🚀 Bigger Projects
```

---

## 🌱 Future Improvements

Some ideas for future versions:

* [ ] 🔐 Improve PIN security
* [ ] 🧑‍💼 Add admin functionality
* [ ] 🔎 Add customer/account search
* [ ] 📊 Add account reports
* [ ] 🧾 Generate transaction receipts
* [ ] 🗃️ Move from JSON to a database
* [ ] 🧪 Add automated tests
* [ ] 🧱 Rebuild using OOP
* [ ] 🎨 Create a graphical interface
* [ ] 🌐 Convert it into a web application

---

## ⚠️ Disclaimer

This project is made **for educational purposes only**.

It is a banking simulation designed for learning Python and software development.

> ❌ Do not use this application to store real banking information, real PINs, or perform real financial transactions.

---

## 💖 Why I Built This

I wanted to move beyond small Python exercises and build something that combines multiple concepts into one complete project.

**PyBank Management CLI** is one of my steps toward building larger applications.

```text
"Don't just learn the syntax.
Build something with it." 🚀
```

---

## 👨‍💻 Author

### Aryan Gour

🎓 BTech Artificial Intelligence Student
🐍 Python • JavaScript • React • Node.js • MongoDB

### 🔗 GitHub

**[@Aryan-gour127](https://github.com/Aryan-gour127)**

---

## ⭐ Support

If you found this project interesting:

⭐ Star the repository
🍴 Fork it
🐛 Report an issue
💡 Suggest an improvement

Every little bit of support means a lot! 💖

---

<p align="center">

### 🐍 Made with Python & lots of learning 💻

**Thanks for visiting PyBank Management CLI! 🏦✨**

</p>
