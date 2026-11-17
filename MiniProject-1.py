from tkinter import *
from tkinter import filedialog, messagebox, Text
from tkinter.ttk import Combobox
from openpyxl import load_workbook
import random
import json


class LifestylePlanner(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.pack()

        self.data={'Sports':[],'Food Plans':[],'Activities':[]}
        self.selected_items={'Sports':[],'Food Plans':[],'Activities':[]}
        self.widgets()

    def widgets(self):
        self.var=StringVar(value='Sports')
        self.combobox=Combobox(self,textvariable=self.var,height=1,width=20,values=['Sports','Food Plans','Activities'])
        self.combobox.grid(row=0,column=2,pady=10)
        self.combobox.bind('<<ComboboxSelected>>',self.update_left_listbox)

        import_button=Button(self, text='Import excel file',command=self.import_excel)
        import_button.grid(row=0,column=0, columnspan=4, pady=10, padx=10)

        self.listbox1=Listbox(self, height=15, width=30)
        self.listbox1.grid(row=1,column=0,padx=10,pady=15)

        self.listbox2=Listbox(self, height=15, width=30)
        self.listbox2.grid(row=1,column=2,columnspan=2,pady=15)

        add_button=Button(self, text='Add', relief=RIDGE, command=self.adding_items)
        add_button.grid(row=2,column=0,pady=10)

        delete_button=Button(self, text='Delete', relief=RIDGE, command=self.deleting_items)
        delete_button.grid(row=2,column=2,columnspan=2,pady=10)

        randomize_button=Button(self, text='Randomize', relief=RIDGE, command=self.random_choice)
        randomize_button.grid(row=3,columnspan=3,padx=30,pady=10)

        self.text=Text(self, height=15, width=90)
        self.text.grid(row=5, columnspan=3,padx=10,pady=10)

        label=Label(self, text='Week Number:')
        label.grid(row=6,column=0,columnspan=3,padx=10,pady=10)

        self.export_type=StringVar(value='txt')
        combobox2=Combobox(self,textvariable=self.export_type,height=1,width=20, values=['txt','json','excel'])
        combobox2.grid(row=7,column=0)

        self.week_number=StringVar()
        entry_box=Entry(self, textvariable=self.week_number)
        entry_box.grid(row=6,column=1, columnspan=2,padx=50,pady=10)


        export_button=Button(self, text='Export', relief=RIDGE, command=self.exporting)
        export_button.grid(row=7,column=2,pady=10)

    def import_excel(self):
        filepath=filedialog.askopenfilename(filetypes=(('Excel files', '*.xlsx'),))
        if not filepath:
            return
        try:
            f=load_workbook(filepath)
            sheet=f.active
            datas=[cell.value for cell in sheet[1]]
            for i, j in enumerate(datas):
                if j in self.data:
                    self.data[j]=[sheet.cell(row=r, column=i+1).value for r in range(2, sheet.max_row+1) if sheet.cell(row=r, column=i+1).value]
            messagebox.showinfo('Success', 'Excel file imported successfully!')
            self.update_left_listbox()
        except Exception as e:
            messagebox.showerror('Importing Error', e)

    def update_left_listbox(self, event=None):
        title=self.var.get()
        self.listbox1.delete(0,END)


        for item in self.data.get(title,[]):
            self.listbox1.insert(END,item)
        self.listbox2.delete(0,END)
        self.refresh_listbox2()

    def adding_items(self):
        title=self.var.get()
        selection=self.listbox1.curselection()
        if  not selection:
            return
        item=self.listbox1.get(selection[0])
        if item in self.selected_items[title]:
            return
        if len(self.selected_items[title]) >=7:
            messagebox.showwarning('You can choose only 7 items')
            return
        self.selected_items[title].append(item)
        self.refresh_listbox2()
        self.refresh_text_widget()

    def deleting_items(self):
        title=self.var.get()
        selection=self.listbox2.curselection()
        if not selection:
            return
        item=self.listbox2.get(selection[0])
        self.selected_items[title].remove(item)
        self.refresh_listbox2()
        self.refresh_text_widget()

    def refresh_listbox2(self):
        title=self.var.get()
        self.listbox2.delete(0,END)
        for i in self.selected_items[title]:
            self.listbox2.insert(END,i)



    def refresh_text_widget(self):
        self.text.delete(1.0,END)
        for category in ['Sports','Food Plans','Activities']:
            self.text.insert(END, f'{category} Plan:\n' )
            for i in self.selected_items[category]:
                self.text.insert(END, f'- {i}\n')
            self.text.insert(END, '\n')

    def random_choice(self):
        for category in ['Sports','Food Plans','Activities']:
            items=self.data.get(category,[])
            if len(items)<7:
                messagebox.showwarning("Insufficient Data", f"Not enough data for category {category} to randomize")
                return
            self.selected_items[category]=random.sample(items,7)
        self.update_left_listbox()
        self.refresh_text_widget()

    def exporting(self):
        week=self.week_number.get().strip()
        if not week:
            messagebox.showerror('Error', 'Please enter a week number')
            return
        export_type=self.export_type.get()
        filename=f'LifestylePlan_for_Week_{week}-{export_type}'
        try:
            if export_type=='txt':
                with open(filename, 'w') as f:
                    f.write(self.text.get(1.0,END))
            elif export_type=='json':
                with open(filename, 'w') as f:
                    json.dump(self.selected_items, f, indent=4)
            elif export_type=='excel':
                from openpyxl import Workbook
                wb = Workbook()
                ws = wb.active
                row=1
                for i in ['Sports','Food Plans','Activities']:
                    ws.cell(row=row, column=1).value=f'{i}\n Plan'
                    row+=1
                    for item in self.selected_items[i]:
                        ws.cell(row=row, column=1).value=item
                        row+=1
                    row+=1
                wb.save(filename)
            messagebox.showinfo(f'{filename} file exported successfully')
        except Exception as e:
            messagebox.showerror('Exporting Error', e)


if __name__=='__main__':
    root=Tk()
    root.geometry("800x770+600+0")
    root.title("Healthy Lifestyle Planner")
    LifestylePlanner(root)
    root.mainloop()



