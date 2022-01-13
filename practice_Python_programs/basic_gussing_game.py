
def secrectGuessingGame():
    secret_key = "Damn"
    guess = ""
    cnt = 0
    guess_limit = 3
    flag = False

    while guess != secret_key and not(flag):
        if cnt >= guess_limit:
            flag = True
        else:
            guess = input("Enter secret word: ")
            cnt += 1

    if flag:
        print("You have occupied your all chances...\nbetter luck next time")
    else:
        print("You win")

secrectGuessingGame()