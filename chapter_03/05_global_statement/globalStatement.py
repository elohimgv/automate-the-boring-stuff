# When you have a line such as global eggs at the
# top of a function, it tells the Python, 'in this
# function, eggs refers to the global variable,
# so don't create a local variable with this name.'

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
