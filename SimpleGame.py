import os
secret = 0
R = 0
O = 0
Y = 0
G = 0
B = 0
V = 0
Room = 0
win = 0
while (win == 0):
    print("choose another room \n1: Red\n2: Orange\n3: Yellow\n4: Green\n5: Blue\n6: Violet")
    Room = int(input())
    os.system('cls')
    if (Room == 0 and secret == 0):
        print("you are in the gray room dude.\nnothing to collect here. move along.")
    if (Room == 0 and secret != 0):
        print("i can't believe it!\nthe gray room is transforming back to it's original state!!!\nit's finally become the rainbow room again!!!\nthank you for all of your help, happy travels adventurer!")
        win = 1
    if (Room == 1):
        if (R == 1):
            print("why did you come back here...? you already got this artifact!")
        if (R == 0):
            tempIn = ''
            print("welcome to ready red room\nthere's a cool crystal that's red wanna collect it?\n(Y/N)")
            tempIn = input()
            if (tempIn == 'Y'):
                R = 1
    if (Room == 2):
        if (O == 1):
            print("why did you come back here...? you already got this artifact!")
        if (O == 0):
            tempIn = ''
            print("welcome to origami orange room\nthere's a cool crystal that's orange wanna collect it?\n(Y/N)")
            tempIn = input()
            if (tempIn == 'Y'):
                O = 1
    if (Room == 3):
        if (Y == 1):
            print("why did you come back here...? you already got this artifact!")
        if (Y == 0):
            tempIn = ''
            print("welcome to yelling yellow room\nthere's a cool crystal that's yellow wanna collect it?\n(Y/N)")
            tempIn = input()
            if (tempIn == 'Y'):
                Y = 1
    if (Room == 4):
        if (G == 1):
            print("why did you come back here...? you already got this artifact!")
        if (G == 0):
            tempIn = ''
            print("welcome to grassy green room\nthere's a cool crystal that's green wanna collect it?\n(Y/N)")
            tempIn = input()
            if (tempIn == 'Y'):
                G = 1
    if (Room == 5):
        if (B == 1):
            print("why did you come back here...? you already got this artifact!")
        if (B == 0):
            tempIn = ''
            print("welcome to blooming blue room\nthere's a cool crystal that's blue wanna collect it?\n(Y/N)")
            tempIn = input()
            if (tempIn == 'Y'):
                B = 1
    if (Room == 6):
        if (V == 1):
            print("why did you come back here...? you already got this artifact!")
        if (V == 0):
            tempIn = ''
            print("welcome to violent violet room\nthere's a cool crystal that's violet wanna collect it?\n(Y/N)")
            tempIn = input()
            if (tempIn == 'Y'):
                V = 1
    if (R == 1 and O == 1 and Y == 1 and G == 1 and B == 1 and V == 1 and secret == 0):
        os.system('cls')
        print("i can't believe it... you actually unified them all...\ncome to the gray room by selecting 0! we must restore the color!")
        secret = 1
        input("press enter to continue...")
input("press enter to continue...")
os.system('cls')
print("thanks for playing the game, i hope you enjoyed this little demo :)")

        