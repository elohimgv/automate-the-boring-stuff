# Terminate a program by using exit from module 'sys'
# Program name: exit_example.py

# Import module (librarie) sys
import sys 
while True:
    print("Type exit to exit.")
    response = input()
    if response == 'exit':
        sys.exit()
    print("You typed " + response + ".")


