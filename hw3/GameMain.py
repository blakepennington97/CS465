import itertools
import random
import math
from deuces import Card
from deuces import Evaluator
from importlib import import_module

class MainProgram:
    def __init__(self):
        self.object1 = None
        self.object2 = None
        self.object3 = None
        self.object4 = None
        self.object5 = None
        self.getPlayers()
        self.deck = self.createDeck()

    def getPlayers(self):
        list_playerClass = [] #List of students' functions
        playerCount = 0
        while(playerCount < 2 or playerCount>5):
            # playerCount = input("Enter Number of Players:")
            playerCount = 3
            if playerCount > 1:
                if playerCount == 2:
                    self.getPlayerSet1(playerCount,list_playerClass)
                elif playerCount == 3:
                    self.getPlayerSet2(playerCount,list_playerClass)
                elif playerCount == 4:
                    self.getPlayerSet3(playerCount,list_playerClass)
                elif playerCount == 5:
                    self.getPlayerSet4(playerCount,list_playerClass)
                else:
                    print "Please enter a valid number of players."
            else:
                print "Please enter a valid number of players."

    def getPlayerSet1(self,playerCount,list_playerClass):
        for i in range(0,playerCount):
            name=raw_input("Enter Player" + str(i + 1) + ":")
            list_playerClass.append(name)
        if list_playerClass is not None and len(list_playerClass) == 2:
            self.object1=self.initializeObjects(list_playerClass[0],list_playerClass[0])
            self.object2=self.initializeObjects(list_playerClass[1],list_playerClass[1])
    
    def getPlayerSet2(self,playerCount,list_playerClass):
        for i in range(0,playerCount):
            name=raw_input("Enter Player"+str(i+1)+":")
            list_playerClass.append(name)
        if list_playerClass is not None and len(list_playerClass)==3:
            self.object1=self.initializeObjects(list_playerClass[0],list_playerClass[0])
            self.object2=self.initializeObjects(list_playerClass[1],list_playerClass[1])
            self.object3=self.initializeObjects(list_playerClass[2],list_playerClass[2])

    def getPlayerSet3(self,playerCount,list_playerClass):
        for i in range(0,playerCount):
            name=raw_input("Enter Player"+str(i+1)+":")
            list_playerClass.append(name)
        if list_playerClass is not None and len(list_playerClass)==4:
            self.object1=self.initializeObjects(list_playerClass[0],list_playerClass[0])
            self.object2=self.initializeObjects(list_playerClass[1],list_playerClass[1])
            self.object3=self.initializeObjects(list_playerClass[2],list_playerClass[2])
            self.object4=self.initializeObjects(list_playerClass[3],list_playerClass[3])

    def getPlayerSet4(self,playerCount,list_playerClass):
        for i in range(0,playerCount):
            name=raw_input("Enter Player"+str(i+1)+":")
            list_playerClass.append(name)
        if list_playerClass is not None and len(list_playerClass)==5:
            self.object1=self.initializeObjects(list_playerClass[0],list_playerClass[0])
            self.object2=self.initializeObjects(list_playerClass[1],list_playerClass[1])
            self.object3=self.initializeObjects(list_playerClass[2],list_playerClass[2])
            self.object4=self.initializeObjects(list_playerClass[3],list_playerClass[3])
            self.object5=self.initializeObjects(list_playerClass[4],list_playerClass[4])

    def initializeObjects(self,module_name,class_name):
        #getClass(module_name,class_name)
        module = __import__(module_name)
        my_class = getattr(module, class_name)
        instance = my_class()
        instance.student_Name = class_name
        return instance

    def gameDriver(self):
        #self.getPlayers()

        list_ExchangeCards = []  # List of boolen values for cards to be exchanged
        list_Exchangeindex = []  # List of indices of cards to exchange

        self.object1.student_Hand = self.dealHand()#['2h','4c','2s','2c','5d']
        self.object2.student_Hand = self.dealHand()#['2h','2c','4s','4c','5d']
        if self.object3 is not None:
            self.object3.student_Hand = self.dealHand()#['Ad','Kd','Jc','Qd','Td']
        if self.object4 is not None:
            self.object4.student_Hand = self.dealHand()
        if self.object5 is not None:
            self.object5.student_Hand = self.dealHand()

        self.exchangeCardsStep() # Call student function for each of the participant students

        self.compareRank() #Evaluator function
        return 1

    def exchangeCardsStep(self):
        self.exchngeCardsPlayer1()
        self.exchngeCardsPlayer2()
        if self.object3 is not None:
            self.exchngeCardsPlayer3()
        if self.object4 is not None:
            self.exchngeCardsPlayer4()
        if self.object5 is not None:
            self.exchngeCardsPlayer5()

    def exchngeCardsPlayer1(self):
        list_Exchangeindex = []  # List of indices of cards to exchange
        list_ExchangeCards = self.object1.student_function()  # List of boolen values for cards to be exchanged
        countExchangeCards = list_ExchangeCards.count(True)
        if(countExchangeCards>0):
            for i in range(0,5):
                if(list_ExchangeCards[i]==True):
                    list_Exchangeindex.append(i)
            self.object1.student_Hand = self.exchangeCards(self.object1.student_Hand, list_Exchangeindex)
    
    def exchngeCardsPlayer2(self):
        list_Exchangeindex = []  # List of indices of cards to exchange
        list_ExchangeCards = self.object2.student_function()  # List of boolen values for cards to be exchanged
        countExchangeCards = list_ExchangeCards.count(True)
        flag = 0
        for i in range(0,5):
            if(list_ExchangeCards[i]==True):
                flag = 1
                list_Exchangeindex.append(i)
        if(flag == 1):
            self.object2.student_Hand = self.exchangeCards(self.object2.student_Hand, list_Exchangeindex)
    
    def exchngeCardsPlayer3(self):
        list_Exchangeindex = []  # List of indices of cards to exchange
        list_ExchangeCards = self.object3.student_function()  # List of boolen values for cards to be exchanged
        countExchangeCards = list_ExchangeCards.count(True)
        flag = 0
        for i in range(0,5):
            if(list_ExchangeCards[i]==True):
                flag = 1
                list_Exchangeindex.append(i)
        if(flag == 1):
            self.object3.student_Hand = self.exchangeCards(self.object3.student_Hand, list_Exchangeindex)
    
    def exchngeCardsPlayer4(self):
        list_Exchangeindex = []  # List of indices of cards to exchange
        list_ExchangeCards = self.object4.student_function()  # List of boolen values for cards to be exchanged
        countExchangeCards = list_ExchangeCards.count(True)
        flag = 0
        for i in range(0,5):
            if(list_ExchangeCards[i]==True):
                flag = 1
                list_Exchangeindex.append(i)
        if(flag == 1):
            self.object4.student_Hand = self.exchangeCards(self.object4.student_Hand, list_Exchangeindex)
    
    def exchngeCardsPlayer5(self):
        list_Exchangeindex = []  # List of indices of cards to exchange
        list_ExchangeCards = self.object5.student_function()  # List of boolen values for cards to be exchanged
        countExchangeCards = list_ExchangeCards.count(True)
        flag = 0
        for i in range(0,5):
            if(list_ExchangeCards[i]==True):
                flag = 1
                list_Exchangeindex.append(i)
        if(flag == 1):
            self.object5.student_Hand = self.exchangeCards(self.object5.student_Hand, list_Exchangeindex)
    
    def convertHand(self,oldhand):
        newhand = []
        for i in range(0,5):
            newhand.append(Card.new(oldhand[i]))
        return newhand

    def printCards(self,oldhand):
        for i in range(0,5):
            print oldhand[i],
        print

    def printHand(self,hand):
        strHand=','.join(map(str,hand))
        return strHand

    def compareRank(self):
        HighRank = 8000
        HingRankIndex = -1
        board = []
        evalulator = Evaluator()

        sh1 = self.convertHand(self.object1.student_Hand)
        HighRank = evalulator.evaluate(board,sh1)
        HighRankIndex = 0
        print "\n"
        print "Player 1: " + self.object1.student_Name + "\t Cards: " + self.printHand(self.object1.student_Hand) + "\t Card-rank: " + str(HighRank)
        
        
        sh2 = self.convertHand(self.object2.student_Hand)
        rank = evalulator.evaluate(board,sh2)
        print "\n"
        print "Player 2: " + self.object2.student_Name + "\t Cards: "+ self.printHand(self.object2.student_Hand) + "\t Card-rank: " + str(rank)
        
        if(rank < HighRank):
            HighRank =rank
            HighRankIndex = 1
        
        if(self.object3 is None):
            print "\n"
            print "Player "+ str(HighRankIndex+1)+ " is winner with rank "+ str(HighRank)
            return 
        else:
            sh3 = self.convertHand(self.object3.student_Hand)
            rank = evalulator.evaluate(board,sh3)
            print "\n"
            print "Player 3: " + self.object3.student_Name + "\t Cards: "+ self.printHand(self.object3.student_Hand) + "\t Card-rank: " + str(rank)
            
            if(rank < HighRank):
                HighRank =rank
                HighRankIndex = 2
        
        if(self.object4 is None):
            print "\n"
            print "Player "+ str(HighRankIndex+1)+ " is winner with rank "+ str(HighRank)
            return 
        else:
            sh4 = self.convertHand(self.object4.student_Hand)
            rank = evalulator.evaluate(board,sh4)
            print "\n"
            print "Player 4: " + self.object1.student_Name + "\t Cards: "+ self.printHand(self.object4.student_Hand) + "\t Card-rank: " + str(rank)
            
            if(rank < HighRank):
                HighRank =rank
                HighRankIndex = 3


    def createDeck(self):
        """
        This creates a single list containing tuples which have the values
        (suit, numerical value)
        """
        deck = []
        #cardSuits = [Suits.H, Suits.D, Suits.S, Suits.C]
        DBShortCardNames = [ '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A' ]
        DBShortSuitNames = [ 'c', 'd', 'h', 's' ]
        
        for c in itertools.product(DBShortCardNames, DBShortSuitNames):
            crd = c[0] + c[1]
            deck.append(crd)
        random.shuffle(deck)
        return deck

    def dealHand(self):
        """
        draws 5 cards and modifies the deck.
        I was told to instead use indexing to draw, instead of modifying the list
        """
        hand = []
        for i in range(5):
            hand.append(self.deck.pop())
        return hand

    def exchangeCards(self, hand, list_Exchangeindex):
        exchangeindexCounter = 0
        #for i in range(0, 5):
        #    if i == list_Exchangeindex[exchangeindexCounter]:
        #        hand[i] = self.deck.pop()
        #        exchangeindexCounter = exchangeindexCounter + 1
        #return hand
        for index in list_Exchangeindex:
            hand[index] = self.deck.pop()
        return hand
