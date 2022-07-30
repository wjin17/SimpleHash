# Simple Hash Table Implementation

This program demonstrates a simple hashing function and implements chaining to avoid collisions.

## Usage

### Initialize hash table

```
hashtable = SimpleHash()
```

### Set value at key

```
hashtable.set(10, "Charmander")
```

### Get value at key

```
hashtable.get(10)
```

### Get value at key

```
hashtable.remove(10)
```

## HashTable

```
hashtable.set(10, "Charmander")
hashtable.set(19, "Squirtle")
hashtable.set(20, "Bulbasaur")
```

| 0                  | 1    | ... | 9                |
| ------------------ | ---- | --- | ---------------- |
| (10, "Charmander") | None | ... | (19, "Squirtle") |
| (20, "Bulbasaur")  | None | ... | None             |

Both keys, 10 and 20, result in a hash of "0", however, both values will be stored sequentially in a list under the hash to avoid collision through chaining.
