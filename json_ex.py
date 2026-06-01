sample_dict = {"name": "Roopesh", "age": 30, "city": "New York"}

import json
json_string = json.dumps(sample_dict)
print(type(json_string))  
print (json_string)

string_data = '{"name": "Roopesh", "age": 30, "city": "New York"}'
print (type(string_data)   )
dict_data = json.loads(string_data)
print (type(dict_data)   )


