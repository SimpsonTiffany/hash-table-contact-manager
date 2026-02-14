class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name}: {self.number}"


class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size: int = 10):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key: str) -> int:
        '''
        Converts a string key into an index using character values.
        '''
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def insert(self, key: str, value: str):
        '''
        Inserts a new contact into the hash table.
        If the key already exists, updates the contact's number.
        '''
        index = self.hash_function(key)

        new_contact = Contact(key, value)
        new_node = Node(key, new_contact)

        # If bucket is empty
        if self.data[index] is None:
            self.data[index] = new_node
            return

        # Traverse linked list for collision handling
        current = self.data[index]
        while current:
            # Update duplicate key
            if current.key == key:
                current.value.number = value
                return
            if current.next is None:
                break
            current = current.next

        # Append new node at end
        current.next = new_node

    def search(self, key: str):
        '''
        Searches for a contact by name.
        Returns the Contact object if found, otherwise None.
        '''
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        '''
        Prints the structure of the hash table.
        '''
        for i in range(self.size):
            print(f"Index {i}:", end=" ")

            current = self.data[i]
            if current is None:
                print("Empty")
            else:
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()


# Test your hash table implementation here.
if __name__ == "__main__":
    table = HashTable(10)

    print("Initial Table:")
    table.print_table()

    print("\nAdding Contacts:")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    print("\nSearching for John:")
    contact = table.search("John")
    print("Search result:", contact)

    print("\nTesting Collisions:")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    table.print_table()

    print("\nUpdating Rebecca:")
    table.insert("Rebecca", "999-444-9999")
    table.print_table()

    print("\nSearching for Missing Contact:")
    print(table.search("Chris"))
