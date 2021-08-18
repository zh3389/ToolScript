import pymysql

"""python
# 环境安装
pip install pymysql
"""

class DataBaseOperation():
    def __init__(self, login_info):
        # 创建连接
        self.con = pymysql.connect(host=login_info["host"],
                                   user=login_info["user"],
                                   password=login_info["password"],
                                   database=login_info["database"],
                                   port=login_info["port"])
        # 创建游标对象
        self.cur = self.con.cursor()

    def create_table_example(self):
        # 编写创建表的sql
        sql = """
              create table dagou_img(
              sno int primary key auto_increment,
              img_path varchar(2000) not null,
              img_hash varchar(30)
              )
              """
        try:
            # 执行创建表的sql
            self.cur.execute(sql)
            print("创建表成功")
        except Exception as e:
            print(e)
            print("创建表失败")
        finally:
            # 关闭游标连接
            self.cur.close()
            # 关闭数据库连接
            self.con.close()

    def insert_data_example(self):
        # 编写插入数据的sql
        sql = "insert into dagou_img (img_path, img_hash) values (%s, %s)"
        try:
            # 执行sql
            self.cur.execute(sql, ("1.jpeg", 18))
            self.con.commit()
            print("插入数据成功")
        except Exception as e:
            print(e)
            self.con.rollback()
            print("插入数据失败")
        finally:
            # 关闭游标连接
            self.cur.close()
            # 关闭数据库连接
            self.con.close()

    def search_data_example(self):
        # 编写查询的sql
        sql = "select * from dagou_img"

        try:
            # 执行sql
            self.cur.execute(sql)
            # 处理结果集
            students = self.cur.fetchall()
            for student in students:
                # print(student)
                sno = student[0]
                img_path = student[1]
                img_hash = student[2]
                print("sno", sno, "img_path", img_path, "img_hash", img_hash)
        except Exception as e:
            print(e)
            print("查询所有数据失败")
        finally:
            # 关闭游标连接
            self.cur.close()
            # 关闭数据库连接
            self.con.close()

    def update_data_example(self):
        # 编写修改的sql
        sql = 'update dagou_img set img_path=%s where sno=%s'

        try:
            # 执行sql
            self.cur.execute(sql, ("1.jpeg", 1))
            self.con.commit()
            print("修改成功")
        except Exception as e:
            print(e)
            self.con.rollback()
            print("修改失败")
        finally:
            # 关闭游标连接
            self.cur.close()
            # 关闭数据库连接
            self.con.close()

    def delete_data_example(self):
        # 编写删除的sql
        sql = 'delete from dagou_img where img_path=%s'

        try:
            # 执行sql
            self.cur.execute(sql, ("1.jpeg"))
            self.con.commit()
            print("删除成功")
        except Exception as e:
            print(e)
            self.con.rollback()
            print("删除失败")
        finally:
            # 关闭游标连接
            self.cur.close()
            # 关闭数据库连接
            self.con.close()


if __name__ == '__main__':
    login_info = {"host": "192.168.31.220",
                  "user": "root",
                  "password": "123123",
                  "database": "dagou_img",
                  "port": 3306}
    dbo = DataBaseOperation(login_info)
    dbo.create_table_example()