dd if=/dev/zero of=$PWD/swap bs=10240 count=1024000
sudo mkswap swap
sudo swapon swap
free -m
# 卸载虚拟内存
# sudo swapoff swap