print("helo")

numbers = [1111111111,2222222222,3333333333,4444444444,5555555555,6666666666,7777777777] # list number
names = ['Amal','Mohammed','Khadijah','Abdullah','Rawan','Faisal','Layla'] # list names

def numbers():
    numbers = input('your number new?')
    if len(numbers)>10 or len(numbers)<10:
        print('this is invalid number')
    elif numbers.isdigit() == False:
        print('this is invalid number')
    elif numbers == str(1111111111):
        print('Amal')
    elif numbers == str(2222222222):
        print('Mohammed')
    elif numbers == str(3333333333):
        print("Khadijah")
    elif numbers == str(4444444444):
        print("Abdullah")
    elif numbers == str(5555555555):
        print("Rawan")
    elif numbers == str(6666666666):
        print('Faisal')
    elif numbers == str(7777777777):
        print('Layla')
    else:
        print('Sorry, the number is not found')
numbers()

def names():
    names = input('your name ')
    if names == 'Amal':
        print(int(1111111111))
    elif names == "Mohammed":
        print(int(2222222222))
    elif names == 'Khadijah':
        print(int(3333333333))
    elif names == 'Abdullah':
        print(int(4444444444))
    elif names == 'Rawan':
        print(int(5555555555))
    elif names == 'Faisal':
        print(int(6666666666))
    elif names == 'Layla':
        print(int(7777777777))
names()

