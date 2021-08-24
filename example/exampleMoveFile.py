import os
import shutil
from tqdm import tqdm

"""
环境搭建
pip install tqdm
移动指定文件夹下的所有下一级下下级下下下...级文件 到指定指定的路径下.
"""

move_dir = "data"
g = os.walk(move_dir)
for path, dir_list, file_list in g:
    for file_name in tqdm(file_list):
        if str(file_name)[:2] == "._":
            continue
        if str(file_name)[0] == ".":
            os.remove(os.path.join(path, file_name))
            continue
        if path != move_dir:
            shutil.move(os.path.join(path, file_name), move_dir)
