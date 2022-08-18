import random
import time

def task(todo):
    print('Task list...')
    for j in todo:
        print(j,end="  ")

    print('\n\n\n')
    print('You should be ',random.choice(todo),'right now.')

print("Enter your tasks : ")
l = []
i = 1
while(i != ''):
    i = input()
    l.append(i)

l.pop()
task(l)
time.sleep(20)
