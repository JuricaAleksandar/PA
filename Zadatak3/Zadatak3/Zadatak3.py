import random

#cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
#cards = [1,5,7,8,3,2,6,8,1] 
#cards = [1,2,3,4,5,6,7,8,9,10]
#cards = [2,4,1,5,7,9,3,2,1,7,10]
#cards = [1,2,3]
cards = [4,6,7,5,1]

options = []

def cmp(a, b) : 
    if a > b:
        return 1
    elif a < b :
        return -1
    else :
        return 0
    
def Blackjack(i) :

    options = [0]

    if n - 1 < 4 : 
        print("Not enough cards in deck!")
        return  0 

    for p in range(2, n - i - 2) :
        player = cards[i] + cards[i + 2] + sum(cards[i + 4 : p + i + 2])
        print("Player score : ", player)

        if player > 21 :
            print("Player score is over 21, it's a bust!")
            options.append(-1 + Blackjack(i + 2 + p))
            break

        for d in range(2, n - i - p) :
            dealer = cards[i + 1] + cards[i + 3] + sum(cards[i + p + 2 : i + p + d])
            print("Dealer score : ", dealer)

            if dealer >= 17 :
                print("Dealer over 17, dealer has stopped drawing cards")
                print("Dealer score : ", dealer)
                break   

        if dealer > 21 :
            dealer = 0
            print("Dealer bust!")

        options.append(cmp(player,dealer) + Blackjack(i + p + d))
        print("Options value : ", options)
    return max(options)


random.shuffle(cards)
n = len(cards)
print(cards)
print(Blackjack(0))
