# Program to convert a sentence into a wordlist and reverse it

# Input a sentence
sentence = input("Enter a sentence: ")

# Convert to wordlist
wordlist = sentence.split()
print("Original Word List:", wordlist)

# Reverse the wordlist
reversed_list = wordlist[::-1]
print("Reversed Word List:", reversed_list)

