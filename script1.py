print('''let's open a file''')
with open('file.csv') as table:
    s=table.readlines()
    print(s)