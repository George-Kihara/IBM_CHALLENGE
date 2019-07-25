# IBM CHALLENGE SOLUTIONS

## Tools used

*Python
*Visual Studio Code IDE

## CHALLENGE ONE

Challenge: Find on average the top seven (7) most travelled routes for a Sunday. Indicate the average of each and rank them in decreasing order

### Solution:
    *The user enters the file path of the CSV.
    *pandas library reads from the CSV to a dataframe.
    *User is prompted to enter day of travel. e.g. Sunday. The dataframe is queried based off this day.
    *The rows without this day are dropped.
    *A new column is added to the dataframe called no_of_travels and grouped according to the highest 7
    *Average for each row is calculated against the total number of the top 7 rows
    *Average column is added to the dataframe
    *The resulting top 7 routes are displayed

Execution: python3 Challenge1.py

## CHALLENGE TWO

Challenge: What is the probability that a passenger travelling from Kijauri will take a Shuttle if they depart before 0730 hours?

### Solution:
    *The user enters the file path of the CSV.
    *pandas library reads from the CSV to a dataframe.
    *User is prompted to enter the travel from route. e.g. kijauri. A query based on this route is done.
    *Rows without that route are dropped.
    *User is then prompted to enter time that the car will depart before it. e.g. 7:30
    *Rows without this time are dropped.
    *User is again prompted to enter the type of vehicle. e.g. shuttle
    *A query is done for all rows matching that car
    *Get the total number of travels before time chosen
    *Get the total number of travels for that car
    *Probability is calculated by dividing the travels of the car against those of the total travels
    *Resulting probabilty is displayed.

Execution: python3 Challenge2.py

## CHALLENGE THREE

Challenge: The Sequence ‘MK’ appears in a payment reference. Based on the tri-gram distribution of characters in all the payment references, what is the most probable next character?

### Solution:
    *The user enters the file path of the CSV.
    *pandas library reads from the CSV to a dataframe.
    *User is prompted to enter the two characters. e.g. MK
    *A list is creates for storing the next character after the two characters for all rows in the dataframe called next_characters.
    *Loop through each value in the 'payment_receipt' column
    *Check if the two characters are in the string value.
    *If they exist, add the next character to the next_characters list by adding 2 to the index of the two characters.
    *Create a count a variable for counting the number of a character appearance in the list.
    *Initialize the first value with a 0 as the frequent value.
    *Loop through the next_characters list for each value.
    *Check the count of the value.
    *if the count is greater than the first count then replace the first count with the current one.
    *Also the value becomes the most frequent character, hence the most probable character.
    *Display the most probable character with its frequency.

Execution: python3 Challenge3.py

## CHALLENGE FOUR

Challenge: When considering opening a new terminus in Kisii, should the terminus have mobile money capabilities? Why?

### Solution:
    *The user enters the file path of the CSV.
    *pandas library reads from the CSV to a dataframe.
    *User is prompted to enter the travel route. e.g. kisii
    *A query is done based of this route. All rows without this route are dropped.
    *All records with payment method as Mpesa are filtered.
    *Check the number of mpesa records
    *Do a percentage of the mpesa_records against the records routes data.
    *Display the number of travels through mpesa and the percentage.
    *If the percentage is more than 50%, the terminus should have mobile money capabilities because most of the users require the service.
    
Execution: python3 Challenge4.py
