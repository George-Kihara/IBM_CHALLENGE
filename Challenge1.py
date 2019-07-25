# pandas library to help read from csv file
import pandas as pd
import os.path
from asn1crypto._ffi import null

#created a class called Top_7_Routes
class Top_7_Routes:
    
    #this is constructor where data_from_csv variable is initialized
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
            self.query_date(data_from_csv)
        except:
            print ("Failed to clean up the data")
            self.read_data_from_csv()
            
    # query rows based on the date and find average  
    def query_date(self, clean_data):
        try:
            travel_day = input("Enter the day to query e.g. Sunday: ")
            if (travel_day == null):
                print ("day cannot be null")
                self.query_date(self.data_from_csv)
            elif not travel_day:
                print ("Please enter correct day")
                self.query_date(self.data_from_csv)
            else:
                try:
                    # convert all the dates to datetime format from travel_date
                    clean_data['travel_date'] = pd.to_datetime(clean_data['travel_date'])
                    
                    # find the day name of that datetime and create a new colum called day
                    clean_data['day'] = clean_data['travel_date'].dt.day_name()
                    
                    # drop all the rows that dont have that day
                    list_of_days = ["Sunday", "Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
                    #ensure it is a valid day
                    if (travel_day.capitalize() in list_of_days):        
                        clean_data.drop(clean_data[clean_data['day'] != travel_day.capitalize()].index, axis=0, inplace=True)
                    
                        # add a new column to the data frame called no_of_travels and group according to the highest 7
                        # show the routes using travel_from and travel_to column
                        clean_data = clean_data.groupby(['travel_from', 'travel_to']).size().reset_index(name='no_of_travels')
                        clean_data.sort_values('no_of_travels', ascending=False)[:7]
                        
                        #calculate total of the 7 rows
                        total_count = clean_data.sort_values('no_of_travels', ascending=False).no_of_travels[:7].sum()
                        
                        # calculate average of the each route
                        clean_data['average'] = clean_data['no_of_travels']/total_count
                        
                        # add average column to the data frame
                        top_7_routes = clean_data.sort_values("average",ascending=False).head(7)
                    
                        print (top_7_routes)
                    else:
                        print ("Day not found.")
                        self.query_date(self.data_from_csv)
                except:
                    print ("Enter correct day e.g. Sunday")
                    self.query_date(self.data_from_csv)  
        except:
            print ("Enter correct day e.g. Sunday")
            self.query_date(self.data_from_csv)
            
        
question1 = Top_7_Routes("")

question1.read_data_from_csv()

