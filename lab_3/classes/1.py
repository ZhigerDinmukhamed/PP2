class UpperString:
    def getString(variable):
        variable.input_string = input()
    
    def printString(variable):
        print(variable.input_string.upper())

String = UpperString()
String.getString()
String.printString()