
money = 5000000
# start up the programming
name = input("please enter your name:")

def balance(show_header):
    if show_header:
        print("-------balance--------")
    print(f"your balance is {money} yuan")

def savings_money(num):
    print("-------savings money--------")
    global money
    money = money+num
    print (f"successfully deposited {num} yuan")

    balance(False)

def withdrawal(num):
    print("-------withdrawal--------")
    global money
    money = money-num
    print (f"successfully withdraw {num} yuan")

    balance(False)
def main():
    print("--------main--------")
    print("query money enter:","1")
    print("save money enter:","2")
    print("withdrawal enter:","3")
    print("quit enter:","4")

while True:
    main()
    keyboard_input = int(input("please enter your choice:"))
    if keyboard_input == 1:
        balance(True)
        continue
    elif keyboard_input == 2:
        num = int(input("enter deposit amount:"))
        savings_money(num)
        continue
    elif keyboard_input == 3:
        num = int(input("enter withdrawal amount:"))
        withdrawal(num)
        continue
    elif keyboard_input == 4:
        print("quit successfully")
        break
    else:
        print("wrong input")


