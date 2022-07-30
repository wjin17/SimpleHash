from src.SimpleHash import SimpleHash

hashtable = SimpleHash()

# Demo storing values
hashtable.set(10, "Charmander")
hashtable.set(20, "Bulbasaur")
hashtable.set(19, "Squirtle")

hashtable.showTable()

# Demo retrieving values
print(hashtable.get(20)) # Should return Bulbasaur
print(hashtable.get(15)) # Should return None

# Demo deleting values
hashtable.remove(25) # Should remove value with key 25
hashtable.remove(30) # Should print "30" not found

