# -*- coding: utf-8 -*-
"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, jsonify
from Flask import app, config, myFunc
import json
import random



posts = []
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    predmet_stats = myFunc.getStat()
    return render_template(
        'index.html',
        title='hi',
        year=datetime.now().year,predmet_stats=predmet_stats
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/'+config.token+'/addball/<ball>/<id_stud>/<id_pred>',methods=['GET'])
def addball(ball,id_stud,id_pred):
    myFunc.add_ball(str(ball),str(id_stud),str(id_pred))
    return ball+ ' ' +id_stud + ' ' + id_pred

@app.route('/'+config.token+'/addstudent/<first>/<last>/<patr>',methods=['GET'])
def addstudent(first,last,patr):
    myFunc.add_stud(first,last,patr)
    return first + ' ' + last + ' ' + patr

@app.route('/'+config.token+'/addpredmet/<predmet_name>/<kolvo_chasov>',methods=['GET'])
def addpredmet(predmet_name,kolvo_chasov):
    myFunc.add_predmet(predmet_name,str(kolvo_chasov))
    return predmet_name + ' ' + kolvo_chasov

@app.route('/'+config.token+'/addotdel/<otdel_name>',methods=['GET'])
def addotdel(otdel_name):
    myFunc.add_otdel(otdel_name)
    return otdel_name

@app.route('/balls')
def showball():
    base = myFunc.return_base()
    balls = base[1]
    students = base[0]
    predmets = base[2]
    spisok_ball = []
    for student in students:
        for predmet in predmets:
            for ball in balls:
                if ball[2] == student[3] and ball[1] == predmet[2]:
                    spisok_ball.append([ball[0], student[0] + ' ' + student[1] + ' ' + student[2],predmet[0],ball[3]])

    return render_template(
        'ball.html',
        balls=spisok_ball,
        year=datetime.now().year
    )

@app.route('/journal')
def showjournal():
    base = myFunc.return_base()
    balls = base[1]
    students = base[0]
    predmets = base[2]
    spisok_ball = []
    for student in students:
        for predmet in predmets:
            for ball in balls:
                if ball[2] == student[3] and ball[1] == predmet[2]:
                    spisok_ball.append([ball[0], student[0] + ' ' + student[1] + ' ' + student[2],predmet[0],ball[3],ball[1]])

    return render_template(
        'journal.html',
        balls=spisok_ball,
        year=datetime.now().year,
        predmets=predmets
    )



@app.route('/students')
def showstudent():
    base = myFunc.return_base()
    students = base[0]
    return render_template(
        'student.html',
        students=students,
        year=datetime.now().year
    )

@app.route('/predmets')
def showpredmet():
    base = myFunc.return_base()
    predmets = base[2]
    return render_template(
        'predmet.html',
        predmets=predmets,
        year=datetime.now().year
        #
    )

@app.route('/otdels')
def showotdel():
    base = myFunc.return_base()
    otdels = base[3]
    return render_template(
        'otdel.html',
        otdels=otdels,
        year=datetime.now().year
    )

@app.route('/getbase')
def getBase():
        with open("bd.json", "r", encoding="utf-8") as opened_file:
            file = json.load(opened_file)
        return jsonify(file)

@app.route('/autoadd')
def autoadd():
    for j in range(10):
        myFunc.add_predmet('Предмет №' + str(j), str(random.randint(24, 89)))
        myFunc.add_stud('Фамилия' + str(j), 'Имя' + str(j), 'Отчество' + str(j))
        myFunc.add_otdel('Отделение №' + str(j))
    for i in range(300):
        myFunc.add_ball(str(random.randint(2,5)),str(random.randint(0,10)),str(random.randint(0,10)))


    return 'done'