def header():
    print('|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|')
    print('|>>>>>>>>  w e l c o m e   t o   t h e  >>>>>>>>|')
    print('|>>> F O U R   A C E S   R A C E   T R A C K >>>|')
    print('|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|')
    
def horse_hearts(progr):
    h = 'H'
    print(f'|{h.rjust(progr*6+3)}')

def horse_spades(progr):
    s = 'S'
    print(f'|{s.rjust(progr*6+3)}')

def horse_diamonds(progr):
    d = 'D'
    print(f'|{d.rjust(progr*6+3)}')

def horse_clubs(progr):
    c = 'C'
    pipe = '|'
    print(f'|{c.rjust(progr*6+3)}')


def bet_check(player, yourbet):
    bet = 100 if yourbet == 1 else 50 if yourbet == 2 else 25
    if player.bankroll < bet:
        print("You don't have enough money for this bet.")
    else:
        return True

def race_progress(card, horses):
    if card.suit == 0:
        horses[0].progress += 1
    if card.suit == 2:
        horses[1].progress += 1
    if card.suit == 1:
        horses[2].progress += 1
    if card.suit == 3:
        horses[3].progress += 1


def progress_check(horses):
    for horse in horses:
        if horse.progress == 7:
            return horse
    else:
        return False


def your_result(player, yourbet, yourpick, winner):
    bet = 100 if yourbet == 1 else 50 if yourbet == 2 else 25
    if yourpick == winner:
        return 'YOU WON!!!'
    else:
        player.bankroll -= bet
        return 'YOU LOST!!!'


def calc_result(player, horses, yourbet, odds, winner):
    bet = 100 if yourbet == 1 else 50 if yourbet == 2 else 25
    ind = 0 if winner == horses[0] else 1 if winner == horses[1] \
        else 2 if winner == horses[2] else 3
    multpl = 1.5 if odds[ind] == "2 to 5" else 3 if odds[ind] == "1 to 3" \
        else 4 if odds[ind] == "1 to 4" else 5
    win = bet * multpl
    player.bankroll += win


def calc_odds(parcours):
    odds = ['2 to 5', '1 to 3', '1 to 4', '1 to 5']
    odds_rarr = []
    hearts, spades, diamonds, clubs = [], [], [], []
    for card in parcours:
        if card.suit == 0:
            hearts.append(card)
        elif card.suit == 1:
            diamonds.append(card)
        elif card.suit == 2:
            spades.append(card)
        else:
            clubs.append(card)
    len_lst = [hearts, spades, diamonds, clubs] 
    sort_lst = sorted(len_lst, key=lambda x: len(x))
    for lst in len_lst:
        ind = sort_lst.index(lst)
        odds_rarr.append(odds[ind])
    
    return odds_rarr
