import constants
import math
from app import app
from flask import render_template, request
@app.route('/hello', methods=['GET'])
def hello():
 # для каждого передаваемого параметра формы нужно установить
 # значение по умолчание, на случай если пользователь ничего не введет
 name1 = 0
 name2 = 0
 subject_id = []
 subjects_select = []
 method = ""
 # получаем параметр из формы
 name1 = int(request.values.get('param1'))
 name2 = int(request.values.get('param2'))
 method = request.values.get('method')
 angle1 = round(math.degrees(math.asin(name1 / name2)), 2)
 angle2 = round(180-angle1, 2)
 angleDD = math.degrees(math.atan2(name1, name2))
 subject_id = request.values.getlist('subject[]')
 subjects_select = [constants.subjects[int(i)] for i in subject_id]
 html = render_template(
 'hello.html',
 name1 = name1,
 name2 = name2,
 subjects_select = subjects_select,
 subject_list = constants.subjects,
 angle1 = angle1,
 angle2 = angle2,
 method = method
 )
 return html