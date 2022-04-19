inputs = list()
message = "write something from user:"

while True:
    current = input(message)
    if current == "quit":
        break
    inputs.append(current)
print(inputs)