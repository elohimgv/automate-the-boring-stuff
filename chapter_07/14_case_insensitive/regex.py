# Import module re
import re

# Creating regex object
robocop = re.compile(r'robocop', re.I) # re.I - case insensitive
txt1 = "RoboCop is part man, part machine, all cop."
txt2 = "Pepe, why does your programming book talk about robocop so much?"
# Matching object
print(robocop.search(txt1).group())
print(robocop.search(txt2).group())
