#######################################
# Project Name - Tic Tac Toe Game
# print (type(projectn))
# Developed by : Vinay Singh
# Date - 5/14/17
import sys
import os
import logging
import webbrowser
import datetime
import re
projectn = 'Tic Tac Toe Game'
#######################################
# print(webbrowser._browsers)
# global variable init
ttt_board = dict.fromkeys(["tl", "tm", "tr", "ml", "mm", "mr", "ll", "lm", "lr"], " ")
player = None
avail_key = ''
continue_playing = True
#####################
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Tic Tac Toe Program Started')
now = datetime.datetime.now()
# print (now)
print("Welcome to : {} . Today's is {:%m/%d/%Y}. ".format(projectn, now ))
pwd=input('Your password ( Hint : is your Birth Year):')
while re.match(r'^\d+$',pwd)==None :
    print('Please enter numeric year')
    pwd = input('Your password ( Hint : is your Birth Year):')
    re.compile(r'asds',)



def clear():
    os.system('cls')


def print_ttt_board():
    print(ttt_board['tl'] + ' | ' + ttt_board['tm'] + ' | ' + ttt_board['tr'])
    print('---------')
    print(ttt_board['ml'] + ' | ' + ttt_board['mm'] + ' | ' + ttt_board['mr'])
    print('---------')
    print(ttt_board['ll'] + ' | ' + ttt_board['lm'] + ' | ' + ttt_board['lr'])

# print (type(print_ttt_board))


def get_player(p):
    if p == None:
        return 'X'
    elif p == 'X':
        return 'O'
    else:
        return 'X'


def avail_option():
    global avail_key
    if avail_key=='':
        for bkey in ttt_board.keys():
           avail_key += bkey
           avail_key += ' '
    else:
        pass
    return avail_key


def get_input():
    global ttt_board
    global avail_key
    valid_input = False
    while valid_input == False:
        gi = input()
        if avail_key.find(gi) == -1:
            print('Invalid Entry. Please try again')
        else:
            print( 'Your Entered ' + gi)
            valid_input = True
    # print ( 'before ' + avail_key)
    avail_key = avail_key.replace(gi,'')
    # print('after ' + avail_key)
    return gi


def ttt_eval():
    done_flag = False
    eval_list = [ ttt_board['tl'] + ttt_board['tm'] + ttt_board['tr'],
                  ttt_board['ml'] + ttt_board['mm'] + ttt_board['mr'],
                  ttt_board['ll'] + ttt_board['lm'] + ttt_board['lr'],
                  ttt_board['tl'] + ttt_board['ml'] + ttt_board['ll'],
                  ttt_board['tm'] + ttt_board['mm'] + ttt_board['lm'],
                  ttt_board['tr'] + ttt_board['mr'] + ttt_board['lr'],
                  ttt_board['tl'] + ttt_board['mm'] + ttt_board['lr'],
                  ttt_board['tr'] + ttt_board['mm'] + ttt_board['ll']]
    # print ('eval list ' + str(eval_list))
    for el in eval_list:
        if el == 'XXX' or el == 'OOO':
            print ("Player " + el[0] + ' won !!!!')
            done_flag = True
            break
    return done_flag


webbrowser.get(using=None).open('https://www.google.com')
#####################################################
# Starting point of Game
####################################################
while continue_playing == True:
    for i in range(9):
        clear()
        print_ttt_board()
        player = get_player(player)
        print('Player ' + player + ' turn\'s')
        print('Your options are ' + avail_option())
        print('Enter your option now ')
        ttt_board[get_input()] = player
        clear()
        print_ttt_board()
        if ttt_eval() == True :
            break
    if ttt_eval ==False: print("Its a draw!!")
    print ("You would like to play another game? Y/N")
    if 'Y' == input().upper().startswith('Y'):
        continue_playing = True
        ttt_board = {"tl": " ", "tm": " ", "tr": " ", "ml": " ", "mm": " ", "mr": " ", "ll": " ", "lm": " ", "lr": " "}
        player = None
        avail_key = ''
    else:
        continue_playing = False
print("Thanks for playing!! Come Back Soon!")
logging.debug('Tic Tac Toe Program Ended')
sys.exit(0)
