import json
jsonobj='{"a":1,"b":2,"c":3,"d":[{"e":4},{"f":7}]}'
json_loaded=json.loads(jsonobj)
print(json_loaded["d"][0])