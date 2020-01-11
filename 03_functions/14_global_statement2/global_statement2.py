# Program name: global_statement2.py

"""Four rules to tell wheter a variable is in local scope or global scope:
   
   1. If the variable is being used in the global scope (that is outside
      of all functions), then is always a global variable.
    
   2. If there is a global statement for that variable in a function, it
      is a global variable.

   3. Otherwise, if the variable is used in an assignment statement in the
      function, is local variable.
      
   4. But if the variable is not used in an assignment statement, it is 
      a global variable.
      
   Rules extracted from the book 'Automate the Boring Stuff with Python' by 
   Al Sweigart."""

def spam():
    global eggs
    eggs = 'spam' # This is the global

def bacon():
    eggs = 'bacon' # This is a local

def ham():
    print(eggs) # This is the global

eggs = 42 # This is the global
spam()
print(eggs)