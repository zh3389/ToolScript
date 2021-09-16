# 动态加密python代码
# 环境搭建
# pip install pyarmor
# 可视化界面加密
# pip install pyarmor-webui
# pyarmor-webui
# 查看机器硬件信息
pyarmor hdinfo
# 递归加密路径下所有py代码, 多个启动文件列举出即可
pyarmor obfuscate main.py -r
# 在 MacOS 平台下加密脚本，这些加密脚本将在Ubuntu下面运行
pyarmor obfuscate --platform linux.x86_64 main.py