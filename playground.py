# Find the rules of this game at https://www.pagat.com/race/horse_race.html
import os

import classes
import parcours
import utils


hearts = classes.Horse('ace of hearts')
spades = classes.Horse('ace of spades')
diamonds = classes.Horse('ace of diamonds')
clubs = classes.Horse('ace of clubs')
horses = [hearts, spades, diamonds, clubs]

game_on = True

utils.header()
enter_track = input('Enter if you are ready to make some bets.')
p1 = classes.Punter()
os.system('cls')

while game_on:
    
    if p1.bankroll < 25:
        print("Your Bankroll is Busted. \nBorrow some money and come back.")
        break

    finished = False
    your_pick = None
    hearts.progress, spades.progress, diamonds.progress, clubs.progress = 0,0,0,0
    deck = classes.Race()
    stock = iter(deck.stock)

    utils.header()
    parcours.race_track(deck)
    odds_lst = utils.calc_odds(deck.parcours)
    print('|-----------------------------------------------|')
    print('|        H O R S E        |      O D D S:       |')
    print('|-------------------------|---------------------|')
    print(f'|      Ace of Hearts\t  |\t{odds_lst[0]}          |')
    print(f'|      Ace of Spades\t  |\t{odds_lst[1]}          |')
    print(f'|      Ace of Diamonds\t  |\t{odds_lst[2]}          |')
    print(f'|      Ace of Clubs\t  |\t{odds_lst[3]}          |')
    print('|-------------------------|---------------------|')
    print(f'|      Your Bankroll      |\t$ {p1.bankroll:.2f}\t\t|')
    print('-------------------------------------------------')
    while True:
        your_input = input("Pick your horse. Type [h], [s], [d] or [c]: ")
        if your_input == 'h' or your_input == 's' or your_input == 'd' or your_input == 'c':
            break
    while True:
        your_bet = int(input("And place your bet. [1] 100, [2] 50, [3] 25: "))
        bet_check = utils.bet_check(p1, your_bet)
        if (your_bet == 1 or your_bet == 2 or your_bet == 3) and bet_check == True:
            break
    inp2 = input("Press enter: The Race Begins!")

    your_pick = hearts if your_input == 'h' else spades if your_input == 's' else diamonds if your_input == 'd' else clubs
    os.system('cls')

    while not finished:

        utils.header()
        parcours.race_track(deck)
        print('|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|')
        print('|-----|-----|-----|-----|-----|-----|-----|-----|')
        utils.horse_hearts(hearts.progress)
        print('|-----|-----|-----|-----|-----|-----|-----|-----|')
        utils.horse_spades(spades.progress)
        print('|-----|-----|-----|-----|-----|-----|-----|-----|')
        utils.horse_diamonds(diamonds.progress)
        print('|-----|-----|-----|-----|-----|-----|-----|-----|')
        utils.horse_clubs(clubs.progress)
        print('|-----|-----|-----|-----|-----|-----|-----|-----|')
        print('|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|')
        
        inp = input("Press enter to draw a card.")

        if inp == '':
            card = next(stock)
            print(card)   

        utils.race_progress(card, horses)
        inp2 = input("Press enter to continue.")
        os.system('cls')        
        finished = utils.progress_check(horses)

        if your_pick == finished:
            utils.calc_result(p1, horses, your_bet, odds_lst, finished)
        
    finished.races_won += 1
    print('|***********************************************|')
    print(f'|**************** {finished.name.upper()} ****************|')
    print('|**************** is the winner ****************|')
    print(f'|***************   {utils.your_result(p1, your_bet, your_pick, finished)}   ***************|')
    print('|***********************************************|')
    print('|               S C O R E B O A R D             |')
    print('|-----------------------------------------------|')
    print(f'|     Ace of Hearts has won {hearts.races_won} races             |')
    print(f'|     Ace of Spades has won {spades.races_won} races             |')
    print(f'|     Ace of Diamonds has won {diamonds.races_won} races           |')
    print(f'|     Ace of Clubs has won {clubs.races_won} races              |')
    print('|-----------------------------------------------|')
    print(f'|      Your Bankroll      |\t$ {p1.bankroll:.2f}\\tt|')
    print('-------------------------------------------------')

    while True:
        finito = input("Want to continue? Type [y] or [n]: ")
        if finito == 'y' or finito =='n':
            break
    
    if finito == 'y' or finito == 'Y':
        game_on = True
    else: 
        game_on = False
    
    finished = False
    os.system('cls')



    