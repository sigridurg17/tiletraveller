#player byrjar á (1,1)
#Það eru áttirnar norður, suður, austur og vestur 
#1,1) => N
#(1,2) => N & S & E
#(1,3) => S & E
#(2,3) => E & W
#(2,2) => S & W
#(2,1) => N
#(3,3) => S & W
#(3,2) => N & S
#(3,1) => Victory
#Valmöguleiki poopar upp þegar mapur velur direction
#Ef það er valið átt sem er ekki í boði "Not a valid direction"

north = '(N)orth'
east = '(E)ast'
west = '(W)est'
south = '(S)outh'
travel = 'You can travel: '
a = 1
b = 1


while b < 4: #notum while til þess að loopa
    location = str(a) + str(b)
        
    if location == '11': #erum á 1,1
        print(travel + north + '.')
        direction = str(input("Direction: "))
        if direction in 'nN':
            b = 2
        else:
            print("Not a valid direction!")
            direction = str(input("Direction: "))
            if direction in 'nN':
                b = 2
            else:
                print("Not a valid direction!")

    elif location == '12': #erum stödd á 1,2
        print(travel + north + ' or ' + east + ' or ' + south + '.')
        direction = str(input("Direction: "))
        if direction in 'nN': #1,3
            b = 3 
        elif direction in 'sS': #1,1
            b = 1
        elif direction in 'eE': #1,2
            a = 2
        else:
            print("Not a valid direction!")
            direction = str(input("Direction: "))
            if direction in 'nN': 
                b = 3 
            elif direction in 'sS':
                b = 1
            elif direction in 'eE':
                a = 2
            else:
                print("Not a valid direction!")

    elif location == '13':
        print(travel + east + ' or ' + south + '.')
        direction = str(input("Direction: "))
        if direction in 'eE':
            a = 2
        elif direction in 'sS':
            b = 2
        else:
            print("Not a valid direction!")
            direction = str(input("Direction: "))
            if direction in 'eE':
                a = 2
            elif direction in 'sS':
                b = 2
            else:
                print("Not a valid direction!")

    elif location == '21': #stödd á 2,1
        print(travel + north + '.')
        direction = str(input("Direction: "))
        if direction in 'nN': #verður 2,2
            b = 2 
        else:
            print("Not a valid direction!")
            direction = str(input("Direction: "))
            if direction in 'nN':
                b = 2
            else:
                print("Not a valid direction!")

    elif location == '22': #stödd á 2,2
        print(travel + south + ' or ' + west + '.')
        direction = str(input("Direction: "))
        if direction in 'sS': #stödd á 2,1
            b = 1
        elif direction in 'wW': #stödd á 1,2
            a = 1
        else:
            print("Not a valid direction!")
            direction = str(input("Direction: "))
            if direction in 'sS':
                b = 1
            elif direction in 'wW':
                a = 1
            else:
                print("Not a valid direction!")

    elif location == '23': #stödd á 2,3
        print(travel + east + ' or ' + west + '.')
        direction = str(input("Direction: "))
        if direction in 'eE': #stödd 3,3
            a = 3
        elif direction in 'wW': #stödd 1,3
            a = 1
        else:
            print("Not a valid direction!")
            direction = str(input("Direction: "))
            if direction in 'eE': 
                a = 3
            elif direction in 'wW':
                a = 1
            else:
                print("Not a valid direction!")

    elif location == '33': #stödd á 3,3
        print(travel + south + ' or ' + west + '.')
        direction = str(input("Direction: "))
        if direction in 'sS': #3,2
            b = 2
        elif direction in 'wW': #2,3
            a = 2
        else:
            print("Not a valid direction!")
            direction = str(input("Direction: "))
            if direction in 'sS':
                b = 2
            elif direction in 'wW':
                a = 2
            else:
                print("Not a valid direction!")

    elif location == '32': #stödd á 3,2
        print(travel + north + ' or ' + south + '.')
        direction = str(input("Direction: "))
        if direction in 'sS': #3,1
            b = 1
        elif direction in 'nN': #3,3
            b = 3
        else:
            print("Not a valid direction!")
            direction = str(input("Direction: "))
            if direction in 'sS':
                b = 1
            elif direction in 'nN':
                b = 3
            else:
                print("Not a valid direction!")
        
    else:
        print('Victory!')
        a = 5
        b = 5