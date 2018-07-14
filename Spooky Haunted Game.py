stuff = ["backpack", "pencil", "notebook", "snack", "baseball glove"]
print stuff
print "Here is all the stuff you have with you. You are going on an adventure."


answers = ["", "Enter"]
answer  = None
while answer not in answers:
    answer = raw_input("Press Enter: ")

print("Great!")

print ""

name = raw_input("What is your name? ")
print ""
print "%s is a pretty cool name. My name is %s, too!" %(name, name)

print ""

enter_second = raw_input("Hmm do you think you really need to take a baseball glove with you? Enter Y or N: ")
if enter_second == "Y":
    print "I disagree, let\'s toss that aside."
elif enter_second == "N":
    print "I agree! Let\'s toss that aside."

stuff.remove("baseball glove")
print "Here is what you have left. Let\'s add a flashlight from home:"
stuff.append('flashlight')
print ""
print stuff
print ""

enter_fourth = raw_input("Now let\'s get going! Enter Y or N: ")
if enter_fourth == "Y":
    print "Let\'s go!"
elif enter_fourth == "N":
    print "What, are you s c a r e d ? HA! Let\'s go!"

print ". . ."
print ""
print ". . ."
print ""
print "Let\'s enter this creepy old house. I think it\'s abandoned! What fun!"
print ""


while 1:

    answer = raw_input("Do you want to go into the basement? ")

    if answer == "N" or answer == "NO" or answer == "No": #assuming this is the right answer
        print("OK! Let\'s move on.")
        break
    elif answer == "Y" or answer == "Yes" or answer == "YES":
        print("You're dead! G A M E  O V E R")

    elif answer == "ya" or answer == "Ya":
        print("Y O U  D I E D")
    elif answer == "nah" or answer == "NAH":
        print("Good call, let\'s shut this door.")

    else:
        print("I'm sorry, that won't work. Try again!")


print ""
enter_tenth = raw_input("Do you think there are ghosts in here? Enter Y or N: ")
if enter_tenth == "Y":
    print "Y-Yes, I bet there are... I hope we see one"
elif enter_tenth == "N":
    print "I've seen one before..."

print ""

enter_eleventh = raw_input("WATCH OUT! There\'s one behind you! Enter LOOK or DON\'T LOOK: ")
if enter_eleventh == "LOOK":
    print "You see a shape move quickly through a doorway....."
elif enter_eleventh == "DON\'T LOOK":
    print "I swear I\'m not lying..."

print ""
print "      /\__/\ "
print "_____( ` 0 `)____ "
print "Vvvvvv  ^ ^ vvvvV"
print ""

enter_fifth = raw_input("I think there's a kitchen over here. Do you want to each the snack you brought? Enter Y or N: ")
if enter_fifth == "Y":
    print "Yum! Strength!"
else:
    print "Ok! Strength for later!"

print ""
enter_sixth = raw_input("I hear a meow. Should we investigate? I love cats! Enter Y or N: ")
if enter_sixth == "Y":
    print "Ouch! It scratched you!"
else:
    print "Hmm ya, it might have bitten you."

print ""
print "    /\__/\ "
print "   / \  / \ "
print " === 0  0 === "
print "   \  --  / "
print "  /        \ "
print " /          \ "
print "|            | "
print " \  ||  ||  / "
print "  \_oo__oo_/#######o "

print ""
print "I hear something! Something big is heading this way! What do you do?!"
print ""
print ""

while 1:

    answer = raw_input("Which way do you run? Enter LEFT, RIGHT, STRAIGHT, or BACK: ")

    if answer == "LEFT" or answer == "left": # the right answer
        print("Whew, you're safe!")
        break
    elif answer == "RIGHT" or answer == "right":
        print("It\'s grabbing you! AHHHHH! Where next?!")

    elif answer == "STRAIGHT" or answer == "straight":
        print("Y O U  D I E D")
    elif answer == "BACK" or answer == "back":
        print("You tripped and fell, where next?!")

    else:
        print("I'm sorry, that won't work. Try again!")

print ""
print "... this is spooky"
print ""
print "OMG! A ghost appeared!!!!"

enter_ninth = raw_input("Do you stay to chat or run away? Enter STAY or RUN: ")
if enter_ninth == "STAY":
    print "But IT\'S A GHOST!!!!!!!!!!!!"
else:
    print "It cut you off! You\'re trapped!"

print ""
enter_seventh = raw_input("Heeellloooooooo. To liiveee, youuu musttt plaayyy my ggaaaameeee. Enter Y or N: ")
if enter_seventh == "Y":
    print "Gooood choooiiceeee"
else:
    print "Tooo baaddddd. Play or dieeee!"
print ""
print "You must guesss the placceeee where my bones are burrieeddd"

# here I'm importing a battleship game from Code Academy
# but how can I add one more guess?

from random import randint

def init_board(board):
    for i in range(0,2):
        board_row = []
        for br in range(0,2):
            board_row.append("O")
        #
        board.append(board_row)
    #
    return board
#

def position_ship(board):
    ship_r = randint(0,len(board)-1)
    ship_c = randint(0,len(board)-1)
    return [ship_r,ship_c]
#

def guess_position(board,ship_pos):
    print_board(board)
    guess = get_input(board)
    guess_row = guess[0]
    guess_col = guess[1]
    ship_row = ship_pos[0]
    ship_col = ship_pos[1]
    # mark our position
    board[guess_row][guess_col]="X"
    # check if guess is correct or not and return
    # 0 if incorrect
    # 1 if correct
    if guess_row==ship_row and guess_col==ship_col:
        return 1
    else:
        return 0
    #
#
def print_board(board):
    for board_row in board:
        print " ".join(board_row)
    #
#
def get_input(board):
    guess_row=0
    guess_col=0
    while(True):
        guess_row = int(raw_input("Guess Row: "))
        guess_col = int(raw_input("Guess Col: "))
        # user will guess from 1-2 so we reduce by 1
        guess_row = guess_row-1
        guess_col = guess_col-1
        if guess_row not in range(2) or guess_col not in range(2):
            print "Oops, outside the playing area!!!"
        elif board[guess_row][guess_col]=="X":
            print "You already guessed this, you fool! Perish!"
        else:
            break

        #
    #
    return [guess_row,guess_col]
#

def play(rounds,board,ship_pos):
    win = 0
    for r in range(rounds):
        print "round %d"%(r+1)
        ok = guess_position(board,ship_pos)
        if ok:
            win = 1
            break
        else:
            print "Die!!!!!!"
        #
    #
    return win
#
board = []
init_board(board)
ship_pos = position_ship(board)
#print ship_pos[0]
#print ship_pos[1]

w = play(2,board,ship_pos)
print "G A M E  O V E R"
if w==0:
    print "My bones were HERE the whole time!!! Now that you're dead, we'll haunt this place together forever!!!!"
    board[ship_pos[0]][ship_pos[1]] = "B"
    print_board(board)
else:
    print "Congratulations, you may live!! Y O U  W I N"
#

print "           _,.-------.,_ "
print "       ,;~'             '~;, "
print "     ,;                     ;, "
print "    ;                         ; "
print "   ,'                         ', "
print "  ,;                           ;, "
print "  ; ;      .           .      ; ; "
print "  | ;   ______       ______   ; | "
print "   |  `/~      ~ . ~      ~ '  | "
print "  |  ~  ,-~~~^~, | ,~^~~~-,  ~  | "
print "   |   |        }:{        |   | "
print "   |   l       / | \       !   | "
print "   .~  (__,.--  .^.  --.,__)  ~. "
print "   |     ---;  / | \ `;---     | "
print "    \__.       \/^\/       .__/ "
print "     V| \                 / |V "
print "      | |T~\___!___!___/~T| | "
print "      | |`IIII_I_I_I_IIII'| | "
print "      |  \,III I I I III,/  | "
print "       \    ~~~~~~~~~~     / "
print "         \   .       .   /     "
print "           \.    ^    ./ "
print "             ^~~~^~~~^ "