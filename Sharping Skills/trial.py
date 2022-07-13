# creating a hash table of size 10 and initially seeting value to None
hash_table = [None, None, None, None, None, None, None, None, None, None]

# craeting a hash function which mods the input and return vlaue
def hash_func(x):
    return x % 10


# creating a insert function to insert element at the specific hash value
def insert(table, key, value):
    # finding address for the key value
    address = hash_func(key)

    # putting element into the table
    table[address] = value


# calling insert on hash table
insert(hash_table, 10, "Nepal")

# printing
print(hash_table)
