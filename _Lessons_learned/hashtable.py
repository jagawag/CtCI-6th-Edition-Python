'''
class HashTable:
    def __init__(self):
        Given a max size (integer), generate an empty HT
    def get_hash(self, key):
        Build a hash by creating a value based on each letter in the key
        Then mod % by the table length to get the remainder
        The remainder indicates the table location for storing the value
    def __getitem__(self, key):
    def __setitem__(self, key, val):
    def __delitem__(self, key):
'''
class HashTable:
   def __init__(self,MAX=100):
       self.MAX = MAX
       self.arr = [None for i in range(self.MAX)]

   def get_hash(self, key):
       hash = 0
       for char in key:
           hash += ord(char)
       return hash % self.MAX # mod by length of table

   def __getitem__(self,key):
      h = self.get_hash(key)
      return self.arr[h]

   def __setitem__(self,key,value):
       h = self.get_hash(key)
       self.arr[h] = value

   def __delitem__(self,key):
       h = self.get_hash(key)
       self.arr[h] = None

if __name__ == '__main__':
    ht = HashTable()
    print(ht.get_hash("cat"))
    t = HashTable()
    t["march 6"] = 310
    print(t['march 6'])