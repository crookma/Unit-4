# By: Magnus Crooke, File Name: unit4.py, last modified: 9-29-2017, This program creates an equation for the user
import random


def main():
    """
    :return: This functions asks user what the highest number they would like to deal with, and asks what kind of
    equation the user would like to try and telling them if they got the equation right or not.
    """
    max_number = int(input("What is the maximum number you would like to deal with?"))
    numberone = random.randint(1, max_number)
    numbertwo = random.randint(1, max_number)
    equation_type = input("What kind of equation would you like: +, -, or *")

    if equation_type == "+":
        print("What is", numberone, "+", numbertwo, "?")
        question_answer = int(input())
        addition = numberone + numbertwo
        if question_answer == addition:
            print("Nice Job you got it right!")
        else:
            print("Sorry that's wrong, the answer is", " ", addition)

    elif equation_type == "-":
        print("What is", numberone, "-", numbertwo, "?")
        question_answer = int(input())
        subtraction = numberone - numbertwo
        if question_answer == subtraction:
            print("Nice Job you got it right!")
        else:
            print("Sorry that's wrong, the answer is", " ", subtraction)

    elif equation_type == "*":
        print("What is", numberone, "*", numbertwo, "?")
        question_answer = int(input())
        multiply = numberone * numbertwo
        if question_answer == multiply:
            print("Nice Job you got it right!")
        else:
            print("Sorry that's wrong, the answer is", " ", multiply)

    else:
        print("What is", numberone, "+", numbertwo, "?")
        addition = numberone + numbertwo
        question_answer = int(input())
        if question_answer == addition:
            print("Nice Job you got it right!")
        else:
            print("Sorry that's wrong, the answer is", " ", addition)

main()
