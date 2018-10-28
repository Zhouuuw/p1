import sqlite3
import time
import random
import difflib

def Findlocations(inputkeyword):
    outputTuple=()
    input_query = 'SELECT * FROM locations WHERE city  LIKE "' + inputkeyword + '%" ' \
                                                                                'UNION SELECT * FROM locations WHERE prov LIKE "' + inputkeyword + '%" ' \
                                                                                                                                                   'UNION SELECT * FROM locations WHERE address LIKE "' + inputkeyword + '%"LIMIT 5'
    location_query = 'SELECT * FROM locations WHERE lcode ==   "' + inputkeyword + '" '
    locationsInRides = getData(location_query)
    locationsInRidesLists = list(locationsInRides)
    if isLcode(inputkeyword, list(locationsInRidesLists)) == False:
        i = 1
        output = getData(input_query)
        for item in output:
            print(str(i) + ': ', end='')
            print(item)
            i += 1
        code = input("Select The Location You Want:\n")
        outputTuple = tuple(output[int(code) - 1])
        return outputTuple

    else:

        output = getData(location_query)
        for item in output:
            print(item)
            outputTuple = tuple(item)
        return outputTuple

def getunique():
    ##This function contributes to get a unique number in given list.


    rno_query = '''
                SELECT rno FROM rides
            '''
    rnosInRides = getData(rno_query)
    rnosInRidesLists = list(rnosInRides)
    rnosInRidesList = [item for sublist in rnosInRidesLists for item in sublist]



    while(1):
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

connection = None
cursor = None

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
    inputkeyword =None


   # givenPrice = input("Please enter price\n")
   # givenRdate = input("Please enter date(YYYY-MM-DD)\n")
    #givenSeats = input("Please enter seats\n")
    #givenSrc = input("Please enter starting position\n")
    #givenDst = input("Please enter destination\n")

    option = input("Do you want to add any set of enrouted locations?  Y/N\n")
    print(option)
    inputkeyword = input("Please enter keyword(s):\n")

    if option.lower() == 'y' and inputkeyword is not None:
        print("You Had Chosen", end='')
        print(Findlocations(inputkeyword))
    else:
        print("Invalid Keyword(s)")













    #inputTuple = (givenRno,givenPrice,givenRdate,givenSeats,givenLugDesc,givenSrc,givenDst,givenDriver,givenCno)



    #do something





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