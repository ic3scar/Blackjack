

class Player:
    default_value_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
                          '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    def __init__(self,name):
        self.name = name
        self.hand = []
        self.scores = []
        self.final_score = 0
    
    def add_card(self,card):
        self.hand.append(card)
    
    def get_possible_scores(self):
        count = 0
        total = 0
        self.scores = []
        for card in self.hand:
            if card.number == 'A':
                count += 1
            total += self.default_value_dict[card.number]
        for i in range(count+1):
            self.scores.append(total-10*i)

    def current_score(self):
        self.get_possible_scores()
        self.scores.sort()
        maxunder = 0
        for score in self.scores:
            if score<=21 and score>maxunder:
                maxunder = score
        if maxunder==0:
            minover = self.scores[0]
            self.final_score = minover
            return minover
        else:
            self.final_score = maxunder
            return maxunder

    def cards_in_hand(self):
        return len(self.hand)

    def empty_hand(self):
        self.hand = []
        self.final_score = 0   

    def __repr__(self):
        return self.name

    def top_card(self):
        return self.hand[-1]
