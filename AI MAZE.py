# I 'd love to share your exp with the game 
# and send me your feedback at davedelks1d@gmail.com


# modules used
import random
import time
import sys # for exit function

# global variables
satus = True
score = 0


def start():
    if satus: 
        print ("""
░█████╗░██╗  ███╗░░░███╗░█████╗░███████╗███████╗
██╔══██╗██║  ████╗░████║██╔══██╗╚════██║██╔════╝
███████║██║  ██╔████╔██║███████║░░███╔═╝█████╗░░
██╔══██║██║  ██║╚██╔╝██║██╔══██║██╔══╝░░██╔══╝░░
██║░░██║██║  ██║░╚═╝░██║██║░░██║███████╗███████╗
╚═╝░░╚═╝╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝
""")
        year = random.randint(2030, 2050)
        intro_phrase = f"""
        Welcome to AI maze game!

        You are now in {year}, when AI massively grew. 

        Everyone has their own AI assistant, but somewhere,

        an Evil person called MAD GUY developed an opposing power of AI!

        His goal was to kick humans out of Earth, leaving the Earth only for smart AI robots.

        Now, the story begins with your AI assistant Jane.

        """
        # converting string to list separated by new line. 
        intro_lines = intro_phrase.split('\n')
        # Running every line in the string with the same time.sleep()
        for x in intro_lines: 
            print(x)
            time.sleep(1) 
            
        # Getting name as input, running first scene function 
        name = input("Please enter your name: ")
        first_scene(name)
        return name  # returning local value to be used in other functions

def first_scene(name):
    # first scene
    # random a word from a list to be used in game chat
    second_phrase_first_scene = ["Are you OK?", "Are you awake?", "How do you feel?"]
    random_string = random.choice(second_phrase_first_scene)

    # using string formatting to use varibales in strings
    phrawse1_scene1 = f"""
    Jane: {name}..{name}... Wake UP!
    {random_string}

    {name}: what happened?!, I can't remember anything.

    Jane: AI developed by MAD GUY is invading the Earth!
    Jane: He is trying to collect all citizens on Earth in one place to send them to the sun!
    Jane: All humans with their AI assistants are collected here, including me and you.

    {name}: Oh, How mad!
    {name}: We have to exploit his plan As Fast As Possible"
    {name}: I need your help Jane to provide me with information about that place,
            and MAD GUY AI robots here.

    {name}: We are the last hope for humanity!"
    """
    lines1_phrase1_scene1 = phrawse1_scene1.split("\n")
    for line in lines1_phrase1_scene1:
        print(line)
        time.sleep(1.75) 

    phrases2_scene1 = f"""
    Jane: For sure, Scanning is loading... 
    ... 
    ... 

    We are in the entrance court, where MAD GUY's robots are storing humans.
    I can see a gate, but can't still recognize what is inside. 

    {name}: why not you go and discover it! 

    Jane: Oh, it is a risk. We can play rock, paper, scissors for who takes the risk! 

    {name}: Ok! 

    TIP: if you won, 5 points will be added to your score!

    """
    phrases2_scene1_lines = phrases2_scene1.split("\n")
    for x in phrases2_scene1_lines:
        print(x)
        time.sleep(1.5)

    
    phrase3_scene1 = "Ok! I will go and explore what is there...\n"
    time.sleep(1.5)
    phrase4_scene1 = """... 
I observed the gate empty, 
with a lock password designed for Mad Guy robots: 
...

It only works with fingerprints!
We should take an action!

"""
    phrase4_scene1_lines = phrase4_scene1.split("\n")

    # starting rock, paper, scissors game 
    # winner in the game will go to explore the mystery gate
    # the game returns either 'Jane', 'player' depending on winner
    winner = rock_paper_scissors()

    if winner == "Jane":
        print("Jane: HAHA, I win now! ")
        time.sleep(2.5)

        print(f"{name}: " + phrase3_scene1)
        time.sleep(2)

        for line in phrase4_scene1_lines: 
            print(line)
            time.sleep(2)


    elif winner == "player":
        print(f"{name}: I won now")
        time.sleep(2)
        print("Jane: " + phrase3_scene1)
        time.sleep(1)
        for line in phrase4_scene1_lines:
            print(line)
            time.sleep(2)
        global score
        score += 5
        print(f"TIP: your score now is {score}\n")
        time.sleep(1)

    time.sleep(1)
    print("There are two possible ways!")

    # returning the updated value of score if player won on Jane.
    # transferring characters to the next scene
    second_scene(name,score)
    

def second_scene(name,score):
    # first options
    phrase1_second_scene = """
    1- Kidnap a robot. 
    2- wait until a robot come and open the gate.

"""
    
    phrase1_second_lines = phrase1_second_scene.split("\n")
    for x in phrase1_second_lines: 
        print(x)
        time.sleep(1.5) #1.5

    # making sure user enters correct inputs
    choice1_second_scene = input("Choice: 1 or 2 ?  ")
    while choice1_second_scene not in ["1","2"]: 
        choice1_second_scene = input("Enter a valid choice! 1 or 2 ?  ")

    # first route based on user choice
    if choice1_second_scene == "1":
        score += 5
        print ("TIP: score +5! for passing the choice.\n")
        phrase2_second_scene = f"""
        Jane: You always have mad ideas {name}. 

        {name}: I beleive it can work, I feel it in my bones!

        Jane: Ok! I can see a robot there, let's kindnap him and see what to do next!

        * * * * * * 
        {name} take him quickly! I am trying to turn its system off. 

        Jane: The CPU board of its system connected to three wires: 
        red,
        yellow,
        black,

        You have to cut off one wire, 
        if you cut two wrong wires, alarm system connected would go on. 

        * * * * * * 
        
        choose a wire to cut: 
"""
        phrase2_second_lines = phrase2_second_scene.split("\n")
        for x in phrase2_second_lines:
            print(x)
            time.sleep(1.5) # 1.5

        # first route second choice
        colors = ["red", "black", "yellow"]
        random_color_choice = random.choice(colors)
        
        # giving player two tries to cut the correct wire
        for i in [1,2]: 
            # checking user input
            choose_wire = input("choose a wire to cut: red, yellow, or black:  ")
            while choose_wire.lower() not in ["red", "yellow", "black"]:
                choose_wire = input("please enter a valid choice from red, yellow, or black")


            # if user could cut the correct randomized wire
            if choose_wire == random_color_choice: 
                time.sleep(2.5)
                print("Jane: You got it right! Robot is now off \n")
                time.sleep(2.5)
                print(f"{name} Let's take his uniform and fingerprint! \n")
                
                time.sleep(1.75)
                print (f"TIP: 10 points added for passing choice!\n")
                time.sleep(1)
                score += 10
                print(f"your total score is: {score}")

                # calling the the third scene
                third_scene(name, score)
                break

            else: 
                time.sleep(2.5)
                print("Jane: focus only another chance left!")
        # end the game if player failed in second try
        lose(score)  

    # second route choice
    else: 
        phrase3_second_scene = f"""
        Jane and {name} are now monitoring the gate... 

        A robot finally comes and open it... 

        Jane: what shall we do now? 

        1- running towards the gate and escape. 
        2- Make Jane act as one of them them. 

"""
        phrase3_second_lines = phrase3_second_scene.split("\n")
        for x in phrase3_second_lines: 
            print(x)
            time.sleep(2.5) #2.5

        # second option in the second route
        # checking user input
        choice_phrase3_scene2 = input("choose 1 or 2: ")
        while choice_phrase3_scene2 not in ["1", "2"]:
            choice_phrase3_scene2 = input("Enter a valid choice! 1 or 2: ")

        # wrong choice
        if choice_phrase3_scene2 == "1": 
            print ("Dangerous Choice! Robots caught you! ")
            time.sleep(1)
            lose(score) 
        # correct choice
        elif choice_phrase3_scene2 == "2": 
            print ("Jane could act as one of them. You successfully passed the gate!")
            time.sleep(1.5)
            print ("TIP: 5 points addes to your score!")
            time.sleep(1.5)
            score += 5
            print (f"your current score is {score}")
            third_scene(name, score)



def third_scene(name,score): 
    phrase1_scene3 = f"""
    Jane: We are currently few meters apart

    {name}: from What? 

    Jane: From the main controlling device. 
          Mad Guy uses this device to control all robots here. 
          We need to crack it down and turn them off!

    {name}: But how?? Ofc it has its security PIN. 

    Jane: Don't worry, I can get into its system,
          But the only thing I can do is telling you, 
          how much far are your from the actual number of each digit. 

    {name}: Jane is there a risk of losing you, after turning all AI off?

    Jane: Perhaps, but don worry, I was created to help humans, 
          It's pleasent for me to end my job with that :), 
          hold yourself {name}, we don't have time! 

    {name}: I will never forget you. 

    TIP: you only have 15 attemps to guess digits. 
         Net earning of passing is + 30 for score. 
         your attemps number will be minused.
         Good Luck {name}!
         
"""
    phrase1_scene3_lines = phrase1_scene3.split("\n")
    for x in phrase1_scene3_lines: 
        print (x)
        time.sleep(1.75)
    # starting guessing the PIN
    pin_guess(name, score)


# Three digits PIN guessing function
def pin_guess(name, score):

    # randomize a PIN of three digits
    pin = str(random.randint(100, 999))

    print("system: Hello Mad Guy, please enter your PIN to access admin.")

    # attemps paraneter (limit is 15)
    max_attempts = 15
    attempts = 0
    # Running the loop 3 times for each digit of the PIN
    i = 0  
    for i in range(3):
        guess = input(f"Guess the {i+1}st digit: ")
        attempts += 1
        print (f"Attemp no {attempts}")

        # ensuring input is valid, continuity of game
        while guess.isdigit() == False or guess != pin[i]:
            if not guess.isdigit() or len(guess) != 1:
                print("please enter a single digit.")
            # hints to help player guess better by 
            # using the difference between guess and actual
            else:
                difference = int(guess) - int(pin[i])
                if difference > 3:
                    print("Incorrect guess. far above from actual")
                elif difference < -3:
                    print("Incorrect guess. far below from actual")
                elif difference > 0:
                    print("Incorrect guess. close above from actual")
                else:
                    print("Incorrect guess. close below from actual")

            guess = input(f"Guess the {i+1}st digit: ")
            attempts += 1 # increase attemps for a new guess
            # check if player lose
            if attempts >= max_attempts:
                break

        if attempts >= max_attempts:
            break

        print(f"Correct, the {i+1}st digit is {guess}")

    if attempts < max_attempts:
        print(f"{pin} UNLOCKED! ")
        time.sleep(1)
        # adding on score depending on attemps
        PIN_score = 20 - attempts
        total_score = score + PIN_score
        score = total_score
        # calling win function and end game
        win(name,score)

    else:
        print(f"Exceeded Attemps! Alarms are turned on!")
        time.sleep(1)
        lose(score)


def rock_paper_scissors():
    # Character choice
    player_choice = input("Choose rock, paper or scissors: ")

    # checking input recieved from player
    while player_choice not in ["rock", "paper", "scissors"]:
        print("Please Enter a Valid Choice: ")
        player_choice = input("Choose rock, paper, or scissors: ")

    # Jane's choice randomed from a list
    choices = ["rock", "paper", "scissors"]
    jane_choice = random.choice(choices)

    print(f"You chose {player_choice}")
    time.sleep(1)
    print(f"Jane chose {jane_choice}")

    # Determine the winner
    if player_choice == jane_choice:
        time.sleep(1)
        print("It's a tie! play again...")
        return rock_paper_scissors()

    # all cases of winning for player in the game
    elif (player_choice == "rock" and jane_choice == "scissors") or \
         (player_choice == "paper" and jane_choice == "rock") or \
         (player_choice == "scissors" and jane_choice == "paper"):
        time.sleep(1)
        print("You Win!")
        winner = "player" # value is used for scene1 actions
        return winner
    # Jane cases of winning
    else:
        time.sleep(1)
        print("Jane wins!")
        winner = "Jane" # value is used for scene1 actions
        return winner


# winning or losing pages, followed by score and play again option

def lose(score): 
    print(f"""
   
                     █▀▀ ▄▀█ █░█ █▀▀ █░█ ▀█▀
                     █▄▄ █▀█ █▄█ █▄█ █▀█ ░█░        ▄︻┻═┳一ཧᜰ꙰ꦿ➢         

░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░██╗
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗██║
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝██║
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗╚═╝
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║██╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝

Your score is {score}
Can you break your score! 

""")
    play_again = input("would you like to play again? y for yes, n for no: ")
    while play_again not in ["y","n","Y","N"]:
        print("please enter a valid choice Y or N: ")
        play_again = input("would you like to play again? ")
    if play_again.lower() == "y": 
        start()
    else: 
        sys.exit()

def win(name, score):
    print(f"""
          *************************
██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗  ███╗░░██╗██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║  ████╗░██║██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║  ██╔██╗██║██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║  ██║╚████║╚═╝
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║  ██║░╚███║██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝  ╚═╝░░╚══╝╚═╝
          *************************
        Congrats! {name} You saved millions of lives from Mad Guy evil plan!
         Your score is {score}
          """) 
    play_again = input("would you like to play again? y for yes, n for no: ")
    while play_again not in ["y","n","Y","N"]:
        print("please enter a valid choice Y or N: ")
        play_again = input("would you like to play again? ")
    if play_again.lower() == "y": 
        start()
    else: 
        sys.exit()

# Game starts with the sequence start() first_scene() 
# second_scene() rock_paper_scissors() third_scene() pin_guess()
# all the work flow is automated once start() runs. 
start()

