guess = 1
NUMBER = 45


while True:
    num = input("Please guess the number (between 0-100)")
    try:
        num = int(num)
    except:
        print("Invalid number, please guess again.")
        continue

    if num < NUMBER:
        print("You guess was under")
    elif num > NUMBER:
        print("You guess was over.")
    else:
        break
    guess += 1

print("Done")

