PROMOMLclass Jar:
    def __init__(self, capacity=12, cookies=0):
        self.capacity = capacity
        self.cookies = cookies

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if self.cookies + n > self.capacity:
            raise ValueError("Adding that many would exceed the cookie jar capacity")
        self.cookies += n

    def withdraw(self, n):
        if self.cookies - n < 0:
            raise ValueError("There aren't that many cookies in the jar")
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._cookies

    @property
    def cookies(self):
        return self._cookies

    @cookies.setter
    def cookies(self, cookies):
        if cookies < 0:
            raise ValueError("Cookies can't be a negative number")
        if cookies > self.capacity:
            raise ValueError("Number of cookies exceeds jar capacity")
        self._cookies = cookies


def main():
    jar = Jar()
    print(jar)


if __name__ == "__main__":
    main()
