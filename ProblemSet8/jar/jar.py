class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Wrong capacity")
        #self.capacity = capacity
        self._capacity = capacity
        #self.size = 0
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Wrong capacity")
        if self.size + n > self.capacity:
            raise ValueError("Wrong capacity")
        #self.size += n
        self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("There are less cookies than asked to remove")
        #self.size -= n
        self._size -= n

        """  
        File "jar.py", line 34, in <module>
            jar = Jar()
        File "jar.py", line 5, in __init__
            self.capacity = capacity
        AttributeError: can't set attribute capacity
        """
    @property
    def capacity(self):
        #return self.capacity
        return self._capacity

    @property
    def size(self):
        #return self.size
        return self._size
    


#jar = Jar()
#jar.deposit(2)
#jar.withdraw(1)
#print(jar)
