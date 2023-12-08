

class InMemoryDB:

    def _new_():
        return super().__new__()

    myDict = dict()
    copy = dict()
    inProgress = False #transaction in progress or not
    #key = string, value = int

    def begin_transaction():
        #begin_transaction() starts a new transaction.
        #At a time only a single transaction may exist.
        if InMemoryDB.inProgress == True:
            raise Exception("Only a single transaction can exist at a given time!")
        else:
            #print("NEW TRANSACTION")
            InMemoryDB.inProgress = True
        
    def put(key, value):
    #put(key, val) will create a new key with the provided value if a key doesn’t exist.
    #Otherwise it will update the value of an existing key.
    #If put(key, val) is called when a transaction is not in progress throw an exception
        if InMemoryDB.inProgress == False:
            raise Exception("'put' function cannot be called when a transaction is not in progress!")
        else:
            #print("VALUE SET")
            InMemoryDB.copy[key] = value

    def get(key):
    #get(key) will return the value associated with the key or null if the key doesn’t exist.
    #Within a transaction you can make as many changes to as many keys as you like. 
    #However, they should not be “visible” to get(), until the transaction is committed.
        try:
            return InMemoryDB.myDict[key]
        except KeyError:
            #print("NONE")
            return None 

    def commit():
    #get(key) can be called anytime even when a transaction is not in progress
    #A transaction ends when either commit() or rollback() is called
    #commit() applies changes made within the transaction to the main state. Allowing any future gets() to “see” the changes made within the transaction
        if InMemoryDB.inProgress == True:
            for key in InMemoryDB.copy:
                InMemoryDB.myDict[key] = InMemoryDB.copy[key]
            InMemoryDB.inProgress = False
        else:
            raise Exception('No transaction in progress!')ex
    def rollback():
    #A transaction ends when either commit() or rollback() is called
    #rollback() should abort all the changes made within the transaction and everything should go back to the way it was before.
        if InMemoryDB.inProgress == True:
            InMemoryDB.copy = InMemoryDB.myDict
            InMemoryDB.inProgress = False
        else:
            raise Exception('No transaction in progress!')


