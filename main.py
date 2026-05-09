from random import randint, sample
from math import log2, ceil


class NumberGame:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self._answer = randint(start, end)
        self._chances = ceil(log2(abs(end - start)))
        # log2 gives max guesses needed using binary search strategy

    def guess(self, num: int) -> tuple[str, bool]:
        """Returns (message, keep_playing)."""
        if num == self._answer:
            return "Wow! You nailed it! 🎉", False

        self._chances -= 1

        if self._chances == 0:
            return f"YOU LOST! The number was {self._answer}.", False

        hint = "LOWER" if num > self._answer else "HIGHER"
        return f"TRY AGAIN! Number is a bit {hint} than {num}. You have {self._chances} chances left...", True


def play_round():
    while True:
        try:
            choice = input("Do you want to select the range or shall i choose for you? [Y = me]: ").lower()
            if choice == 'y':
                start, end = sorted(sample(range(0, 10000), 2))
            else:
                start = int(input("Start: "))
                end = int(input("End: "))

            if abs(end - start) < 4:
                print("Range too small, Lets try again!")
                continue

            print(f"Guessing between {start} and {end}.")
            break

        except ValueError:
            print("Numbers only please.")

    game = NumberGame(start, end)
    playing = True

    while playing:
        try:
            num = int(input("Your guess: "))
        except ValueError:
            print("Enter a valid number.")
            continue

        if not (start <= num <= end):
            print(f"Guessing out of the range, huh? Try within {start}–{end}!")
            continue

        message, playing = game.guess(num)
        print(message)


if __name__ == "__main__":
    while True:
        play_round()
        again = input("Wanna play again? [Y/N]: ").upper()
        if again != 'Y':
            break
    print("Thanks for playing. BYE!")
