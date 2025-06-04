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

    def get_score(self):
        """Return the current score of the user."""
        return self.score

    def get_name(self):
        """Return the name of the user."""
        return self.learner_name
    
    def update_score(self, new_score:str):
        """Update the learner score and write it to disk."""
        try:
            with open(f"{self.learner_name}.info", "at", encoding="utf-8") as score_file:
                score_file.write(f"{new_score}\n")
        except IOError as e:
            print("Piper: Oops, looks like there's been a problem updating your score on disk.")
            exit(-1)
        return 1

def write_score_file(user_name:str, score: int):
    """Write file to disk."""
    with open(f"{user_name}.info", "wt", encoding="utf-8") as score_file:
        score_file.write(f"{user_name}\n")
        score_file.write(f"{score}\n")
    return 1

def get_score(learner:Learner):
    try:
        with open(f"{learner.name}.info", "rt", encoding="utf-8") as score_file:
            dummy = score_file.readline()           # Reads the name in line 1
            current_score = score_file.readline()   # Reads the score in line 2
    except FileNotFoundError as e:
        print("Piper: Eek! Couldn't read your score file! I'll have to quit.")
        exit(-1)
    return current_score

def main():
    """Learn Python Data Types"""

    user_name:str
    print("\nPiper: Hello! This program will help you learn about Python data types.\n")
    print("Piper: What is your name? ", end="")
    user_name = input()
    print(f"Piper: Hi {user_name}, it's great to meet you! ")
    print("I'm Piper and I'll be teaching you about the different data types in Python.")
  
    # Create the Learner object
    learner = Learner(user_name)
    print(f"\nPiper: Ok, {learner.learner_name}. Before we get started, your current score is {learner.get_score()}.")
    print(f"Piper: I'm going to store a file in the current directory called {learner.get_name()}.info.")
    print("Piper: We'll use that to keep track of your score. Let's get started!")
    
    # Try to save the learner's name and current score.
    try:
        write_score_file(learner.get_name(), learner.get_score())
    except IOError as e:
        print(f"\nPiper: Oops! Something went wrong writing the file. Let's start again. [{e}]")
        exit(-1)

    print("Great! That seemed to work!")

    print("\n\n===== Starting with Lists ======\n")
    print("Piper: We'll start with Lists. Lists are like arrays found in C, but have more power.")
    print("Piper: Lists can hold a mixture of data types, including other lists!")
    print("Piper: To start, enter three integers seperated by commas: ", end="")
    values = input()
    print("Piper: Cool. By using the split() function, I can automatically split the string at each comma.")
    str_list = values.split(sep=",")

    # Let's declare an empty list when we need it. But I'm not happy about it.
    my_list = []
    for i in str_list:
        my_list.append(int(i))

    print(f"Piper: Like this: {my_list}. Oh. Right. I also had to convert them to ints. No biggie.")
    print("Piper: Looks like you can handle it from here. It takes too long for me to do all the talking!")

    # Some list functions
    my_list.append("Piper is cool.")    # Append a string
    my_list.append(5)                   # Append an int
    my_list.append([4,6])               # Append a list
    print(f"The list is: {my_list}")
    print(f"Part of the list by slicing is: {my_list[0:3:1]}")

    print("\nPiper: Hey great work! +10 points!")
    learner.update_score(learner.get_score + 10)

    # Check the current score.
    print(get_score(learner))

        
if __name__ == "__main__":
    main()
