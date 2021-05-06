from time import sleep
from os import name, system
import random

n, m = 10, 10

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def print_grand(grand):
    for i in range(len(grand)):
        for j in range(len(grand[0])):
            print(grand[i][j],end=' ')
        print()


def check(grand):
    n = len(grand)
    m = len(grand[0])
    grand_out = [[ ' ' for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            neighbors = 0
            if i > 0:
                if grand[i-1][j] == '*':
                    neighbors += 1
                if j > 0 and grand[i-1][j-1] == '*':
                    neighbors += 1
                if j < m-1 and grand[i-1][j+1] == '*':
                    neighbors += 1

            if j > 0 and grand[i][j-1] == '*':
                neighbors += 1
            if j < m-1 and grand[i][j+1] == '*':
                neighbors += 1
            
            if i < n-1:
                if grand[i+1][j] == '*':
                    neighbors += 1
                if j > 0 and grand[i+1][j-1] == '*':
                    neighbors += 1
                if j < m-1 and grand[i+1][j+1] == '*':
                    neighbors += 1
            
            if grand[i][j] == '*':
                if neighbors == 2 or neighbors == 3:
                    grand_out[i][j] = '*'
            elif neighbors == 3:
                grand_out[i][j] = '*'

    return grand_out

grand = []
random.seed()
for i in range(n):
    temp = []
    for j in range(m):
        if random.randint(0,1) == 1:
            temp.append('*')
        else:
            temp.append(' ')
    grand.append(temp)


while True:
    clear_screen()
    print_grand(grand)
    grand = check(grand)
    sleep(0.2)
