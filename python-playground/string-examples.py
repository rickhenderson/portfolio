from copy import copy, deepcopy
# I created wrote this code as a way to beef up my Python skills.
# The main impetus was for a job interview with Google as a Security Engineer. Some of the examples are based on a previous interview I had with SunLife, 
# and others are based on suggestions from Grace Nolan's repo: https://github.com/gracenolan/Notes/blob/master/interview-study-notes-for-security-engineering.md.

# String subset, string slicing
# * string[start:stop:step]
# Quite honestly, when I first learned Python I thought this was a stupid trick to perform string manipulation. obfu_string[::-1] certainly isn't a readable or intuitive way to reverse a string.
# In three years of writing Python scripts for product security, automation, and poc I never used string slicing.

# Iterables are memory efficient. You don't have to load the entire object or stream into memory at once.
# For later: https://www.geeksforgeeks.org/5-simple-ways-to-tokenize-text-in-python/

def print_list():
    print("[+] A list is a collection of objects in parens seperated by commas.")
    my_list = ("AI", 4, "Jess", "kess"[:2:])
    print(f"[+] The list: {my_list}")
    for item in my_list:
        print(item)

def print_tuple():
    print("[+] A tuple is a collection of objects in brackets seperated by commas.")
    my_tuple = (100, 65, 344) # Minecraft location
    print(f"[+] The tuple is: {my_tuple}")
    for item in my_tuple:
        print(item)

def print_string():
    print("[+] A string is a collection of characters in quotation marks - double or single.")
    my_string = "Splitgate2"
    print(f"[+] The string is: {my_string}")
    for item in my_string:
        print(item)

def reverse(string_to_reverse):
    # a_string[start:stop:step]
    return string_to_reverse[::-1]

def shallow_copy(string_to_copy):
    print("[!] Shallow copy will point to the same nested object as the original. Faster and memory efficient. Uses copy.copy().")
    print("[!] String slicing is a shallow copy.")
    new_copy = copy(string_to_copy)
    print(new_copy)

def deep_copy(string_to_copy):
    print("[!] This deep copy creates a new object so the original is not modified.")
    new_copy = deepcopy(string_to_copy)
    print(new_copy)

def main():
    msgtext = "The quick brown fox."
    print(f"Message text: {msgtext}")
    print(f"Reversed text: {reverse(msgtext)}")

    # Display various iterables. Iterables use an iterator to display each item.
    print_list()
    print_tuple()
    print_string()
    
    print("\n[+] Shallow and deepcopy:\n")
    shallow_copy("Kurgan")
    print("[+] Deep copies create new objects.")
    deep_copy("MacLeod")

if __name__ == "__main__":
    main()
