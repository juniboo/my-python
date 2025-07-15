import random 
import time
def guess_num_game():
    attempts = 10
    num = random.randint(1,100)
    guesses = []
    print("welcome to guess_num_game!!!")
    print("you have 10 times to guess a num")
    print("------------------------------------")
    for attempt in range(1,attempts+1):
        while True:
            try:
                guess_num = int(input("enter your guess:"))
                if 1<=guess_num<=100:
                    break
                else:
                    print("number out of range!")
            except ValueError:
                print("wrong input!")
        guesses.append(guess_num)
        if   guess_num > num:
            print(f"your guess is higher!,you have {attempts-attempt} times ")
        elif guess_num < num:
            print(f"your guess is lower!,you have {attempts-attempt} times ")
        else:
            print("you are right!!!")
            print(f"your guess recording are {guesses}")
            return
    print(f"sorry,you did not guess right {attempts} times")
    print(f"your guess recording are {guesses}")
if __name__ == "__main__":
    guess_num_game()

    while True:
        play_again = input("play again? (y/n): ")
        if play_again == "y":
            guess_num_game()
        else:
            print("bye")
            time.sleep(2)
            break








           
                 