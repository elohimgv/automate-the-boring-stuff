# This cause an error because we need to declare eggs
# variable before use in print function.

def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'

eggs = 'global'
spam()
