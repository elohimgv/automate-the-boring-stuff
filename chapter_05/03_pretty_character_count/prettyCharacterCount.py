# Module pprint
import pprint 
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

# Using .setdefault() method
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# Using pretty printing with lists
pprint.pprint(count)
# To obtain the prettified text as string  value instead
# of displaying it on the screen
#print(pprint.pformat(count))

