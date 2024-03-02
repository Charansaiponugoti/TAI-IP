import re

def validate_credit_card(card_number):
    # Remove non-numeric characters from the input
    card_number = re.sub(r'\D', '', card_number)
    
    # Check if the card number is 16 digits long and contains only digits
    if len(card_number) != 16 or not card_number.isdigit():
        return False
    
    # Apply the Luhn algorithm to validate the card
    total = 0
    for i, digit in enumerate(card_number[::-1]):
        num = int(digit)
        total += num if i % 2 == 0 else num * 2 - 9 if num * 2 > 9 else num * 2
    
    return total % 10 == 0

# Accept a credit card number as input
card_number = input("Enter your credit card number: ")

# Call the function to validate the card and print the result
if validate_credit_card(card_number):
    print("Valid credit card number!")
else:
    print("Invalid credit card number.")