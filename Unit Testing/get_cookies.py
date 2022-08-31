#!/usr/bin/env python3

import os
import json 

# cookies 文件解析
def parse_cookies():
	data_cookie, header_cookies = {}, ""
	cookies = json.loads(open('../cookies.txt').read())
	for i in range(len(cookies)):
		data = json.loads(json.dumps(cookies[i]))
		data_cookie.update({data['name']: data['value']})
		header_cookies += f"{data['name']}={data['value']}; "
		header_cookies = header_cookies.replace('"', '\\"')
	return data_cookie, header_cookies

print(parse_cookies()[0])
print(parse_cookies()[1])