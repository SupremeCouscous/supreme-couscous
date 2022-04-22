FILE1 = "./data/demo93.output"
outputFile1 = open(FILE1, 'w')
linesToWrite = ["write something first\n", " add something next\n"]
outputFile1.writelines(linesToWrite)
outputFile1.close()

for i in range(0, 10):
    outputFile1 = open(FILE1, 'a')
    nextLine = [f'[{i}] add something extra\n']
    outputFile1.writelines(nextLine)
    outputFile1.close()