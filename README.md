**Flask conversion for  https://github.com/wongcyrus/deepracerrewardfunctionapi by [wongcyrus](https://github.com/wongcyrus)**

Deepracer reward example

```python
import urllib.request
import urllib.parse
import json

def reward_function(params):
    url = 'http://10.10.10.10:5000/api/reward'
    query_string = urllib.parse.urlencode({"json":json.dumps(params)})
    url = url + "?" + query_string
    with urllib.request.urlopen( url ) as response:
        response_text = response.read().decode('utf-8')
        result = json.loads(response_text)
        body = json.loads(result['body'])

    return float(body['reward'])
```