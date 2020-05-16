# This will take in a sentence and a letter and return all the words starting with the given letter.
def starting_letter():
    st = input("Please write a sentence here: ").lower().split()
    letter = input("Please enter a letter which you want the word to star with: ").lower().strip()
    result = [word for word in st if word[0] == letter]
    return result
# ---------------------------------------------------------------------------------------------------------
# return the lesser num if both are even and the bigger one if one or both are odd
def lesser_of_two_evens(sum1, sum2):
    if sum1 % 2 == 0 and sum2 % 2 == 0:
       return min(sum1, sum2)
    else:
        return  max(sum1, sum2)
    
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5
# ---------------------------------------------------------------------------------------------------------
# returns True if the first letter of both words are same
def animal_crackers(string):
    split_string = string.lower().split()
    return split_string[0][0] == split_string[1][0]

# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False
# ---------------------------------------------------------------------------------------------------------
# Return True if the sum of 2 numbers or either one of the two numbers is 20
def makes_twenty(sum1, sum2):
    return sum1 + sum2 == 20 or sum1 == 20 or sum2 == 20

# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False
# ---------------------------------------------------------------------------------------------------------
# Turn the first and the fourth letter capital
def first_n_forth_capital(word):
    first_half = word[:3].capitalize()
    sec_half = word[3:].capitalize()
    return first_half + sec_half

# first_n_forth_capital('macdonald') --> MacDonald
# ---------------------------------------------------------------------------------------------------------
# Turns the string backwards
def yoda_reverse(text):
   split_st = text.split()
   reverse_word_list = split_st[::-1]
   return " ".join(reverse_word_list)

def yoda_reverse_2(text):
    return " ".join(text.split()[::-1])
    
# yoda_reverse('I am home') --> 'home am I'
# yoda_reverse('We are ready') --> 'ready are We'
# ---------------------------------------------------------------------------------------------------------
# Returns True if the given number is within 10 of either 100 or 200
def almost_there(n):
    return abs(100-n) <= 10 or abs(200-n) <= 10

# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
# ---------------------------------------------------------------------------------------------------------
# Return True if there is a 3 right after another 3
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3:
            if nums[i + 1] == 3:
                return True
    return False

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
# ---------------------------------------------------------------------------------------------------------
# Returns the stringe with each letter x 3
def times_three(word):
    word1 = ""
    for letter in word:
        word1 += (letter * 3)
    return word1

# times_three('Hello') --> 'HHHeeellllllooo'
# times_three('Mississippi') --> 'MMMiiissssssiiippppppiii'

# ---------------------------------------------------------------------------------------------------------
# BlackJack
def blackjack(num1, num2, num3):
    if sum([num1, num2, num3]) <= 21:
        return sum([num1, num2, num3])
    elif 11 in [num1, num2, num3] and sum([num1, num2, num3]) <= 31:
        return sum([num1, num2, num3]) - 10
    else:
        return "BUST"
    
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
# ---------------------------------------------------------------------------------------------------------
# Does not count number between 6 and 9
def game_69(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

def game_69_two(lst):
    indx_6 = lst.index(6)
    indx_9 = lst.index(9, indx_6)
    return sum(lst[:indx_6]) + sum(lst[indx_9 + 1:])
    
# game_69([1, 3, 5]) --> 9
# game_699([4, 5, 6, 7, 8, 9]) --> 9
# game_699([2, 1, 6, 9, 11]) --> 14
# ---------------------------------------------------------------------------------------------------------
