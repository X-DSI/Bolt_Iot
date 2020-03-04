from boltiot import Bolt
api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
device_id  = "BOLTXXXXX"
mybolt = Bolt(api_key, device_id)
response = mybolt.digitalWrite('0', 'HIGH')
print (response)