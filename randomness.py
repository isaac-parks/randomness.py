import random
import time
from datetime import datetime

num_places = 1000000000
min_i = 0
max_i= num_places - 1
space = [0] * num_places
frog = int(num_places / 2)
space[frog] = 1

def random_move():
    global frog
    move = random.choice([-1, 1])
    new_frog = frog + move
    if min_i <= new_frog and max_i >= new_frog: 
        frog = new_frog
    
    if space[frog] == 0:
        print('new space!', frog)

    space[frog] = 1


def check_done():
    for i in space:
        if i != 1:
            return False 

    return True


started = datetime.now()
print(f'time started: {started}')
while not check_done():
    time.sleep(0.001)
    random_move()
ended = datetime.now()
print(f'time started {ended}')
print(f'time ended {ended}')
