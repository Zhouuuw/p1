import sqlite3
import time
import random
import difflib

def Findlocations(inputkeyword):
    input_query = 'SELECT * FROM locations WHERE city  LIKE "' + inputkeyword + '%" ' \
                                                                                'UNION SELECT * FROM locations WHERE prov LIKE "' + inputkeyword + '%" ' \
                                                                                                                                                   'UNION SELECT * FROM locations WHERE address LIKE "' + inputkeyword + '%"'
    location_query = 'SELECT * FROM locations WHERE lcode ==   "' + inputkeyword + '" '
    locationsInRides = getData(location_query)
    locationsInRidesLists = list(locationsInRides)
    if isLcode(inputkeyword, list(locationsInRidesLists)) == False:

        output = getData(input_query)
        return output

    else:

        output = getData(location_query)
        for item in output:
            print(item)

        return output

def getunique():
    ##This function contributes to get a unique number in given list.


    rno_query = '''
                SELECT rno FROM rides
            '''
    rnosInRides = getData(rno_query)
    rnosInRidesLists = list(rnosInRides)
    rnosInRidesList = [item for sublist in rnosInRidesLists for item in sublist]



    while True:
        unique_no = random.randint(0, 1005)
        if unique_no not in rnosInRidesList:
            rnosInRidesList.append(unique_no)
            break
        else:
            continue
    return rnosInRidesList

def getData(input_query):
    global connection, cursor
    outputTuple =()
    cursor.execute(input_query)
    outputTuple = cursor.fetchall()
    connection.commit()
    return outputTuple


def isLcode(inputKeyWord,inputList):
    isLcode = False
    for item in inputList:
        if inputKeyWord == item[0]:
            isLcode = True
            break
        else:
            continue
    return isLcode


def selectLocation(intputkeywords):
    outputlists = []
    inputkeywordlist = intputkeywords.split(' ')
    for item in inputkeywordlist:
        output = Findlocations(item)
        outputlists.append(output)

    index = 0
    outputlist = [item for sublist in outputlists for item in sublist]
    for item in outputlist[:5]:
        index += 1
        print(str(index) + ": ", end='')
        print(item)
    if index >= 5:
        optionM = input("Do You Want To See More Matches? Y/N\n")
        if optionM.lower() == 'y':
            for element in outputlist[5:]:
                index += 1
                print(str(index) + ": ", end='')
                print(element)
            while True:
                try:
                    postion = int(input("Enter The Code To Select The Location\n"))
                    break
                except ValueError:
                    print("Invalid Code")
        elif optionM.lower() == 'n':
            while True:
                try:
                    postion = int(input("Enter The Code To Select The Location\n"))
                    break
                except ValueError:
                    print("Invalid Code")
        else:
            print("Invalid Option")
    else:
        while True:
            try:
                postion = int(input("Enter The Code To Select The Location\n"))
                break
            except ValueError:
                print("Invalid Code")

    print("You have Chosen: ", end='')
    insertTuple = outputlist[postion - 1]
    print(outputlist[postion - 1])

    return insertTuple


def login(username,pwd):
    global connection, cursor
    '''
    
    :param username: input_username
    :param pwd: input_pwd
    :return login success or failure
    '''

def connect(path):
    global connection, cursor
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()
    return

def offerRide():
    global connection,cursor

    givenRno = None
    givenPrice = None
    givenRdate = None
    givenSeats = None
    givenLugDesc = None
    givenSrc = None
    givenDst = None
    givenDriver = None
    givenCno = None

    givenPrice = input("Please enter price\n")
    givenRdate = input("Please enter date(YYYY-MM-DD)\n")
    givenSeats = input("Please enter seats\n")
    givenSrc = input("Please enter starting position\n")
    givenDst = input("Please enter destination\n")


    srclcode = selectLocation(givenSrc)[0]
    dstlcode = selectLocation(givenDst)[0]

    outputlists = []


    insert_query = ''' INSERT INTO rides(rno,price,rdate,seats,lugDesc,src,dst,driver,cno)
                  VALUES(?,?,?,?,?,?,?,?,?) '''

    option = input("Do you want to add any set of enrouted locations?  Y/N\n")
    if option.lower() == 'y':
        while True:
            try:
                inputkeyword = input("Please enter keyword(s), separated by space:\n")
                break
            except ValueError:
                print("Invalid KeyWords")
        enroutedlcode = selectLocation(inputkeyword)[0]

        givenCno = int(input("Enter The Car Number(Optional):"))


    elif option.lower() == 'n':
        print("Test")

















def searchRide(locations):
    global connection, cursor
    '''

    param locations: list
     contains 1-3 location keywords

    '''

    #do something
    return

def BookOrCancelBookings(isBook):
    global connection, cursor
    '''

    :param isBook: boolean value:
    isBook = true
    then do booking action
    else
    isBook =false
    then do cancel action
    :return: None
    '''
    return


def post_requests(rdate,pickup,dropoff,amount):
    global connection, cursor
    '''

    :param rdate: date
    :param pickup: char(5)
    :param dropoff: cahr(5)
    :param amount:  int
    :return: None
    comments: rid is set by system to a unique number
    '''
    return

def SearchOrDeleteRideRequests(isSearch):
    global connection, cursor
    '''

    :param isSearch:

    isBook = true
    then do search action
    else
    isBook =false
    then do delete action
    :return: None
    '''

    return

def main():
        global connection,cursor
        path = "./project1.db"
        connect(path)

        operation = input("Eneter Operation Code To Select:\n"
                          "1: Offer A Ride\n"
                          "2: Search For Ride\n"
                          "3: Book Members Or Cancel Bookings\n"
                          "4: Post Ride Request\n"
                          "5: Search And Deleter Ride Requests\n"
                          "Code:")

        if operation == '1':
            offerRide()
        elif operation == '2':
            searchRide()
        else:
            print("Invalid Code")


        connection.commit()
        connection.close()
        return


if __name__ == "__main__":
    main()