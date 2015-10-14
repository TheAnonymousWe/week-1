import random

class Player:
    
    playerID = 0
    pot = 0
    lastCard=0     
        
    def __init__(self, inputID, startingPot):
        self.playerID = inputID
        self.pot = startingPot
  
            
    def play(self, dealerCard):
        self.lastCard = random.choice(cards)
        

    if self.lastCard < dealerCard:         
        self.pot -= gameStake
        return 'player ' + str(self.playerID) + ' lose, ' + str(self.lastCard) + ' vs ' + str(dealerCard)
            
    else:
        self.pot += gameStake     
        return 'player ' + str(self.playerID) + ' win, ' + str(self.lastCard) + ' vs ' + str(dealerCard)
            
        
    def returnPot(self):
        return self.pot
        
       
    def returnID(self):
        return self.playerID
        

def playHand(players):
        
     for player in players:
        print player.play(random.choice(cards))
       

def checkBalances(players):
    
    for player in players:
        print 'player ' + str(player.returnID()) + ' has $' + str(player.returnPot()) + 'left.'
        
gameStake = 50  
cards = range(10)

players = []      

for i in range(5):
    players.append(Player(i, 500))

for i in range(10):
    print ''
    print 'start game ' + str(i)
    playHand(players)


print ''
print 'game results:'
checkBalances(players)
