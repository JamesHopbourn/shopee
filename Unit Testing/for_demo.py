# 单元模版
data = {
	"index": []
}
# 汇总保存到 result
result = []
for i in range(5):
		data['index'].append(i)
		result.append(data)
print(result)

"""
预期结果
[
	{'index': [0]}, 
	{'index': [1]}, 
	{'index': [2]}, 
	{'index': [3]}, 
	{'index': [4]}
]
"""

"""
实际结果
[
	{'index': [0, 1, 2, 3, 4]}, 
	{'index': [0, 1, 2, 3, 4]}, 
	{'index': [0, 1, 2, 3, 4]}, 
	{'index': [0, 1, 2, 3, 4]}, 
	{'index': [0, 1, 2, 3, 4]}
]
"""