import tkinter as tk
from tkinter import messagebox
import time

def start_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=time_format)
        root.update()
        time.sleep(1)
        seconds -= 1
    messagebox.showinfo('专注结束', '专注时间结束！')

# 创建窗口
root = tk.Tk()
root.title('专注时钟')

# 设置窗口大小
root.geometry('300x150')

# 创建标签用于显示时间
label = tk.Label(root, text='', font=('Helvetica', 48))
label.pack(pady=20)

# 设置专注时间（以分钟为单位）
focus_time = 25

# 创建开始按钮
start_button = tk.Button(root, text='开始专注', command=lambda: start_timer(focus_time))
start_button.pack()

# 运行窗口
root.mainloop()
