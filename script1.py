print('''let's open a file''')
with open('file.csv') as table:
    s=table.readlines()
    ns=[]
    for l in s:
        ns.append(l.replace('\n',','))

for i in range(3,len(ns),4):
    ns[i]=ns[i].replace(',','\n')

with open('out.csv',mode='w')  as targ:
    for item in ns:
        targ.write(item)