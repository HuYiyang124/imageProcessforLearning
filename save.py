import os

def show_files(path, all_files):
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files)
        else:
            # 拼接文件路径
            all_files.append(path+"/"+file)
    return all_files

contents = show_files("./", [])
# 循环打印show_files函数返回的文件名列表

for content in contents:
    # print(content)
    # 判断是否为图片
    if content.endswith('jpg') or content.endswith('png'):
        destinate = os.path.dirname(content)+"/"+os.path.basename(content)[:-4]
        os.mkdir(destinate)
        content
