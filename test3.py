from tkinter import *
import time


def myset(num, var):
#    var = StringVar()
#    disp_label = Label(top, textvariable=var)

    var.set("{0}".format(num))
#    disp_label.pack(fill=X, expand=NO, pady=2, padx=2)


def mytest():
    var = StringVar()
    disp_label = Label(top, textvariable=var)
    disp_label.pack(fill=X, expand=NO, pady=2, padx=2)
    for i in range(0, 3):
        print(i)
        myset(i, var)
        time.sleep(2)
    pass


top = Tk()
top.title("测试 作者:刘锐")
top.geometry('250x150')
butt_frame = Frame(top)
butt_frame.pack(side=BOTTOM)
commit_butt = Button(butt_frame, text='开始', command=mytest)
commit_butt.pack(side=RIGHT)

top.mainloop()