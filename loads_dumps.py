import json
# json to json string
dit = {
    'name': 'hafeez'
}

dumps_con = json.dumps(dit)
print("dumps_con",dumps_con)

# json string to json
loads_con = json.loads(dumps_con)
print("loads",loads_con)
