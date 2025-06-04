"""
Learn Python Data Types
"""

# Created by: Rick Henderson
# Created on: June 3, 2025

import re
import sys

class Learner:
    """A Learner object representing the user or learner."""

    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def get_score(self):
        """Return the current score of the user."""
        return self.score

    def get_name(self):
        """Return the name of the user."""
        return self.name

    def update_score(self, new_score: str):
        """Update the learner score and write it to disk."""

        # Do this or the score of the learner doesn't get updated.
        self.score = new_score
        try:
            with open(f"{self.name}.info", "at", encoding="utf-8") as score_file:
                score_file.write(f"{new_score}\n")
        except IOError as e:
            print(
                "Piper: Oops, looks like there's been a problem updating your score on disk."
            )
            sys.exit
        return 1


def write_score_file(user_name: str, score: int):
    """Write file to disk."""
    with open(f"{user_name}.info", "wt", encoding="utf-8") as score_file:
        score_file.write(f"{user_name}\n")
        score_file.write(f"{score}\n")
    return 1


def get_score(learner: Learner):
    """Get the score from the score file."""
    try:
        with open(f"{learner.name}.info", "r", encoding="utf-8") as score_file:
            dummy = (
                score_file.readlines()
            )  # Reads the whole file because score is not second line.
            if dummy:
                return dummy[
                    -1
                ].strip()  # returns the score from the last line, with no newline.
    except FileNotFoundError as e:
        print("Piper: Eek! Couldn't read your score file! I'll have to quit.")
        return None


def play_with_lists(learner: Learner):
    """Use different List methods."""
    print("\n\n===== Starting with Lists ======\n")
    print(
        "Piper: We'll start with Lists. Lists are like arrays found in C, but have more power."
    )
    print("Piper: Lists can hold a mixture of data types, including other lists!")
    print("Piper: To start, enter three integers seperated by commas: ", end="")
    values = input()
    print(
        "Piper: Cool. By using the split() function, I can automatically split the string at each comma."
    )
    str_list = values.split(sep=",")

    # Let's declare an empty list when we need it. But I'm not happy about it.
    my_list = []
    for i in str_list:
        my_list.append(int(i))

    print(
        f"Piper: Like this: {my_list}. Oh. Right. I also had to convert them to ints. No biggie."
    )
    print(
        "Piper: Looks like you can handle it from here. It takes too long for me to do all the talking!"
    )

    # Some list functions
    my_list.append("Piper is cool.")  # Append a string
    my_list.append(5)  # Append an int
    my_list.append([4, 6])  # Append a list
    print(f"The list is: {my_list}")
    print(f"Part of the list by slicing is: {my_list[0:3:1]}")

    print("\nPiper: Hey great work! +10 points!")
    learner.update_score(learner.get_score() + 10)

    print(f"Piper: There are now {len(my_list)} elements in the array.")
    last_item = my_list.pop()
    print(f"Piper: Popped {last_item} off the list.")
    my_list.insert(3, 3)  # Insert a 3 at the 4th position
    my_list.insert(5, 3)  # Insert a 3 at the 6th position
    print(
        f"Piper: There are now {my_list.count(3)} elements in the array with value 3. (I made some changes.)"
    )
    print(my_list)
    # my_list.sort()
    print(
        "Piper: Sorry, turns out I can't sort the list if the values are mixed types."
    )
    my_list.reverse()
    print(f"Piper: The list has been reversed! {my_list}: +15 points!")
    learner.update_score(
        learner.score + 15
    )  # Uses the memoic idiom of Python, as explained to me by Google Gemini.

    print(
        f"Piper: Hey! Your score is now {get_score(learner)}. Great stuff!"
    )  # Read score from file, just because.
    print(
        "Piper: You're hardcore. Clearing the list to save space for... tuples! Yay tuples!"
    )

    # Clear the list.
    my_list.clear()
    print(f"Piper: (And empty list looks like this: {my_list}).")


def play_with_tuples():
    """Learn with Tuples"""
    my_tuple = (4, 7, 3, 6, 7)
    print(my_tuple)
    count = my_tuple.count(7)
    print(f"The value 7 appears {count} times in the tuple.")
    print(f"The value 3 appears at {my_tuple.index(3)}.")
    try:
        index = my_tuple.index(2)
    except ValueError:
        print("Exception: The value 2 is not in the tuple. I checked.")
    finally:
        print("Piper: It's ok though, we can keep going.")

    ### Math with tuples? Never considered this with lists....
    x = (1, 5)
    y = (1, 6)
    result = x + y
    print(result)
    print("Piper: Looks like adding tuples just makes a bigger tuple. Weird eh?")


def play_with_dictionaries():
    """Work with Dictionaries."""
    print("\n ==========  Dictionaries ================")

    print(
        "Note: Dictonary items are ordered, changeable, and duplicates are not allowed."
    )
    malware_sample = {
        "malware_name": "BlackBasta",
        "malware_type": "ransomware",
        "threat_actor": "BlackBasta",
        "sha256": [
            "bade58de277d0b06d2c74b1181142a8b3288c4e44e8bf649a8899ed3c7eca276",
            "aa3f58e4d7ed6e3a4d3d619423e0a6c927d36e2ae7208dcaba5614e2507904c3",
            "f7fdbbcd974ddad321ae089b5ddb02ce92a1074fce403c6500db9e3ea0d2a8a5",
        ],
    }

    print("Created a dictonary for BlackBasta malware.")
    print(malware_sample)
    # print(f"Malware type: {malware_sample["malware_type"]}")
    print(
        f"{malware_sample['malware_name']} is still active, adding that to dictionary."
    )
    malware_sample["still_active"] = True
    malware_sample["bad_entry"] = "sfjk;alck"
    print(malware_sample)
    malware_sample.pop("bad_entry")

    print("\nAll the items:")
    for item in malware_sample.items():
        print(item)

    print("\nAll the keys:")
    for key in malware_sample.keys():
        print(key)

    print("\nAll the values:")
    for value in malware_sample.values():
        print(value)


def play_with_regular_expressions():
    """Work a bit with regular expressions, for they are tricky."""

    msg = "The quick brown fox jumped over the lazy dog."
    print("\n ==========  Regular Expressions ================")
    print(f"Using: {msg}")

    print("Using compiled pattern .*b.* and match():")
    pattern = re.compile(".*b.*")
    if pattern.match(msg):
        print("Found the letter b somewhere in the string.")

    result = re.match("^The", msg)
    if result:
        print("The word 'The' is at the beginning of the sentence.")

    malicious_command = "EXEC xp_cmdshell 'netstat -an';"
    used_netstat = re.match(".*netstat.*", malicious_command)
    if used_netstat:
        print(
            f"The `netstat` command is present in the malicious command IOC: {malicious_command}"
        )

    malicious_command = 'cscript C:\\Backinfo\\ufn.vbs <TargetIP> "C:\\Backinfo\\104.dll" C:\\Delta\\104.dll"'
    strange_dll = re.match(".*[0-9][0-9][0-9].dll.*", malicious_command)
    if strange_dll:
        print(
            "The command used a dll name matching the pattern '.*[0-9][0-9][0-9].dll.*'"
        )


def main():
    """Learn Python Data Types"""

    user_name: str
    print("\nPiper: Hello! This program will help you learn about Python data types.\n")
    print("Piper: What is your name? ", end="")
    user_name = input()
    print(f"Piper: Hi {user_name}, it's great to meet you! ")
    print(
        "I'm Piper and I'll be teaching you about the different data types in Python."
    )

    # Create the Learner object
    learner = Learner(user_name)
    print(
        f"\nPiper: Ok, {learner.name}. Before we get started, your current score is {learner.get_score()}."
    )
    print(
        f"Piper: I'm going to store a file in the current directory called {learner.get_name()}.info."
    )
    print("Piper: We'll use that to keep track of your score. Let's get started!")

    # Try to save the learner's name and current score.
    try:
        write_score_file(learner.get_name(), learner.get_score())
    except IOError as e:
        print(
            f"\nPiper: Oops! Something went wrong writing the file. Let's start again. [{e}]"
        )
        sys.exit

    print("Great! That seemed to work!")

    # Each of the sections can now be commented out to make life easier.
    # play_with_lists(learner)
    play_with_tuples()
    play_with_dictionaries()
    play_with_regular_expressions()

    print(
        f"\nPiper: Well you made it! Great work! Your final score is {learner.score}! Good luck in the interview, superstar! 🥰\n\n"
    )


if __name__ == "__main__":
    main()
