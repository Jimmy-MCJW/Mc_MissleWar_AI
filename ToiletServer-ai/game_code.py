import tkinter as tk
from tkinter import *
import random
import sqlite3
import pyautogui
from datetime import *
from pathlib import Path
from PYdatabase_lib import SQLiteDatabase
# 定义动作和权重
KEY_LIST = {
    'forward': 'w',
    'backward': 's',
    'left': 'a',
    'right': 'd',
    'jump': 'space',
    'duck': 'shift',
    'shoot': 'mouse_right'
}

WEIGHT_LIST = {
    'forward': 0.05,
    'backward': 0.00,
    'left': 0.4,
    'right': 0.4,
    'jump': 0.05,
    'duck': 0.05,
    'shoot': 0.05
}
tot_weight=0
for i in range(0,len(KEY_LIST)):
    tot_weight += WEIGHT_LIST.values()[i]
assert tot_weight == 1 ,'starting weight error:total weight should be 1'

class TSMWAiObj:
    def __init__(self):
        self.weight_key_dict = {action: [KEY_LIST[action], WEIGHT_LIST[action]] for action in KEY_LIST}
        self.actions = list(self.weight_key_dict.keys())
        self.weights = [weight[1] for weight in self.weight_key_dict.values()]
        self.μ = 0.1
        self.bias = 0.01
        self.running = True

    def do_action(self):
        """根据权重选择动作，并模拟按键"""
        action = random.choices(self.actions, self.weights, k=1)[0]
        key = self.weight_key_dict[action][0]
        pyautogui.press(key)

    def adjust_weight(self, action:str):
        """调整指定动作的权重"""
        if action in self.weight_key_dict:
            self.weight_key_dict[action][1] += self.μ
            self.weights = [weight for _, weight in self.weight_key_dict.values()]

    def stop(self):
        """停止AI运行"""
        self.running = False

def create_table(self, table_name, columns: dict):
    """根据列定义创建表"""
    # 使用列表推导式生成列定义
    column_defs = ', '.join([f"{col_name} {col_type}" for col_name, col_type in columns.items()])
    
    # 构造完整的创建表的 SQL 语句
    create_table_sql = f"""CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        {column_defs}
    );"""
    
    # 执行 SQL 语句创建表
    self.conn.execute(create_table_sql)

    def log(self, action:list):
        """记录动作到数据库"""
        with self.conn:
            insert_sql = f"INSERT INTO {self.table_name} ({str(action)}) VALUES ({len[action]})"
            self.conn.execute(insert_sql, (action, datetime.now().isoformat()))

    def close_connection(self):
        """关闭数据库连接"""
        self.conn.close()

class AiCore(TSMWAiObj):
    def mainloop(self, time_limit=1800):
        """AI主循环,运行指定时间"""
        start_time = datetime.now().timestamp()
        end_time = start_time + time_limit
        while self.running and datetime.now().timestamp() <= end_time:
            self.do_action()
            # TODO:其他逻辑...

class GUIHandler(TSMWAiObj):
    def __init__(self):
        super().__init__()  # 调用父类构造函数
        Tk().title("Toilet Server Misslewars AI Player")
        self.db_action = SQLiteDatabase()  # 实例化数据库操作类
        self.rick=Path("../rick.gif")
    def never_gonna_give_you_up(self):
        canvas = Canvas(tk,width=400,height=400)
        canvas.pack()
        tk.label(tk,self.rick)

    def gui_interface(self):
        """设置GUI界面"""
        startbtn = Button(Tk(), text="Start training", command=self.start_training)
        endbtn = Button(Tk(), text="End training", command=self.stop)
        startbtn.pack()
        endbtn.pack()

    def start_training(self):
        """启动AI训练"""
        time_str = datetime.now().strftime("%Y%m%d%H%M%S")
        columns = {
            'action': 'TEXT',#hen!
            'time': 'TEXT'
        }
        self.db_action.init_table(f"log_{time_str}", columns)
        ai_core = AiCore()
        ai_core.db_action = self.db_action  # 将数据库操作对象传递给AiCore
        ai_core.mainloop()

# 创建主窗口并设置GUI界面
gui_handler = GUIHandler()
gui_handler.gui_interface()
Tk.mainloop()