# Create a program using maths and f-Strings that tells us how many days, weeks, months 
# we have left if we live until 90 years old.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

new_age = int(age)

days_left = int((90 - new_age) * 365)
weeks_left = int((90 - new_age) * 52)
months_left = int((90 - new_age) * 12)

message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message)