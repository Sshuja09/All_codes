# This will take in a sentence and a letter and return all the words starting with the given letter.
def starting_letter():
    st = input("Please write a sentence here: ").lower().split()
    letter = input("Please enter a letter which you want the word to star with: ").lower()
    result = [word for word in st if word[0] == letter]
    return result
