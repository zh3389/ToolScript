## opyrator可视化接口

#### 可视化接口

```bash
# 命令行执行以下cmd启动可视化UI接口
opyrator launch-ui main:hello_world
# 命令行执行以下cmd启动HTTP API接口
opyrator launch-api main:hello_world
```

#### 命令行直接执行

```bash
# 直接使用项目文件
opyrator call main:hello_world '{"message": "hello"}'
# 使用opyrator导出的zip格式
opyrator call main.zip '{"message": "hello"}'
```

