import random
import array

MAX_LEN =int(input("enter the desired length"))

DIGITS = ['0','1','2','3','4','5','6','7','8','9']
LOWCASE_CHAR = ['a','b','c','d','e','f','g','h',
                'i','j','k','l','m','n','o','p',
                'q','r','s','t','u','v','w','x','y','z']
UPCASE_CHAR = ['A','B','C','D','E','F','G','H',
               'I','J','K','L','M','N','O','P',
               'Q','R','S','T','U','V','W','X','Y','Z']
SYMBOLS = ['!','@','#','$','%','^','&','*','(',')',':','<','>','.','?','/','~']

COMBINED_LIST = DIGITS + LOWCASE_CHAR + UPCASE_CHAR + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHAR)
rand_lower = random.choice(LOWCASE_CHAR)
rand_symbol = random.choice(SYMBOLS)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
for x in range(MAX_LEN-4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)

    temp_pass_list = array.array('u',temp_pass)
    random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
    password = password+x


print("your password is:",password)