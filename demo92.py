PATH1 = "./data/Python_Introduction"
PATH2 = "./data/demo92.clone1"
PATH3 = './data/demo92.clone2'

file1 = open(PATH1, encoding='utf-8')
readme_txt = file1.read()
file1.close()
print(type(readme_txt), len(readme_txt), readme_txt[:20])

with open(PATH1, encoding='utf-8') as file2:
    readme_txt2 = file2.read()
print(type(readme_txt2), len(readme_txt2), readme_txt2[:20])

file2 = open(PATH2, 'w', encoding='utf-8')
file2.write(readme_txt)
file2.close()

with open(PATH3, 'w', encoding='utf-8') as file3:
    file3.write(readme_txt2)