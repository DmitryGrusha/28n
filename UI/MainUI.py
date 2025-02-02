import tkinter as tk
from tkinter import filedialog
import pandas as pd

from Handlers.MainHandlers import *
from CreateFiles.Excel import *
from CreateFiles.Word import *


inputValues = pd.DataFrame()
cabinesNumbers = {}
root = tk.Tk()
cabinetsCheckmark = tk.Canvas
cabinetsSquare = cabinetsCheckmark
inputCheckmark = tk.Canvas
inputSquare = inputCheckmark
button3 = tk.Button

def createData(input):
    global inputValues
    allData = input.iloc

    for user in allData:
        fullName = user["ФИО:"]
        print(f"Создание файла для пациента - {fullName}")
        birthday = user["Дата рождения:"]
        age = getAge(birthday)
        sex = getSex(user["Пол:"])
        job = user["Место работы:"]
        position = user["Должность:"]
        agePeriodization = getAgePeriodization(sex, age)
        p = user["Пункты вредности:"]

        problems = definingPoints(user["Пункты вредности:"])
        doctors = getUniqueDoctors(problems, sex, cabinesNumbers)
        cabinets = getUniqueCabinets(problems, sex, agePeriodization, cabinesNumbers)

        date_only = birthday.strftime("%Y-%m-%d")
        createWordA5(fullName, sex.value, date_only, f'{age}', job, position, p, doctors, cabinets)

    inputCheckmark.itemconfig(cabinetsSquare, fill='red', outline='red')
    inputValues = pd.DataFrame()
    button3.config(state='disabled')


def openFile():
    global inputValues
    global cabinesNumbers
    global button3
    file_path = filedialog.askopenfilename(
        title="Выберите файл",
        filetypes=[("Excel files", "*.xlsx")]
    )
    if file_path:
        try:
            input = pd.read_excel(file_path, engine='openpyxl')
            inputValues = input
            inputCheckmark.itemconfig(cabinetsSquare, fill='#90EE90', outline='#90EE90')

            if not inputValues.empty:
                if len(cabinesNumbers) != 0:
                    button3.config(state='normal')


        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")



def loadCabinetNumber():
    global cabinesNumbers
    global inputValues
    global cabinetsCheckmark
    global cabinetsSquare
    file_path = filedialog.askopenfilename(
        title="Выберите файл со списком кабинетов",
        filetypes=[("Excel files", "*.xlsx")]
    )
    if file_path:
        try:
            cabinets = pd.read_excel(file_path, engine='openpyxl')
            cabinetsDict = {}

            for cabinet in cabinets.iloc:
                name = cabinet["Кабинет:"]
                number = cabinet["№:"]
                cabinetsDict[name] = number

            cabinesNumbers = cabinetsDict

            cabinetsCheckmark.itemconfig(cabinetsSquare, fill='#90EE90', outline='#90EE90')

            if not inputValues.empty:
                if len(cabinesNumbers) != 0:
                    button3.config(state='normal')

        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")

def createFiles():
    global inputValues
    if not inputValues.empty:
        createData(inputValues)
    else:
        print("Нет данных для создания файлов")

def createUI():
    global root
    global cabinetsCheckmark
    global cabinetsSquare
    global inputCheckmark, inputSquare
    global button3
    root.title("")

    main_frame = tk.Frame(root)
    main_frame.pack(pady=10)

    frame1 = tk.Frame(main_frame)
    frame1.pack(side=tk.LEFT)

    button1 = tk.Button(frame1, text="Загрузись список кабинетов", command=loadCabinetNumber)
    button1.pack(side=tk.LEFT, padx=5)

    cabinetsCheckmark = tk.Canvas(frame1, width=12, height=12, bg='white', bd=0, highlightthickness=0)
    cabinetsCheckmark.pack(side=tk.LEFT, padx=5)

    cabinetsSquare = cabinetsCheckmark.create_rectangle(0, 0, 12, 12, fill='red', outline='red')

    frame2 = tk.Frame(main_frame)
    frame2.pack(pady=10, fill=tk.X)

    button2 = tk.Button(frame2, text="Загрузить список пациентов", command=openFile)
    button2.pack(side=tk.LEFT, padx=5)

    inputCheckmark = tk.Canvas(frame2, width=12, height=12, bg='white', bd=0, highlightthickness=0)
    inputCheckmark.pack(side=tk.LEFT, padx=5)

    inputSquare = inputCheckmark.create_rectangle(0, 0, 12, 12, fill='red', outline='red')

    button3 = tk.Button(root, text="Создать", command=createFiles, font=("Arial", 12, "bold"))
    button3.pack(side=tk.BOTTOM, pady=10)
    button3.config(state='disabled')

    root.update_idletasks()

    width = root.winfo_width()
    height = root.winfo_height()

    padding = 50
    root.geometry(f"{width + 2 * padding}x{height + 2 * padding}")

    root.resizable(False, False)

    root.mainloop()