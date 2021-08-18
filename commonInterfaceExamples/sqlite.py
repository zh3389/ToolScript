import sqlite3


def create_database():
    '''创建了一个数据库结构'''
    conn = sqlite3.connect(database='atm_data.db')  # 创建一个数据库名称为atm_data.db
    conn.execute("DROP TABLE USERS; ")  # 删除USERS这个表
    # 创建一个USERS表 里面创建一些字段 ID PASSWORD NAME MONEY
    conn.execute('''CREATE TABLE IF NOT EXISTS USERS
                    (ID INT PRIMARY KEY NOT NULL ,
                    PASSWORD CHAR(16) NOT NULL ,
                    NAME TEXT(10) NOT NULL ,
                    MONEY REAL);''')
    conn.commit()  # 提交
    conn.close()  # 关闭连接


create_database()


def insert_db(ID_user, PASSWORD_user, NAME_user, MONEY_user=0):
    '''将用户输入的用户信息写入到数据库'''
    conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
    cmd = "INSERT INTO USERS (ID,PASSWORD,NAME,MONEY) VALUES ({},\"{}\",\"{}\", {})".format(ID_user, PASSWORD_user,
                                                                                            NAME_user,
                                                                                            MONEY_user)  # 将用户输入的信息写入数据库
    print(cmd)
    conn.execute(cmd)  # 写入数据到数据库
    conn.commit()  # 提交
    conn.close()  # 关闭数据库链接


def del_db(user_ID):
    '''注销账户用,将账户的用户信息删除'''
    conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
    cmd = "DELETE FROM USERS WHERE ID = {}".format(user_ID)  # 命令
    conn.execute(cmd)  # 删除该账号
    # 验证一下用户名 和 密码 确认删除 否则 return 请重新输入账号
    conn.commit()
    conn.close()


def updata_db(self, user_password):
    '''更改密码'''
    conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
    conn.execute("UPDATE USERS SET PASSWORD = \"{}\" WHERE ID ={}".format(user_password, self.id))  # 传入用户的新密码 进行更改
    print('更新信息完成.')
    conn.commit()
    conn.close()


def select_other_db(self, other_ID):
    '''查询该账户的所有信息'''
    conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
    message = conn.execute("SELECT MONEY FROM USERS WHERE ID = {}".format(other_ID))  # 查询指定id的余额信息.
    for i in message:
        print('你余额为:{}'.format(i))
        conn.commit()
        conn.close()
        return i
    else:
        return '没有此用户的信息...'
