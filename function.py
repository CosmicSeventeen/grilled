function
groceries = ['spoons', 'forks', 'pots', 'pans', 'knives']
print('spoons')
print('forks')
print('pots')
print('pans')
print('knives')
9.42+5.57+3.25+13.40+7.50
9.42+5.57+3.25+13.40+(7.50*5)
print('rice', 'bread', 'spoons', 'forks', 'pans')
def all_the_snacks(snack):
    print( snack * 100)
all_the_snacks('spoons ')
def another_all_the_snacks(c, n):
    return c * n
another_all_the_snacks('bread', 100)
 def grocery_list(item):
          g_list = ('rice', 'bread', 'spoons', 'forks', 'pans')
          if item in g_list:
              return True
          else:
              return: False 
grocery_list('gummies')
grocery_list('rice')
 def price_matcher():
     grocery_list = ('rice', 'bread', 'spoons', 'forks', 'pans')
     prices = (9.42, 5.57, 3.25, 13.40, 7.50)
     print(random.choice(grocery_list) + " ", random.choice(prices))
price_matcher()
price_matcher()
price_matcher()
price_matcher()
price_matcher()
def all_the_snacks(snack, spacer= ' , ', number=100):
    print((snack + spacer) * 100)
all_the_snacks('cocopuffs') 
 snacks = ['rice', 'bread']
for snack in snacks:
    all_the_snacks(snack) 
 def all_the_snacks(snack, spacer= ' , ', number=100):
     print((snack + spacer) * 100)
all_the_snacks('plantain chips', '!')
all_the_snacks('plantain chips', ' ')
all_the_snacks('plantain chips', number=42)
all_the_snacks('gummies', number=42, spacer='>>>')
def april_fool_swapper():
    my_color = input("please enter your favorite color: ")
    neighbors_color = input("please enter your nighbors favorite color: ")
    print("my favorite color is " + my_color)
    print("my neighbors favorite color is " + neighbors_color)
    print("my favorite color is " + neighbors_color)
    print("my neighbors favorite is " + my_color)
    april_fool_swapper()
