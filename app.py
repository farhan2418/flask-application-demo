from models import app, db
from flask import render_template, url_for, request, redirect
from models.todo import Todo
from index_blueprint import index_bp


app.register_blueprint(index_bp)


@app.route('/delete/<int:id>')
def delete(id):
    
    task_to_delete = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'sorry, couldn\'t delete it'


@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form.get('content')

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'sorry could\'nt update it'
    else:
              
        return render_template("update.html", task = task)
if __name__ == "__main__":
    app.run(debug=True)