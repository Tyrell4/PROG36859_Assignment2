'''
Assignment No. 2
Course: PROG36859
Tyrell St. Kitts
991539017
November 29, 2026
William Barry
'''

import json
import csv
from dataclasses import dataclass, asdict

def LoadSettings():
    #Load the settings file and return it as a dictionary, or None.
    try:
        with open("./settings.json", "r") as file:
            settings = json.load(file)
    except FileNotFoundError:
        print(f"Error: settings.json file was not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: settings.json is not valid JSON file. {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    if not isinstance(settings, dict):
        print(f"Error: settings.json doesn't have proper dictionary/json format.")
        return None

    '''Do more error checking
    
    missing = [key for key in REQUIRED_KEYS if key not in settings]
    if missing:
        print(f"Error: settings file is missing: {', '.join(missing)}")
        return None
    '''
    
    return settings

@dataclass
class Movie:
    id: int
    title: str
    genre: str
    qty: int
    price: float
    release_date: str
    
    def __post_init__(self):
        if self.qty < 0:
            raise ValueError("Quantity can't be negative")
        if self.price < 0:
            raise ValueError("Price can't be negative")

@dataclass
class VideoGame:
    id: int
    name: str
    qty: int
    price: float
    release_date: str
    
    def __post_init__(self):
        if self.qty < 0:
            raise ValueError("Quantity can't be negative")
        if self.price < 0:
            raise ValueError("Price can't be negative")


def LoadMovieCSV(filepath):
    movies = []
    
    #Do try catch here
    with open(filepath) as file:
        dict_reader = csv.DictReader(file, delimiter=',')
        for record in dict_reader:
            if record.get("id") not in movies:
                movies.append(Movie(int(record.get("id")), record.get("title"), record.get("genre"), int(record.get("qty")), 
                                                 float(record.get("price")), record.get("release_date")))

    # print(movies)
    return movies  
 
    
def LoadVideoGameCSV(filepath):
    videogames = [] 
    
    #Do try catch here
    with open(filepath) as file:
        dict_reader = csv.DictReader(file, delimiter=',')
        for record in dict_reader:
            if record.get("id") not in videogames:
                videogames.append(VideoGame(int(record.get("id")), record.get("name"), int(record.get("qty")), 
                                                    float(record.get("price")), record.get("release_date")))
   
    # print(videogames)
    return videogames
    
# def WriteMovieJSON(movies, filepath):
#     #Try catch
#     with open(filepath, "w") as file :
#         for movie in movies:
#             json_data = asdict(movie)
#             json.dump(json_data, file, indent=4)

# def WriteVideoGameJSON(videogames, filepath):
#     #Try catch
#     with open(filepath, "w") as file :
#         for game in videogames:
#             json_data = asdict(game)
#             json.dump(json_data, file, indent=4)
            
    
def WriteJSON(csv_collection, filepath):
    #Try catch
    json_data = [asdict(item) for item in csv_collection]
    with open(filepath, "w") as file :
        json.dump(json_data, file, indent=4)


def LoadJSON(filepath, item_class):
    json_list = []
    with open(filepath, "r") as file:
        json_dict = json.load(file)
    
    for i in range(len(json_dict)):
        json_list.append(item_class(**json_dict[i]))
    
    return json_list
            

#Program will load each JSON file and compare the items from the csv to the ones from the JSON file. If an item doesn't exist in the JSON file, report it to the user
def VerifyData(csv_collection, filepath, item_class):
    #try catch
    json_list = LoadJSON(filepath, item_class)
    
    if csv_collection == json_list:
        print("Data is the same")
    else:
        print("Data is different")
        
    #Check length of each list, Loop through using length of longest list. Compare each item with the other list at i and report the name of item then return
    
    
      


def main():
    settings = LoadSettings()
    
    if settings is None:
        return
    
    movies = LoadMovieCSV(settings["movie_csv"])
    videogames = LoadVideoGameCSV(settings["videogame_csv"])
    
    
    WriteJSON(movies, settings["movie_json"])
    WriteJSON(videogames, settings["videogame_json"])
    
    VerifyData(movies, settings["movie_json"], Movie)
    VerifyData(videogames, settings["videogame_json"], VideoGame)
        
    #Menu options for Save JSON Data, Verify, Quit
    

if __name__ == "__main__":
    main()
#with open("./Files/monsters.csv", "r") as file:


'''
Settings File and Reading
1. Load a settings.json file
    When loading, can't use a dataclass and must access items in file as a dictionary
    
CSV File Reading
    Exceptions

JSON File Writing
    Exceptions

Verification
5. Program will load each JSON file and compare the items from the csv to the ones from the JSON file. If an item doesn't
    exist in the JSON file, report it to the user. Test by loading all and then deleting an item from the JSON and them compare again.
    Then it will say what was missing
    
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
    · Your application must use exceptions throughout the program to make sure that it runs without
    crashing. It must use these when working with files, reading and writing at a minimum but should be
    used throughout the application
    
    
CSV file reading
    · Catch ValueError from dataclass qty and price
    
JSON file writing
    · Exceptions
    
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
