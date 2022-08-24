import os

path = input('粘贴工作目录：')
prefix = input('输入文件夹前缀：')
start = input('输入起始数字：')
end = input('输入结束数字：')

prefix = os.path.join(path, prefix)

for index in range(int(start),int(end)+1):
    path = os.path.join(os. getcwd(), prefix + str(index))
    os.makedirs(path, exist_ok = True)

# rm james100{0..9}