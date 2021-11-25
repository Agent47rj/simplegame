import random


def bot():
    botmove  = 0
    pick = random.randint(1,3)
    if(1 == pick):
        # print("bot choose rock")
        botmove = 1
    if(2 == pick):
        # print("bot choose paper")
        botmove = 2
    if(3 == pick):
        # print("bot choose scissor")
        botmove = 3
    return botmove


print('''choose : 
    1 for rock
    2 for paper
    3 for scissor''')
def player():
    

    playermove = int(input("enter here : "))
    if(playermove == 1):
        # print("you choose rock")
        playermove = 1
    if(playermove == 2):
        # print("you choose paper")
        playermove = 2
    if(playermove == 3):
        # print("you choose scissor")
        playermove = 3
    return playermove



# print(f"bot choose {bot()} and player choose {player()}")
def gamefun():
    # rock = 1
    # paper = 2
    # scissor = 33

    # print(player())
    # print(bot())
    robot = bot()
    human = player()
    if(bot()==1 and human==1):
        # print(f"bot choose {bot()} and player choose {player()}")
        print("game draw becouse you choose rock and bot also choose rock")
    elif(robot==1 and human==2):
        print("you win becouse you choose paper and bot choose rock")
    elif(robot==1 and human==3):
        print("you loose becouse you choose scissor and bot choose rock")
    elif(robot==2 and human==1):
        print("you loose becouse you choose rock and bot choose paper")
    elif(robot==2 and human==2):
        print("game draw becouse you choose paper and bot choose paper")
    elif(robot==2 and human==3):
        print("you win becouse you choose scissor and bot choose paper")
    elif(robot==3 and human==1):
        print("you win becouse you choose rock and bot choose scissor")
    elif(robot==3 and human==2):
        print("you loose becouse you choose paper and bot choose scissor")
    elif(robot==3 and human==3):
        print("game draw becouse you choose scissor and bot choose scissor")

while True:
    gamefun()
