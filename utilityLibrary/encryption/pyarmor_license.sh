# 环境搭建
# pip install pyarmor
# 加时间许可加密代码
pyarmor licenses --expired 2021-08-21 --bind-mac f0:18:98:e8:bc:e7 --bind-dis C07844202QWKXPGA6 --fixed 1 ./
pyarmor obfuscate --with-license licenses/license.lic main.py -r