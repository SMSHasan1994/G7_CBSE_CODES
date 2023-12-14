#1. Write a program to check if a String is palindrome or not

#A palindrome is a word, phrase, number, or sequence of characters
#that reads the same backward as forwards, like "madam," "racecar," or "level."

def isPalindrome(string):
    return string == string[::-1]
 
 
#String
string = "level"
#string = "racecar"
#string = "madam"
#string = "hi"

#Check whether the String is a palindrome
ans = isPalindrome(string)
 
if ans:
    print("Yeah, it is a plaindrome")
else:
    print("No, it is not a plaindrome")
