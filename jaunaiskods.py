import tkinter as tk

root = tk.Tk()
root.title("Programme")
root.geometry('800x800')
root.resizable(False, False)

canvas = tk.Canvas(root, bg="#AAD6BE", height=800, width=800)
canvas.pack(fill="both", expand=True)

jours = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche")

list1 = ("Fizika", "Matemātika", "Angļu valoda", "Vēsture")
list2 = ("Latviešu valoda", "Ģeogrāfija", "Bioloģija", "Ķīmija", "Fizika", "Franču valoda")
list3 = ("Sports", "Matemātika", "Programmēšana")
list4 = ("Latviešu valoda", "Matemātika", "Angļu valoda", "Sports", "Programmēšana")
list5 = ("Literatūra", "Ķīmija", "Klases stunda")
nav = ("Stundas nav!",)
all_lists = [list1, list2, list3, list4, list5]

def show_message(text):
    canvas.delete("all")
    canvas.create_text(400, 100, text=text, font=("Comic Neue", 20), fill="#000000")

def show_subjects(subjects):
    canvas.delete("all")
    canvas.create_text(400, 100, text="Šodienas stundas:", font=("Comic Neue", 22, "bold"), fill="#382B21")
    y = 160
    for subj in subjects:
        canvas.create_text(400, y, text=subj, font=("Comic Neue", 20), fill="#385D47")
        y += 40
    again_button = tk.Button(root, text="Izvēlēties citu dienu", command=start)
    canvas.create_window(400, y + 40, window=again_button)


###izvada sarakstu###
def check_day():
    day = entry.get().strip()
    entry.delete(0, tk.END)

    if day == "Lundi":
        show_subjects(list1)
    elif day == "Mardi":
        show_subjects(list2)
    elif day == "Mercredi":
        show_subjects(list3)
    elif day == "Jeudi":
        show_subjects(list4)
    elif day == "Vendredi":
        show_subjects(list5)
    elif day in ("Samedi", "Dimanche"):
        show_subjects(nav)
    else:
        show_message("Kaut kas ievādīts nepareizi!")

def start():
    canvas.delete("all")
    canvas.create_text(400, 100, text="Ievādi dienas nosaukumu:", font=("Comic Neue", 22), fill="#382B21")
    global entry
    entry = tk.Entry(root, font=("Comic Neue", 18))
    canvas.create_window(400, 150, window=entry)
    ok_button = tk.Button(root, text="OK", command=check_day)
    canvas.create_window(400, 200, window=ok_button)

start()


###saskaita prekšmētu skaitu###
i = 0
def pskaits():
    prieksmets = entry.get().strip()
    entry.delete(0, tk.END)
    
    while i < len(all_lists):
        current_list = all_lists[i]
        canvas.create_text(400, 100, text=f"\Parbaudu sarakstu {i + 1}: {current_list}", font=("Comic Neue", 22), fill="#382B21")
        j = 0
        while j < len(current_list):
            if current_list[j] == prieksmets:
                canvas.create_text(400, 100, text=f"\Atrādu 'prieksmets' in list {i + 1}, vietā {j}", font=("Comic Neue", 22), fill="#382B21")
            j += 1
        i += 1
    
def pskaits():
    prieksmets = entry.get().strip()
    entry.delete(0, tk.END)
    i = 0

     


root.mainloop()
