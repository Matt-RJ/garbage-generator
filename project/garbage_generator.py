import os
import random
import string
import json

extra_chars = ["!","?","$","#"]
forenames = json.loads(open("data/forenames.json").read())
surnames = json.loads(open("data/surnames.json").read())
random_words = json.loads(open("data/random_words.json").read())
email_domains = ["yahoo.com", "yahoo.co.uk", "yahoo.ie",
                 "gmail.com","gmail.net","gmail.co.uk","gmail.ie",
                 "hotmail.com","outlook.com",
                 "inbox.com","inbox.net","inbox.co.uk","inbox.ie",
                 "mail.com","mail.net","mail.co.uk","mail.ie"]


def generateRandomEmail():
    """Generates a random bogus email"""
    forename = random.choice(forenames).lower()
    surname = ""
    has_surname = random.choice([True,False])
    middle_digit_count = 0
    middle_digits = ""
    end_digit_count = random.randint(0,6)
    end_digits = ""

    if (has_surname):
        surname = random.choice(surnames).lower()
        has_middle_numbers = random.choice([True,False])
        middle_digit_count = random.randint(1,4)

    for digit in range(middle_digit_count):
        middle_digits = middle_digits + random.choice(string.digits)

    for digit in range(end_digit_count):
        end_digits = end_digits + random.choice(string.digits)

    surname_first = random.choice([True,False])
    if(surname_first):
        forename,surname = surname,forename

    email = forename + middle_digits + surname + end_digits + "@" + random.choice(email_domains)
    return email

def generateRandomPassword():
    """Generates a random bogus password. Warning: Security is not guaranteed, do not use them for actual accounts."""
    word_count = random.randint(2,3)
    password = ""
    words = []

    for word in range(word_count):
        new_word = random.choice(random_words)
        has_capital = random.choice([True,False])
        if (has_capital == True):
            new_word.capitalize()
        else:
            new_word = new_word.lower()
        words.append(new_word)

    extra_digit_count = random.randint(1,4)
    extra_digits = ""
    for digit in range(extra_digit_count):
        extra_digits += random.choice(string.digits)
    
    password = ""
    for word in words:
        password += word

    password += extra_digits

    has_extra_char = random.choice([True,False])
    extra_char = ""
    if (has_extra_char):
        extra_char = random.choice(extra_chars)

    password += extra_char
    return password

