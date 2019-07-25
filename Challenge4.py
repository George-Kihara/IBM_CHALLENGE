from __future__ import division
import pandas as pd
import os.path
from asn1crypto._ffi import null

class Check_If_Worth():
    #this is constructor 
    def __init__(self,data_from_csv):
        "Nothing to return"
        self.data_from_csv = data_from_csv
        
    # a method to read data from the csv
    def read_data_from_csv(self):
        try:
            #prompts the user to enter path of the file. e.g ./dataset/train_revised.csv
            path_file = input("Enter path of csv file: ")
            if (path_file == null):
                print ("Path cannot be null")
                self.read_data_from_csv()
            elif not path_file:
                print ("Path cannot be empty")
                self.read_data_from_csv()
            elif os.path.splitext(path_file)[1] != '.csv':
                print ("Path is not of a csv file")
                self.read_data_from_csv()
            else:                
                #panda reads the data here and saves it to data_from_csv
                self.data_from_csv = pd.read_csv(path_file)
                self.clean_up_data(self.data_from_csv)
        except:
            #display the error
            print ("Cannot read from the csv")
            self.read_data_from_csv()

    # ensure the data from the csv is readable    
    def clean_up_data(self,raw_data):
        try:
            raw_data.shape
            data_from_csv = raw_data
            self.query_route(data_from_csv)
        except:
            print ("Failed to clean up the data")
            self.clean_up_data(self.data_from_csv)
        
    #query the route based on what route the user picked
    def query_route(self,clean_data):
        try:
            route = input("Enter the route of travel (e.g. kisii): ")
            if (route == null):
                print ("route cannot be null")
                self.query_route(self.data_from_csv)
            elif not route:
                print ("Please enter correct route")
                self.query_route(self.data_from_csv)
            else:
                #drop the rows that do not have travel_day
                clean_data.drop(clean_data[clean_data['travel_from'] != route.capitalize()].index,
                                axis=0, inplace=True)
                #call method based on time
                self.filter_data(clean_data)           
        except:
            print ("Route could not be found. Enter another route")
            self.read_data_from_csv()
        
    def filter_data(self, query_data):
        try:
            #check the number mpesa records
            mpesa_records = len(query_data[query_data['payment_method'] == 'Mpesa'])
            
            #calculate the average of the mpesa records
            mpesa_percentage = mpesa_records/len(query_data) *100
            
            #display the results
            print ("Travels through mpesa are: ", mpesa_records)
            print ("mpesa percentage of the kisii travels are: ", mpesa_percentage)
            if (mpesa_percentage > 50):
                print("The terminus should have mobile money capabilities because most of its users are using mpesa")
        except:
            print ("Could not filter data. Try again")
            self.read_data_from_csv()
        
        
question4 = Check_If_Worth("")

question4.read_data_from_csv()


