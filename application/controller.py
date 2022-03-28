# CST8333 - Programing Research Project
# Section: 350
# Semester: 22W
# Professor: Leanne Seaward
# Student name: Nicole Yue
# Student ID: 040991455
# Student Email: yue00015@algonquinlive.com
# Assignment 3


import pymongo
from bson import ObjectId
from pymongo import MongoClient
import certifi
import csv
from .view import View
from .models import Record


# Confroller is the class where the project is connected to database and fetch data as requiered from the database
# this class inheritant from the model class of Record
class Controller():
    datum = {}

    def __init__(self):
        self.view = View(self)

    def db_connect(self):
        '''
        This is to connect to a cloud version of MongoDB
        :return:
        '''
        try:
            client = MongoClient(
                'mongodb+srv://admin:admin@cluster0.o48jx.mongodb.net/dreamwell?retryWrites=true&w=majority',
                tlsCAFile=certifi.where())
            data_connection = client['Python']
            return data_connection
        except ConnectionError as e:
            print("error occurred", e)

    def get_all(self):
        '''
        to get all data in a given collection from the database
        :return:
        '''
        data = self.db_connect()
        col = data['pipeline']
        myQuery = {'Incident Number': 1, 'Incident Types': 1, 'Reported Date': 1, 'Nearest Populated Centre': 1,
                   'Province': 1, 'Company': 1, 'Substance': 1, 'Significant': 1, 'What happened category': 1,
                   '_id': 0}
        datum = col.find({}, myQuery)
        return datum

    def data_init(self):
        '''
        data_init is to initialize the database, read data and insert data into database if data doesn't exist
        :return:
        '''
        dt = self.db_connect()
        if dt is None:
            with open('pipeline.csv', newline='') as csvfile:
                rows = csv.reader(csvfile, delimiter=',')
                for r in rows:
                    dt.create_collection('pipeline').insert_one(r)

    def insert_to_database(self, new_rc):
        '''
        this is to connect to database and provide the collection name you would like to work with
        then insert a new record to atabase
        :param new_rc:
        :return:
        '''
        new_rc = new_rc.split(",")
        col = self.db_connect()['pipeline']
        show_pre = col.count_documents({})
        print("Before insert, the total records in database is ", show_pre)
        new_obj = Record(new_rc[0], new_rc[1], new_rc[2], new_rc[3], new_rc[4], new_rc[5], new_rc[6], new_rc[7],
                         new_rc[8]).asdict()
        col.insert_one(new_obj)
        show = col.count_documents({})
        print("After insert, he total records in database is  ", show)

    def count_records(self):
        '''
        this is to count the total number of records in a given collection of database
        :param :
        :return: number of count
        '''
        col = self.db_connect()['pipeline']
        count = col.count_documents({})
        return count

    def update_record(self, toUpdate):
        '''
        this is to connect to database and provide the collection name you would like to work with
        then update selected record from database
        :param toUpdate: a given string
        :return:
        '''
        col = self.db_connect()['pipeline']
        new_rc = toUpdate.split(",")
        show_pre = col.count_documents({"Reported Date": new_rc[1]})
        print("Current search for Incident Number as ", new_rc[0], " is: ", show_pre)
        col.update_one({"Incident Number": new_rc[0]}, {"$set": {"Reported Date": new_rc[1]}})
        show = col.count_documents({"Reported Date": new_rc[1]})
        print("After update, the search for Incident Number ", new_rc[0], " is: ", show)

    def search_record(self, str):
        '''
        this is to find records matching a specific creation
        :param str: a given string
        :return:
        '''
        col = self.db_connect()['pipeline']
        temp = col.find({"Incident Number": str})
        if temp is None:
            return "There is no matching record."
        else:
            return temp

    def delete_record(self, toDelete):
        '''
        this is to connect to database and provide the collection name you would like to work with
        then delete selected record from database
        :param toDelete:
        :return:
        '''
        col = self.db_connect()['pipeline']
        new_rc = toDelete.split(",")
        show_pre = col.count_documents({})
        print("Before delete, the total records in database is ", show_pre)
        col.find_one_and_delete({"Incident Number": new_rc[0]})
        show = col.count_documents({})
        print("After delete, he total records in database is  ", show)

    def main(self):
        '''
        this is the main method to run
        it first get all data ready
        then loops show_menu and user_select
        '''
        self.db_connect()
        while True:
            print("Program coded by Nicole Yue, Student# 040991455")
            self.view.show_menu()
            self.view.user_select()


'''
this runs the program
'''
# if __name__ == '__main__':
#     c = Controller()
#     c.main()

c = Controller()
c.db_connect()
t = c.search_record("INC2007-097")
# print(type(t))
# for i in t:
#     print(i)
#     for o in i:
#         print(o)
# print(type(i))
