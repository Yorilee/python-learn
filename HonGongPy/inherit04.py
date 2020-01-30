class CustomException(Exception):
    def __init__(self, message, value):
        Exception.__init__(self)
        self.message = message
        self.value = value

    def __str__(self):
        return self.message

    def print(self):
        print("### Error Info ###")
        print("Message:", self.message)
        print("Value:", self.value)

try:
    raise CustomException("No reason...", 273)
except CustomException as e:
    e.print()

