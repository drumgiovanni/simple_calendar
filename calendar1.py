from tkinter import Frame, Button, LEFT, RIGHT, BOTTOM, StringVar, Label, Entry, END, CENTER
import calendar


class Calendar1(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("カレンダー")
        self.year = 2018
        self.month = 1
        # タイトル
        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="カレンダーだよ", font=("Sans-serif", 32)).pack()
        # 入力フィールド
        frame3 = Frame(self)
        frame3.pack()
        self.ent1 = Entry(frame3, font=("Helvetica", 24), width=5)
        self.ent1.insert(END, self.year)
        self.ent1.pack(side=LEFT)
        Label(frame3, text="年", font=("Sans-serif", 23)).pack(side=LEFT)
        self.ent2 = Entry(frame3, font=("Helvetica", 24), width=2)
        self.ent2.insert(END, self.month)
        self.ent2.pack(side=LEFT)
        Label(frame3, text="月", font=("Sans-serif", 23)).pack(side=LEFT)
        Button(frame3, text="表示", command=self.setcal, font=("Times", 20)).pack(side=RIGHT)
        self.result = StringVar()
        Label(self, textvariable=self.result, font=("Times", 18), width=30).pack()
        self.setcal()

    def setcal(self):
        self.year = int(self.ent1.get())
        self.month = int(self.ent2.get())
        cal = calendar.month(self.year, self.month)
        self.result.set(cal)

Calendar1().mainloop()
