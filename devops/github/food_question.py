#!/usr/bin/env python3

# Dictionary to keep track of food likes
counter = {}

# Open up the favorite foods log and count frequencies using the dictionary
with open("favorite_foods.log", "r") as f:
    for line in f:
        item = line.strip()
        if item not in counter:
            counter[item] = 1
        else:
            counter[item] += 1

# Print out all the available liked foods
print("Select your favorite food below:")
for item in counter:
    print(item)

# Ask which food is the user's favorite
answer = input("Which of the foods above is your favorite? ")
answer = answer.lower()

# Print out how many others like the user's favorite food, otherwise say it can't be found
try:
    print("{} of your friends like {} as well!".format(counter[answer], answer))
    exit(0)
except KeyError:
    print("Hmm we couldn't find anyone who also likes \"{}\".".format(answer))
    print("Did you enter one of the foods listed above?")
    exit(0)

"""
In this section, we'll fix the script food_question.py, which displayed an error when executing it. You can run the file again to view the error.

./food_question.py

Output:

5079d715c2f97126.png

This script gives us the error: "NameError: name 'item' is not defined" but your colleague says that the file was running fine before the most recent commit they did.

In this case, we'll revert back the previous commit.

For this, check the git log history so that you can revert back to the commit where it was working fine.

git log

Output:

e89b58d398338a9d.png

Here, you'll see the commits in reverse chronological order and find the commit having "Rename item variable to food_item" as a commit message. Make sure to note the commit ID for this particular commit.

Enter q to exit.

To revert, use the following command:

git revert [commit-ID]

Replace [commit-ID] with the commit ID you noted earlier.

This creates a new commit again. You can continue with the default commit message on the screen or add your own commit message.

Then continue by clicking Ctrl-o, the Enter key, and Ctrl-x.

Now, run food_question.py again and verify that it's working as intended.

./food_question.py

Output:

cedea93d17157044.png

Merge operation

Before merging the branch improve-output, switch to the master branch from the current branch improve-output branch using the command below:

git checkout master

Merge the branch improve-output into the master branch.

git merge improve-output

Output:

f1ea7fd1a1500f03.png

Now, all your changes made in the improve-output branch are on the master branch.

./food_question.py

Output:

5216220ceb4627f1.png

To get the status from the master branch, use the command below:

git status

Output:

c18b4c4d4dd08623.png

To track the git commit logs, use the following command:

git log

Output:

b78661eaf4c93cf1.png


"""