# Okay, let's dive deeper into how linked lists are used for separate chaining in hash maps (also known as hash tables) to handle collisions, along with a Python example.

# 1. The Goal of a Hash Map

# A hash map's primary goal is to store key-value pairs in a way that allows for very fast average-time operations: insertion, deletion, and lookup (finding the value associated with a key). Ideally, these operations take O(1) or constant time on average.

# 2. The Basic Mechanism: Hashing

# Hash Function: A hash map uses a hash function to convert a given key into an integer.
# Buckets: This integer is then typically used (often with the modulo operator %) to calculate an index into an underlying array-like structure. Each slot in this array is called a "bucket".
# Ideal Scenario: If every key produced a unique bucket index, you could just store the value (or key-value pair) directly in the array bucket at that index, achieving O(1) operations.
# 3. The Problem: Collisions

# It's highly likely (especially with many keys and a limited number of buckets) that different keys will produce the same hash value, and therefore map to the same bucket index. This is called a collision.
# Question: If two different key-value pairs (e.g., ("apple", 1) and ("banana", 2)) are supposed to go into bucket index 5, how do you store both? You can't just overwrite the first one with the second.
# 4. The Solution: Separate Chaining with Linked Lists

# Separate chaining is a common strategy to resolve collisions. Here's how it works:

# Instead of storing the value directly in the bucket array, each bucket stores a pointer to the head of a separate data structure that holds all the key-value pairs that hashed to that specific bucket index.
# The Linked List: A linked list is an excellent choice for this separate data structure because:
# Dynamic Size: You don't know beforehand how many keys will collide into a single bucket. A linked list can easily grow to accommodate any number of colliding elements.
# Simple Insertion: Adding a new key-value pair that hashes to an existing bucket is typically just adding a new node to the front (or end) of that bucket's linked list (an O(1) operation for the list itself).
# How Operations Work with Separate Chaining:

# Insertion (e.g., insert ("grape", 3))

# Calculate the hash of "grape" -> get bucket index (e.g., index 7).
# Go to bucket 7 in the array.
# If bucket 7 is empty (e.g., None): Create a new linked list. Add a node containing ("grape", 3) to this list. Make bucket 7 point to the head of this new list.
# If bucket 7 already points to a linked list: Add a new node containing ("grape", 3) to the existing linked list (often prepending to the start for simplicity, which is O(1)). Optional Check: You might first traverse the list to see if "grape" already exists, and if so, update its value instead of adding a duplicate key.
# Lookup (e.g., get value for "apple")

# Calculate the hash of "apple" -> get bucket index (e.g., index 5).
# Go to bucket 5 in the array.
# If bucket 5 is empty (None): The key "apple" is not in the map.
# If bucket 5 points to a linked list: Traverse the linked list starting from its head. For each node in the list, compare the node's key with the target key ("apple").
# If a node with the key "apple" is found, return its associated value.
# If you reach the end of the linked list without finding the key, then "apple" is not in the map.
# Deletion (e.g., delete "banana")

# Calculate the hash of "banana" -> get bucket index (e.g., index 5).
# Go to bucket 5 in the array.
# If bucket 5 is empty (None): The key "banana" is not in the map; nothing to do.
# If bucket 5 points to a linked list: Traverse the linked list, looking for the node containing the key "banana".
# If found, remove that node from the linked list (this involves updating the next pointer of the previous node in the list, or updating the head pointer in the bucket if the first node is deleted).
# If the key is not found in the list, do nothing.
# Performance:

# Average Case: If the hash function distributes keys evenly and the number of buckets is reasonably large compared to the number of keys, the linked lists in each bucket will be very short (often containing 0 or 1 elements). Operations will effectively be O(1) on average.
# Worst Case: If the hash function is poor or you're unlucky, many keys could hash to the same bucket. In the absolute worst case, all keys hash to one bucket. The hash map then degenerates into a single linked list, and operations become O(N), where N is the number of key-value pairs stored.
# Python Example:

# --- Step 1: Define the Node for the Linked List ---
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None # Pointer to the next node in the list

    def __repr__(self):
        # Helper for printing nodes
        return f"({self.key}: {self.value})"

# --- Step 2: Define the Hash Map class ---
class HashMap:
    def __init__(self, capacity=10):
        # Choose an initial size for the bucket array
        self.capacity = capacity
        # Create the bucket array, initially all empty (None)
        self.buckets = [None] * self.capacity
        self.size = 0 # Keep track of the number of items stored

    def _hash(self, key):
        # Simple hash function: use Python's built-in hash()
        # and modulo operator to get an index within capacity
        return hash(key) % self.capacity

    def insert(self, key, value):
        """Inserts or updates a key-value pair."""
        index = self._hash(key)
        node = self.buckets[index]

        # Scenario 1: Bucket is empty
        if node is None:
            self.buckets[index] = ListNode(key, value)
            self.size += 1
            # print(f"Inserted {key} into empty bucket {index}")
            return

        # Scenario 2: Bucket has a linked list (collision or update)
        prev = None
        while node is not None:
            # Check if the key already exists in the list
            if node.key == key:
                # Update the value if key found
                node.value = value
                # print(f"Updated key {key} in bucket {index}")
                return
            prev = node
            node = node.next

        # If key wasn't found, add a new node to the end of the list
        # (Could also add to beginning for O(1) list insertion)
        prev.next = ListNode(key, value)
        self.size += 1
        # print(f"Appended {key} to list in bucket {index} (collision)")


    def get(self, key):
        """Gets the value associated with a key."""
        index = self._hash(key)
        node = self.buckets[index]

        # Traverse the linked list in the bucket
        while node is not None:
            if node.key == key:
                return node.value # Key found!
            node = node.next

        # Key not found in the list or bucket was empty
        raise KeyError(f"Key '{key}' not found.")

    def delete(self, key):
        """Deletes a key-value pair."""
        index = self._hash(key)
        node = self.buckets[index]
        prev = None

        # Traverse the list to find the node
        while node is not None:
            if node.key == key:
                # Key found, now remove the node
                if prev is None:
                    # Node to delete is the head of the list
                    self.buckets[index] = node.next
                else:
                    # Node to delete is in the middle or end
                    prev.next = node.next
                self.size -= 1
                # print(f"Deleted {key} from bucket {index}")
                return # Deletion successful
            prev = node
            node = node.next

        # Key not found
        raise KeyError(f"Key '{key}' not found for deletion.")

    def __len__(self):
        return self.size

    def __str__(self):
        """For printing the hash map contents."""
        items = []
        for i, bucket in enumerate(self.buckets):
            elements = []
            node = bucket
            while node:
                elements.append(str(node))
                node = node.next
            if elements:
                 items.append(f"Bucket {i}: {' -> '.join(elements)}")
            # else:
            #    items.append(f"Bucket {i}: Empty") # Optional: show empty buckets
        return "\n".join(items) if items else "HashMap is empty"

# --- Step 3: Example Usage ---
my_map = HashMap(capacity=5) # Small capacity to force collisions

# hash("apple") % 5 might be, say, 2
my_map.insert("apple", 10)
print(my_map)
print("-" * 20)

# hash("banana") % 5 might also be 2 (collision!)
my_map.insert("banana", 20)
print(my_map)
print("-" * 20)

# hash("grape") % 5 might be 0
my_map.insert("grape", 30)
print(my_map)
print("-" * 20)

# hash("orange") % 5 might also be 2 (another collision!)
my_map.insert("orange", 40)
print(my_map)
print("-" * 20)

# Get values
print(f"Value for apple: {my_map.get('apple')}")     # Output: 10
print(f"Value for orange: {my_map.get('orange')}")   # Output: 40

# Update a value
my_map.insert("apple", 15)
print(f"Updated value for apple: {my_map.get('apple')}") # Output: 15
print(my_map)
print("-" * 20)

# Delete a value from the middle of a list
my_map.delete("banana")
print("Map after deleting banana:")
print(my_map)
print("-" * 20)

# Delete the head of a list
my_map.delete("apple")
print("Map after deleting apple:")
print(my_map)
print("-" * 20)

# Try to get deleted key
try:
    my_map.get("banana")
except KeyError as e:
    print(e) # Output: Key 'banana' not found.

print(f"Current map size: {len(my_map)}") # Output: 2


# This example demonstrates how collisions cause multiple 
# ListNode objects (containing key-value pairs) to form 
# a linked list within a single bucket of the HashMap. 
# Operations like get and delete must then traverse these 
# short lists to find the correct key.