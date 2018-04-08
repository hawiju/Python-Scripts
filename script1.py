print('''let's open a file''')
import sys
columns=4
fil='file.csv'
if len(sys.argv) ==2 :
    columns=int(sys.argv[1])
elif len(sys.argv)>2:
    fil=sys.argv[1]
    columns=int(sys.argv[2])

with open('file.csv') as table:
    s=table.readlines()
    ns=[]
    for l in s:
        ns.append(l.replace('\n',','))
for i in range(columns-1,len(ns),columns):
    ns[i]=ns[i].replace(',','\n')

with open('out.csv',mode='w')  as targ:
    for item in ns:
        targ.write(item)