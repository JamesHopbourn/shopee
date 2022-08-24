#!/usr/bin/env python3

import string


def demo():
	return "james done"

data = {
	"ip": "103.152.220.92",
	"city": "Sham Shui Po",
	"region": "Sham Shui Po",
	"country": "HK",
	"loc": "22.3302,114.1595",
	"org": "AS138997 Eons Data Communications Limited",
	"timezone": "Asia/Hong_Kong",
	"readme": "https://ipinfo.io/missingauth"
}

print({v: k for k, v in data.items()})

print(data.get('james'))

Names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
print(list(filter(lambda x: x.startswith('B'),Names)))

print(sum(range(1,1001)))
print([x+1 for x in range(10)])
print(set(range(100)))
print(list(map(lambda x:x*x, range(1,20))))
print(list(filter(lambda x: x%2==1, range(20))))
print(list(filter(lambda x: x%2==1, [ord(item) for item in string.ascii_letters])))


print(max(["this","is","a","list","of","words"], key=len))

print("unbrella".count('l'))

data, result = {}, {}
data.update({"james":"12"})
print(data,result)
