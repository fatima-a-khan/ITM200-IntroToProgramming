#invman.py
#Fatima Khan 500766544

def rdfile(file):
    open_file = open(file, 'r')
    content = list()
    for line in open_file:
        nbr = str(line)
        content.append(nbr)
    open_file.close()
    return content

def invalue(list):
    sum = 0

    for item in list:
        itemList = item.split(',')
        sum = sum + (float(itemList[2])*float(itemList[1]))
    return sum

def modify(list,command):
    command2 = command.split(' ')
    for i in range(len(list)):
        list2 = list[i].split(', ')
        if list[i].startswith(command2[1]):
            list2[2] = command2[2]
            list[i] = list2[0] + ", " + list2[1] + ', ' + list2[2]

def refresh(list,command):
    command2 = command.split(' ')
    bool = 1
    for i in range(len(list)):
        list2 = list[i].split(', ')
        if list[i].startswith(command2[1]):
            bool = 0
            list2[2] = command2[3]
            list2[1] = str(int(command2[2])+int(list2[1]))
            list[i] = list2[0] + ", " + list2[1] + ', ' + list2[2]
    if bool == 1:
            list.append(command2[1] + ", " + command2[2] + ', ' + command2[3])

def wrfile(file, list):
    with open(file, 'w') as text:
        for item in list:
            text.write(item)

#TODO
records = rdfile('inventory.txt')
cmds = rdfile('commands.txt')

print('Before update')
print('Inventory value: $'+str(invalue(records)))
print(records)

for cmd in cmds:
    if cmd.startswith('modify'):
        modify(records,cmd)
    elif cmd.startswith('refresh'):
        refresh(records,cmd)
    else:
        continue
wrfile('inventory.txt',records)

print('\nAfter update')
print('Inventory value: $'+str(invalue(records)))
print(records)