import json

s = '{"success": "true", "status": 200, "message": "Hello"}'
d = json.loads(s)
print(d["success"], d["status"])
print(d)


json_string = """"""