## [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) 是一个强大的、自托管的互联网归档解决方案，用于收集、保存和查看您想要离线保存的站点。

您可以在 Linux、macOS 和 Windows 上将其设置为命令行工具、Web 应用程序和[桌面应用程序](https://github.com/ArchiveBox/electron-archivebox)(alpha)。您可以一次提供一个 URL，或者安排从浏览器书签或历史记录、RSS 等提要、Pocket/Pinboard 等书签服务等定期导入。有关完整列表，请参阅[输入格式](https://archivebox.io/#input-formats)。

它以多种格式保存您提供给它的 URL 的快照： HTML、PDF、PNG 屏幕截图、WARC 等等，并自动提取和保存各种内容（文章文本、音频/视频、 git repos 等）。有关完整列表，请参阅[输出格式](https://archivebox.io/#output-formats)。

我们的目标是睡个安稳觉，知道您关心的互联网部分会在它宕机后的几十年内自动以耐用、易于访问的格式保存。



```bash
# 下载ArchiveBox docker-compose.yml文件
curl -O 'https://raw.githubusercontent.com/ArchiveBox/ArchiveBox/master/docker-compose.yml'
# 运行初始化并设置创建管理员用户
docker-compose run archivebox init --setup
# 启动服务器, 并登录后台 http://127.0.0.1:8000 + 上一步设置的账号
docker-compose up
```

