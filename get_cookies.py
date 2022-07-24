#!/usr/bin/env python3

#!/usr/bin/env python3

import os
import json 

with open('cookies.txt', 'r') as content:
	cookies = json.loads(content.read())


data_cookie = {}
header_cookies = ""
for i in range(len(cookies)):
	data = json.loads(json.dumps(cookies[i]))
	temp = {data['name']: data['value']}
	data_cookie.update(temp)
	header_cookies += f"{data['name']}={data['value']}; "
print(data_cookie)
print(header_cookies.replace('"', '\\"'))
