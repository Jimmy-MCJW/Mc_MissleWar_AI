#1.tk.Tk()
#创建主窗口。
#示例：
import tkinter as tk
root=tk.Tk()

#2.mainloop()
#启动事件循环。
#示例：
root.mainloop()

#3.destroy()
#销毁窗口。
#示例：
root.destroy()

#4.geometry()
#设置窗口大小和位置。
#示例：
root.geometry("300x200+100+100")#宽度x高度+x位置+y位置

#5.title()
#设置窗口标题。
#示例：
root.title("我的窗口")

#6.Label()
#创建标签。
#示例：
label=tk.Label(root,text="你好，世界！")
label.pack()

#7.Button()
#创建按钮。
#示例：
def say_hello():
     print("你好！")

button=tk.Button(root,text="点击我",command=say_hello)
button.pack()

#8.Entry()
#创建文本输入框。
#示例：
entry=tk.Entry(root)
entry.pack()

#9.Text()
#创建多行文本框。
#示例：
text=tk.Text(root)
text.pack()

#10.Canvas()
#创建画布。
#示例：

canvas=tk.Canvas(root,width=200,height=200)
canvas.pack()


#11.Listbox()
#创建列表框。
#示例：

listbox=tk.Listbox(root)
listbox.pack()
listbox.insert(tk.END,"项目1")
listbox.insert(tk.END,"项目2")


#12.Checkbutton()
#创建复选框。
#示例：

check=tk.Checkbutton(root,text="复选框")
check.pack()


#13.Radiobutton()
#创建单选按钮。
#示例：

radio1=tk.Radiobutton(root,text="选项1",value=1)
radio2=tk.Radiobutton(root,text="选项2",value=2)
radio1.pack()
radio2.pack()


#14.Scrollbar()
#创建滚动条。
#示例：

scroll=tk.Scrollbar(root)
scroll.pack(side=tk.RIGHT,fill=tk.Y)


#15.Scale()
#创建滑动条。
#示例：

scale=tk.Scale(root,from_=0,to=100)
scale.pack()


#16.Frame()
#创建框架。
#示例：

frame=tk.Frame(root)
frame.pack()


#17.pack()
#组件的自动布局。
#示例：

label.pack(side=tk.TOP)


#18.grid()
#组件的网格布局。
#示例：

label.grid(row=0,column=0)


#19.place()
#组件的绝对布局。
#示例：

label.place(x=10,y=10)


#20.bind()
#绑定事件。
#示例：

root.bind("<Key>",lambda event:print("按键:",event.char))
