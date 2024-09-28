# Todo list app made in Flask
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)  # new flask instance setting the root of the app


class Tasks:
    def __init__(self, task, status):
        self.task = task
        self.status = status


task_list = []


@app.route('/')
def index():
    return render_template('index.html', task=task_list)


@app.route('/add', methods=['POST'])
def add():
    task_content = request.form['content']
    new_task = Tasks(task_content, 'To-do')
    task_list.append(new_task)
    return redirect(url_for('index'))


@app.route('/delete/<int:index>')
def delete(index):
    del task_list[index]
    return redirect(url_for('index'))


@app.route('/done/<int:index>')
def done(index):
    task_list[index].status = 'Done'
    return redirect(url_for('index'))


@app.route('/todo/<int:index>')
def todo(index):
    task_list[index].status = 'To-do'
    return redirect(url_for('index'))


# Show only tasks marked as done
# @app.route('/doneonly')
# def doneonly():
#     return 
