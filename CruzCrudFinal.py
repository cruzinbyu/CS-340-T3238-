from pymongo import MongoClient


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
    # Initializing the MongoClient. This helps to 
    # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:%d/?authSource=AAC'  % (username, password))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert_result=self.database.animals.insert(data)  # data should be dictionary        
            if insert_result.inserted_id!=0:    
                return True
            else:
                   return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")



# Create method to implement the R in CRUD.
    def read(self, search):
        return self.database.animals.find(data)

    def locate(self, query):
         if query is not None:
             
            search_result=self.database.animals.find(query)
            self.database.animals.find(query)
            if search_result is not None:
                return search_result
            else:
                return("Animal not found")
            
          
            raise Exception("Nothing to search, because search parameter is empty")
 #Update CRUD

    def update(self, animal, change):
        animalToFind = animal
        informationToUpdate = change
        if change is not None:
            result = self.database.animals.find_one_and_update(animalToFind, informationToUpdate)
        if result is not None:
            return result
        else:
            return ("Update failed")
    
        raise Exception("No change")

#Delete CRUD

    def delete(self, animal):

        if animal is not None:
            delete_result = self.database.animals.delete_one(animal)
            return delete_result
        else:
            raise Exception("No animal ID provided")
     
