print("PALINDROME HUNT!")

user_input = raw_input("Please enter a word: ")

reverse_string = user_input[::-1]


print("User input is: \"" + user_input + "\"")

print("The reverse user input is: \"" + reverse_string + "\"")

if reverse_string.lower() == user_input.lower():
    print("Yes, it is a Palindrome!")
else:
    print("Nope, it's not a Palindrome")
