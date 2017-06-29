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
    out = ''

#    print((light_x, light_y, initial_tx, initial_ty, E, N), file=sys.stderr) for debugging


    if N < 0:
        out += 'N'
        initial_ty -= 1
    elif N > 0:
        out += 'S'
        initial_ty += 1

    if E > 0:
        out += 'E'
        initial_tx += 1
    elif E < 0:
        out += 'W'
        initial_tx -= 1


    print(out)

# To debug: print("Debug messages...", file=sys.stderr)

# A single line providing the move to be made: N NE E SE S SW W or NW

#print(light_x, light_y, initial_tx, initial_ty)
