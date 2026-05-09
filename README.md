# 🎯 Number Guessing Game

A CLI number guessing game written in Python. The computer picks a random number from your chosen range — you have to guess it. Chances are calculated using **binary search math** so you always get the optimal number of guesses.

## How it works

The number of chances you get is calculated as:

```
chances = ceil(log2(range_size))
```

This means if the range is 1–100, you get 7 chances — the exact number needed to find any number using binary search. No more, no less.

## Demo

```
Enter range yourself or let me choose? [Y = me]: n
Start: 1
End: 100
Guessing between 1 and 100.

Your guess: 50
Try HIGHER. 6 chances left.

Your guess: 75
Try LOWER. 5 chances left.

Your guess: 62
Try HIGHER. 4 chances left.

Your guess: 68
You got it! 🎉

Play again? [Y/N]: n
Thanks for playing. Bye!
```

## Features

- Custom range or auto-generated range
- Optimal chances using binary search math
- Input validation for non-numbers and out-of-range guesses
- Play again without restarting

## Setup

**No dependencies needed — pure Python.**

```bash
# Clone the repo
git clone https://github.com/Hash-PJ/Number-Guessing-Game.git
cd Number-Guessing-Game

# Run the game
python user_guesses.py
```

Requires Python 3.10+

## Project structure

```
Number-Guessing-Game/
├── main.py   ← game logic
├── .gitignore
└── README.md
```

## License

MIT
