import json

def return_base():
    with open("bd.json", "r", encoding="utf-8") as opened_file:
        base = json.load(opened_file)
    return base

def writeToBase(base):
    with open("bd.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(base, ensure_ascii=False))

def add_ball(ball,id_stud,id_pred):
    base = return_base()
    id_ball = len(base[1])
    base[1].append([ball,id_pred,id_stud,str(id_ball)])
    writeToBase(base)

def add_stud(first_name, last_name, patr):
    base = return_base()
    id_stud = len(base[0])
    base[0].append([first_name,last_name,patr,str(id_stud)])
    writeToBase(base)

def add_predmet(predmet_name,kolvo_chasov):
    base = return_base()
    id_pred = len(base[2])
    base[2].append([predmet_name,kolvo_chasov,str(id_pred)])
    writeToBase(base)

def add_otdel(otdel_name):
    base = return_base()
    id_otdel = len(base[3])
    base[3].append([otdel_name,str(id_otdel)])
    writeToBase(base)