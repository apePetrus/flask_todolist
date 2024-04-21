# TodoList App in Flask

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  # Creates a new Flask instance, determining the root of the application.

tasks = {'Task': [], 'Done': []}  # The Todo List in a dictionary.

@app.route('/')  # The root URL of the app.
def index():
	return render_template('index.html', tasks=tasks)  # Renders the index.html of the project.

'''
methods=['POST'] specifies that the function will be triggered when a HTTP POST request is sent
to the '/add' URL. In this case, it's going to add a task to the list.
'''
@app.route('/add', methods=['POST'])  # Route for adding tasks in the list.
def add_task():
	task_content = request.form['content']  # Extracts the task content from the form data submitted with the POST request.
	tasks['Task'].append(task_content)  # Appends the task to the task list.
	tasks['Done'].append('To Do')  # Appends the todo status to the done list
	return redirect(url_for('index'))  # Redirects to the index url


'''
This route will be used to delete a task from the list.
It deletes the task in the list by receiving its position in the list number (its index)
It takes the index number by using the loop.index0 in the html file.
'''
@app.route('/delete/<int:index>')
def delete_task(index):
	del tasks['Task'][index]  # Deletes the task
	del tasks['Done'][index]
	return redirect(url_for('index'))  # Redirect to the index url


@app.route('/complete/<int:index>')  # Route to complete the task
def complete_task(index):
	tasks['Done'][index] = 'Done'  # Change the task status
	return redirect(url_for('index'))  # Redirect to the index url


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5555, debug=True)  # Starts the app.
