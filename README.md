# File-based-key-value-data-store
It is a File based key-value data store that supports three basic functions of Create,Read and Delete

It is a file-based key-value data store that supports the basic CRD (create, read, and delete)
operations. This data store is meant to be used as a local storage for one single process on one
laptop.
The data store supports the following functional requirements.
1. It can be initialized using an optional file path. If one is not provided, it will reliably
   create itself in a reasonable location on the laptop.
2. A new key-value pair can be added to the data store using the Create operation. The key
   is always a string - capped at 32chars. The value is always a JSON object - capped at
   16KB.
3. If Create is invoked for an existing key, an appropriate error must be returned.
4. A Read operation on a key can be performed by providing the key, and receiving the
   value in response, as a JSON object.
5. A Delete operation can be performed by providing the key.
6. Appropriate error responses must always be returned to a client if it uses the data store in
   unexpected ways or breaches any limits.
  
The four functions that are present in the data-store are: create, read, set, delete .
The create method helps to create a datastore, read method helps to read the value provided the key, set method is used to add values to the databases by providing the key and value, delete method is used to delete the value provided suitable key, and show method is used to show the entire database.

It can be used as a library as:
from DB import Create

How to use the methods:
1.Through terminal:

create method:
object=Create(location,filename)
If location and filename are not provided it will make a databse in the Documents folder with name myCustomDB.db.

read method:
object.read(key)

set method:
object.set(key,value)

delete method:
object.delete(key)

show method:
object.show()
This method shows the current content of the database.


If you want to access a database which has been created but is not currently accessible, then to make the database accessible you have to create a object using Create method as follows:
object=Create(location,filename,3)   //If the file doesnot exist the Error message is returned
        or
object=Create(loaction,filename)


Features to be added:
TTL is a feature that has to be added and thread-safe is another feature.
The problem with TTL while implemetation are:
The json file creates problem while dumping when TTL is being implementated using python with TTLCache.
When we try to access the database after closing the file it creates error which seems to be an internal problem that can be solved by modifying the TTLCache library.


Inorder to import the library there should exist a blank file with name '__init__.py' in the same folder as DB.py.
The test_DB.py is file which performs the unit test on few trivial cases.






