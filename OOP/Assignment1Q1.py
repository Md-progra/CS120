"""
Question 1: Rock, Paper, Scissors Game
"""

import random
#Random generates random choices for the computer

class Rock_Paper_Scissors:
    def __init__(self, rounds_of_game): #Parameter rounds_of_game represents number of rounds to be played

        self.rounds_of_game = rounds_of_game

        self.current_round = 0   #Keeps track of the round being played

        self.computer_score = 0   #Keeps track of computer's score

        self.player_score = 0   #Keeps track of player's score

        self.tie_score = 0     #Keeps track of tie scores

        self.choices = ['rock', 'paper', 'scissors']

        #This is a function that returns the choice of the computer
    def get_computer_choice(self):
        self.computer_choice = random.choice(self.choices)
        print(f"Computer chose {self.computer_choice}")
        return self.computer_choice
    
    #This is a function that returns the player's choice
    def get_player_choice(self):
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        while choice not in self.choices: #used while loop to keep asking for input until a valid choice is made
            print("Invalid choice. Try again.")
            choice = input("Enter your choice (rock, paper, scissors): ").lower()
        return choice
    #This function uses condtional statements to pick winner of each round
    #It also keeps track of score and prints out funny statements about the winner
    def find_winner(self, computer, player):
        if computer == player:
            print(f"Both chose {player}. It's a tie!")
            self.tie_score += 1
        elif (computer == 'rock' and player == 'scissors') or \
             (computer == 'scissors' and player == 'paper') or \
             (computer == 'paper' and player == 'rock'):
            #Breaking long lines of code into multiple lines
            print(f"Computer wins!")
            self.computer_score += 1
        else:
            print(f"Player wins! {player} beats {computer}")
            self.player_score += 1
      # Displays the scores and ties of the game
    def display_scores(self):
        print("\nCurrent Scores:")
        print(f"Player: {self.player_score} | Computer: {self.computer_score} | Ties: {self.tie_score}\n")
    #Checks the winner of the game
    def winner(self):
        if self.player_score > self.computer_score:
            print("Congratulations! You win the game! 🎉")
        elif self.player_score < self.computer_score:
            print("Computer wins the game! Better luck next time. 🤖")
        else:
            print("It's a tie game!")

        # Combines the functions above and plays the game
    def play_game(self):
        print("Welcome to Rock Paper Scissors!")
        for _ in range(self.rounds_of_game):
            self.current_round += 1
            print(f"\n ____Round {self.current_round}___")
            computer_choice = self.get_computer_choice()
            player_choice = self.get_player_choice()
            self.find_winner(computer_choice, player_choice)
            self.display_scores()
        self.winner()



if __name__ == "__main__":
    game = Rock_Paper_Scissors(5)
    game.play_game()




