class GuessNumber:
    def __init__(self, number, min=0, max=100) -> None:
        super().__init__()
        self.number = number
        self.guesses = 0
        self.min = min
        self.max = max

    def get_guess(self):
        guess = input("Please guess the number (between 0-100)")

        if self.valid_number(guess):
            return int(guess)
        print("Please enter a valid number.")
        return self.get_guess()

    def valid_number(self, str_number):
        # return False or True
        # check the condition 1
        try:
            # convert string to number
            # alphabet > cause the error
            number = int(str_number)
        except:
            # go to this one
            return False
        # check the condition 2
        return self.min < number < self.max

    def play(self):
        while True:
            self.guesses += 1

            guess = self.get_guess()

            print("Guess")

            if guess < self.number:
                print("You guess was under")
            elif guess > self.number:
                print("You guess was over.")
            else:
                break
        print("Done")


game = GuessNumber(25, 4, 100)
game.play()
