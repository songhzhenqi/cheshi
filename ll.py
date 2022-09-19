# coding=utf-8
import tkinter as tk
import tkinter.messagebox
import random
import re
if __name__ == '__main__':

 game = tk.Tk()
game.geometry('450x200')
game.title('猜数字小游戏')

# 全局变量：不重复的四位数
list1 = (random.sample(range(0,10), 4))
flag = 1

label1 = tk.Label(game, fg='Teal', text="系统随机生成一个不重复的四位数，请你猜出这个数",
                  wraplength=250, justify='center', font=('楷体', 10))
label1.grid(row=0, padx=20, pady=8, columnspan=2, rowspan=2)

label2 = tk.Label(game, text='输入一个各位不相同的4位数字', bg='LightSeaGreen', font=('楷体', 10))
label2.grid(row=2, column=0, sticky='w', padx=5)

text = tk.Entry(game, width=20)
text.grid(row=2, column=1, sticky='w')

# 点击确定，按钮触发事件


def hs():
    gn = text.get()
    if gn == '':
        tk.messagebox.showwarning("警告", "输入不能为空")
    else:
        if not re.findall('[0-9]+', str(gn)):
            tk.messagebox.showwarning("警告", "只能输入数字")
        elif len(str(gn)) > 4:
            tkinter.messagebox.showwarning("提示", '输入长度大于4，请重新输入')
        elif len(str(gn)) < 4:
            tkinter.messagebox.showwarning("提示", '输入长度小于4，请重新输入')
        else:
            num = int(gn)
            array = [int(num / 1000), int((num / 100) % 10), int((num / 10) % 10), int(num % 10)]
            print(array)
            (a, b) = (0, 0)
            count = 0
            while count < len(array) - 1:
                print (len(array))
                if array[count] == array[count + 1]:
                    tkinter.messagebox.showwarning("提示", '请输入不重复的四位数')
                else:
                    count += 1
                break
            for i in range(0, 4):
              if array[i] == list1[i]:
               a += 1
              else:
                if any([list1[i] == array[0], list1[i] == array[1], list1[i] == array[2], list1[i] == array[3]]):
                    b += 1
            if a == 4:
                tkinter.messagebox.showinfo("正确", "恭喜你，猜对了!")
            else:
                tkinter.messagebox.showinfo("答案提示", "%dA%dB" % (a, b))


def hy():
    tkinter.messagebox.showinfo("答案",list1)


def rules():
    tkinter.messagebox.showinfo("玩法",'每猜一次，出数者就要根据这个数字给出几A几B，其中A前面的数字表示位置正确的数的个数，而B前的数字表示数字正确而位置不对的数的个数。如正确答案为 5234，而猜的人猜 5346，则是 1A2B，其中有一个5的位置对了，记为1A，而3和4这两个数字对了，而位置没对，因此记为 2B，合起来就是 1A2B。')


def fresh():
    global list1
    list1 = (random.sample(range(0, 10), 4))
    tkinter.messagebox.showinfo("重置", '重置成功，继续游戏吧')


def myself():
    tkinter.messagebox.showinfo("自定义",'未开发！')


button2 = tkinter.Button(game, text='确定', command=hs, width=10, bg='SkyBlue', font=('楷体', 10))
button2.grid(row=2, column=2, sticky='s', padx=6, pady=5)

button5 = tkinter.Button(game, text='玩法', command=rules, width=10, bg='SkyBlue', font=('楷体', 10))
button5.grid(row=3, column=1, sticky='s', padx=5, pady=5)

button4 = tkinter.Button(game, text='答案', command=hy, width=10, bg='SkyBlue', font=('楷体', 10))
button4.grid(row=3, column=2, sticky='s', padx=5, pady=5)

button5 = tkinter.Button(game, text='重置', command=fresh, width=10, bg='SkyBlue', font=('楷体', 10))
button5.grid(row=4, column=1, sticky='s', padx=5, pady=5)

button3 = tkinter.Button(game, text='退出', command=quit, width=10, bg='SkyBlue', font=('楷体', 10))
button3.grid(row=4, column=2, sticky='s', padx=5, pady=5)

button6 = tkinter.Button(game, text='自定义', command=myself, width=12, bg='SkyBlue', font=('楷体', 10))
button6.grid(row=5, column=2, sticky='s', padx=5, pady=5)



game.mainloop()
