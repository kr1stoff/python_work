prompt = "\nTell me something, and I'll repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

"""
while message != 'quit':
    message = input(prompt)
# 不repeat指令quit
    if message != 'quit':
        print(message)
"""

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(message)