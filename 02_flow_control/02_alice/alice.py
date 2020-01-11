# Practice if, elif statement and else option. 
# Program name: alice.py

name = 'Chayanne'
age = 101

if name == 'Alice':
    print("Hi, Alice.")
elif age < 12 and age > 14:
    print("You are not Alice, kiddo.")
elif age > 100:
    print("Unlike you, Alice is not an undead, immortal vampire.")
elif age > 2000:
    print("You are not Alice, grannie.")
else:
    print("You are neither Alice nor a little kid.") 
