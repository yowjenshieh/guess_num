import random
number = random.randint(1, 100)
attempts = 0

def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return str(n) + suffix

while True:
    num = input('Guess a number from 1 to 100:')
    num = int(num)
    attempts += 1
    attempt_ordinal = ordinal(attempts)
    if num == number:
        print('Congrats! You got it!')
        break
    elif num < number:
        print("Too low! That's your", attempt_ordinal, "attempt.")
    else:
        print("Too high! That's your", attempt_ordinal, "attempt.")