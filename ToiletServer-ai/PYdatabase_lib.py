import sqlite3
from sqlite3 import Error

class SQLiteDatabase:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def create_connection(self):
        """创建到SQLite数据库的连接"""
        try:
            self.conn = sqlite3.connect(self.db_file)
            print("SQLite connection successful")
        except Error as e:
            print(f"The error '{e}' occurred")

    def close_connection(self):
        """关闭数据库连接"""
        if self.conn:
            self.conn.close()
            print("SQLite connection is closed")

    def execute_sql(self, sql, data=None):
        """执行SQL语句，并处理事务"""
        try:
            cursor = self.conn.cursor()
            if data:
                cursor.execute(sql, data)
            else:
                cursor.execute(sql)
            self.conn.commit()
            return cursor
        except Error as e:
            self.conn.rollback()
            print(f"Transaction rolled back due to an error: {e}")
            raise

    def insert_data(self, table, data):
        """插入数据"""
        keys = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        sql = f"INSERT INTO {table} ({keys}) VALUES ({placeholders})"
        self.execute_sql(sql, list(data.values()))

    def delete_data(self, table, condition):
        """删除数据"""
        sql = f"DELETE FROM {table} WHERE {condition}"
        self.execute_sql(sql)

    def update_data(self, table, data, condition):
        """更新数据"""
        set_clause = ', '.join([f"{key}=?" for key in data.keys()])
        sql = f"UPDATE {table} SET {set_clause} WHERE {condition}"
        self.execute_sql(sql, list(data.values()))

    def select_data(self, table, condition=''):
        """查询数据"""
        sql = f"SELECT * FROM {table}" + (f" WHERE {condition}" if condition else "")
        cursor = self.execute_sql(sql)
        return cursor.fetchall()

    def execute_custom_sql(self, sql, data=None):
        """执行自定义SQL语句"""
        return self.execute_sql(sql, data)
