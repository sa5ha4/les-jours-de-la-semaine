
class les_jours():
    def __init__(self, jours):
        self.jours = jours
        
jours = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche")

class subjects_list():
    def __init__(self, subjects):
        self.subjects = subjects
        
list1 = ("Fizika", "Matemātika", "Angļu valoda", "Vēsture")
list2 = ("Latviešu valoda", "Ģeogrāfija", "Bioloģija", "Ķīmija", "Fizika", "Franču valoda")
list3 = ("Sports", "Matemātika", "Programmēšana")
list4 = ("Latviešu valoda", "Matemātika", "Angļu valoda", "Sports", "Programmēšana")
list5 = ("Literatūra", "Ķīmija", "Klases stunda")
nav = ("Stundas nav!")

def start():
    print("Ievādi dienas nosaukumu:")
    x = input(":  ")

    if x == "Lundi":
        print(list1)
    elif x == "Mardi":
        print(list2)
    elif x == "Mercredi":
        print(list3)
    elif x == "Jeudi":
        print(list4)
    elif x == "Vendredi":
        print(list5)
    elif x == ("Samedi" or "Dimanche"):
        print(nav)
    else:
        print("Kaut kas ievādits nepareizi")
    question2()

def question2():   
    print("Vai gribi paskatīties sarākstu uz citu dienu?")
    x2 = input()

    if x2 == "oui":
        start()
    elif x2 == "non":
        return
    else:
        print("Ievadi 'oui' vai 'non'!!!!!!")


start()
