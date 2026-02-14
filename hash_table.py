class Contact:
    """
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    """

    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name}: {self.number}"


class Node:
    """
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    """

    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.

    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    """

    def __init__(self, size: int = 10):
        if size <= 0:
            raise ValueError("HashTable size must be a positive integer.")
        self.size = size
        self.data = [None] * size  # buckets

    def hash_function(self, key: str) -> int:
        """
        Convert a string key into an index (0 to size-1).
        Uses a simple polynomial rolling hash with ord().
        """
        key = str(key)
        hash_value = 0
        prime = 31

        for ch in key:
            hash_value = (hash_value * prime + ord(ch)) % self.size

        return hash_value

    def insert(self, key: str, value: str) -> None:
        """
        Insert a contact into the hash table using separate chaining.
        If the key already exists, update the contact's number.
        """
        index = self.hash_function(key)

        # If bucket is empty, add first node
        if self.data[index] is None:
            contact = Contact(key, value)
            self.data[index] = Node(key, contact)
            return

        # Otherwise, traverse the chain
        current = self.data[index]
        while current is not None:
            if current.key == key:
                # Update existing contact number
                current.value.number = value
                return
            if current.next is None:
                break
            current = current.next

        # Add new node at the end of the chain
        contact = Contact(key, value)
        current.next = Node(key, contact)

    def search(self, key: str):
        """
        Search for a contact by name (key).
        Returns the Contact if found, otherwise None.
        """
        index = self.hash_function(key)
        current = self.data[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self) -> None:
        """
        Print the structure of the hash table for debugging.
        """
        for i in range(self.size):
            current = self.data[i]
            if current is None:
                print(f"Index {i}: Empty")
            else:
                parts = []
                while current is not None:
                    parts.append(f"- {current.value}")
                    current = current.next
                print(f"Index {i}: " + " ".join(parts))


# Test your hash table implementation here.
if __name__ == "__main__":
    table = HashTable(10)

    print("---- Empty Table ----")
    table.print_table()

    print("\n---- Insert John + Rebecca ----")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    print("\n---- Search John ----")
    result = table.search("John")
    print("Search result:", result)

    print("\n---- Collision + Duplicate Tests ----")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    table.print_table()

    print("\n---- Update Duplicate Key (Rebecca) ----")
    table.insert("Rebecca", "999-444-9999")
    table.print_table()

    print("\n---- Search Missing ----")
    print(table.search("Chris"))  # None


# -------------------------
# DESIGN MEMO (200–300 words)
# -------------------------
"""
For this project, I chose a hash table because the main goal 
of the system is fast lookups by name. If we store contacts 
on a regular list, the program would have to check each 
contact one by one until it finds a match. That works for a 
small number of entries, but it would slow down as more 
contacts are added.

A hash table improves that by using a hash function to 
convert a name into an index in an array. Instead of 
searching everything, the program jumps directly to a 
specific location in the table. That makes lookup much 
faster and more efficient.

To handle collisions, I used separate chaining. This means 
each index in the array can store a linked list of contacts 
instead of just one. If two names hash to the same index, 
they are connected in a short chain. When searching, the 
program only checks that small chain rather than the entire 
table.

An engineer would choose a hash table over a list when 
quick, direct lookups are more important than keeping data 
in order. Trees are useful when sorted data or range-based 
searches are needed, but this system only requires matching 
a name exactly. For that reason, a hash table is a simple 
and practical solution.

"""
