correct_pin = "1234"
attempts = 3

while attempts > 0:
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin == correct_pin:
        print("✅ Login successful!")
        break
    else:
        attempts -= 1
        print(f"❌ Incorrect PIN. {attempts} attempts left.")
else:
    print("🔒 Account locked due to too many incorrect attempts.")
    exit()

if entered_pin == correct_pin:
    print("Welcome to the ATM!")
    
balance= 0
while True:
    print("\n ATM Menu:")
    print("1.Check Balance")
    print("2.deposit Money")
    print("3.withdraw Money")
    print("4.Exit")
    choice=int(input("Enter your choice(1-4):"))
    
    if choice ==1:
        print ("your balance is:",balance)
    elif choice ==2:
        deposit=int(input("Enter amount to deposit: "))
        if deposit > 0:
            balance +=deposit
            print("Deposit successful! New balance is:", balance)
        else:
            print("INvalid desposit amount.")
    elif choice ==3:
        amount=int(input('Enter amount to withdraw: '))
        if amount > balance:
            print("❌ Insufficient balance.")
        elif amount <= 0:
            print("❌ Invalid withdrawal amount.")
        else:
            balance -= amount
            print(f"✅ Withdrawn ₹{amount}. New balance: ₹{balance}")
    elif choice ==4:
        print("Exiting the ATM. Thank you!")