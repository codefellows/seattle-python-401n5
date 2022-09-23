class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = size * [None]

    def set(self, key, value):
        pass

        # set
        # Arguments: key, value
        # Returns: nothing
        # This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

    def get(self, key):
        pass

        # get
        # Arguments: key
        # Returns: Value associated with that key in the table

    def contains(self, key):
        pass

        # contains
        # Arguments: key
        # Returns: Boolean, indicating if the key exists in the table already.

    def keys(self):
        pass

        # keys
        # Returns: Collection of keys

#     'roger' 10431 list: 1024
    def hash(self, key):
        pass

        # hash
        # Arguments: key
        # Returns: Index in the collection for that key

        total = 0

        for ch in key:
            total += ord(ch)

        primed = total * 19

        index = primed % self.size
        return index
