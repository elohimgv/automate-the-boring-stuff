import random

# Message list
messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook no so good',
    'Very doubtful']

# Why len(messages) - 1, because index account from
# 0 to ... and the value of len(messages) is 9, that
# is correct. But if we have to use the total of 
# index in messages list, we need to substract 1 
# (i.e -1); 0 - 8 index and the length of 9.
print(messages[random.randint(0, len(messages) -1 )])
