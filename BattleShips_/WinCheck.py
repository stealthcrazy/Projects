
def check(playerHits,compHits):
    win  = False
    winner = ' '
    if playerHits == 18:
        win = True
        winner = 'player'
    if compHits == 18:
        win = True
        winner = 'computer'
    return [win,winner]