#Hello world
print('Snowball numbers! \n')
print('Would you like to have a specific number or a range of numbers?')
print('You can also get information by typing info')
print('Type -999 to end')
ended = False

num = 0
length = 0
highlength = [0, 0]

def change_number():
    global num, length
    print(int(num))

    num = int(num)
    if num % 2 == 1:
        num = num * 3 + 1
    elif num % 2 == 0:
        num = num / 2

    if num != 1:
        length += 1
        change_number()
    else:
        print('done')

while ended == False:
    mode = input('0 for specific number, 1 for a range, or type info or -999')
    num = 0
    length = 0
    highlength = [0, 0]

    if mode == '0':
        num = input('\n Which number?')
        change_number()
        print('Length:', length)
        print('\n')
    elif mode == '1':
        least = int(input('Lower number:'))
        most = int(input('Max number:'))

        for thing in range(least, most):
            length = 0
            num = thing

            print(num)
            change_number()

            print('Length:', length)
            if length > highlength[0]:
                highlength[0] = length
                highlength[1] = thing
            print('\n')
        
        print('\n')
        print('Longest length:', highlength[0], 'from number', highlength[1])

    elif mode == 'info':
        print('\n The snowball number sequence is truly unique.')
        print('Any input integer can be used in the sequence. \n')
        print('If the number or n is odd, it changes to 3n+1.')
        print('If n is even, it is merely divided by 2.')
        print('When the sequence goes to 1, it ends. If it continues, it will go in a loop. \n')
        print('This simple sequence gave rise to lots of pondering.')
        print('There is a conjecture that every number will eventually reach 1.')
        print('Besides mathematicians working to prove or disprove this, you can')
        print('also dig deeper into number theory and tinker with the sequence.')
        print('\n Have fun with this calculator!')

    elif mode == '-999':
        ended = True

    else:
        print('Error. Try again.')


print('we are done here')
