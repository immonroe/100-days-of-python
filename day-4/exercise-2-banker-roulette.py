# You are going to write a program that will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 8 splits the string names_string into individual names and puts them inside a 
# List called names. For this to work, you must enter all the names as names followed by 
# comma then space. e.g. name, name, name

# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Get total list # and - 1 so index isn't offset
count = (len(names)) - 1

# Grab random value of index
random_choice = random.randint(0,count)

# choose a random name
random_name = names[random_choice]

# alternate method - random.choice()
# enter "random_name" variable in and you're good to go!
# random_name = random.choice(names)

# print outcome
print(f"{random_name} is going to buy the meal today!")