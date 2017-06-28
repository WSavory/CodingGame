#https://www.codingame.com/ide/puzzle/power-of-thor-episode-1

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop


#E = light_x - initial_tx # positive -> go east, negative -> go west
#N = light_y - initial_ty # positive -> go north, negative -> go south


while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    E = light_x - initial_tx # positive -> go east, negative -> go west
    N = light_y - initial_ty

    if N < 0 and E == 0:
        print('N')
        initial_ty += 1
    elif N > 0 and E == 0:
        print('S')
        initial_ty -= 1
    elif E > 0 and N == 0:
        print('E')
        initial_tx += 1
    elif E < 0 and N == 0:
        print('W') #N : 17-17 , E0 -18
        initial_tx -= 1
    elif N < 0 and E < 0:#N : 17-4 and E : 0-15
        print('NW')
        initial_ty += 1
        initial_tx -= 1
    elif N > 0 and E > 0:
        print('SE')
        initial_ty += 1
        initial_tx += 1
    elif N < 0 and E > 0:
        print('NE')
        initial_ty += 1
        initial_tx += 1
    elif N > 0 and E < 0: # N 17-0 >0 , 0 -31
        print('SW')
        initial_ty += 1
        initial_tx -= 1
    else: pass



# A single line providing the move to be made: N NE E SE S SW W or NW

#print(light_x, light_y, initial_tx, initial_ty)
