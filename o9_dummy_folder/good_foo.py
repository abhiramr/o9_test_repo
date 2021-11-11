import logging

class GoodFoo:
    def __init__(self, a, b):
        self.logger = logging.getLogger("o9_logger")
        self.a = a
        self.b = b

    def add(self) -> int:
        """ Adds two numbers """
        try:
            _sum = self.a + self.b
            return _sum
        except Exception as e:
            self.logger.exception("Error in adding two numbers - {}".format(e))

    def sub(self) -> int:
        """ Subtracts two numbers """
        try:
            return self.a - self.b
        except Exception as e:
            self.logger.exception("Error in subtracting two numbers - {}".format(e))
