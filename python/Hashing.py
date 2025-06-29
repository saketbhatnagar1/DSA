# Python3 program to implement hashing with chaining
BUCKET_SIZE = 7
#Simple chaining in hashing:

# class Hash(object):
#     def __init__(self, bucket):
#         # Number of buckets
#         self.__bucket = bucket
#         # Hash table of size bucket
#         self.__table = [[] for _ in range(bucket)] #[[],[],[],[],[],[],[]]

#     # hash function to map values to key
#     def hashFunction(self, key):
#         return (key % self.__bucket) #

#     def insertItem(self, key):
#         # get the hash index of key
#         index = self.hashFunction(key)
#         self.__table[index].append(key)

#     def deleteItem(self, key):
#         # get the hash index of key
#         index = self.hashFunction(key)

#         # Check the key in the hash table
#         if key not in self.__table[index]:
#             return

#         # delete the key from hash table
#         self.__table[index].remove(key)

#     # function to display hash table
#     # def displayHash(self):
#     #     for i in range(self.__bucket):
#     #         print("[%d]" % i, end='')
#     #         for x in self.__table[i]:
#     #             print(" --> %d" % x, end='')
#     #         print()




# # Drive Program
# if __name__ == "__main__":
#     # array that contains keys to be mapped
#     a = [15, 11, 27, 8, 12]

#     # Create a empty has of BUCKET_SIZE
#     h = Hash(BUCKET_SIZE)

#     # insert the keys into the hash table
#     for x in a:
#         h.insertItem(x)

#     # delete 12 from the hash table
#     h.deleteItem(x)
#     # Display the hash table
#     h.displayHash()
# '''
# Chaining with Rehashing
# Let's discuss another method where we have no boundation on number of buckets. 
# Number of buckets will increase when value of load factor is greater than 0.5. 

# We will do rehashing when the value of load factor is greater than 0.5.
# In rehashing, we double the size of array and add all the values again to new array (doubled size array is new array) based on hash function. 
# Hash function should also be change as it is depends on number of buckets. Therefore, hash function behaves differently from the previous one.

# Link to article: https://www.geeksforgeeks.org/dsa/c-program-hashing-chaining/
# '''

class Hash(object):
    def __init__(self,size):
        self.size = size
        self.table = [[] for _ in range((size))]
    def hashfunction(self,key):
        index = key%self.size
        return index
    def insertItem(self,value):
        index = self.hashfunction(key=value)
        self.table[index].append(value)
    def delete(self, value):
        index = self.hashfunction(value)
        if value in self.table[index]:
            self.table[index].remove(value)
        # function to display hash table
    def displayHash(self):
        for i in range(self.size):
            print("[%d]" % i, end='')
            for x in self.table[i]:
                print(" --> %d" % x, end='')
            print()
BUCKET_SIZE = 7
table = Hash(BUCKET_SIZE)
print(table)
a = 10

table.insertItem(1)

table.insertItem(8)
table.insertItem(832)
table.insertItem(1)

table.insertItem(8)
table.insertItem(832)
table.displayHash()
