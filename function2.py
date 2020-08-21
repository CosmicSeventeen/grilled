def sumofmultiples():
     multiples = []
     for number in range (1, 1000):
        if number % 3 == 0 and number % 5==0:
             multiples.append(number)
        elif number % 3==0 or number % 5==0:
                 multiples.append(number)
        else:
           print(number, 'this number is not a multiple of 3 or 5')
     return sum(multiples)
sumofmultiples()
def duplicates(lst):
    new_list=[]
    for i in lst:
        if lst.count(i) > 1:
            new_list.append(i)
        else:
            print('i is not duplicate')
    return new_list
paul = [1,2,3,4,5,6,4,3,6]
duplicates(paul)
def duplicates(lst):
    new_list=[]
    for i in lst:
        if lst.count(i) > 1:
            if i in new_list:
                pass
            else:
                new_list.append(i)
        else:
                 print('i is not duplicate')
         return new_list
duplicates(paul)

In [27]: def get_user_info():
         name = input('please enter your full name: ')
         address = input('please enter your address: ')
         zip_code = input('please enter your zipcode: ')
         age = input('please enter your age: ')
         hair_color = input('please enter your hair color: ')
         eye_color = input('please enter your eye color: ')
         user_info = {'name':name,'address':address,'zipcode':zip_code,'age':age,'hair color':hair_color,'eye color':eye_color}
         for k in user_info.items():
             print(k)
get_user_info