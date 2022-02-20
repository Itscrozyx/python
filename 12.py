import csv
from os import path
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

bgColor = "#C6E2E9"

app = Tk()
app.option_add("*font", "Tahoma 16 bold")
app.geometry("700x400")
app.config(background=bgColor)
app.title("ประเมินอาการเสี่ยง")
locationVar = StringVar()
timeVar = StringVar()
peopleVar = StringVar()

def save():
    global de
    global dmhtavar
    global var1
    global var2
    global var3
    global var4
    
    try:
        data = [de.get_date(), dmhtavar.get(), var1.get(), var2.get(), var3.get() , var4.get()]
        
        if not path.exists("ประเมินอาการเสี่ยง.csv"):
            header = ["วันที่", "DMHTA", "1", "2", "3", "4"]
            with open('ประเมินอาการเสี่ยง.csv', 'w', encoding='UTF-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerow(data)
        else:
            with open('ประเมินอาการเสี่ยง.csv', 'a', encoding='UTF-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)
        messagebox.showinfo("Saved", "ข้อมูลของคุณถูกบันทึกแล้ว")
    except Exception as err:
        messagebox.showerror("Error", err)



dmhtavar = StringVar()
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()


Label(app, text="ประเมินอาการเสี่ยง", background=bgColor).grid(row=0, column=1)
Label(app, background=bgColor).grid(row=1, column=0)
Label(app, text="วันที่", background=bgColor).grid(row=2, column=0)
de = DateEntry(app,selectmode='day', date_pattern='dd/MM/yyyy')
de.grid(row=2, column=1)

Label(app, text="ท่านปฎิบัติตามมาตรการ DMHTA", background=bgColor).grid(row=3, column=0)
Label(app, text="ปฎิบัติ", background=bgColor).grid(row=3, column=1)
Radiobutton(app, value="ปฎิบัติ", variable=dmhtavar).grid(row=3, column=2)
Label(app, text="ไม่ปฎิบัติ", background=bgColor).grid(row=3, column=3)
Radiobutton(app, value="ไม่ปฎิบัติ", variable=dmhtavar).grid(row=3, column=4)


Label(app, text="มีอาการเสี่ยง", background=bgColor).grid(row=5, column=0)
Label(app, text="มี", background=bgColor).grid(row=5, column=1)
Radiobutton(app, value="มี", variable=var1).grid(row=5, column=2)
Label(app, text="ไม่มี", background=bgColor).grid(row=5, column=3)
Radiobutton(app, value="ไม่มี", variable=var1).grid(row=5, column=4)

Label(app, text="เสียการดมกลิ่น ลิ้นไม่รับรส", background=bgColor).grid(row=7, column=0)
Label(app, text="มี", background=bgColor).grid(row=7, column=1)
Radiobutton(app, value="มี", variable=var2).grid(row=7, column=2)
Label(app, text="ไม่มี", background=bgColor).grid(row=7, column=3)
Radiobutton(app, value="ไม่มี", variable=var2).grid(row=7, column=4)

Label(app, text="หายใจลำบาก เจ็บแน่นหน้าอก", background=bgColor).grid(row=9, column=0)
Label(app, text="มี", background=bgColor).grid(row=9, column=1)
Radiobutton(app, value="มี", variable=var3).grid(row=9, column=2)
Label(app, text="ไม่มี", background=bgColor).grid(row=9, column=3)
Radiobutton(app, value="ไม่มี", variable=var3).grid(row=9, column=4)

Label(app, text="มีการเดินทางไปสถานที่เสี่ยง", background=bgColor).grid(row=11, column=0)
Label(app, text="มี", background=bgColor).grid(row=11, column=1)
Radiobutton(app, value="มี", variable=var4).grid(row=11, column=2)
Label(app, text="ไม่มี", background=bgColor).grid(row=11, column=3)
Radiobutton(app, value="ไม่มี", variable=var4).grid(row=11, column=4)




Label(app, background=bgColor).grid(row=15, column=0)
Button(app, text="บันทึก", width=5, height=1, command=save).grid(row=16, column=1)





app.mainloop()