
# import json
#
# s = "{"x": 1, "y": 2}"
# d = json.loads(s)
# print(d)

import ast

original_string = '{"x": "y + x + y", "y": "x - y - x"}'

# printing original string
print("The original string is : " + str(original_string))

# using json.loads() method
result = ast.literal_eval(original_string)

# print result
print("The converted dictionary is  : " + str(result))