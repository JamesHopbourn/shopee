import os

prefix = input('请输入文件夹前缀：')
start = input('请输入起始数字：')
end = input('请输入结束数字：')

for index in range(int(start),int(end)+1):
    path = os.path.join(os. getcwd(), prefix + str(index))
    os.makedirs(path, exist_ok = True)

# rm james100{0..9}