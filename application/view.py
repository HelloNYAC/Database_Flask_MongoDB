# CST8333 - Programing Research Project
# Section: 350
# Semester: 22W
# Professor: Leanne Seaward
# Student name: Nicole Yue
# Student ID: 040991455
# Student Email: yue00015@algonquinlive.com
# Assignment 3

# view class is the user interface of the program, it works together with controller to provide functionalities
class View:
    '''
    this is the view class
    it will be used in the controller as user interface
    '''

    def __init__(self, controller):
        '''
        init the controller for future use
        '''
        self.controller = controller

    def show_menu(self):
        '''
        displays menu
        '''
        print()
        print("PROGRAM coded BY Nicole Yue, 040991455")
        print("----------------- MENU -----------------")
        print("0. Exit")
        print("1. Reload the data from the csv file to database")
        print("2. Display all data in database file")
        print("3. Search and Display a specific record")
        print("4. Add an new record")
        print("5. Update an existing record")
        print("6. Delete and Update a record")

    def selection(self):
        '''
        takes user input as an integer
        '''
        option = int(input("Please type 1-6 to select: "))
        return option

    def user_select(self):
        '''
        user select takes user_input as an param to loop the user selection
        it execute the program based on user's input
        calls methods in controller to show record, add, edit, delete etc
        '''
        opt = self.selection()
        if opt == 0:
            exit(0)
        elif opt == 1:
            self.controller.db_connect()
            self.controller.data_init()
            print("Data loaded successfully!")
        elif opt == 2:
            # Load data from database
            print("Display all records in database: ")
            dt = self.controller.get_all()
            for d in dt:
                print(d)
            count = self.controller.count_records()
            print("Total records in database is: ", count, "\n")
        elif opt == 3:
            # search and display a specific record
            user_input = input("Please input the Incident Number you are searching for in for format of: INC1111-111:")
            rec_to_update = self.controller.search_record(user_input)
            for r in rec_to_update:
                print("Matching Records: ")
                print(r)
        elif opt == 4:
            # add new record to database
            print("Number of records before insert: ", self.controller.count_records())
            print("Please input the following info to add a record")
            print(
                "'Incident Number', 'Incident Types', 'Reported Date', 'Nearest Populated Centre', 'Province', 'Company', 'Substance', 'Release Type'")
            new_rec = input("Please input with comma between values: ")
            self.controller.insert_to_database(new_rec)
        elif opt == 5:
            # update a record in database
            user_input = input("Please input the Incident Number and field value to update in for format of: INC1111-111, 3/3/2022: ")
            self.controller.update_record(user_input)
        elif opt == 6:
            # delete a record from database
            user_input = input("Please input the Incident Number you wish to delete for format of: INC1111-111:")
            self.controller.delete_record(user_input)
        else:
            # any other option will not be accepted
            print("Invalid option. Please try again! Only type 0 to 7.")
