from boltiot import Bolt
api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
device_id  = "BOLTXXXXX"
mybolt = Bolt(api_key, device_id)
response = mybolt.analogWrite('0', '10')
print (response)