from utils import Utils

# test reversed function
try:
    testInstance = Utils()
    print(testInstance.reversed("1234"))
except:
    print("reversed function does not support string input")

try:
    testInstance = Utils()
    print(testInstance.reversed(1.23))
except:
    print("reversed functiom does not accept float input")

try:
    testInstance = Utils()
    assert (testInstance.reversed(1234) == 4321)
except:
    print("Wrong input")

#test formatter function
try:
    testInstance = Utils()
    print(testInstance.formatter("1234"))
except:
    print("formatter function does not support string input")

try:
    testInstance = Utils()
    print(testInstance.formatter(1.23))
except:
    print("formatter functiom does not accept float input")

try:
    testInstance = Utils()
    assert (testInstance.formatter(1234) == ('0b10011010010', '0o2322'))
except:
    print("Wrong input")
