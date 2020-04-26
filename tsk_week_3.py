
input ("\nGame 1. Press any key to create a story.\n")
# This program is called STORYTELLER.
# You can create your character and I'll tell you a story about them.
# This program uses input() and format().
def storyteller():
    name = str (input("What is your character's name? "))
    while True:
        try:
            age = int (input("How old is " + name +"? "))
            break
            # input() is waiting for the user to enter their answer, and then stores it in a variable. 
        except:
            print("Enter a legit age, please. ")
 
    if age in range(1,100):
    # I could have also used >=	Greater than or equal to.
        story = "So, here's a story. Once upon a time {} went for a walk and got lost. What an embarrassing situation to find yourself in, when you're {}...\nTHE END.\n"
        # {} these two placeholders are empty now and will be filled with data later.
        print (story.format(name, age))
        # format() inserts the values stored in variables name and age into the two corresponding placeholders in the story string.
    
    else:
        print (name + " is either too old or too young for this story.\nTHE END.\n")

storyteller()
# Calling the function here.



input ("Game 2. Press any key to check if your word is a palindrome.\n")
# This program is called PALINDR-o-CHECK. 
# It checks whether a word is a palindrome or not.
# This program uses lower(), reversed() and list().

def palindr_o_check():
    word = str (input("What's your word? "))
    no_caps = word.lower()
    # lower() converts any caps in the string to lower register.
    
    word_reversed = reversed(no_caps)
    # reversed() reverses the string and converts it's content into an object (?).
    
    if list(no_caps) == list(word_reversed):
        # list() converts the objects into lists. == compares their contents.
        print(word + " is a palindrome!\nTHE END.\n")
    else:
        print (word + " is not a palindrome.\nTHE END.\n")

palindr_o_check()
# Calling the function here.