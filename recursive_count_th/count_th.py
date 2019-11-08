'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # First find if the word has one occurence if it does run count_th again
    # Base case will be when there are no more "th" in a word
    # When base case is met retuirn the number

    #Need to figure out how to remove only the first occurence of th for the recuresive call
    count = 0
    if "th" in word:
        count += 1
        print("yes", count)
    else:
        print("no")
        return 

    count_th("this")

count_th("thisth")