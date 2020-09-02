# Import module re
import re

# Creating regex object
namesRegex = re.compile(r'Agent \w+')
txtNames = "Agent Alice gave the secret documents to Agent Bob."
# Matching object, replace and print 
print(namesRegex.sub('CENSORED', txtNames))

# Creating regex object
agentNamesRegex = re.compile(r'Agent (\w)\w*')
txtAgentNames = "Agent Alice told Agent Carol that Agent Eve knew AgentBob was a double agent." 
# Matching object, replace and print
print(agentNamesRegex.sub(r'\1****', txtAgentNames))
