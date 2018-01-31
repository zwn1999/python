import os

path = input("输入文件夹路径(C:\\Users):")
att = input("请输入保留的文件属性:(.txt):")
for root, dirs, files in os.walk(path):
    for name in files:
        fname, fext = os.path.splitext(name)
        if fext != att:
            print(os.path.join(root, name), '已删除')
            os.remove(os.path.join(root, name))
print('\n整理完成')