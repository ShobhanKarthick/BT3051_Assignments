class BinaryNumber():
    def __init__(self, a):
        self._binary = a

    def base_10(self):
        return str(int(self._binary, 2))

    def __str__(self):
        return ("({0})\u2082, ({1})\u2081\u2080".format(self._binary, self.base_10()))

number = BinaryNumber("010100")
print(number)

