# Q1-Task 1

import json

with open('university_data.json', 'r') as file:
    data = json.load(file)

    faculty_names = []
    faculty_count=0
    total_credit=[]
    course_name_and_code={}
    for departments in data['faculties']:
        faculty_names.append(departments['faculty_name'])
        faculty_count+=1
        if departments['faculty_name']=='Faculty of Engineering':
            for courses in departments['departments']:
                for credits in courses['courses']:
                    integer=int(credits['credits'])
                    total_credit.append(integer)
    #print(faculty_names)
    print(f"Number of Faculties:{faculty_count}")
    print(f"Faculty of Engineering total number of credits:{sum(total_credit)}\n")
    for departments in data['faculties']:
        for courses in departments['departments']:
            for codes in courses['courses']:
                course_name_and_code[codes['course_name']]=codes['course_code']
                #course_name_and_code.append((codes['course_name'])+codes['course_code'])
    print(f"\n{' '*6}Course Codes With Their Names \n{"--"*25}")
    for name,code in course_name_and_code.items():
        print(f"{name} : {code}")



# Q1-Task 2

from openpyxl import load_workbook


file='school_data.xlsx'
excel=load_workbook(file)
sheet=excel.active

male_students=0
female_students=0


student_list=[]
high_gpa={}
header=[cell.value for cell in sheet[1]]
ages=[]
total_gpa_male_students=[]


for i in sheet.iter_rows(min_row=2, values_only=True):
    student_data=dict(zip(header,i))
    student_list.append(student_data)


for data in student_list:
    ages.append(data['Age'])
    if data['Gender']=='Male':
        male_students += 1
    elif data['Gender']=='Female':
        female_students += 1
    if data['GPA']>=3.5:
        high_gpa[data["Name"]]=data['GPA']
    if data['Gender']=='Male':
        total_gpa_male_students.append(data['GPA'])

print(f"Number of male students:{male_students}")
print(f"Number of female students:{female_students}\n")
print(f"{" "*6}Students with 3.5 GPA or Above\n{"--"*20}")
for name,gpa in high_gpa.items():
    print(f"{name} : {gpa}")
print("\n")

ages.sort()
number=len(ages)
if number%2==1:
    median=ages[int(number//2)]
    print(f"Median Age of Students: {int(median)}")
else:
    median=(ages[int(number//2)]+ages[int(number//2)-1])/2
    print(f"Median Age of Students: {int(median)}")

print(f"The Total GPA of Male Students:{sum(total_gpa_male_students)}")


# Q1-Task 3

import os

def find_files(directory, extension):
    m_files=[]
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                m_files.append(os.path.join(root, file))
    return m_files

directory_path="C:\\Users\\Rasim\\PycharmProjects"
extension=".py"
result= find_files(directory_path, extension)

for file in result:
    print(file)


# Q1-Task 4

with open('abc.txt','r') as f:
    reversed_text=[]
    f.seek(0)
    abc_data=f.readlines()
    for line in abc_data[::-1]:
        reversed_text.append(line)
    with open('reversed_text.txt','w+') as file:
        for i in reversed_text:
            file.write(i)



# Q1-Task 5

with open('words.txt','r') as f:
    f.seek(0)
    read=f.read()
    letter_frequency={}
    for words in read.lower().split('\n'):
        #print(words)
        for letter in words:
            if letter in letter_frequency:
                letter_frequency[letter]+=1
            else:
                letter_frequency[letter]=1
    #print(letter_frequency)
    with open('letter_frequency.txt','w+') as file:
        letter_n=0
        l_count="Letter"
        for i,j in letter_frequency.items():
            letter_n+=1
            file.write(f"{l_count+str(letter_n)} is '{i}' frequency is: {j}\n")



# Q1-Task 6

def error_handling(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")

def main():
    num1=error_handling("Enter first number:")
    num2=error_handling("Enter second number:")

    try:
        result=num1/num2
        print(f"The result is: {result}")
    except ZeroDivisionError:
        print("Please enter a valid number.")

main()




# Q1-Task 7

file_name='not_existing_file.txt'

try:
    with open(file_name,'r') as f:
        read_file=f.read()
        print(read_file)

except FileNotFoundError:
    print(f"File with the name:'{file_name}' does not exist. "
          f"Please check the file name and ensure you typed it correctly.")



# Q2-Task 1


import tkinter as tk

def selections():
    selects=[color for color, var in check_vars.items() if var.get() ]
    if selects:
        print('Selected colors:',','.join(selects))
    else:
        print('No colors selected.')

root = tk.Tk()
root.title('Favorite Color Selection')
a=tk.Label(root,text="What is Your Favorite Color?",font=10)
a.pack(pady=10)

check_vars={
    "Red":tk.BooleanVar(),
    "Green":tk.BooleanVar(),
    "Blue":tk.BooleanVar(),
    "Yellow":tk.BooleanVar(),
    "Purple":tk.BooleanVar(),
    "White":tk.BooleanVar()
}
for color, var in check_vars.items():
    tk.Checkbutton(root, text=color, variable=var, command=selections).pack(anchor="w")

root.mainloop()


# Q2-Task 2

# Version-1
import tkinter as tk

def greeting():
    name=entry.get()
    if name:
        print(f"Hello and 'Bye' {name}")
    else:
        print("Please enter a name.")

root=tk.Tk()
root.title('TKINTER App')

tk.Label(root,text="Enter your name").pack(pady=10)
entry=tk.Entry(root)
entry.pack(pady=10)

tk.Button(root, text="Submit", command=greeting).pack(pady=10)
root.mainloop()




# Version-2

import tkinter as tk

def greeting():
    name=entry.get()
    if name:
        greeting_label.config(text=f"Hello and 'Bye' {name}")
        greeting_box.pack(pady=10,padx=30)
    else:
        messagebox.showwarning("Please enter a name.")

def closing_box():
    root.quit()

root=tk.Tk()
root.title('TKINTER App')
tk.Label(root,text="Enter your name").pack(pady=20,padx=30)

entry=tk.Entry(root)
entry.pack(pady=20,padx=30)

tk.Button(root, text="Submit", command=greeting).pack(pady=20,padx=30)

greeting_box=tk.Frame(root)
greeting_label=tk.Label(greeting_box,text="Greeting")
greeting_label.pack(pady=10,padx=30)

greeting_box.pack_forget()
root.protocol("WM_DELETE_WINDOW", closing_box)

root.mainloop()




# Q2-Task 3

import tkinter as tk
from tkinter import messagebox

def selecting(event):
    selected_item=listbox.curselection()
    if selected_item:
        selected_text=listbox.get(selected_item)
        label.config(text=f"Selected:{selected_text}")

root=tk.Tk()
root.title('Hello World')
listbox=tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=10,padx=30)

texts=["Uskudar","Kadikoy","Maltepe","Kartal"]
for text in texts:
    listbox.insert(tk.END, text)

listbox.bind('<<ListboxSelect>>',selecting)
label=tk.Label(root)
label.pack(pady=10,padx=30)
root.mainloop()