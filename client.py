import requests
from datetime import datetime
import json

now = datetime.now()

hour = now.strftime("%H")
min = now.strftime("%M")
url= "http://localhost:8989"
getAns = url + "/test_get_method" + "?hour="+hour+"&minute="+min

response = requests.request("GET", getAns)


body= json.dumps({'hour': hour, 'minute': min,'requestId': response.text})
postAns = url + "/test_post_method"
response = requests.post(postAns, data=body)
response_id = json.loads(response.text)['message']

putAns = url+"/test_put_method"+"?id="+response.text
body= json.dumps({
                     'hour': (int(hour)+21)%24,
                     'minute': (int(min)+13)%60})
response = requests.put(putAns, data = body)
response_id = json.loads(response.text)['message']


deleteAns = url+"/test_delete_method"+"?id="+response_id
response = requests.delete(deleteAns)



#adding comments