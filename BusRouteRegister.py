#DorgyBus Passenger Transportation

#Global Variables
AuxList = []
BusList = ''
Change = False

#1 - Add Serial Number of Bus Route
def numRoute(num=''):
    NumRoute = input('Number of Bus Route: ')
    if NumRoute == '' or NumRoute.isalpha():
        NumRoute = num
    return NumRoute

#2 - Add Bus Route
def BusRoute(line=''):
    Route = input('Name of Bus Route: ')
    if Route == '':
        Route = line
    return Route

#3 - Search The Bus Route.
def Search(number):
    Number = number
    for e, p in enumerate(BusList):
        if p[0] == Number:
            return e

#4 - Add New Bus Line
def register():
    global AuxList, BusList, Change
    Numroute = numRoute()
    if Numroute not in AuxList:
        Busroute = BusRoute()
        AuxList.extend([Numroute, Busroute])
        BusList = [AuxList[i:i+2] for i in range(0, len(AuxList), 2)]
        print('Line registered!')
        Change = True
    else:
        print('Number already registered in our system.')
        Change = False

#5 - Confirm Change/Delete?
def Confirm(op):
    while True:
        print('Do You Want to Change? Y or N')
        op = input('Answer: ').upper()
        if op in 'YN':
            return op
        else:
            print('Invalid Option!')

#6 - Change info about Bus Line
def ChangeRoute():
    global Change
    search = Search(numRoute())
    if search != None:
        numline = BusList[search][0]
        nameline = BusList[search][1]
        print('Bus line found!')
        newNum = numRoute(numline)        
        if newNum in BusList[search][0]:
            print('Number already registered in our system.')
            Change = False
        else:
            print('Number of Bus Line modified.')
            Change = True
            if Confirm('Change') == 'Y':
                BusList[search] = [newNum, newRoute]
                Change = True        
        
        newRoute = BusRoute(nameline)
        if newRoute in BusList[search][1]:
            print('Bus Route already registered in our system.')
            Change = False
        else:
            print('Number of Bus Line modified.')
            Change = True
        
            if Confirm('Change') == 'Y':
                BusList[search] = [newNum, newRoute]
                Change = True
    else:
        print('Bus Line Not Found.')
        Change = False

#7 - Delete Bus Line
def DeleteRoute():
    global BusList, Change
    NUM = numRoute()
    search = Search(NUM)
    if search != None:
        if Confirm('Delete') == 'Y':
            del BusList[search]
            Change = True
    else:
        print('Bus Line Number Not Found.')
        Change = False

#8 - Show the Bus List
def ShowLines():
    global BusList
    print(BusList)

#9 - Main Program
def main():
    again = 'Y'
    while again == 'Y':
        print()
        print('{:80}'.format('DorgyBus Passenger Transportation\n1-Add\n2-Change\n3-Delete\n4-Show List\n5-Exit'))
        print()
        opt = input('Choose Your Option: ')
        if opt == '1':
            register()
        elif opt == '2':
            ChangeRoute()
        elif opt == '3':
            DeleteRoute()
        elif opt == '4':
            ShowLines()
        elif opt == '5':
            print('Leaving The System...')
            break
        
        print()
        print('Do you want to do any more operations? Y or N')
        print()
        again = input('Answer: ').upper()
        if again == 'N':
            print('Shutdown!!!')
            exit()
    else:
        print('Invalid Option!!!')

main()
    





