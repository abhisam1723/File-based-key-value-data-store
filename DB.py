import json
import os

class Create(object):
    
    def __init__(self,location='',db_name='',flag=0):
        self.flag = flag
    
        if location != '':
            self.location = os.path.expanduser(location)
    
            if db_name != '':
                self.db_name = db_name
    
            else:
                self.db_name = 'myCustomDB.db'
            self.location = os.path.join(self.location,self.db_name)

    
        else:
    
            if db_name != '':
                self.db_name = db_name
    
            else:
                self.db_name = 'myCustomDB.db'
            self.location = os.path.expanduser('~')
            self.location = os.path.join(self.location,'Documents',self.db_name)
        
        if self.flag == 3:
    
            if os.path.exists(self.location):
                self.load(self.location)
    
            else:
                print("Error: No such file exists")
    
        if os.path.exists(self.location):
    
            if self.flag != 3:
                self.load(self.location)
                self.flag = 0      
    
        else:
            self.load(self.location)
    ''' 
    The below method checks if the path exits then it calls the loadDB method else it creates a DB an empty DB.              
    '''   
    def load(self,location):
        if os.path.exists(location):
            self.loadDB()

        else:
            self.db = {}
            self.dumpDB()
        return True

    '''
    The below method loads the contents of DB for reading them.
    '''
    def loadDB(self):
        self.db = json.load(open(self.location,'r'))

    '''
    The below method helps to save the contents to the DB.
    '''
    def dumpDB(self):
        try:
            json.dump(self.db,open(self.location,'w+'))
            return True

        except:
            return False

    '''
    The below method helps to add new values to the DB
    '''
    
    def set(self,key,value):
        if len(key)>32:
            return "Length of key beyond limit : Shouldnot be more than 32CHARS"

        try:
            self.db[str(key)] = value
            self.dumpDB()

        except:
            return "Error while saving"

    '''
    The below method helps to read the contents of DB provided correct keys.
    '''
    def read(self,key):
        try:
            return self.db[key]

        except:
            return "Key error"
    
    '''
    The below method resets the DB.
    '''

    def resetDB(self):
        self.db={}
        self.dumpDB()
        return True

    '''
    The below method deletes the contents of the database provided suitable keys.
    '''
    def delete(self,key):
        try:
            del self.db[str(key)]
            self.dumpDB()
            return True

        except:
            return "No such key to delete"