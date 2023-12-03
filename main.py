import tkinter as tk
from tkinter import ttk
from animals import *


class InfoAnimals(tk.Frame):

    def __init__(self, win):   
        super().__init__(win)
        self.init_info_animals()
        self.btn()
        self.tree_view()
        self.db = Shelter()
        self.output()

    def init_info_animals(self):
        self.fr = ttk.Frame().pack(padx=0, pady=26)

    def btn(self):
        ttk.Button(self.fr, text="Ввод данных", command=DataAnimals)\
            .place(x=10, y=13)
        ttk.Button(self.fr, text="Удаление", command=self.delete_animal)\
            .place(x=130, y=13)
        ttk.Button(self.fr, text="Выход", command=win.destroy)\
            .place(x=600, y=13)

    def tree_view(self):
        list_anim = ["id", "animals", "name", "bread", "age", "gender"]
        list_head = ["ID", "Животное", "Кличка", "Порода", "Возраст", "Пол"]
        dict_list = dict(zip(list_anim, list_head))
        self.tree = ttk.Treeview(self, columns=(list_anim),\
                                height=26, show="headings")
        self.tree.column("id", width=40, anchor=tk.CENTER)
        for i in list_anim[1:]:
            self.tree.column(i, width=140, anchor=tk.CENTER)
        for k, v in dict_list.items():
            self.tree.heading(k, text=v)

        self.tree.pack(expand=True, fill="both")

    def output(self):        
        self.db.cur.execute("SELECT * FROM animals_table")
        for i in self.tree.get_children():
            self.tree.delete(i)
        for i in self.db.cur.fetchall():
            self.tree.insert("", "end", values=i)

    def delete_animal(self):
        for j in self.tree.selection():
            self.db.cur.execute("""DELETE FROM animals_table WHERE
                                id==?""", (self.tree.set(j, "#1"),))
            self.db.db.commit()
            self.tree.delete(j)


class DataAnimals(tk.Toplevel):    
    
    def __init__(self):
        super().__init__()
        self.init_data_animals()
        self.str_var()
        self.label()
        self.entry()
        self.cmbox()
        self.radio_button()
        self.btn()
        self.sh = Shelter()
        self.app = app        

    def init_data_animals(self):
        self.title("Ввод данных")
        self.geometry("580x340+480+280")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

    def str_var(self):        
        self.animals_result = tk.StringVar(value="Собака")
        self.name_al = tk.StringVar()
        self.breed_al = tk.StringVar()
        self.age_al = tk.StringVar()
        self.gender_als = tk.StringVar()

    def label(self):        
        ttk.Label(self, text="Вы ввели данные:",\
                  font=title_font).place(x=370, y=80)

        ttk.Label(self, text="Животное", font=title_font).place(x=240, y=10)
        ttk.Label(self, textvariable=self.animals_result).place(x=460, y=105)
        ttk.Label(self, text="Животное:").place(x=365, y=105)
        
        ttk.Label(self, text="Кличка:").place(x=20, y=100)
        ttk.Label(self, textvariable=self.name_al).place(x=460, y=125)
        ttk.Label(self, text="Кличка:").place(x=386, y=125)

        ttk.Label(self, text="Порода:").place(x=20, y=130)
        ttk.Label(self, textvariable=self.breed_al).place(x=460, y=145)
        ttk.Label(self, text="Порода:").place(x=384, y=145)

        ttk.Label(self, text="Возраст:").place(x=20, y=160)
        ttk.Label(self, textvariable=self.age_al).place(x=460, y=165)
        ttk.Label(self, text="Возраст:").place(x=380, y=165)

        ttk.Label(self, text="Пол:").place(x=20, y=190)
        ttk.Label(self, textvariable=self.gender_als).place(x=460, y=185)
        ttk.Label(self, text="Пол:").place(x=410, y=185)
        
    def entry(self):
        ttk.Entry(self, width=20, textvariable=self.name_al,\
            font=_font).place(x=100, y=100)        
        ttk.Entry(self, width=20, textvariable=self.breed_al,\
            font=_font).place(x=100, y=130)
        ttk.Entry(self, width=20, textvariable=self.age_al,\
            font=_font).place(x=100, y=160)
    
    def radio_button(self):
        ttk.Radiobutton(self, text="муж.", value="мужской",\
            variable=self.gender_als,\
            command=self.gender_animals).place(x=120, y=190)
        ttk.Radiobutton(self, text="жен.", value="женский",\
            variable=self.gender_als,\
            command=self.gender_animals).place(x=200, y=190)

    def btn(self):
        ttk.Button(self, text="Готово",\
                   command=self.data_animals).place(x=420, y=230)
        ttk.Button(self, text="Закрыть",\
                   command=self.destroy).place(x=450, y=280)

    def gender_animals(self):
        gender_al = self.gender_als.get()
        if gender_al == "мужской":
            return "мужской"
        else:
            gender_al == "женский"
            return "женский"
        
    def cmbox(self):
        self.animal = ["Собака", "Кот"]
        ttk.Combobox(self, font=_font, values=self.animal,\
                    textvariable=self.animals_result,\
                    state="readonly").place(x=200, y=30)
                
    def data_animals(self):
        anim = self.animals_result.get()
        if anim == "Кот":
            self.sh.main(animal=anim, name=self.name_al.get(),\
                         breed=self.breed_al.get(),\
                         age=self.age_al.get(), gender=self.gender_animals())            
        elif anim == "Собака":
            self.sh.main(animal=anim, name=self.name_al.get(),\
                         breed=self.breed_al.get(),\
                         age=self.age_al.get(), gender=self.gender_animals())            
        self.app.output()


if __name__ == "__main__":
    win = tk.Tk()
    app = InfoAnimals(win)
    app.pack()
    win.title("Приют для животных")
    win.geometry("720x640+420+180")
    win.resizable(False, False)
    title_font = ("JetBrains", "11", "bold")
    _font = ("JetBrains", "11")
    style = ttk.Style()
    style.configure(win, font=_font, foreground="#222540")
    win.mainloop()