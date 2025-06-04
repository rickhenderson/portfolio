""" 
    Learn Python Data Types
"""

# Created by: Rick Henderson
# Created on: June 3, 2025

class Learner():
    """A Learner object representing the user or learner."""
    def __init__(self, learner_name:str):
        self.learner_name = learner_name
        self.score = 0


def main():
    """Learn Python Data Types"""

    user_name:str
    print("\nPiper: Hello! This program will help you learn about Python data types.\n")
    print("Piper: What is your name? ", end="")
    user_name = input()
    print(f"Piper: Hi {user_name}, it's great to meet you! ")
    print("I'm Piper and I'll be teaching you about the different data types in Python.")
    print()

if __name__ == "__main__":
    main()
