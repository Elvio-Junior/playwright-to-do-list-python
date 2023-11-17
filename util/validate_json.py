from jsonschema import validate

def validate_json(json_response, json_schema):
    
    return True if validate(json_response, json_schema) == None else False