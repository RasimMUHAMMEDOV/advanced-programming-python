import pandas as pd
import numpy as np
import tkinter as tk 
import matplotlib.pyplot as plt
from tkinter import ttk, filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Data:
    def __init__(self):
        self.df=None 


class Upload:
    def __init__(self, mast, data):
        self.data=data
        self.mast=mast

        self.upload_btn=tk.Button(mast, text='Upload CSV',command=self.upload_file)
        self.upload_btn.pack(pady=15)
        root.geometry('400x100')

    def upload_file(self):
        self.file_csv=filedialog.askopenfilename(filetypes=[('CSV files','*.csv')])
        if not self.file_csv:
            return
        try:
            self.data=pd.read_csv(self.file_csv)
            messagebox.showinfo(title='Success',message=f'Your "{self.file_csv}" is uploaded succesfully')
            Widgets(self.mast, self.data)
        except Exception as e:
            messagebox.showerror(title='Fail',message=f'File you chose "{self.file_csv}" {e}')
        

class Widgets:
    def __init__(self, master,data):
        self.df=data
        self.master=master
        self.filter_data=self.df.copy()
        self.finish=None
        root.geometry('700x700+800+50')

        self.column_label=tk.Label(self.master, text='Select Column:')
        self.column_label.pack(pady=10)

        self.combo=ttk.Combobox(self.master, values=list(self.df.columns)[:3])
        self.combo.current(0)
        self.combo.bind('<<ComboboxSelected>>', self.data_box_update)
        self.combo.pack(pady=10)

        self.data_box=tk.Text(self.master, width=50,height=8)
        self.data_box.pack()

        self.frame1 = tk.Frame(self.master)
        self.frame1.pack()

        self.filter=tk.Label(self.frame1, text='Value Range Filter:')
        self.filter.grid(row=0,column=0, pady=10)

        self.min_value=tk.Entry(self.frame1)
        self.min_value.grid(row=0,column=1, pady=10,padx=3)

        self.max_value=tk.Entry(self.frame1)
        self.max_value.grid(row=0,column=2, pady=10,padx=3)

        self.apply_filter=tk.Button(self.frame1, text='Apply Filter', command=self.apply_filters)
        self.apply_filter.grid(row=0, column=3, pady=10,padx=3)

        self.frame2=tk.Frame(self.master)
        self.frame2.pack()

        self.histogram=tk.Button(self.frame2, text='Histogram',command=self.hist_button)
        self.histogram.grid(row=1,column=0,pady=10,padx=10)

        self.line_plot=tk.Button(self.frame2, text='Line Plot',command=self.line_button)
        self.line_plot.grid(row=1,column=1, pady=10,padx=10)

        self.scatter_plot=tk.Button(self.frame2, text='Scatter Plot',command=self.scatters)
        self.scatter_plot.grid(row=1,column=2, pady=10,padx=10)

        self.pie_chart=tk.Button(self.frame2, text='Pie Chart',command=self.pie_button)
        self.pie_chart.grid(row=1,column=3, pady=10,padx=10)

        self.scatter_x=tk.Label(self.master,text='Scatter X:')
        self.scatter_x.pack(pady=5)

        self.scat_x_box=ttk.Combobox(self.master, values=list(self.df.columns)[:3])
        self.scat_x_box.set('Age')
        self.scat_x_box.pack()

        self.scatter_y=tk.Label(self.master,text='Scatter Y:')
        self.scatter_y.pack(pady=5)

        self.scat_y_box=ttk.Combobox(self.master, values=list(self.df.columns)[:3])
        self.scat_y_box.set('Age')
        self.scat_y_box.pack()

        self.pie_column=tk.Label(self.master,text='Pie Chart Column:')
        self.pie_column.pack(pady=5)

        self.pie_box=ttk.Combobox(self.master, values=self.df.columns[3])
        self.pie_box.set('Department')
        self.pie_box.pack(pady=3)
        
        self.cor=tk.Button(self.master, text='Correlation Heatmap',command=self.heat_map_button)
        self.cor.pack(pady=10)

        self.save_bn=tk.Button(self.master, text='Save Last Plot',command=self.save_plot)
        self.save_bn.pack(pady=10)

        self.last_df=None

        self.data_box_update()

    def apply_filters(self):
        self.combo_get=self.combo.get()     

        self.min_strip=self.min_value.get().strip()
        self.max_strip=self.max_value.get().strip()

        if not self.min_strip and not self.max_strip:
            self.filter_data=self.df.copy()
            self.data_box.delete('1.0', tk.END)
            self.data_box.insert(tk.END, self.filter_data[self.combo_get].describe())
            return

        self.min_get=float(self.min_value.get())
        self.max_get=float(self.max_value.get())


        
        if self.min_get > self.max_get:
            messagebox.showwarning(title='Input error', message='Enter valid numeric inputs')


        else:
            self.filter_data=self.df[(self.df[self.combo_get]>=self.min_get) & (self.df[self.combo_get]<=self.max_get)]
            self.data_box.delete('1.0',tk.END)
            self.data_box.insert(tk.END, self.filter_data[self.combo_get].describe())
       

    def data_box_update(self, event=None):
        self.combo_get=self.combo.get()

        self.data_box.delete('1.0', tk.END)
        self.data_box.insert(tk.END,self.filter_data[self.combo_get].describe())

    def hist_button(self,event=None):
        self.combo_get=self.combo.get()
        self.drawing, self.unpacking=plt.subplots()
        self.unpacking.hist(self.filter_data[self.combo_get], bins=10, edgecolor='black', width=2.5)
        self.unpacking.set_title(f'Histogram of {self.combo_get}')

        self.show_draws(self.drawing,f'Figure 1: "{self.combo_get}"')
    
    def line_button(self):
        self.combo_get=self.combo.get()
        self.drawing, self.unpacking=plt.subplots()
        self.unpacking.plot(self.filter_data[self.combo_get], marker='o')
        self.unpacking.set_title(f'Line Plot of {self.combo_get}')

        self.show_draws(self.drawing,f'Figure 1:{self.combo_get}')


    def scatters(self):
        scatt_x=self.scat_x_box.get()
        scatt_y=self.scat_y_box.get()

        if scatt_x not in self.filter_data.columns or scatt_y not in self.filter_data.columns:
            messagebox.showerror('error','no columns')
            return



        self.drawing, self.unpacking=plt.subplots()
        self.unpacking.scatter(self.filter_data[scatt_x], self.filter_data[scatt_y])
        self.unpacking.set_title(f'Scatter Plot {scatt_x} vs {scatt_y}')
        self.unpacking.set_xlabel(scatt_x)
        self.unpacking.set_ylabel(scatt_y)
        self.show_draws(self.drawing,f'Figure 1')


    def pie_button(self):
        self.pie_get=self.pie_box.get()
        self.datas_box=self.df[self.pie_get].value_counts()
        self.drawing, self.unpacking=plt.subplots()
        self.unpacking.pie(self.datas_box, labels=self.datas_box.index, autopct='%1.1f%%')
        self.unpacking.set_title('Pie Chart')
        self.show_draws(self.drawing, 'Figure 1')


    def heat_map_button(self):
        self.cor_data=self.df.select_dtypes(include=[np.number])
        self.correlation=self.cor_data.corr()
        self.drawing, self.unpacking=plt.subplots()
        self.unpack=self.unpacking.imshow(self.correlation, cmap='coolwarm', interpolation='nearest')
        self.unpacking.set_xticks(np.arange(len(self.correlation.columns)))
        self.unpacking.set_yticks(np.arange(len(self.correlation.columns)))
        self.unpacking.set_xticklabels(self.correlation.columns,rotation=45, ha='right')
        self.unpacking.set_yticklabels(self.correlation.columns)
        self.drawing.colorbar(self.unpack)
        self.unpacking.set_title('Correlation Heatmap')
        self.show_draws(self.drawing, 'Figure 1')
        print(self.df.corr())

    def show_draws(self,draws, title):
        self.lib=tk.Toplevel(self.master)
        self.lib.title(title)
        self.canvas=FigureCanvasTkAgg(self.drawing, master=self.lib)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        self.finish=draws

    def save_plot(self):
        if self.finish:
            file_path=filedialog.asksaveasfilename(defaultextension='.png',filetypes=[('PNG files','*.png')])

            if file_path:
                self.finish.savefig(file_path)
                messagebox.showinfo(title='Success', message=f'{file_path} Plot saved')
        else:
            messagebox.showerror(title='Fail',message='Nothing to save')





if __name__=='__main__':
    root=tk.Tk()
    root.title('Visual Data Explorer')
    root.geometry('400x100')
    data=Data()
    Upload(root, data)
    root.mainloop()


"""
References:

Heatmap: https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html

Pie Chart: https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html 



https://www.google.com/search?q=PythonProgramming.net%3A+How+to+Embed+a+Matplotlib+Graph+into+Your+Tkinter+GUI&oq=PythonProgramming.net%3A+How+to+Embed+a+Matplotlib+Graph+into+Your+Tkinter+GUI&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRiPAjIHCAIQIRiPAjIHCAMQIRiPAtIBCTE0NTdqMGoxNagCCLACAQ&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:ef995b7e,vid:lVTC8CvScQo,st:0
"""

    
