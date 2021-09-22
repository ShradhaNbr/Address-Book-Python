class ValidationException(Exception):
    """Raised when the details does not satisfy the validation"""

    def __init__(self, message):
        self.message = message

