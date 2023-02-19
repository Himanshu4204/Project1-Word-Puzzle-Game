# import random module 
import random

# create a choose() function .which will return us 1 word.
def choose():
    # create a list of words 
    word_list=['python','mango','apple','java','banana','javascript','html','grapes','fig','language','monkey']
    # This will pick a random word from the list.
    default_word=random.choice(word_list)
    return default_word


# Create a shuffle() function.
def shuffle(word):
    # This will change the random word into a jumble word and return it.
    shuffle_word=''.join(random.sample(word, len(word)))
    return shuffle_word


# create result function().which will return us score of the game.
def result(score):
    print("your score is :",score)

# display a quit option on the screen       
print("(If you want to Quit Game Press 'Q' :)")

# create a play_game() function.
def play_game():

    score=0
    # these loop will run on 5 times Only
    for i in range(1,6):
         # call choose() function and assign the function value in pick_word   
        pick_word=choose()
        # call shuffle() function and assign the jumble word in the question variable
        question=shuffle(pick_word)
        print("Your word is :", question)  # Print word on the Screen.
        
        # input user word and assign in answer variable.
        answer=input("Enter your Guess Word in Lower case:")
        
        # check if answer and pick-word are same. then increment score by 1
        if answer==pick_word:
            score+=1
        elif answer=='Q': # if answer is Q then break the function and show result.
            break
        else:   # decrement score by 1
            score-=1
    # call result function
    result(score)   
# call play_game function
play_game()