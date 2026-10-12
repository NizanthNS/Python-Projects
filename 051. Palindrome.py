# PALINDROME

text = input("Enter the Text: ").lower()

def palindrome(my_text):

    reverse_text = my_text[::-1]

    if reverse_text == my_text:
        print("It's Palindrome")
    else:
        print("It's not Palindrome")

palindrome(text)
