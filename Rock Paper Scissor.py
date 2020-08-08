import random
import time
print('''Hello welcome to Rock Paper Scissors\n
In this game you will play with a Bot.''')
win = 0
loss = 0
draw = 0
comp_throw = 0

def options():
    print('\nPress the keys accordingly:\nPress 1 for Rock.\nPress 2 for Paper.\nPress 3 for Scissors.\nPress Q for quitting.\nPress O for viewing options again.')


options()
while(True):
   
    inp = input('Enter your choice\n')
    comp = random.randint(1,3)
    if(inp == '1'):
        if (comp == 1):
            print('You threw Rock. Bot threw Rock. Game Draw.')
            draw += 1
        elif (comp == 2):
            print('You threw Rock. Bot threw Paper. You lose.')
            loss += 1
        else:
            print('You threw Rock. Bot threw Scissor. You win.')
            win += 1
        time.sleep(2)
            
    elif(inp == '2'):
        if (comp == 1):
            print('You threw Paper. Bot threw Rock. You win.')
            win += 1
        elif (comp == 2):
            print('You threw Paper. Bot threw Paper. Game draw.')
            draw += 1
        else:
            print('You threw Paper. Bot threw Scissor. You lose.')
            loss += 1
        time.sleep(2)

    elif(inp == '3'):
        if (comp == 1):
            print('You threw Scissor. Bot threw Rock. You lose.')
            loss += 1
        elif (comp == 2):
            print('You threw Scissor. Bot threw Paper. You win.')
            win += 1
        else:
            print('You threw Scissor. Bot threw Scissor. Game draw.')
            draw += 1
        time.sleep(2)


    elif(inp.upper() == 'Q'):
        print('You quit. Game Over')
        print('Total score is:\nWin = ',win,' Loss = ',loss,' Draw = ',draw)
        time.sleep(3)
        exit()


    elif(inp.upper() == 'O'):
        options()


    else:
        print('Are you dumb?? Enter a valid choice')
        
        
    



            
