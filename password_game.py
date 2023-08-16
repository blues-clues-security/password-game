import re
from flask import url_for

def check_rule1(password):
    return 1, len(password) >= 5, "Your password must be at least 5 characters.", {}

def check_rule2(password):
    return 2, any(char.isdigit() for char in password), "Your password must include a number.", {}

def check_rule3(password):
    return 3, any(char.isupper() for char in password), "Your password must include an uppercase letter.", {}

def check_rule4(password):
    return 4, any(char in '!@#$%^&*()-_=+[{]};:\'",<.>/?' for char in password), "Your password must include a special character.", {}

def check_rule5(password):
    digits = [int(char) for char in password if char.isdigit()]
    return 5, sum(digits) == 25, "The digits in your password must add up to 25.", {}

def check_rule6(password):
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    return 6, any(month in password for month in months), "Your password must include a month of the year.", {}

def check_rule7(password):
    numerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    romans = list(numerals.keys())
    return 7, any(roman in password for roman in romans), "Your password must include a roman numeral.", {}

def check_rule8(password):
    sponsors = ['usaf','lions','salt']
    sponsor_images = {
        'usaf': '/static/usaf.png',
        'lion': '/static/lions.jpg',
        'salt': '/static/salt.jpg'
    }
    return 8, any(sponsor in password for sponsor in sponsors), "Your password must include one of our sponsors.", sponsor_images

def check_rule9(password):
    numerals = {'IV':4,'III':3,'II':2,'I':1,'V':5,'VII':7,'VI':6,'VIII':8,'X':10,'L':50,'C':100,'D':500,'M':1000,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    i = 0
    roman_numerals = []
    while i < len(password):
        if i + 1 < len(password) and password[i:i+3] in numerals:
            roman_numerals.append(numerals[password[i:i+3]])
            i += 2
        elif password[i] in numerals:
            roman_numerals.append(numerals[password[i]])
            i += 1
        else:
            i += 1
    product = 1
    for numeral in roman_numerals:
        product *= numeral

    return 9, product == 35, "The roman numerals in your password should multiply to 35.", {}

def display_rules(rules):
    for rule in rules:
        print(rule[1])

def main(password):
    rules = [
        check_rule1,
        check_rule2,
        check_rule3,
        check_rule4,
        check_rule5,
        check_rule6,
        check_rule7,
        check_rule8,
        check_rule9
    ]

    satisfied_rules = []
    unsatisfied_rules = [rule for rule in rules]

    n = 0
    message = "Password does not satisfy the current rule."
    sponsor_images = {}
    while n < len(rules):
        rule_result = rules[n](password)
        rule_num, check, description = rule_result[:3]
        if n == 7: # Rule 8
            rule_num, check, description, sponsor_images = rules[n](password)
        if check:
            satisfied_rules.append(description)
            message = f"Password accepted for Rule: {rule_num}"
            n += 1
        else:
            break

    if n < len(rules):
        next_rule = rules[n](password)[2]
    else:
        next_rule = "You have successfully created a password that meets all the rules."
    
    return message, next_rule, satisfied_rules, sponsor_images
#password = 'password1P!55554OctobersaltVIIrV'
if __name__ == "__main__":
    main()
    #main(password)
