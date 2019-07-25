from __future__ import division
import pandas as pd
from asn1crypto._ffi import null
import os.path

class Find_Probability():
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
            self.read_data_from_csv()
        
    #query the route based on what route the user picked
    def query_route(self,clean_data):
        try:
            route = input("Enter the route of travel (e.g. kijauri): ")
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
                print(len(clean_data))
                if(len(clean_data) != 0):
                    #call method based on time
                    self.query_time(clean_data)  
                else:
                    print ("Route could not be found. Enter another route")
                    self.read_data_from_csv()       
        except:
            print ("Route could not be found. Enter another route")
            self.query_route(self.data_from_csv)
               
    #query the time based on what timw the user entered
    def query_time(self,query_data):
        try:
            travel_time = input("Enter the time. e.g 7:30: ")
            if (travel_time == null):
                print ("time cannot be null")
                self.query_time(self.data_from_csv)
            elif not travel_time:
                print ("Please enter correct time")
                self.query_time(self.data_from_csv)
            else:
                #change travel_time to the correct time format
                query_data['time'] = pd.to_datetime(query_data['travel_time'])
                #drop the rows that do not have travel_time
                query_data.drop(query_data[query_data['time'] >= travel_time].index,
                                axis=0, inplace=True) 
                
                #call method based on time
                self.query_car_type(query_data)              
        except:
            print ("Time could not be found. Enter another time")
            self.read_data_from_csv()
                
    #query based off the car used
    def query_car_type(self,query_route_data):
        try:
            car_type = input("Enter the car type used. e.g shuttle: ")
            if (car_type == null):
                print ("car cannot be null")
                self.query_car_type(self.data_from_csv)
            elif not car_type:
                print ("Please enter correct car")
                self.query_car_type(self.data_from_csv)
            else:
                #display the rows with that car type
                list_cars = ["Bus","shuttle"]
                if car_type in list_cars:
                    routes_filtered = query_route_data[query_route_data['car_type'] == "shuttle"]
                    # get total number of rows
                    total_routes_no = len(query_route_data)
                    # get number of rows with routes_filtered
                    routes_no = len(routes_filtered)
                    # find probability of the car chosen
                    probability = routes_no/total_routes_no
                    print("Probability of "+ car_type + " is: ", str(round(probability,4)))
                else:
                    print ("The car does not exist. Enter another car")
                    self.query_car_type(self.data_from_csv)           
        except:
            print ("Route could not be found for that car. Enter another car")
            self.query_car_type(self.data_from_csv)
        
        
question2 = Find_Probability("")

question2.read_data_from_csv()
