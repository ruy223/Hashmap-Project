# Hashmap-Project
Two HashMap variants built from scratch: Separate Chaining (linked list collision resolution, O(N) find_mode()) and Open Addressing (quadratic probing, tombstone deletion, iterator protocol). All operations target O(1) average-case complexity. No built-in Python data structures used. HashMap Implementation

# Overview
Separate ChainingOpen AddressingFilehash_map_sc.pyhash_map_oa.pyCollision ResolutionSingly linked listsQuadratic probingResize ThresholdLoad factor ≥ 1.0Load factor ≥ 0.5Deletion StrategyDirect removalTombstone markers

# Methods
Both implementations support: MethodDescriptionput(key, value)Insert or update a key/value pairget(key)Return the value associated with a key, or Noneremove(key)Remove a key/value pair; does nothing if key absentcontains_key(key)Return True if key exists, False otherwiseresize_table(capacity)Rehash all entries into a new capacitytable_load()Return the current load factorempty_buckets()Return the number of empty bucketsget_keys_and_values()Return all key/value pairs as a DynamicArray of tuplesclear()Remove all entries while preserving capacity

Open Addressing only: MethodDescription__iter__() / next()Iterate over active (non-tombstone) entries

Separate Chaining only: FunctionDescriptionfind_mode(da)Return the most frequent value(s) in a DynamicArray with their frequency — O(N) Design Notes

Table capacity is always maintained as a prime number All operations target O(1) average-case time complexity No built-in Python data structures (dict, set, etc.) are used Backed by custom DynamicArray, LinkedList, and HashEntry classes from a6_include.py

# Files
FileDescriptionhash_map_sc.py
Separate chaining HashMaphash_map_oa.py
Open addressing HashMapa6_include.py

Supporting data structures and hash functions Usage pythonfrom hash_map_sc import HashMap, find_mode from hash_map_oa import HashMap as HashMapOA from a6_include import DynamicArray, hash_function_1, hash_function_2

Separate chaining
m = HashMap(53, hash_function_1) m.put("name", "Alice") print(m.get("name")) # Alice print(m.contains_key("age")) # False

Find mode
da = DynamicArray(["apple", "apple", "grape", "melon"]) mode, frequency = find_mode(da) print(mode, frequency) # ['apple'] 2

Open addressing with iteration
m2 = HashMapOA(11, hash_function_2) m2.put("x", 10) m2.put("y", 20) for entry in m2: print(entry.key, entry.value)
