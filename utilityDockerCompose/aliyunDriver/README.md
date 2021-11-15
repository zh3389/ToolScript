## [aliyunDriveWebdav](https://github.com/zxbu/webdav-aliyundriver)是一个阿里云盘webdav开源实现, 用于将阿里云盘变身为webdav协议的文件服务器

本项目实现了阿里云盘的webdav协议，只需要简单的配置一下，就可以让阿里云盘变身为webdav协议的文件服务器。 基于此，你可以把阿里云盘挂载为Windows、Linux、Mac系统的磁盘，可以通过NAS系统做文件管理或文件同步，更多玩法等你挖掘

```
# 下载aliyunDrive docker-compose.yml文件
# 根据github项目文件的流程登陆阿里云盘在线版获得RefreshToken
# 自定义webdav的账号和密码,用于本地webdav服务器登陆
# 启动 docker-compose up -d
# 下载支持webdav软件通过第三步中的账号密码进行连接
```

