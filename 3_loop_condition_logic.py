#Task 1: Loop Condition Exploration

while True:
    infinity = input('Would you like to break the loop? (yes/no)')

    if infinity == 'yes':
        print('Loop broken!')
        break
    else:
        print('Wrong, youre stuck forever!')

#Task 2: Conditional Exit

list_1 = ['#1','#2','#3','#4','#5']
index = 0

while index < len(list_1):
    print('This is iteration', list_1[index])
    index += 1