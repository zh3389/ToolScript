import os
import shutil
import compileall

"""
1. 编译py文件为pyc
2. 将__pycache__下的pyc文件拷贝到编译前的位置
3. 将编译后的pyc的文件名改为编译前的文件名
4. 可选是否删除原文件
"""


def move_pyc(path):
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            move_pyc(os.path.join(path, i))
    if os.path.exists(os.path.join(path, '__pycache__')):
        for name in os.listdir(os.path.join(path, '__pycache__')):
            file_name = name.split('.')[0] + '.py'
            if os.path.exists(os.path.join(path, file_name)):
                print(os.path.join(path, file_name))
                # os.remove(os.path.join(path, file_name))  # 删除py文件，慎重
            shutil.move(os.path.join(path, '__pycache__', name), os.path.join(path, name.replace('cpython-36.', '')))
        if os.path.exists(os.path.join(path, '__pycache__')):
            os.rmdir(os.path.join(path, '__pycache__'))


if __name__ == '__main__':
    path = './'
    compileall.compile_dir(path)
    move_pyc(path)
