'''
Assignment No. 2
Course: PROG36859
Tyrell St. Kitts
991539017
November 29, 2026
William Barry
'''



def main():
    pass

#with open("./Files/monsters.csv", "r") as file:


'''
Settings File and Reading
1. Load a settings.json file
    When loading, can't use a dataclass and must access items in file as a dictionary
    
CSV File Reading
2. Load two different CSV files and store results in a dataclass that represents each type of inventory item 
    Design classes needed based off what is reqired for Video Game and Movie (must ensure qty and price are not negative)
3. Create the csv files with the headers seen below and at least 5 different records (can use container of choice to store obj)
    Movie header: id,title,genre,qty,price,release_date
    Video Game header: id,name,qty,price,release_date

JSON File Writing
4. Using data loaded from CSV, write eac hcollection of games and movies to their respectiev JSON file from the settings

Verification
5. Program will load each JSON file and compare the items from the csv to the ones from the JSON file. If an item doesn't
    exist in the JSON file, report it to the user
    
6. Main Application Flow
    · Load Settings and CSV Data
    · The user should be prompted with what action they would like to do:
        o Convert Data
        o Verify
        o Quits
    · The only time the program and terminate instantly is if there is an error reading the CSV data
    · Otherwise the program should continue to run with proper exception handling
'''




'''
Create a Python program that does the following:
    · Your program must load a JSON settings file and use the entries in the file to know what files to read
    from and what files to write too
    · Your application must use exceptions throughout the program to make sure that it runs without
    crashing. It must use these when working with files, reading and writing at a minimum but should be
    used throughout the application
    · Your program should exhibit best practices and use functions to do the respective work below.
    Writing you entire application in the main function will receive deductions
    · Your program can be written in one py file
    · You must use a main function for your application
    
Settings file and reading:
    · When your program starts it must load a settings.json file
    · A settings.json template file has been provide for you to use, you must update the values for the files
    to read from and to write too
    · You may also modify the settings.json file for anything else you may need for your program
    · When loading the settings file you cannot use a dataclass and must access the items in the file as a
    dictionary
    
CSV file reading
    · At the beginning of your application (after reading the settings) you must load the two different CSV
    files and store the results in a dataclass that represents each type of inventory item (you must design
    the class needed based off what is required for a Video Game and a Movie)
        o You dataclass must ensure that the qty and price are not negative
    · No CSV files have been provided for this assignment and must be create it manually (not through
    code)
    · You must create a CSV file for Video Games and one for Movies that have a header (seen below) and
    at least 5 different records that follow the header format (the separator can be changed if you prefer
    to use a different character):
    
        Movie header: id,title,genre,qty,price,release_date
        Video Game header: id,name,qty,price,release_date
        
    · How you store your object for each record is left up to you, you can choose any container we have
    discussed recently
    · Movies and Video Games can be fictitious and do not have to be real
    
JSON file writing
    · Using the data loaded from the CSV. Write each collection of Video Games and Movies to their
respective JSON file from the settings.
Verification
    · The program will load the each JSON file and compare the items from the CSV to the ones from the
    JSON file.
    · If there an item does not exist in the JSON file it must be reported to the user

Main Application Flow:
    · Load Settings and CSV Data
    · The user should be prompted with what action they would like to do:
        o Convert Data
        o Verify
        o Quits
    · The only time the program and terminate instantly is if there is an error reading the CSV data
    · Otherwise the program should continue to run with proper exception handling

'''
