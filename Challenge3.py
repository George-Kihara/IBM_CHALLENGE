import pandas as pd
import os.path
from asn1crypto._ffi import null

class Find_Probable_Next_Character():
        
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
            self.find_next_character(data_from_csv)
        except:
            print ("Failed to clean up the data")
            self.read_data_from_csv()
        
    #query the route based on what route the user picked
    def find_next_character(self,clean_data):
        try:
            characters = input("Enter the characters (e.g. MK): ")
            if (characters == null):
                print ("characters cannot be null")
                self.find_next_character(self.data_from_csv)
            elif not characters:
                print ("Please enter correct characters")
                self.find_next_character(self.data_from_csv)
            else:
                
                #create a list to store the next character of the string for all the rows
                next_characters = []
                
                # loop through the data with payment_receipt
                for value in clean_data['payment_receipt']:
                        # check if the charcter exists in the string value
                        if characters in value:
                                #get the length of the string
                                value_len = len(value)
                                #check if the index of the next character does not exceed the string length 
                                if(value.index(characters)+2) < value_len:
                                        #add the next charcter in the next character list
                                        next_characters.append(value[value.index(characters)+2])
                                       
                
                # create a count to be used for checking the number of a specific character
                frequency = 0
                #grab the first character and use it as the starting point
                frequent_value = next_characters[0]
                #for loop to loop all the characters in the list
                for i in next_characters:
                        #count the number of appearances of the character and store it in a variable
                        current_frequency = next_characters.count(i)
                        #check if the count above is greater than the current_frequency
                        if current_frequency>frequency:
                                #replace frequency with the current_frequency if it is bigger
                                frequency = current_frequency
                                #the character becomes the most frequent
                                frequent_value = i

                print ("The most frequent character is: ", frequent_value)
                print ("Frequency: ", frequency)
                     
        except:
            print ("Characters could not be found. Enter other characters")
            self.find_next_character(self.data_from_csv)
        
 
question3 = Find_Probable_Next_Character("")

question3.read_data_from_csv()