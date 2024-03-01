import pymysql

class DBUtil:
    def __init__(self,config) -> None:
        '''
        获取链接
        获取游标
        '''
        self.con = pymysql.connect(**config)
        self.cursor = self.con.cursor()
    
    def close(self) ->None:
        '''
        关闭链接与游标
        '''
        if self.cursor:
            self.cursor.close()
        if self.con:
            self.con.close()

    def execute_dml(self,sql):
        '''
        可以执行dml语句，用于数据的增加、删除、修改
        '''
        try:
            # 执行SQL
            self.cursor.execute(sql)
            # 提交事务
            self.con.commit()
        except Exception as e:
            print(e)
            if self.con:
                self.con.rollback()
        # finally:
        #     self.close()

    def query_one(self,sql):
        '''
        获取一条数据
        '''
        try:
            # 执行SQL
            self.cursor.execute(sql)
            # 获取结果
            rs = self.cursor.fetchone()
            # 返回数据
            return rs
        except Exception as e:
            print(e)
        # finally:
        #     self.close()

    def query_all(self,sql):
        '''
        获取所有数据
        '''
        try:
            # 执行SQL
            self.cursor.execute(sql)
            # 获取结果,并返回数据
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
        # finally:
        #     self.close()


if __name__ == '__main__':
    config = {'host': '192.168.0.12', 'user': 'root', 'passwd': 'zyxd123', 'db': 'sms_code', 'charset': 'utf8'}
    db = DBUtil(config)
    sql = "SELECT msg FROM sms_code WHERE send_time>='2024-02-23 14:45:46' AND send_time<'2024-02-23 14:46:46' AND to_phone_number = '15643494688' AND msg LIKE '%支付宝%';"
    # print(db.query_one(sql,3))
    print(db.query_one(sql))