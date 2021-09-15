#### 安装pyinstaller环境
```bash
pip install pyinstaller
```
#### 尝试打包
```python
pyinstaller test.py
# 如果提示： no model named 'pymysql' 只需显示导入该包重新执行打包操作
import pymysql
# 重新打包的时候记得删除掉spec文件，否则会有缓存，或者是加上–clean选项清除掉
```

#### 打包详细参数
```python
pyinstaller -D -p F:\Python27\Lib -i logo.ico mian.py

-D:打包成多个文件
-p：指定python安装包路径
-i：指定图标，到网上下载一个图标,保存为logi.ico文件，
mian.py：要打包的文件
```

#### 如遇错误 按提示解决即可
参考：http://www.langzi.fun/Python%E6%89%93%E5%8C%85exe%E6%96%87%E4%BB%B6%E6%96%B9%E6%B3%95.html