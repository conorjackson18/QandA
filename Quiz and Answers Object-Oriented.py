import time

def loading(string): #function displays a 7 letter string in a nice display
    bar = [
    f" {string[6]}       ",
    f" {string[5]}{string[6]}      ",
    f" {string[4]}{string[5]}{string[6]}     ",
    f" {string[3]}{string[4]}{string[5]}{string[6]}    ",
    f" {string[2]}{string[3]}{string[4]}{string[5]}{string[6]}   ",
    f" {string[1]}{string[2]}{string[3]}{string[4]}{string[5]}{string[6]}  ",
    f" {string[0]}{string[1]}{string[2]}{string[3]}{string[4]}{string[5]}{string[6]} ",
    f"  {string[0]}{string[1]}{string[2]}{string[3]}{string[4]}{string[5]}{string[6]}",
    f"   {string[0]}{string[1]}{string[2]}{string[3]}{string[4]}{string[5]}",
    f"    {string[0]}{string[1]}{string[2]}{string[3]}{string[4]}",
    f"     {string[0]}{string[1]}{string[2]}{string[3]}",
    f"      {string[0]}{string[1]}{string[2]}",
    f"       {string[0]}{string[1]}",
    f"        {string[0]}"
    ]
    i = -1

    while i>-29:
        print(bar[i % len(bar)], end="\r")
        time.sleep(.1)
        i -= 1
    
class Quiz():
    def __init__(self, qAndAs): #Initializes the player's turn
        self.player = ''
        self.playerScore = 0
        self.rightAnswer = False
        self.qAndAs = qAndAs


    def playerName(self): #asks for the player's name

        self.player = str(input(f"Please insert player {studentNo+1}'s name here: "))


    def questions(self, roundNumber): #Asks the question and checks answer.

        print(f'Question {roundNumber+1}.')
        answer = str(input(f'{qAndAs[roundNumber][0]}\n'))
        if answer.lower() == qAndAs[roundNumber][1].lower():
            self.rightAnswer=True
        else:
            self.rightAnswer=False


    def score(self): #The player's scoreboard

        if self.rightAnswer:
            self.playerScore+=1
            print(f'Correct! Your score is: {self.playerScore}')
        else:
            self.playerScore+=0
            print(f'Incorrect! Your score is: {self.playerScore}')


    def scoreKeep(self): #Adds the player's name and score to the global scoreboard.

        listOfScores.append([self.player,self.playerScore])
        

qAndAs =[   #The Questions and answers in a 2d list, to add/change questions, simply edit this 2d list.
    ['Who is the minister for magic in the first 5 books?', 
    'Cornelius Fudge'],
            ['When Buckbeak was a fugitive, what was their name?', 'Witherwings'],
            ['Which Weasley brother gets married in the last book?', 
            'Bill'],
            ["What is Hermione's cat's name?", 
            'Crookshanks'],
            ['What is the name of the bronze currency in the wizarding world?', 'Knut'],
            ['Is this a great example of Object Oriented Programming?', 'Yes']
            ]

studentNo=0
intInput=False
while not intInput: #Asks how many players are playing.
    try:
        howMany = int(input('Input amount of players: '))
    except:
        print('Must be an int')
    else:
        intInput = True

listOfScores = []

while studentNo != howMany:
    player = Quiz(qAndAs) #Creates the quiz object
    player.playerName()  #Asks for the player's name
    round=1
    for round in range(len(qAndAs)): #Runs through every round of the game
        player.questions(round)
        player.score()
        round+=1

    player.scoreKeep()#end of every game.
    studentNo+=1

print('Goodbye!')   #Displays the global scoreboard
for name in range(len(listOfScores)):
    print(f"{listOfScores[name][0]}'s score: {listOfScores[name][1]}")

loading('Thanks!') #Calls the loading function with the string 'Thanks!'