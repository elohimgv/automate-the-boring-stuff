# Practice for loop statement 

print("My name is")
for i in range(5):
    print('Jimmy Five Times (' + str(i) +')')
    
# You can even use a negative number for the step 
# argument to make the for loop count down instead
# of up.
for i in range(5, -1, -1):
    print(i)

# Other form to obtain the same result with 
# a while loop
"""print("My name is")
i = 0
while i < 5:
    print("Jimmy Five times ("+ str(i) +")")
    i = i + 1"""
