# # Data types
#
# # String
# print("Hello"[4])
# print("123" + "456")
#
# # Integer
# print(123)
# print(123 + 456)
# print(123_456_789)
#
# # Float
# print(1.23)
# print(3.14159)
#
# # Boolean
# print(True)
# print(False)
#
# # types and casting
# num_chars = len(input("What is your name? "))
# print(type(num_chars))
# str_num_char = str(num_chars)
# print("Your name has " + str_num_char + " characters.")

# print(round(8 / 3))         # 3
# print(round(8 / 3, 2))      # 2.67
# print(8 // 3)               # 2
# print(8 % 5)                # 3

import pandas as pd
from io import StringIO

data = """Exchange ID;ExchangeRate;Exchange Currency
1;1;USD
2;0,75;GBP
3;0,85;EUR
4;3,67;AED
5;1,3;AUD"""
df = pd.read_csv(StringIO(data), sep=';')

# Return the transformed dataframe
df