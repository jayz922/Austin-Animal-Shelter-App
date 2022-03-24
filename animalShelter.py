from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self, username, password):
        #Initializing the MongoClient. This helps access the MongoDB databases & collections
        self.client = MongoClient('mongodb://%s:%s@localhost:50034/AAC' % (username, password))
        self.database = self.client['AAC']
        print("Connected to Database")
        
    #CREATE in CRUD   
    def create(self,data):
        try:
            if data is not None:
                insert_result = self.database.animals.insert_one(data) #data should be dictionary
                print(insert_result)
                return True
            else:
                #raise error
                raise Exception("Data is empty")
        except:
            return False
        
    #READ in CRUD     
    def read(self, target):
        try:
            if target is not None:
                read_result = list(self.database.animals.find(target, {"_id":False}))
                return read_result
            else:
                raise Exception("Target is empty")
                return False
        except Exception as e:
            print("Exception has occured: ", e)
    
    #UPDATE in CRUD
    def update(self, fromTarget, toTarget):
        if fromTarget is not None:
            update_result = self.database.animals.update(fromTarget, toTarget)
            print("Successfully Updated")
            print(update_result)
            return True
        else:
            raise Exception("Nothing to Update, target parameters are empty")
            return False
        
    #DELETE in CRUD
    def delete(self, target):
        if target is not None:
            try:
                delete_result = self.database.animals.delete_one(target)
                print("Successfully Deleted")
                return True
            except Exception as e:
                print("Exception occured: ", e)
        else:
            raise Exception("Nothing to delete, target empty")
            return False
            
    
    
    
       
            
            
        
        
                
                
    
                                                      
                              
    
