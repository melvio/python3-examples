#!/usr/bin/env python3


some_string = "That will be 42.69€"
print(some_string)
print(type(some_string))

utf8_str = some_string.encode("utf-8")
print(utf8_str)
print(type(utf8_str))

same_string = utf8_str.decode("utf-8")
print(same_string)
print(type(same_string))

rotation = "That will be 9042.69€"
print(rotation.encode("utf-8").decode("utf8"))       #That will be 9042.69€
print(rotation.encode("utf-8").decode("iso-8859-1")) #That will be 9042.69â ¬





