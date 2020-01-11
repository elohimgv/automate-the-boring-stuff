# How to import modules
# Program name: print_random.py

# Import module (librarie) random
import random
for i in range(5):
    print(random.randint(1, 10))

print()

# Other form to import modules
from random import randint
for i in range(5):
    print(randint(1, 10))