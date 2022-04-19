inputs = list()
message = "write something from user:"

while (current := input(message)) != "quit":
    inputs.append(current)
print(inputs)