class Utils:
    @staticmethod
    def reversed(number: int) -> int:
        stringNum = str(number)
        stringReversed = stringNum[::-1]
        reversedNum = int(stringReversed)
        return reversedNum
    
    @staticmethod
    def formatter(number: int) -> int:
        binary_number = bin(number)
        octal_format = oct(number)
        return binary_number, octal_format