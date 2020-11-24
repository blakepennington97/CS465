# CS465 HW3

This is a repository that uses the poker deuces library to predict scores of the hand in 5 card draw Poker. It also has algorithms to determine which cards to discard or keep to achieve an optimal win rate.



## How It Works

When GameMain.py is ran, five cards are drawn from the deck and distributed to a playerbase which range from 2-5. Each player has an opportunity to discard any number of cards of their choosing in order to maximize their chances of having the winning hand. Once all the players have made their decisions, the player's hand is rated through a ranking system by the deuces library. The player with the highest rating (lowest score) is the winner.



## Discard strategy

To determine which cards to discard, a fairly straight-forward checking method is used. blakepennington.py parses and extracts the ranks and suites of the five cards in the hand. Then, some obvious checks are performed on the hand that checks for high ranking hands. If any high ranked hands return a match, then that hand is kept and no cards are discarded. The following hands are first checked in order of highest priority:

1. Royal Flush
2. Straight Flush
3. Four of a Kind
4. Full House
5. Flush
6. Straight

After these high-ranked hands are checked, the following strategy is followed with the idea of aiming for an above-average hand frequently rather than a high-ranked hand rarely:
* If we have a pair we draw 3 and try and make trips.
* If we have trips, we draw two and try to make Quads or a full house. 
* If we have a flush-draw or straight-draw we draw one and try to hit.
* If we have total garbage (usually in a free play situation) we can hold on to cards above a Queen or Jack and replace the others.

With this idea in mind, the following is checked in order of highest priority, following the numbered list above:

7. Flush draw (1 card away from a flush)
8. Straight draw (1 card away from a straight)
9. Three of a Kind
10. Pair
11. High card

![Image of Poker Hands](https://www.oddsshark.com/sites/default/files/styles/default/public/sb_101/2018/09/13/os-poker-hands-editorial-800x492.jpg)

#### Interesting finds on the discard strategy
One interesting thing I noticed when implementing this logic was that if I used a two pair check anywhere within my checks, it would drop my win-rate quite significantly. Thus, I decided not to include a two-pair check in my final implementation.


**To execute this program, follow the steps below:**
    
- First, run 'PyPokerMain.py' This will prompt the user for the desired amount of players and which players to be used.
- Usage `python2 PyPokerMain.py`
- Enter the desired amount of players (2-5 players) and the name of the players. However, the name of the players MUST match the name of the Python file/class.
- Example input/output:
- ![Image of Example Input/Output](https://i.imgur.com/x2itJQr.png)


**Requirements:**
    Python 2.7
    deuces
    
**Sources used:**
-   https://towardsdatascience.com/poker-with-python-how-to-score-all-hands-in-texas-holdem-6fd750ef73d
-   https://github.com/BradAJ/video_poker_analyzer
-   https://github.com/worldveil/deuces
-   https://www.oddsshark.com/poker/hand-rankings
-   https://www.pokervip.com/strategy-articles/texas-hold-em-no-limit-beginner/5-card-draw-poker-basic-strategy