import random
import numpy as np
from datetime import datetime

num_places = 1000000000
min_i = 0
max_i= num_places - 1
space = np.zeros(num_places, dtype=np.int32)
frog_start = int(num_places / 2)
frog = frog_start
space[frog] = 1
all_visited = False

def getnow():
    now = datetime.now()

    return now.strftime("%m/%d/%Y %I:%M:%S %p")

def random_move():
    global frog
    move = random.choice([-1, 1])
    new_frog = frog + move
    if min_i <= new_frog and max_i >= new_frog: 
        frog = new_frog
    
    if space[frog] == 0:
        print(f'New space found! Time: {getnow()} Location: {frog}')

    space[frog] = 1

def check_done():
    global frog
    global frog_start
    global all_visited
    if not all_visited:
        for i in range(len(space)):
            if space[i] != 1:
                return False 
    
    if not all_visited:
        all_visited = True
        print(f'All locations have been visited!!! Waiting to return back to the start... Time: {getnow()}')
    
    if not frog == frog_start:
        return False

    return True


started = getnow()
print(f'time started: {started}')
while not check_done():
    # time.sleep(0.001)
    random_move()
ended = getnow()
print(f'time started {started}')
print(f'time ended {ended}')
