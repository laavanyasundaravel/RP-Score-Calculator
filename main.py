from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def form():
    return render_template('form.html')


@app.route('/generate-timetable', methods=['POST'])
def generate_timetable():
    name = request.form['name']
    subjects = request.form['subjects'].split(',')
    
    
    
    return render_template('timetable.html', name=name, subjects=subjects)