# docker加入用户组
sudo groupadd docker
sudo usermod -aG docker ${USER}
sudo systemctl restart docker
su root
su ${USER}