#!/usr/bin/env python3

import string

def passwordStrengthCheck(password):
	strength = 0
	level = {0:'密码长度至少6位！', 1:'弱强度', 2:'中低强度', 3:'中高强度',4:'高强度'}
	define = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
	if(len(password) < 6):
		return level[strength]
	for i in range(len(define)):
		if strength == 4: return
		for j in range(len(password)):
			if (password[j] in define[i]):
				strength += 1
				break
	return level[strength]

while(True):
	password = input("请输入密码：")
	print("密码强度等级：" + passwordStrengthCheck(password)) 