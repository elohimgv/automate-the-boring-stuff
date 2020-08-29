# collatz function
def collatz(number):
    if (number % 2) == 0:
        print(number // 2)
        return number // 2
    else: 
        print(3 * number + 1)
        return 3 * number + 1

print('Enter number')
try:
    number = input()
    number = int(number)
except ValueError:
    print('Please enter an integer.')
    number = input()
    number = int(number)
            
# Calling collatz function
collatz(number)
