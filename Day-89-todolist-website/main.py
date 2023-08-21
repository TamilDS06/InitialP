from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from random import choice
from forms import AddTaskForm
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
db = SQLAlchemy()
app.secret_key = "Secret1234"
db.init_app(app)
bootstrap = Bootstrap5(app)

# TODOLIST Table configuration
class ToDoList(db.Model):
    __tablename__ = 'todolist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    start_date = db.Column(db.String(250), nullable=False)
    end_date = db.Column(db.String(250), nullable=False)
    status = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    tasks = None
    results = db.session.execute(db.select(ToDoList).order_by(ToDoList.id))
    all_tasks = results.scalars().all()
    if all_tasks:
        tasks = True
    return render_template("index.html", all_tasks=all_tasks, tasks=tasks)


@app.route('/add_task', methods=['POST', 'GET'])
def add_task_():
    if request.method == 'POST':
        add_task_form = ToDoList(
            name=request.form.get('name'),
            start_date=request.form.get('start_date'),
            end_date=request.form.get('end_date'),
            status=bool(request.form.get('status'))
        )
        db.session.add(add_task_form)
        db.session.commit()
        result = db.session.execute(db.select(ToDoList).where(ToDoList.name==request.form.get('name')))
        result_cafe = result.scalar()
        data = {'result':"data added failed."}
        if result_cafe:
            data['result'] = "data added successfully."
        return redirect(url_for('home'))
    form = AddTaskForm()
    return render_template("add.html", form=form)

@app.route('/remove', methods=['POST', 'GET'])
def delete():
    data = {'result':"Data Deleted Failed."}
    result = db.session.execute(db.select(ToDoList).where(ToDoList.status==1)).scalar()
    if not result:
        data['result'] = "No Task to Delete"
        return f'<h1>{data}</h1>'
    db.session.delete(result)
    db.session.commit()
    result = db.session.execute(db.select(ToDoList).where(ToDoList.status==1)).scalar()
    if not result:
        data['result'] = "Data Deleted Successfull."
    return f'<h1>{data}</h1>'
        

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')