import extracredit
import unittest 



#TEST 1\\
# should return null, because A doesn’t exist in the DB yet


# should throw an error because a transaction is not in progress
class TestException(unittest.TestCase):
    
    def test_get(self):
        # should return null, because A doesn’t exist in the DB yet
        inmemoryDB = extracredit.InMemoryDB
        result = inmemoryDB.get("A")
        self.assertTrue(result == None)
    
        #should throw an error because a transaction is not in progress
        inmemoryDB = extracredit.InMemoryDB
        with self.assertRaises(Exception):
            inmemoryDB.put("A",5)
        #starts a new transaction
        inmemoryDB = extracredit.InMemoryDB
        inmemoryDB.begin_transaction()
        self.assertTrue(inmemoryDB.inProgress == True)

        #set’s value of A to 5, but its not committed yet
        inmemoryDB.put("A", 5)
        result = inmemoryDB.get("A")
        #should return null, because updates to A are not committed yet
        self.assertTrue(inmemoryDB.get("A") == None)

        #update A’s value to 6 within the transaction
        inmemoryDB.put("A", 6)
        inmemoryDB.commit()
        #should return 6, that was the last value of A to be committed
        self.assertTrue(inmemoryDB.get("A") == 6)
        #throws an error, because there is no open transaction
        with self.assertRaises(Exception):
            inmemoryDB.commit()
        #throws an error because there is no ongoing transaction
        with self.assertRaises(Exception):
            inmemoryDB.rollback()

        #should return null because B does not exist in the database
        self.assertTrue(inmemoryDB.get("B") == None)

        #starts a new transaction
        inmemoryDB.begin_transaction()
        inmemoryDB.put("B", 10)
        inmemoryDB.rollback()

        self.assertTrue(inmemoryDB.get("B") == None)

        
unittest.main()


