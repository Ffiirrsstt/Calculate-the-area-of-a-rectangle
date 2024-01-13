from tkinter import Tk ,ttk,messagebox

def submitOk(entryWidth, entryHeight, root):
    widthValue = int(entryWidth.get())
    heightValue = int(entryHeight.get())
    result = widthValue*heightValue
    
    root.destroy()

    root = Tk()
    root.title('Area Calculator')
    answer = ttk.Frame(root, padding=(100,15))
    answer.grid()
    # แสดงคำตอบ
    ttk.Label(answer,text=f"Area of rectangle is : {result}").grid(column=0, row=0)
    btnRetry = ttk.Button(answer,text='Retry',command=lambda:Program_Retry(root))
    btnRetry.grid(column=0, row=4, pady=(15,0))

def Program_Retry(root):
    root.destroy()
    Program()

def Program():
    root = Tk()
    root.title('Area Calculator')
    frm = ttk.Frame(root,padding=(100,40))
    frm.grid()

    style = ttk.Style()
    style.map('TButton',
            background=[('active', 'blue'),('focus', 'blue')],
            color=[('focus', 'blue')],
            )

    # คำถาม
    ttk.Label(frm, text="Enter width").grid(column=0, row=0)
    ttk.Label(frm, text="Enter height").grid(column=0, row=2)
    # คำตอบความกว้าง
    entryWidth = ttk.Entry(frm)
    entryWidth.grid(column=0, row=1,columnspan=2)
    # คำตอบความสูง
    entryHeight = ttk.Entry(frm)
    entryHeight.grid(column=0, row=3,columnspan=2)
    # ปุ่มยกเลิกคำถาม
    btnCancel = ttk.Button(frm, text="Cancel", command=root.destroy)
    btnCancel.grid(column=0, row=4, pady=(10,0))
    # ปุ่มโอเคและทำการคำนวณพื้นที่สี่เหลี่ยม
    btnOK = ttk.Button(frm, text="OK", command=lambda: submitOk(entryWidth, entryHeight, root))
    btnOK.grid(column=1, row=4, pady=(10,0))
    btnOK.configure(style='TButton')
    btnOK.focus_set()
    root.mainloop()

Program()