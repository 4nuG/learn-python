'''
This program runs the first lab.
These three lines, between triple quotes, are "comments".
Python ignores them; they're just there to help you, the programmer.
'''
# BTW, lines that begin with a hash-sign are also ignored
reply = input('Type something! ')
print ("You typed", reply)
name = input( "What is your name? ")
message = 'Hello ' + name + '. Nice to meet you!'
print (message)
celsius = input('celsius? ')
celsius = float(celsius)
fahrenheit = celsius * 1.8 + 32
print (celsius, 'C is', fahrenheit, 'F')

