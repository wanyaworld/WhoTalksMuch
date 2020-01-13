#-*-coding:utf-8

def f2(x):
    return x[1]

chat_file_name="2020.txt"
f = open(chat_file_name, "r");

lines = f.readlines()
mymap = {};
for line in lines:
    if line[0] != '[':
        continue;
    name = line.split('[')[1].split(']')[0]
    if name in mymap:
        mymap[name] += 1;
    else:
        mymap[name] = 0;

res = sorted(mymap.items(), key=f2, reverse=True)
#for e in res:
#    print e
for e in res:
    print e[0]
