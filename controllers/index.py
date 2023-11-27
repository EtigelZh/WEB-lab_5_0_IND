from app import app
from flask import render_template
import constants
@app.route('/', methods=['GET'])

def index():
 # выводим форму
 html = render_template(
  'index.html',
  subject_list = constants.subjects,
  len=len
 )

 return html
app.run(debug=True)