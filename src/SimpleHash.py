class SimpleHash:
    # initialize hashtable
    hash_table = [[] for _ in range(10)]

    def hash_function(self, key):
        # returns a value between 0 - 9 as the hash
        # deterministic, fixed output size, uniform
        hash_key = hash(key) % len(self.hash_table)
        return self.hash_table[hash_key]

    def showTable(self):
        print(self.hash_table)
    
    def set(self, key, value):
        # implements chaining to avoid collisions
        # if there is a value at the determined hash,
        # appends value to list at hash
        bucket = self.hash_function(key)
        key_exists = False

        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def get(self, key):
        # iterates through list at hash
        # returns value with key that matches input key
        bucket = self.hash_function(key)
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v
    
    def remove(self, key):
        # removes key/value from hash table
        bucket = self.hash_function(key)
        key_exists = False
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print(f"Removed {v} at {key} from hash table")
        else:
            print(f"{key} not found")
