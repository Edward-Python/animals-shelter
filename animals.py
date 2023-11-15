"""
Приют для животных Shelter
1. Имя name
2. Возраст age
3. Порода breed
4. Пол gender
"""
class Shelter:

    def __init__(self, name, breed, age, gender):
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender

    def main(self):
        list_animal = (
                       f"Животное: {self.special_characteristic()}\n"
                       f"---------------\n"
                       f"Имя: {self.name}\n"
                       f"Порода: {self.breed}\n"
                       f"Возраст: {self.age}\n"
                       f"Пол: {self.gender}\n"              
                      )
        print(list_animal)
        # with open(r"D:\Project\shelter\shelter.txt", "a") as shelter_write:
        #     shelter_write.write(list_animal + "\n")