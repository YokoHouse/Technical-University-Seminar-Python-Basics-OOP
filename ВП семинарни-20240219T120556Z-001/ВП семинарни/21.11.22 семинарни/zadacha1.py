def display_menu():
    print("1. Convert BGN to EUR")
    print("2. Convert BGN to TL")
    print("3. Convert BGN to USD")
    print("4. Exit")

def BGN_to_EUR(value):
    return value/1.95
def BGN_to_TL(value):
    return value/0.10
def BGN_to_USD(value):
    return value/1.91

while True:
    display_menu()
    choice=int(input())
    if choice==4:
        print("Bye!")
        break
    else:
        amount=float(input("Enter an amount in BGN: "))
        if choice==1:
            print(amount,"BGN", BGN_to_EUR(amount),"Euro")
        elif choice==2:
            print(amount,"BGN", BGN_to_TL(amount), "Turkish Lira")
        elif choice==3:
            print(amount,"BGN",BGN_to_USD(amount),"USD")
            