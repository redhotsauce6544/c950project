# hashtable.py
class ChainingHashTable:
    def __init__(self, size_capacity=20):
        self.buckets = []
        for _ in range(size_capacity):
            self.buckets.append([])

 #using O(n) to iterate in each bucket to check if the key exists

    def insert(self, key, item):
        bucket = hash(key) % len(self.buckets)
        bucket_list = self.buckets[bucket]

        for idx, pair in enumerate(bucket_list):
            if pair[0] == key:
                pair[1] = item
                return True

        bucket_list.append((key, item))
        return True
        #looking up items in hash table
    def lookup(self, key):
        bucket = hash(key) % len(self.buckets)
        bucket_list = self.buckets[bucket]

        for pair in bucket_list:
            if pair[0] == key:
                return pair[1]

        return None
        #removes items from hashtable
    def hash_delete(self, key):
        placeholder = hash(key) % len(self.buckets)
        destination = self.buckets[placeholder]

        for idx, pair in enumerate(destination):
            if pair[0] == key:
                del destination[idx]
                return True

        return False