import sqlite3
import time

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

def offerRide(rdate,seats,price,lugDesc,src, dst):
    global  connection,cursor
    '''
    option of adding and any set of enroute location
    
    rno		    int,   automatically assign a unique ride number and set the member as the driver of the ride
    price		int,    
    rdate		date,
    seats		int,
    lugDesc	    char(10), 
    src		    char(5),
    dst		    char(5),
    driver	    char(15),
    cno		    int,         
    '''

    #do something
    return


def search(locations):
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
        test_query ='''
                SELECT * FROM members
        '''
        cursor.execute(test_query)
        members = cursor.fetchall()
        for member in members:
            print(member)
        connection.commit()
        connection.close()
        return







if __name__ == "__main__":
    main()