import time
import math
import random

name = input("Enter your name: ")

print(f"Hello there, {name}")

def final_grade():
    repeat = True
    while repeat:
        time.sleep(.1)
        score = random.randint(50,100)
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F" 
        
        print(f"Your score was {score}")
        print(f"Your grade was {grade}")
        
        if score < 70:
            retake = input("Would you like to try again? (y/n)").lower()
            if retake != "y":
                repeat = False
final_grade()