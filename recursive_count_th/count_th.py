'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # First find if the word has one occurence if it does run count_th again
    #
    if "th" in word:
        print("yes")
    else:
        print("no")

count_th("this")