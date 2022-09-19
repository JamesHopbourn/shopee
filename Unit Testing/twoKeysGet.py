#!/usr/bin/env python3

data = {
	"ip": "140.227.127.160",
	"hostname": "140-227-127-160.indigo.static.arena.ne.jp",
	"city": "Tondabayashichō",
	"region": "Ōsaka",
	"country": "JP",
	"loc": "34.5007,135.6021",
	"org": "AS2514 NTT PC Communications, Inc.",
	"postal": "584-0033",
	"timezone": "Asia/Tokyo",
	"readme": "https://ipinfo.io/missingauth"
}

print(data.get('city',data.get('城市')))


data = {
	"ip": "140.227.127.160",
	"hostname": "140-227-127-160.indigo.static.arena.ne.jp",
	"城市": "Tondabayashichō",
	"region": "Ōsaka",
	"country": "JP",
	"loc": "34.5007,135.6021",
	"org": "AS2514 NTT PC Communications, Inc.",
	"postal": "584-0033",
	"timezone": "Asia/Tokyo",
	"readme": "https://ipinfo.io/missingauth"
}
print(data.get('city',data.get('城市')))