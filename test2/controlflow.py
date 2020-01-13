answer = 8
guess = int(input('Enter a guess'))

if answer>guess:
    result = "Oops!  Your guess was too low."
elif answer<guess:
    result = "Oops!  Your guess was too high."
elif answer==guess:
    result = "Nice!  Your guess matched the answer!"

print(result)