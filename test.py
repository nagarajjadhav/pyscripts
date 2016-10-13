'''def swap1(p,q):
    p,q = q,p
    print("after swap in function",p,q)
    print("global value of a and b",a,b)
a=2
b=3
print("before swap",a,b)
swap1(a,b)
print("after swap in main",a,b)'''

#******************************************************************

'''def collatz(number):
    if number%2==0:
        return number//2
    else:
        return 3*number+1
try:
    i = int(input("enter the number :"))
except ValueError:
    print("input should be an integer")
while True:
    if i==1:
        break
    else:
        i=collatz(i)
        print(i)'''

#******************************************************************

'''def conver(lst):
    str1 = ''
    for i in range(len(lst)):
        if i == len(lst)-1:
            str1 += 'and'+' '+lst[i]+'.'
            break
        str1 += lst[i]+','+' '
    print(str1)
lst1 = ['cat','dog','bruno','soda','nirmala']
conver(lst1)'''

#*****************************************************************

'''grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
for i in range(6):
    for j in range(len(grid)):
        print(grid[j][i],end='')
    print(end='\n')'''

#******************************************************************
#tprogram to count the number of occurancs of each character in a long mess
'''from pprint import pprint,pformat
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(pformat(count))'''

#******************************* TIC TAC TOE **************************

'''theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def check(b,t):
    if (b.get('top-L')==t and b.get('top-M')==t and b.get('top-R')==t):
        return 'game won by ',t
    elif (b.get('mid-L')==t and b.get('mid-M')==t and b.get('mid-R')==t):
        return 'game won by ',t 
    elif (b.get('low-L')==t and b.get('low-M')==t and b.get('low-R')==t):
        return 'game won by ',t 
    elif (b.get('top-L')==t and b.get('mid-L')==t and b.get('low-L')==t):
        return 'game won by ',t 
    elif (b.get('top-M')==t and b.get('mid-M')==t and b.get('low-m')==t):
        return 'game won by ',t 
    elif (b.get('top-R')==t and b.get('mid-R')==t and b.get('low-R')==t):
        return 'game won by ',t
    elif (b.get('top-L')==t and b.get('mid-M')==t and b.get('low-R')==t):
        return 'game won by ',t
    elif (b.get('top-R')==t and b.get('mid-M')==t and b.get('low-L')==t):
        return 'game won by ',t
    

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def moves():
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        theBoard[move] = turn
        res = check(theBoard,turn)
        if res:
            print(res)
            printBoard(theBoard)
            return 1
        
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    return

res = moves()
if res == None:
    printBoard(theBoard)
    print("game got draw between two")'''

#******************************* INVENTORY **************************

'''def addToInventory(inventory, addedItems):
    for i in addedItems:
       
        if i not in inventory:
            inventory.setdefault(i,0)
            inventory[i] = inventory[i]+1
        else:
            inventory[i] = inventory[i]+1
    return inventory


def displayInventory(inventory):
    print("Inventory: \n")
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
        
    print("\nTotal number of items: " + str(item_total))

        
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby','gold coin']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)'''



'''import re
pat = re.compile(r'^(?=.{8,}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).*')
mo = pat.search('naGAraja1')
print(mo.group())'''

f = open('content.txt','w')
f.write('hello world!')
f.close()
f = open('content.txt')
a=f.read()
f.close()
print(a)
f= open('content.txt','a'
































    
            
