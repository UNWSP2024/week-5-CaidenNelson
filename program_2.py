import random

#create number display and define numbers
def number_display():
    global number1
    global number2
    number1 = (random.randint(1, 1000))
    number2 = (random.randint(1, 1000))
    print(number1,'+',number2)
#find user input and determine if they are correct or incorrect
def answer():
    correct = number1 + number2

    user_ans = int(input("what is the sum of these two numbers? "))
    if user_ans == correct:
        print("You are correct.")
    else:
        print("Incorrect answer.")
#define more
more = input("would you like to take a simple math quiz? y for yes ")
#create game
while more == 'y':
    #call number display
    number_display()
    #call answer
    answer()
    #find if user wants to keep playing
    more = input('Would you like to play again? y for yes ')
#exit game if user no want to play
if more != 'y':
    print("Goodbye")
# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect a message showing the correct answer should be displayed.
# The program must use a function that accomplishes part of the needed tasks.
