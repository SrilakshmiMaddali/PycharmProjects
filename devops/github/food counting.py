#!/usr/bin/env python3

# Dictionary to keep track of food likes
counter = {}

# Open up the favorite foods log and add it to the dictionary
with open("favorite_foods.log", "r") as f:
    for i in f:

        #print("before "+i)
        #i=i.strip()
        i = i[:-1]
        #print("after "+i)
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1

# Sorts the liked foods in descending order
sort_foods = sorted(counter.items(), key = lambda x : x[1], reverse = True)
print("Favourite foods, from most popular to least popular")
# Prints out the liked foods
for i in range(len(sort_foods)):
    print("{}, {}".format(sort_foods[i][0], sort_foods[i][1]))

"""
There is a Git repository named food-scripts consisting of a couple of food-related Python scripts.

Navigate to the repository using the following command:

cd ~/food-scripts

Now, list the files using the ls command. There are three files named favorite_foods.log, food_count.py, and food_question.py.

75dd0326f2eee979.png

Let's explore each file. Use the cat command to view each file.

favorite_foods.log: This file consists of a list of food items. You can view it using the following command:

cat favorite_foods.log

Output:

47403089d228e2c1.png

food_count.py: This script returns a list of each food and the number of times the food appeared in the favorite_foods.log file.
Let's execute the script food_count.py:

./food_count.py

Output:

1c36a02d5ebaef5d.png

food_question.py: This prints a list of foods and prompts the user to enter one of those foods as their favorite. It then returns an answer of how many others in the list like that same food.
Run the following command to see the output of food_question.py script:

./food_question.py

Output:

5079d715c2f97126.png

Uh oh , this gives us an error. One of your colleagues reports that this script was working fine until the most recent commit. We'll be fixing this error later during the lab.

Understanding the repository

Let's use the following Git operations to understand the workflow of the repository:

git status
git log
git branch
Git status: This displays paths that have differences between the index file and the current HEAD commit; paths that have differences between the working tree and the index file; and paths in the working tree that are not tracked by Git. You can view the status of the working tree using the command: [git status]

git status

You can now view the status of the working tree.

Git log: This lists the commits done in the repository in reverse chronological order; that is, the most recent commits show up first. This command lists each commit with its SHA-1 checksum, the author's name and email, date, and the commit message.

You can see logs by using the following command:

git log

Output:

37aaa3162a88b121.png

Enter q to exit.

Git branch: Branches are a part of the everyday development process on the master branch. Git branches effectively function as a pointer to a snapshot of your changes. When you want to add a new feature or fix a bug, no matter how big or small, you spawn a new branch to encapsulate your changes. This makes it difficult for unstable code to get merged into the main codebase.

Configure Git

Before we move forward with the lab, let's configure Git. Git uses a username to associate commits with an identity. It does this by using the git config command. Set the Git username with the following command:

git config user.name "Name"

Replace Name with your name. Any future commits you push to GitHub from the command line will now be represented by this name. You can even use git config to change the name associated with your Git commits. This will only affect future commits and won't change the name used for past commits.

Let's set your email address to associate them with your Git commits.

git config user.email "user@example.com"

Replace user@example.com with your email-id. Any future commits you now push to GitHub will be associated with this email address. You can also use git config to change the user email associated with your Git commits.

Add a new feature

In this section, we'll be modifying the repository to add a new feature, without affecting the current iteration. This new feature is designed to improve the food count (from the file food_count.py) output. So, create a branch named improve-output using the following command:

git branch improve-output

Move to the improve-output branch from the master branch.

git checkout improve-output

Here, you can modify the script file without disturbing the existing code. Once modified and tested, you can update the master branch with a working code.

Now, open food_count.py in the nano editor using the following command:

nano food_count.py

Add the line below before printing for loop in the food_count.py script:

print("Favourite foods, from most popular to least popular")

Save the file by pressing Ctrl-o, the Enter key, and Ctrl-x. Then run the script food_count.py again to see the output:

./food_count.py

Output:

food_count_output.png

After running the food_count.py script successfully, commit the changes from the improve-output branch by adding this script to the staging area using the following command:

git add food_count.py

Now, commit the changes you've done in the improve-output branch.

git commit -m "Adding a line in the output describing the utility of food_count.py script"

Output:

12899198fa08815f.png

Click Check my progress to verify the objective.
"""