import random
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock 石頭
# 1 - Spock 史巴克
# 2 - paper 布
# 3 - lizard 蜥蜴
# 4 - scissors 剪刀

# helper functions

def name_to_number(name):
    if name.lower()=='rock':
        return 0
    elif name.lower()=='spock':
        return 1
    elif name.lower()=='paper':
        return 2
    elif name.lower()=='lizard':
        return 3
    elif name.lower()=='scissors':
        return 4
    else :
        return 5
    
    pass

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    if number==0:
        return 'rock'
    elif number==1:
        return 'spock'
    elif number==2:
        return 'paper'
    elif number==3:
        return 'lizard'
    elif number==4:
        return 'scissors'
    elif number==5:
        return 'no'
    
    pass
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
def play(player,pc):
    if player==pc:
        print("Draw Game!")
    elif player==0 and (pc==3 or pc==4):
        print("Player wins!")
    elif player==1 and (pc==0 or pc==4):
        print("Player wins!")
    elif player==2 and (pc==0 or pc==1):
        print("Player wins!")
    elif player==3 and (pc==1 or pc==2):
        print("Player wins!")
    elif player==4 and (pc==3 or pc==2):
        print("Player wins!")
    else:
        print("Computer wins!")
    
    pass
    

def rpsls(player_choice): 

    print(" ")
    
    print("Player chooses "+ player_choice)
    #print(name_to_number(player_choice))
    pc_choice=number_to_name(random.randint(0,4))
    print("Computer chooses " + pc_choice)
    play(name_to_number(player_choice),name_to_number(pc_choice))
       
    pass


   # test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


