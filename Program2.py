# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user question and evaluate if the user has the correct question
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random

def random_number():
    first = random.randint(0,99)
    second = random.randint(0,99)
    question = first + second
    print(f"\nQuestion:")
    print(f"{first} + {second}")
    return question

def user_answer():
    global question
    question = random_number()
    user_answer = int(input("Enter your answer: "))
    return question == user_answer

def start():
    user_name = input("\nEnter your name: ")
    print(f"\nHI {user_name}, WELCOME TO ADDITION QUIZ!")
    print("\nThere would be 10 random addition question that you need to answer. ")
    print(input("\nPress 'enter' to proceed"))

    user_score = 0
    for i in range(10):
        correct_answer = user_answer()
        if correct_answer:
            user_score += 1
            print(f"Hi {user_name}, you got the correct answer!")      
        else:
            user_score = user_score    
            print(f"Hi {user_name}, you're wrong. The correct answer is {question}.") 

    print("\nPlease wait! We are processing your score.")
    print(input("\nPress 'enter' to proceed"))
    
    if user_score == 10:
        print(f"{user_name}, you got the total score of {user_score}/10.")
        print(f"\nExcellent! You got the perfect score.")
    elif user_score >= 5 and user_score == 9:
        print(f"{user_name}, you got the total score of {user_score}/10.")
        print(f"\nVery Good! Keep it up.")
    elif user_score >= 1 and user_score == 4:
        print(f"{user_name}, you got the total score of {user_score}/10.")
        print(f"\nGood! Needs improvement.")
    else:
        print(f"{user_name}, you got the total score of {user_score}/10.")
        print(f"\nBetter luck next time.")

start()
