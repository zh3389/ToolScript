from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Float, String, DateTime, JSON, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

"""
环境搭建
pip install SQLAlchemy
此ORM工具用于链接各大数据库, 此脚本用于最简示例程序。
"""

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'test'
    # 表的结构:
    id = Column(String(20), primary_key=True)
    path = Column(String)
    feature = Column(JSON())
    name = Column(String(20))
    # from sqlalchemy.dialects.postgresql import ARRAY
    # vector = Column(ARRAY(Float))
    created_at = Column(DateTime, default=datetime.utcnow)


"""初始化数据库链接 创建表"""
engine = create_engine('sqlite://')  # 指定空path使用memory
# engine = create_engine('sqlite:////absolute/path/to/dbname.db')
# engine = create_engine("mysql://root:password@localhost:3306/dbname")
# engine = create_engine('oracle://root:password@localhost:1521/dbname')
# engine = create_engine("postgresql://root:password@localhost:5432/dbname")
# engine = create_engine('mssql+pymssql://root:password@localhost:port/dbname')
Base.metadata.create_all(bind=engine)  # 创建表
DBSession = sessionmaker(bind=engine)  # 创建DBSession类型

"""增加指定数据"""
session = DBSession()  # 创建session对象
new_user = User(id='5', name='Bob')  # 创建新User对象
session.add(new_user)  # 添加到session
session.commit()  # 提交即保存到数据库
session.close()  # 关闭session

"""查找指定数据"""
session = DBSession()  # 创建Session
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
user = session.query(User).filter(User.id == '5').one()
print('type:', type(user), 'name:', user.name)  # 打印类型和对象的name属性
session.close()  # 关闭Session

"""修改指定数据"""
session = DBSession()  # 创建Session
session.query(User).filter(User.id == '5').update({"name": "Lily"})
session.commit()
session.close()

"""删除指定数据"""
session = DBSession()  # 创建Session
session.query(User).filter(User.id == '5').delete()
session.commit()
session.close()