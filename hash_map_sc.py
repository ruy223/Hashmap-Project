# Name: Zachary Quinn Fields
# OSU Email: fieldsz@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6
# Due Date: 01/06/2026
# Description: Two HashMap variants built from scratch: Separate Chaining
# (linked list collision resolution, O(N) find_mode()) and Open Addressing
# (quadratic probing, tombstone deletion, iterator protocol). All operations
# target O(1) average-case complexity. No built-in Python data structures used.
# HashMap Implementation


from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number and the find the closest prime number
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        Updates a key/value pair in the hash map.
        If the key is already present in the hash map,
        the value will be replaced with the new value.
        """
        # check load factor
        if self.table_load() >= 1.0:
            self.resize_table(self._capacity * 2)

        # Calculate index
        index = self._hash_function(key) % self._capacity
        temp = self._buckets.get_at_index(index)
        returned_node = temp.contains(key)

        # Check if key already exist
        if returned_node:
            returned_node.value = value
        else:
            temp.insert(key, value)
            self._size += 1


    def resize_table(self, new_capacity: int) -> None:
        """
        Changes capacity of the table.
        If new_capacity is less than 1, it does nothing.
        """
        # Check if new_capacity is less than 1
        if new_capacity < 1:
            return

        # Check if number is prime, change if not
        if not self._is_prime(new_capacity):
            new_capacity = self._next_prime(new_capacity)

        # Save all pairs
        saved_pairs = self.get_keys_and_values()

        # Make a new table
        self._size = 0
        self._buckets = DynamicArray()
        self._capacity = new_capacity
        for i in range(new_capacity):
            self._buckets.append(LinkedList())

        # Add saved pairs to new table
        for i in range(saved_pairs.length()):
            temp = saved_pairs.get_at_index(i)
            self.put(temp[0], temp[1])


    def table_load(self) -> float:
        """
        Returns the current hash table load factor
        """
        table_load = self._size / self._capacity
        return table_load

    def empty_buckets(self) -> int:
        """
        Return number of empty buckets in the hash table
        """
        counter = 0
        for i in range(self._capacity):
            temp = self._buckets.get_at_index(i)
            if temp.length() == 0:
                counter += 1
        return counter

    def get(self, key: str) -> object:
        """
        Returns value associated with given key.
        If the key is not present in the hash map,
        None is returned.
        """
        # Calculate index
        index = self._hash_function(key) % self._capacity
        temp = self._buckets.get_at_index(index)
        returned_node = temp.contains(key)

        # Check if key already exist
        if returned_node:
            return returned_node.value
        else:
            return None

    def contains_key(self, key: str) -> bool:
        """
        Returns True if the given key is present in the hash map.
        Otherwise, it returns False.
        """
        # Calculate index
        index = self._hash_function(key) % self._capacity
        temp = self._buckets.get_at_index(index)
        returned_node = temp.contains(key)

        # Check if key already exist
        if returned_node:
            return True
        else:
            return False

    def remove(self, key: str) -> None:
        """
        Removes the given key from the hash map.
        If the key is not present in the hash map,
        the method does nothing.
        """
        pass

    def get_keys_and_values(self) -> DynamicArray:
        """
        Returns a dynamic array with keys and values pairs.
        """
        # Create empty DA to store results
        new_array = DynamicArray()

        # Loop through every bucket
        for i in range(self._capacity):
            temp = self._buckets.get_at_index(i)
            for node in temp:
                new_array.append((node.key, node.value))
        return new_array

    def clear(self) -> None:
        """
        Clears the hash table
        """
        self._size = 0
        self._buckets = DynamicArray()
        for i in range(self._capacity):
            self._buckets.append(LinkedList())


def find_mode(da: DynamicArray) -> tuple[DynamicArray, int]:
    """
    TODO: Write this implementation
    """
    # if you'd like to use a hash map,
    # use this instance of your Separate Chaining HashMap
    map = HashMap()


# ------------------- BASIC TESTING ---------------------------------------- #


if __name__ == "__main__":

    print('\nPDF - put example 1')
    print('-------------------')
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print('\nPDF - put example 2')
    print('-------------------')
    m = HashMap(41, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print('\nPDF - resize example 1')
    print('----------------------')
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print('\nPDF - resize example 2')
    print('----------------------')
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print('\nPDF - table_load example 1')
    print('--------------------------')
    m = HashMap(101, hash_function_1)
    print(round(m.table_load(), 2))
    m.put('key1', 10)
    print(round(m.table_load(), 2))
    m.put('key2', 20)
    print(round(m.table_load(), 2))
    m.put('key1', 30)
    print(round(m.table_load(), 2))

    print('\nPDF - table_load example 2')
    print('--------------------------')
    m = HashMap(53, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print('\nPDF - empty_buckets example 1')
    print('-----------------------------')
    m = HashMap(101, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print('\nPDF - empty_buckets example 2')
    print('-----------------------------')
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print('\nPDF - get example 1')
    print('-------------------')
    m = HashMap(31, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print('\nPDF - get example 2')
    print('-------------------')
    m = HashMap(151, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print('\nPDF - contains_key example 1')
    print('----------------------------')
    m = HashMap(53, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print('\nPDF - contains_key example 2')
    print('----------------------------')
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print('\nPDF - remove example 1')
    print('----------------------')
    m = HashMap(53, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print('\nPDF - get_keys_and_values example 1')
    print('------------------------')
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(2)
    print(m.get_keys_and_values())

    print('\nPDF - clear example 1')
    print('---------------------')
    m = HashMap(101, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print('\nPDF - clear example 2')
    print('---------------------')
    m = HashMap(53, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print('\nPDF - find_mode example 1')
    print('-----------------------------')
    da = DynamicArray(['apple', 'apple', 'grape', 'melon', 'peach'])
    mode, frequency = find_mode(da)
    print(f'Input: {da}\nMode : {mode}, Frequency: {frequency}')

    print('\nPDF - find_mode example 2')
    print('-----------------------------')
    test_cases = (
        ['Arch', 'Manjaro', 'Manjaro', 'Mint', 'Mint', 'Mint', 'Ubuntu', 'Ubuntu', 'Ubuntu'],
        ['one', 'two', 'three', 'four', 'five'],
        ['2', '4', '2', '6', '8', '4', '1', '3', '4', '5', '7', '3', '3', '2']
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f'Input: {da}\nMode : {mode}, Frequency: {frequency}\n')
