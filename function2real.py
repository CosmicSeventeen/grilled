def isdivisibleby7(num):
    if num % 7 == 0:
        return True
    else:
        return False
isdivisibleby7(21)
isdivisibleby7(24)
def shout(word):
    print(word.upper() + "!")
shout('cosmic')
def introduce():
    name = input('please enter your name: ')
    print('hello ' + name.upper() + '!')
introduce()
def snack_check(snack):
    favorite_snack = 'sour patch'
    if snack == favorite_snack:
        return True
    else:
         return False
snack_check('gummies')
snack_check('sour patch')     
def snack_check(snack):
    favorite_snack = 'sour patch'
    if snack == favorite_snack:
        print('aww, thats so cute')
    else:
        print('really?!?!, what makes you think i like such a thing')
snack_check('bread')
snack_check('sour patch')
grocery_item = 'bread'
type(grocery_item) == str
grocery_item = 25
type(grocery_item) == str
def in_grocery_list(grocery_item):
    if type(grocery_item) == str:
        pass
    else:
        print("WARNING: the item you entered is not a string")
grocery_item = 'bread'
import random
def you_won():
    price_list = [9.42, 5.57, 3.25, 13.40, 7.50]
    if random.choice(price_list) >= 10:
        return True
you_won()
you_won()
import datetime
def return_current_times():
    now = datetime.datetime.now()
    current_time = now.strftime('%H:%M:%S')
    if now.hour >= 7 and now.hour < 12:
        print(current_time, ": Morning Classes")
    elif now.hour > qw and now.hour <= 17:
        print(current_time, ": Afternoon Classes")
    elif now.hour > 17 and now.hour <= 22:
        print(current_time, ": Evening Classes")
    else:
        print(current_time, "why are you still in school")
return_current_time()
def volume(length, width, height):
    return length * width * height
volume(2, 5, 10)   