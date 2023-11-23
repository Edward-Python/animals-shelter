"""
Приют для животных Shelter
1. Имя name
2. Возраст age
3. Порода breed
4. Пол gender
"""
import sqlite3

class Shelter:

    def __init__(self):    
        self.db = sqlite3.connect("animal_shelter.db")
        self.cur = self.db.cursor()
        self.list_anim = ["animal", "name", "breed", "age", "gender"]
        
        self.cur.execute(f"""
        CREATE TABLE IF NOT EXISTS animals_table (
                id INTEGER PRIMARY KEY NOT NULL,
                {self.list_anim[0]} TEXT,
                {self.list_anim[1]} TEXT,
                {self.list_anim[2]} TEXT,
                {self.list_anim[3]} INTEGER,
                {self.list_anim[4]} TEXT)""")
        self.db.commit()
    
    def main(self, animal, name, breed, age, gender):
        self.cur.execute(f"""INSERT INTO animals_table (
                {self.list_anim[0]},
                {self.list_anim[1]},
                {self.list_anim[2]},
                {self.list_anim[3]},
                {self.list_anim[4]})
                VALUES (?, ?, ?, ?, ?)""",
                (animal, name, breed, age, gender))        
        self.db.commit()